#!/usr/bin/env python3
"""Scan npm registry for new MCP server packages.

Queries the npm registry search API for packages matching 'mcp-server'
and similar patterns, then compares against the current registry to
find new packages that could be added.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import httpx

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = REPO_ROOT / "src" / "mcpx" / "registry_data.json"

# npm search queries to find MCP server packages
SEARCH_QUERIES = [
    "mcp-server",
    "mcp server",
    "model-context-protocol server",
    "@modelcontextprotocol",
]

NPM_SEARCH_URL = "https://registry.npmjs.org/-/v1/search"
NPM_SEARCH_SIZE = 250  # max results per query


def load_registry(path: Path | None = None) -> dict[str, Any]:
    """Load registry data from JSON file."""
    registry_path = path or REGISTRY_PATH
    with open(registry_path, encoding="utf-8") as f:
        return json.load(f)


def get_existing_packages(data: dict[str, Any]) -> set[str]:
    """Extract the set of npm package names already in the registry."""
    return {server["package"] for server in data.get("servers", [])}


def search_npm(
    query: str,
    size: int = NPM_SEARCH_SIZE,
    client: httpx.Client | None = None,
) -> list[dict[str, Any]]:
    """Search npm registry for packages matching query.

    Returns list of package info dicts with keys:
    name, description, version, date, keywords, links, publisher.
    """
    params = {"text": query, "size": size}
    if client is not None:
        response = client.get(NPM_SEARCH_URL, params=params)
    else:
        response = httpx.get(NPM_SEARCH_URL, params=params, timeout=30.0)

    response.raise_for_status()
    results = response.json()

    packages = []
    for obj in results.get("objects", []):
        pkg = obj.get("package", {})
        packages.append(
            {
                "name": pkg.get("name", ""),
                "description": pkg.get("description", ""),
                "version": pkg.get("version", ""),
                "date": pkg.get("date", ""),
                "keywords": pkg.get("keywords", []),
                "links": pkg.get("links", {}),
                "publisher": pkg.get("publisher", {}),
                "score": obj.get("score", {}).get("final", 0),
            }
        )
    return packages


def is_mcp_server_package(pkg: dict[str, Any]) -> bool:
    """Heuristic: check if a package looks like an MCP server.

    Checks name patterns and keywords to filter out unrelated packages.
    """
    name = pkg.get("name", "").lower()
    keywords = [k.lower() for k in pkg.get("keywords", [])]
    desc = pkg.get("description", "").lower()

    # Name-based checks
    name_signals = [
        "mcp-server" in name,
        "mcp_server" in name,
        name.startswith("@modelcontextprotocol/server-"),
        "server-mcp" in name,
    ]

    # Keyword-based checks
    keyword_signals = [
        "mcp" in keywords and "server" in keywords,
        "model-context-protocol" in keywords,
        "mcp-server" in keywords,
    ]

    # Description-based checks
    desc_signals = [
        "mcp server" in desc,
        "model context protocol" in desc,
    ]

    return any(name_signals) or any(keyword_signals) or any(desc_signals)


def guess_category(pkg: dict[str, Any]) -> str:
    """Guess a category for the package based on name/keywords/description."""
    name = pkg.get("name", "").lower()
    desc = pkg.get("description", "").lower()
    keywords = [k.lower() for k in pkg.get("keywords", [])]
    text = f"{name} {desc} {' '.join(keywords)}"

    category_hints = {
        "database": [
            "database",
            "sql",
            "postgres",
            "mysql",
            "sqlite",
            "mongodb",
            "redis",
            "db",
        ],
        "devtools": ["github", "git", "docker", "kubernetes", "terminal", "dev"],
        "communication": ["slack", "discord", "email", "gmail", "messaging", "chat"],
        "search": ["search", "brave", "tavily"],
        "web": ["fetch", "scraping", "crawl", "http", "web"],
        "browser": ["browser", "puppeteer", "playwright", "selenium"],
        "cloud": ["aws", "azure", "gcp", "cloudflare", "cloud"],
        "ai": ["openai", "anthropic", "llm", "ai", "ml", "vector", "embedding"],
        "monitoring": ["sentry", "datadog", "grafana", "monitoring", "observability"],
        "productivity": ["notion", "todoist", "confluence", "productivity"],
        "project-management": ["jira", "linear", "project", "sprint"],
        "payments": ["stripe", "payment", "billing"],
        "filesystem": ["file", "filesystem", "directory"],
        "memory": ["memory", "knowledge-graph"],
        "utilities": ["time", "utility", "tool"],
    }

    for category, hints in category_hints.items():
        if any(hint in text for hint in hints):
            return category

    return "utilities"


def build_new_entry(pkg: dict[str, Any]) -> dict[str, Any]:
    """Build a registry entry from an npm package."""
    name = pkg["name"]
    # Derive a short name from the package name
    short_name = name
    for prefix in ["@modelcontextprotocol/server-", "mcp-server-", "mcp-", "@"]:
        if short_name.startswith(prefix):
            short_name = short_name[len(prefix) :]
    short_name = short_name.replace("/", "-").replace("_", "-").strip("-")

    return {
        "name": short_name,
        "description": pkg.get("description", ""),
        "package": name,
        "install_type": "npm",
        "command": "npx",
        "args": ["-y", name],
        "env": {},
        "config_params": {},
        "category": guess_category(pkg),
        "tags": [k.lower() for k in pkg.get("keywords", []) if len(k) < 30][:10],
        "official": name.startswith("@modelcontextprotocol/"),
        "stars": 0,
    }


def scan_for_new_packages(
    registry_path: Path | None = None,
    client: httpx.Client | None = None,
) -> list[dict[str, Any]]:
    """Scan npm for new MCP server packages not in the registry.

    Returns list of new entry dicts ready to add to registry_data.json.
    """
    data = load_registry(registry_path)
    existing = get_existing_packages(data)

    # Collect all candidate packages from multiple search queries
    seen_names: set[str] = set()
    candidates: list[dict[str, Any]] = []

    for query in SEARCH_QUERIES:
        try:
            packages = search_npm(query, client=client)
        except httpx.HTTPError:
            continue

        for pkg in packages:
            pkg_name = pkg["name"]
            if pkg_name in seen_names or pkg_name in existing:
                continue
            seen_names.add(pkg_name)

            if is_mcp_server_package(pkg):
                candidates.append(pkg)

    # Build registry entries for new packages
    new_entries = [build_new_entry(pkg) for pkg in candidates]

    # Sort by score (best first)
    new_entries.sort(key=lambda e: e["name"])

    return new_entries


def main() -> int:
    """Main entry point."""
    try:
        new_entries = scan_for_new_packages()
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    if not new_entries:
        print("No new MCP server packages found.")
        return 0

    print(f"Found {len(new_entries)} new MCP server package(s):\n")
    for entry in new_entries:
        print(f"  - {entry['name']} ({entry['package']})")
        print(f"    {entry['description']}")
        print(f"    Category: {entry['category']}")
        print()

    # Write discoveries to a JSON file for the workflow to pick up
    output_path = REPO_ROOT / "new_servers_discovered.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(new_entries, f, indent=2)
    print(f"Wrote discoveries to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
