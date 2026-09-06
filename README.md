# mcpx

> The package manager for MCP servers. Discover, install, and manage Model Context Protocol servers for Claude Code, Cursor, and VS Code.

[![PyPI version](https://img.shields.io/pypi/v/mcpx.svg)](https://pypi.org/project/mcpx/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/LakshmiSravyaVedantham/mcpx/actions/workflows/ci.yml/badge.svg)](https://github.com/LakshmiSravyaVedantham/mcpx/actions)

---

## What is mcpx?

**mcpx** is like `npm` or `brew` -- but for MCP servers. It provides a curated registry of **51+ MCP servers** and lets you install them into Claude Code, Cursor, or VS Code with a single command.

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

- **51+ curated MCP servers** across 21 categories (database, devtools, cloud, AI, etc.)
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

The built-in registry includes 51+ servers across these categories:

| Category | Examples |
|----------|----------|
| AI & ML | Openai, Pinecone, Anthropic |
| Browser Automation | Puppeteer, Playwright |
| Cloud Providers | Aws, Cloudflare, Azure, Gcp |
| Communication | Slack, Twilio, Discord, Gmail |
| CRM | Hubspot |
| Databases | Postgres, Sqlite, Redis, Mysql, Mongodb, ... |
| Deployment | Vercel |
| Design | Figma |
| Developer Tools | Github, Docker, Kubernetes, Terminal, Context7 |
| E-Commerce | Shopify |
| Filesystem | Filesystem |
| Location & Maps | Google Maps |
| Memory & Context | Memory |
| Monitoring | Sentry, Grafana, Datadog |
| Payments | Stripe |
| Productivity | Notion, Todoist, Confluence, Google Drive |
| Project Management | Linear, Jira |
| Reasoning | Sequential Thinking |
| Search | Brave Search, Tavily |
| Utilities | Time |
| Web & Scraping | Fetch, Firecrawl |

## All Servers

| Name | Description | Category | Stars |
|------|-------------|----------|-------|
| filesystem ⭐ | Read, write, and manage files on your local filesystem | filesystem | 90,108 |
| memory ⭐ | Persistent memory using a local knowledge graph for long-term context | memory | 90,108 |
| sequential-thinking ⭐ | Break down complex problems into sequential thinking steps | reasoning | 90,108 |
| context7 | Pull up-to-date documentation and code examples for any library | devtools | 61,686 |
| playwright | Automate browsers with Playwright for testing and scraping | browser | 36,843 |
| firecrawl | Crawl and scrape websites with Firecrawl for LLM-ready content | web | 7,407 |
| github ⭐ | Interact with GitHub repositories, issues, PRs, and more | devtools | 6,500 |
| puppeteer ⭐ | Automate browser interactions, take screenshots, and scrape web pages | browser | 4,500 |
| postgres ⭐ | Query and manage PostgreSQL databases with read-only or read-write access | database | 4,200 |
| sqlite ⭐ | Query and manage SQLite databases | database | 3,800 |
| slack ⭐ | Send messages, manage channels, and interact with Slack workspaces | communication | 3,200 |
| fetch ⭐ | Fetch and extract content from URLs and web pages | web | 3,100 |
| brave-search ⭐ | Search the web using Brave Search API | search | 2,800 |
| stripe | Manage Stripe payments, customers, subscriptions, and invoices | payments | 2,500 |
| google-maps ⭐ | Search places, get directions, and geocode addresses via Google Maps | location | 2,400 |
| tavily | AI-optimized web search and research with Tavily API | search | 2,370 |
| openai | Use OpenAI models (GPT-4, DALL-E, Whisper) from within your AI assistant | ai | 2,200 |
| mysql | Query and manage MySQL databases | database | 2,106 |
| aws | Interact with AWS services including S3, EC2, Lambda, and more | cloud | 2,100 |
| notion | Search, read, and manage Notion pages, databases, and blocks | productivity | 1,900 |
| docker | Manage Docker containers, images, volumes, and networks | devtools | 1,800 |
| anthropic | Use Anthropic Claude API directly as an MCP server | ai | 1,800 |
| supabase | Manage Supabase projects, databases, and edge functions | database | 1,600 |
| kubernetes | Manage Kubernetes clusters, pods, deployments, and services | devtools | 1,576 |
| cloudflare | Manage Cloudflare Workers, KV, R2, and DNS | cloud | 1,500 |
| vercel | Manage Vercel deployments, domains, and environment variables | deployment | 1,400 |
| redis | Interact with Redis databases for caching and data storage | database | 1,200 |
| figma | Access Figma designs, components, and design tokens | design | 1,200 |
| mongodb | Query and manage MongoDB databases and collections | database | 1,100 |
| grafana | Query Grafana dashboards, alerts, and datasources | monitoring | 1,100 |
| gmail | Read and send Gmail messages | communication | 1,100 |
| jira | Manage Jira issues, sprints, and project boards | project-management | 1,000 |
| pinecone | Manage Pinecone vector databases for AI/ML applications | ai | 900 |
| datadog | Query Datadog metrics, monitors, and APM traces | monitoring | 900 |
| google-drive | Search, read, and manage Google Drive files | productivity | 900 |
| sentry | Query Sentry issues, events, and error monitoring data | monitoring | 843 |
| elasticsearch | Search and manage Elasticsearch indices and documents | database | 800 |
| discord | Send messages and manage Discord servers and channels | communication | 800 |
| azure | Manage Azure cloud resources, deployments, and services | cloud | 800 |
| time ⭐ | Get current time, convert timezones, and manage time-related operations | utilities | 800 |
| twilio | Send SMS, make calls, and manage Twilio communications | communication | 700 |
| confluence | Search and manage Confluence pages and spaces | productivity | 700 |
| snowflake | Query and manage Snowflake data warehouse | database | 700 |
| gcp | Manage Google Cloud Platform resources and services | cloud | 700 |
| todoist | Manage Todoist tasks, projects, and labels | productivity | 600 |
| bigquery | Query Google BigQuery datasets and tables | database | 600 |
| airtable | Read and manage Airtable bases, tables, and records | database | 500 |
| hubspot | Manage HubSpot CRM contacts, deals, and companies | crm | 500 |
| terminal | Execute shell commands and terminal operations securely | devtools | 19 |
| linear | Manage Linear issues, projects, and workflows | project-management | 2 |
| shopify | Manage Shopify stores, products, and orders | ecommerce | 0 |

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
