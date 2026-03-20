#!/usr/bin/env python3
"""Check freshness of registry packages.

Verifies that npm packages in the registry still exist on npm and
updates star counts from GitHub where possible.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any, Optional

import httpx

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = REPO_ROOT / "src" / "mcpx" / "registry_data.json"

NPM_REGISTRY_URL = "https://registry.npmjs.org"
GITHUB_API_URL = "https://api.github.com"


def load_registry(path: Path | None = None) -> dict[str, Any]:
    """Load registry data from JSON file."""
    registry_path = path or REGISTRY_PATH
    with open(registry_path, encoding="utf-8") as f:
        return json.load(f)


def save_registry(data: dict[str, Any], path: Path | None = None) -> None:
    """Save registry data to JSON file."""
    registry_path = path or REGISTRY_PATH
    with open(registry_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def check_npm_package(
    package_name: str,
    client: httpx.Client | None = None,
) -> dict[str, Any]:
    """Check if an npm package exists and get its metadata.

    Returns dict with keys: exists, version, deprecated, repository_url.
    """
    # Encode scoped package names (@ -> %40, / -> %2f)
    encoded_name = package_name.replace("/", "%2f")
    url = f"{NPM_REGISTRY_URL}/{encoded_name}"

    try:
        if client is not None:
            response = client.get(url)
        else:
            response = httpx.get(url, timeout=15.0)

        if response.status_code == 404:
            return {"exists": False, "package": package_name}

        response.raise_for_status()
        data = response.json()

        # Get latest version info
        latest_version = data.get("dist-tags", {}).get("latest", "")
        versions = data.get("versions", {})
        latest_info = versions.get(latest_version, {})
        deprecated = latest_info.get("deprecated", None)

        # Extract repository URL
        repo = data.get("repository", {})
        repo_url = repo.get("url", "") if isinstance(repo, dict) else str(repo)

        return {
            "exists": True,
            "package": package_name,
            "version": latest_version,
            "deprecated": deprecated,
            "repository_url": repo_url,
        }

    except httpx.HTTPError:
        return {"exists": None, "package": package_name, "error": "network_error"}


def extract_github_repo(repo_url: str) -> Optional[str]:
    """Extract 'owner/repo' from a GitHub repository URL.

    Handles formats like:
    - https://github.com/owner/repo
    - git+https://github.com/owner/repo.git
    - git://github.com/owner/repo.git
    - github:owner/repo
    """
    if not repo_url:
        return None

    # Try github:owner/repo
    match = re.match(r"github:([^/]+/[^/]+)", repo_url)
    if match:
        return match.group(1).rstrip(".git")

    # Try URL patterns
    match = re.search(r"github\.com[/:]([^/]+/[^/\s#]+)", repo_url)
    if match:
        return match.group(1).rstrip(".git")

    return None


def get_github_stars(
    owner_repo: str,
    client: httpx.Client | None = None,
    github_token: Optional[str] = None,
) -> Optional[int]:
    """Get star count for a GitHub repository.

    Returns star count or None if unavailable.
    """
    url = f"{GITHUB_API_URL}/repos/{owner_repo}"
    headers: dict[str, str] = {"Accept": "application/vnd.github.v3+json"}
    if github_token:
        headers["Authorization"] = f"token {github_token}"

    try:
        if client is not None:
            response = client.get(url, headers=headers)
        else:
            response = httpx.get(url, headers=headers, timeout=15.0)

        if response.status_code != 200:
            return None

        data = response.json()
        return data.get("stargazers_count")

    except httpx.HTTPError:
        return None


def check_all_packages(
    registry_path: Path | None = None,
    npm_client: httpx.Client | None = None,
    github_client: httpx.Client | None = None,
    github_token: Optional[str] = None,
) -> dict[str, Any]:
    """Check all packages in the registry for freshness.

    Returns dict with:
    - removed: list of packages that no longer exist on npm
    - deprecated: list of packages that are deprecated
    - star_updates: dict of {server_name: new_star_count}
    - errors: list of packages that couldn't be checked
    """
    data = load_registry(registry_path)
    servers = data.get("servers", [])

    removed: list[str] = []
    deprecated: list[dict[str, str]] = []
    star_updates: dict[str, int] = {}
    errors: list[str] = []

    for server in servers:
        name = server["name"]
        package = server["package"]

        # Check npm
        npm_info = check_npm_package(package, client=npm_client)

        if npm_info.get("exists") is False:
            removed.append(name)
            continue

        if npm_info.get("exists") is None:
            errors.append(name)
            continue

        if npm_info.get("deprecated"):
            deprecated.append({"name": name, "reason": npm_info["deprecated"]})

        # Try to get GitHub stars
        repo_url = npm_info.get("repository_url", "")
        owner_repo = extract_github_repo(repo_url)
        if owner_repo:
            stars = get_github_stars(
                owner_repo,
                client=github_client,
                github_token=github_token,
            )
            if stars is not None and stars != server.get("stars", 0):
                star_updates[name] = stars

    return {
        "removed": removed,
        "deprecated": deprecated,
        "star_updates": star_updates,
        "errors": errors,
    }


def apply_star_updates(
    star_updates: dict[str, int],
    registry_path: Path | None = None,
) -> dict[str, Any]:
    """Apply star count updates to the registry and save."""
    data = load_registry(registry_path)

    for server in data.get("servers", []):
        if server["name"] in star_updates:
            server["stars"] = star_updates[server["name"]]

    save_registry(data, registry_path)
    return data


def main() -> int:
    """Main entry point."""
    import os

    github_token = os.environ.get("GITHUB_TOKEN")

    try:
        results = check_all_packages(github_token=github_token)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    # Report results
    if results["removed"]:
        print("Packages no longer on npm:")
        for name in results["removed"]:
            print(f"  - {name}")
        print()

    if results["deprecated"]:
        print("Deprecated packages:")
        for item in results["deprecated"]:
            print(f"  - {item['name']}: {item['reason']}")
        print()

    if results["star_updates"]:
        print("Star count updates:")
        for name, stars in results["star_updates"].items():
            print(f"  - {name}: {stars:,}")
        # Apply updates
        apply_star_updates(results["star_updates"])
        print("\nRegistry updated with new star counts.")

    if results["errors"]:
        print("Could not check (network errors):")
        for name in results["errors"]:
            print(f"  - {name}")

    if not any([results["removed"], results["deprecated"], results["star_updates"]]):
        print("All packages are fresh. No updates needed.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
