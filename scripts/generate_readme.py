#!/usr/bin/env python3
"""Regenerate README.md from registry_data.json.

Reads the registry data and produces a consistent README with accurate
server count, category table, and full server listing.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = REPO_ROOT / "src" / "mcpx" / "registry_data.json"
README_PATH = REPO_ROOT / "README.md"

# Category icons used in the README table
CATEGORY_ICONS: dict[str, str] = {
    "database": "🗄️",
    "devtools": "🔧",
    "communication": "💬",
    "search": "🔍",
    "web": "🌐",
    "browser": "🌐",
    "cloud": "☁️",
    "ai": "🤖",
    "monitoring": "📊",
    "productivity": "✅",
    "project-management": "📋",
    "payments": "💳",
    "deployment": "🚀",
    "filesystem": "📁",
    "memory": "🧠",
    "reasoning": "💡",
    "location": "📍",
    "design": "🎨",
    "crm": "👥",
    "ecommerce": "🛒",
    "utilities": "🔧",
}


def load_registry(path: Path | None = None) -> dict[str, Any]:
    """Load registry data from JSON file."""
    registry_path = path or REGISTRY_PATH
    with open(registry_path, encoding="utf-8") as f:
        return json.load(f)


def build_category_table(data: dict[str, Any]) -> str:
    """Build the markdown category table from registry data."""
    servers = data.get("servers", [])
    categories = data.get("categories", {})

    # Group servers by category
    cat_servers: dict[str, list[str]] = {}
    for server in servers:
        cat = server["category"]
        cat_servers.setdefault(cat, []).append(server["name"])

    lines = ["| Category | Examples |", "|----------|----------|"]
    for cat_key in sorted(cat_servers.keys()):
        cat_info = categories.get(cat_key, {})
        label = cat_info.get("label", cat_key.title())
        examples = ", ".join(
            s.title().replace("-", " ") for s in cat_servers[cat_key][:5]
        )
        if len(cat_servers[cat_key]) > 5:
            examples += ", ..."
        lines.append(f"| {label} | {examples} |")

    return "\n".join(lines)


def build_server_table(data: dict[str, Any]) -> str:
    """Build the full server listing table."""
    servers = data.get("servers", [])
    sorted_servers = sorted(servers, key=lambda s: -s.get("stars", 0))

    lines = [
        "| Name | Description | Category | Stars |",
        "|------|-------------|----------|-------|",
    ]
    for server in sorted_servers:
        name = server["name"]
        desc = server["description"]
        cat = server["category"]
        stars = server.get("stars", 0)
        official = " ⭐" if server.get("official") else ""
        lines.append(f"| {name}{official} | {desc} | {cat} | {stars:,} |")

    return "\n".join(lines)


def generate_readme(data: dict[str, Any]) -> str:
    """Generate the full README content from registry data."""
    servers = data.get("servers", [])
    server_count = len(servers)
    category_count = len(set(s["category"] for s in servers))

    category_table = build_category_table(data)
    server_table = build_server_table(data)

    return f"""# mcpx

> The package manager for MCP servers. Discover, install, and manage Model Context Protocol servers for Claude Code, Cursor, and VS Code.

[![PyPI version](https://img.shields.io/pypi/v/mcpx.svg)](https://pypi.org/project/mcpx/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/LakshmiSravyaVedantham/mcpx/actions/workflows/ci.yml/badge.svg)](https://github.com/LakshmiSravyaVedantham/mcpx/actions)

---

## What is mcpx?

**mcpx** is like `npm` or `brew` -- but for MCP servers. It provides a curated registry of **{server_count}+ MCP servers** and lets you install them into Claude Code, Cursor, or VS Code with a single command.

No more manually editing JSON config files. No more hunting for package names. Just:

```bash
mcpx install github
```

## Quick Start

```bash
pip install mcpx
```

```bash
# Search for servers
mcpx search database

# See what's popular
mcpx top

# Install a server
mcpx install github --param token=ghp_xxxxx

# List installed servers
mcpx list

# Check your setup
mcpx doctor
```

## Features

- **{server_count}+ curated MCP servers** across {category_count} categories (database, devtools, cloud, AI, etc.)
- **One-command install** -- `mcpx install <name>` writes the config for you
- **Auto-detects** Claude Code, Cursor, and VS Code configurations
- **Smart search** -- find servers by name, description, or tags
- **Doctor command** -- diagnose configuration issues
- **Beautiful CLI** powered by Rich and Typer
- **Zero config** -- works out of the box with sensible defaults

## Commands

| Command | Description |
|---------|-------------|
| `mcpx search <query>` | Search the server registry |
| `mcpx install <name>` | Install an MCP server |
| `mcpx uninstall <name>` | Remove an MCP server |
| `mcpx list` | List installed servers |
| `mcpx info <name>` | Show detailed server info |
| `mcpx top` | Show most popular servers |
| `mcpx categories` | List all categories |
| `mcpx browse <category>` | Browse servers by category |
| `mcpx doctor` | Diagnose config issues |
| `mcpx init` | Create a new config file |
| `mcpx platforms` | Detect installed AI platforms |

## Examples

### Search for database servers

```bash
$ mcpx search database
```

### Install a server with parameters

```bash
$ mcpx install postgres --param connection_string=postgresql://localhost/mydb
```

### Check your setup

```bash
$ mcpx doctor
```

## Supported Platforms

mcpx auto-detects and writes config for:

- **Claude Code** (`~/.claude.json`)
- **Cursor** (platform-specific path)
- **VS Code** (platform-specific path)
- **Project-level** (`.mcp.json`)

## Registry

The built-in registry includes {server_count}+ servers across these categories:

{category_table}

## All Servers

{server_table}

## Contributing

Contributions welcome! To add a new server to the registry:

1. Fork the repo
2. Edit `src/mcpx/registry_data.json`
3. Submit a PR

## Development

```bash
git clone https://github.com/LakshmiSravyaVedantham/mcpx.git
cd mcpx
python -m venv venv && source venv/bin/activate
pip install -e ".[dev]"
pytest
```

## License

MIT License -- see [LICENSE](LICENSE) for details.

## What is MCP?

The [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) is an open standard by Anthropic that lets AI assistants connect to external tools and data sources. MCP servers provide capabilities like file access, database queries, API integrations, and more.

**mcpx** makes it easy to discover and manage these servers.
"""


def main() -> int:
    """Main entry point."""
    try:
        data = load_registry()
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading registry: {e}", file=sys.stderr)
        return 1

    readme_content = generate_readme(data)

    README_PATH.write_text(readme_content, encoding="utf-8")
    server_count = len(data.get("servers", []))
    print(f"README.md regenerated with {server_count} servers.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
