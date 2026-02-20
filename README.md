# mcpx

> The package manager for MCP servers. Discover, install, and manage Model Context Protocol servers for Claude Code, Cursor, and VS Code.

[![PyPI version](https://img.shields.io/pypi/v/mcpx.svg)](https://pypi.org/project/mcpx/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/LakshmiSravyaVedantham/mcpx/actions/workflows/ci.yml/badge.svg)](https://github.com/LakshmiSravyaVedantham/mcpx/actions)

---

## What is mcpx?

**mcpx** is like `npm` or `brew` — but for MCP servers. It provides a curated registry of **50+ MCP servers** and lets you install them into Claude Code, Cursor, or VS Code with a single command.

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

- **50+ curated MCP servers** across 21 categories (database, devtools, cloud, AI, etc.)
- **One-command install** — `mcpx install <name>` writes the config for you
- **Auto-detects** Claude Code, Cursor, and VS Code configurations
- **Smart search** — find servers by name, description, or tags
- **Doctor command** — diagnose configuration issues
- **Beautiful CLI** powered by Rich and Typer
- **Zero config** — works out of the box with sensible defaults

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
┌─────────────────────────────────────────────────────┐
│ Search results for 'database'                       │
├──────────┬──────────────────────┬──────────┬────────┤
│ Name     │ Description          │ Category │ Stars  │
├──────────┼──────────────────────┼──────────┼────────┤
│ postgres │ PostgreSQL database  │ database │ ★ 4200 │
│ sqlite   │ SQLite database      │ database │ ★ 3800 │
│ mysql    │ MySQL database       │ database │ ★ 2100 │
│ mongodb  │ MongoDB database     │ database │ ★ 1800 │
│ redis    │ Redis key-value      │ database │ ★ 2500 │
└──────────┴──────────────────────┴──────────┴────────┘
```

### Install a server with parameters

```bash
$ mcpx install postgres --param connection_string=postgresql://localhost/mydb
╭──────────── Installed ────────────╮
│ ✓ Server 'postgres' installed     │
│                                   │
│ Config: ~/.claude.json            │
│ Restart your AI tool to activate. │
╰───────────────────────────────────╯
```

### Check your setup

```bash
$ mcpx doctor
╭── MCP Configuration Doctor ──╮
│                               │
│ ✓ Config file: Found          │
│ ✓ Valid JSON                  │
│ ✓ MCP servers: 3 configured  │
│ ✓ npx available              │
│ ✓ Node.js v20.11.0           │
│ ! Server 'slack': Unconfigured│
│   env vars: SLACK_TOKEN       │
│ ✓ Platforms: Claude Code      │
│                               │
│ 5 ok, 1 warning              │
╰───────────────────────────────╯
```

## Supported Platforms

mcpx auto-detects and writes config for:

- **Claude Code** (`~/.claude.json`)
- **Cursor** (platform-specific path)
- **VS Code** (platform-specific path)
- **Project-level** (`.mcp.json`)

## Registry

The built-in registry includes 50+ servers across these categories:

| Category | Examples |
|----------|----------|
| Database | PostgreSQL, SQLite, MySQL, MongoDB, Redis |
| DevTools | GitHub, Docker, Kubernetes, Terminal |
| Communication | Slack, Discord, Gmail, Twilio |
| Search | Brave Search, Tavily, Google |
| Cloud | AWS, Azure, GCP, Cloudflare |
| AI | OpenAI, Anthropic, Sequential Thinking |
| Monitoring | Sentry, Datadog, Grafana |
| Productivity | Notion, Linear, Todoist, Airtable |
| Web | Fetch, Firecrawl, Puppeteer, Playwright |
| Design | Figma |
| CRM | HubSpot |
| Payments | Stripe |
| And more... | 21 categories total |

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

MIT License — see [LICENSE](LICENSE) for details.

## What is MCP?

The [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) is an open standard by Anthropic that lets AI assistants connect to external tools and data sources. MCP servers provide capabilities like file access, database queries, API integrations, and more.

**mcpx** makes it easy to discover and manage these servers.
