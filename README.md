# mcpx

> The package manager for MCP servers. Discover, install, and manage Model Context Protocol servers for Claude Code, Cursor, and VS Code.

[![PyPI version](https://img.shields.io/pypi/v/mcpx.svg)](https://pypi.org/project/mcpx/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/LakshmiSravyaVedantham/mcpx/actions/workflows/ci.yml/badge.svg)](https://github.com/LakshmiSravyaVedantham/mcpx/actions)

---

## What is mcpx?

**mcpx** is like `npm` or `brew` -- but for MCP servers. It provides a curated registry of **715+ MCP servers** and lets you install them into Claude Code, Cursor, or VS Code with a single command.

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

- **715+ curated MCP servers** across 21 categories (database, devtools, cloud, AI, etc.)
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

The built-in registry includes 715+ servers across these categories:

| Category | Examples |
|----------|----------|
| AI & ML | Openai, Pinecone, Anthropic, 1Mcp Agent, Affine Mcp Server, ... |
| Browser Automation | Puppeteer, Playwright, Agent Infra Mcp Server Browser, Browserless.Io Mcp, Browsermcp Mcp, ... |
| Cloud Providers | Aws, Cloudflare, Azure, Gcp, Azure Mcp, ... |
| Communication | Slack, Twilio, Discord, Gmail, Anki Mcp Http, ... |
| CRM | Hubspot |
| Databases | Postgres, Sqlite, Redis, Mysql, Mongodb, ... |
| Deployment | Vercel |
| Design | Figma |
| Developer Tools | Github, Docker, Kubernetes, Terminal, Context7, ... |
| E-Commerce | Shopify |
| Filesystem | Filesystem, Adpharm Mcp Server Filesystem Ro, Agent Install, Negokaz Excel Mcp Server, Ouedyan Modelcontextprotocol Server Filesystem, ... |
| Location & Maps | Google Maps |
| Memory & Context | Memory, Agentage Server Memory, Graphite Atlas Mcp Server, Knowledge01 Mcp, Neurodivergent Memory |
| Monitoring | Sentry, Grafana, Datadog, Autotel Mcp Instrumentation, Datadog Mcp Server, ... |
| Payments | Stripe, Stripe Mcp |
| Productivity | Notion, Todoist, Confluence, Google Drive, Delorenj Mcp Server Trello, ... |
| Project Management | Linear, Jira, Bitrix24 Tasks Mcp Server, Linear Mcp Server, Myspec Mcp Server, ... |
| Reasoning | Sequential Thinking |
| Search | Brave Search, Tavily, Adenot Mcp Google Search, Ai Mentora Mcp Server, Aml Modelcontextprotocol Aml Watcher Mcp, ... |
| Utilities | Time, 0Xmonaco Mcp Server, Aborruso Ckan Mcp Server, Adrkit Mcp, Agent5Ive Mcp, ... |
| Web & Scraping | Fetch, Firecrawl, Agenticpay Mcp Bridge, Agentproto Driver Mcp, Agimon Ai Log Sink Mcp, ... |

## All Servers

| Name | Description | Category | Stars |
|------|-------------|----------|-------|
| github ⭐ | Interact with GitHub repositories, issues, PRs, and more | devtools | 6,500 |
| memory ⭐ | Persistent memory using a local knowledge graph for long-term context | memory | 5,500 |
| filesystem ⭐ | Read, write, and manage files on your local filesystem | filesystem | 5,000 |
| puppeteer ⭐ | Automate browser interactions, take screenshots, and scrape web pages | browser | 4,500 |
| postgres ⭐ | Query and manage PostgreSQL databases with read-only or read-write access | database | 4,200 |
| sequential-thinking ⭐ | Break down complex problems into sequential thinking steps | reasoning | 3,900 |
| sqlite ⭐ | Query and manage SQLite databases | database | 3,800 |
| playwright | Automate browsers with Playwright for testing and scraping | browser | 3,500 |
| slack ⭐ | Send messages, manage channels, and interact with Slack workspaces | communication | 3,200 |
| fetch ⭐ | Fetch and extract content from URLs and web pages | web | 3,100 |
| context7 | Pull up-to-date documentation and code examples for any library | devtools | 3,000 |
| brave-search ⭐ | Search the web using Brave Search API | search | 2,800 |
| stripe | Manage Stripe payments, customers, subscriptions, and invoices | payments | 2,500 |
| google-maps ⭐ | Search places, get directions, and geocode addresses via Google Maps | location | 2,400 |
| openai | Use OpenAI models (GPT-4, DALL-E, Whisper) from within your AI assistant | ai | 2,200 |
| aws | Interact with AWS services including S3, EC2, Lambda, and more | cloud | 2,100 |
| firecrawl | Crawl and scrape websites with Firecrawl for LLM-ready content | web | 2,000 |
| notion | Search, read, and manage Notion pages, databases, and blocks | productivity | 1,900 |
| docker | Manage Docker containers, images, volumes, and networks | devtools | 1,800 |
| tavily | AI-optimized web search and research with Tavily API | search | 1,800 |
| anthropic | Use Anthropic Claude API directly as an MCP server | ai | 1,800 |
| sentry | Query Sentry issues, events, and error monitoring data | monitoring | 1,700 |
| supabase | Manage Supabase projects, databases, and edge functions | database | 1,600 |
| kubernetes | Manage Kubernetes clusters, pods, deployments, and services | devtools | 1,500 |
| cloudflare | Manage Cloudflare Workers, KV, R2, and DNS | cloud | 1,500 |
| vercel | Manage Vercel deployments, domains, and environment variables | deployment | 1,400 |
| linear | Manage Linear issues, projects, and workflows | project-management | 1,300 |
| redis | Interact with Redis databases for caching and data storage | database | 1,200 |
| figma | Access Figma designs, components, and design tokens | design | 1,200 |
| mongodb | Query and manage MongoDB databases and collections | database | 1,100 |
| grafana | Query Grafana dashboards, alerts, and datasources | monitoring | 1,100 |
| gmail | Read and send Gmail messages | communication | 1,100 |
| jira | Manage Jira issues, sprints, and project boards | project-management | 1,000 |
| terminal | Execute shell commands and terminal operations securely | devtools | 1,000 |
| mysql | Query and manage MySQL databases | database | 900 |
| pinecone | Manage Pinecone vector databases for AI/ML applications | ai | 900 |
| datadog | Query Datadog metrics, monitors, and APM traces | monitoring | 900 |
| google-drive | Search, read, and manage Google Drive files | productivity | 900 |
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
| shopify | Manage Shopify stores, products, and orders | ecommerce | 600 |
| airtable | Read and manage Airtable bases, tables, and records | database | 500 |
| hubspot | Manage HubSpot CRM contacts, deals, and companies | crm | 500 |
| 0xmonaco-mcp-server | MCP server for the Monaco SDK | utilities | 0 |
| 1mcp-agent | One MCP server to aggregate them all - A unified Model Context Protocol server implementation | ai | 0 |
| 2digits-tlo-mcp | MCP (Model Context Protocol) server for TeamLeader Orbit (TLO) - project management and time tracking. | devtools | 0 |
| aborruso-ckan-mcp-server | MCP server for interacting with CKAN open data portals | utilities | 0 |
| adamik-signer-mcp-server | This is an [MCP (Model Context Protocol)](https://github.com/modelcontextprotocol/spec) server that provides digital signature capabilities for blockchain transactions. It is designed to work **in tandem with** the `adamik-mcp-server`, which handles trans | devtools | 0 |
| adenot-mcp-google-search | A Model Context Protocol server for Google Search | search | 0 |
| adisuryanathanael-mcp-server-filesystem2 | MCP-compatible server tool for filesystem access from https://github.com/adisuryanathan/modelcontextprotocol-servers.git | devtools | 0 |
| adpharm-mcp-server-filesystem-ro | Read-only MCP server for filesystem access (fork of @modelcontextprotocol/server-filesystem) | filesystem | 0 |
| adrkit-mcp | Local, read-only Model Context Protocol server exposing adrkit decision retrieval over stdio. | utilities | 0 |
| affine-mcp-server | Model Context Protocol server for AFFiNE - enables AI assistants to interact with AFFiNE workspaces, documents, and collaboration features. | ai | 0 |
| agent-infra-mcp-server-browser | MCP server for browser use access | browser | 0 |
| agent-inspect-mcp-server | Read-only MCP server for local AgentInspect TraceFacts, causal failure, and Evidence tools | ai | 0 |
| agent-install | Install SKILL.md files, MCP servers, and AGENTS.md guidance for any coding agent. Ships both a Node API and a CLI. | filesystem | 0 |
| agent5ive-mcp | An MCP server for Agent5ive, built with the official @modelcontextprotocol/sdk. | utilities | 0 |
| agentage-server-memory | The agentage Memory MCP server: exposes your local vaults as the frozen 6 memory__* tools over stdio. The open, cross-vendor counterpart to @modelcontextprotocol/server-memory. | memory | 0 |
| agentation-mcp | MCP server for Agentation - visual feedback for AI coding agents | database | 0 |
| agentcat | Analytics tool for MCP (Model Context Protocol) servers and AI agents - tracks tool usage patterns and provides insights | ai | 0 |
| agenticpay-mcp-bridge | Real MCP server (stdio + @modelcontextprotocol/sdk) that exposes x402-paywalled HTTP endpoints as MCP tools. Drop into Claude Desktop, Cursor, or any MCP client. | web | 0 |
| agentproto-driver-mcp | agentproto/mcp-runtime — AIP-32 MCP provider specialisation. Sugar over @agentproto/driver for Model Context Protocol servers (stdio/SSE/HTTP transports). v0.1 ships frontmatter-driven dispatch; full MCP client wraps @modelcontextprotocol/sdk in v0.2. | web | 0 |
| agimon-ai-log-sink-mcp | Log sink MCP server with HTTP ingestion and AI analysis | web | 0 |
| agimon-ai-workflow-mcp | MCP server for running GitHub Actions workflows locally | devtools | 0 |
| ahrefs-mcp | Ahrefs MCP server | utilities | 0 |
| ai-mentora-mcp-server | MCP server for AI Mentora, compatible with ModelContextProtocol. Provides es-fulltext-retrieve tool for Canadian case law search. | search | 0 |
| aikidosec-mcp | Aikido MCP server | ai | 0 |
| ainative-memory-mcp | Enhanced MCP server-memory with ZeroDB cloud persistence and semantic vector search. Drop-in replacement for @modelcontextprotocol/server-memory that stores your knowledge graph in the cloud instead of local JSONL files. | database | 0 |
| ainative-postgres-mcp | Zero-config Postgres MCP server with auto-provisioning. Drop-in replacement for @modelcontextprotocol/server-postgres — no DATABASE_URL needed. Auto-provisions a managed PostgreSQL instance with pgvector on first run. | database | 0 |
| aiondadotcom-mcp-ssh | MCP Agent for managing SSH hosts - A Model Context Protocol server for SSH operations | ai | 0 |
| airtable-mcp-server | A Model Context Protocol server that provides read and write access to Airtable databases. This server enables LLMs to inspect database schemas, then read and write records. | database | 0 |
| akoskomuves-appstoreconnect-mcp | Model Context Protocol server for the Apple App Store Connect API. | ai | 0 |
| akutishevsky-lunchmoney-mcp | Model Context Protocol server for LunchMoney personal finance management | ai | 0 |
| alchemy-mcp-server | MCP server for using Alchemy APIs | ai | 0 |
| alcyone-labs-modelcontextprotocol-sdk | Upgrade to Zod V4 for Model Context Protocol implementation for TypeScript | utilities | 0 |
| alfe.ai-github-mcp | GitHub MCP proxy server — bridges the official @modelcontextprotocol/server-github with Alfe OAuth credentials (Pattern A multi-account) | devtools | 0 |
| amap-amap-maps-mcp-server | MCP server for using the AMap Maps API | utilities | 0 |
| aml-modelcontextprotocol-aml-watcher-mcp | MCP server for AML Watcher API search | search | 0 |
| amltemp-modelcontextprotocol-aml-watcher-mcp | MCP server for AML Watcher API search | search | 0 |
| ampersend-ai-modelcontextprotocol-sdk | Model Context Protocol implementation for TypeScript | ai | 0 |
| amplitude-mcp-analytics | Amplitude MCP Analytics SDK - MCP server usage tracking for Amplitude Analytics | utilities | 0 |
| angelogiacco-elevenlabs-mcp-server | An ElevenLabs MCP server | utilities | 0 |
| anki-mcp-http | Model Context Protocol server for Anki - enables AI assistants to interact with your Anki flashcards | communication | 0 |
| ankimcp-anki-mcp-server | Model Context Protocol server for Anki - enables AI assistants to interact with your Anki flashcards | communication | 0 |
| api-now-mcp | API Now Model Context Protocol Server | utilities | 0 |
| apify-actors-mcp-server | Apify MCP Server | utilities | 0 |
| apple-shortcuts | MCP server for automation using Apple Shortcuts | utilities | 0 |
| arabold-docs-mcp-server | MCP server for fetching and searching documentation | search | 0 |
| arc-mcp-xsuaa-auth | XSUAA / OAuth authentication + BTP principal propagation for Model Context Protocol (MCP) servers built on Express and @modelcontextprotocol/sdk. | utilities | 0 |
| argocd-mcp | Argo CD MCP Server | devtools | 0 |
| arizeai-phoenix-mcp | A MCP server for Arize Phoenix | ai | 0 |
| atomicmail-mcp-modelcontextprotocol | Atomic Mail MCP server — local stdio proxy with PoW auth and JMAP, for AI agents. (modelcontextprotocol install channel) | communication | 0 |
| auth | Plug and play auth for Model Context Protocol (MCP) servers | utilities | 0 |
| auth0-auth0-mcp-server | Auth0 Model Context Protocol (MCP) Server (Beta) — A secure and extendable implementation of an MCP server that provides AI assistants with controlled access to the Auth0 Management API through natural language. This project is in beta and not intended fo | ai | 0 |
| autotel-mcp-instrumentation | OpenTelemetry instrumentation for Model Context Protocol (MCP) with distributed tracing support | monitoring | 0 |
| aventurevc-mcp-server | MCP server that gives AI assistants access to aVenture research data on companies, people, funding, and news. | search | 0 |
| awesome-copilot-mcp | Model Context Protocol server for awesome-copilot agents and collections | devtools | 0 |
| aws-nx-plugin-mcp | A lightweight, standalone MCP (Model Context Protocol) server for the [Nx Plugin for AWS](https://github.com/awslabs/nx-plugin-for-aws). | devtools | 0 |
| axe-mcp-server | Axe DevTools accessibility analysis and remediation MCP Server for AI coding agents | devtools | 0 |
| azure-devops-mcp | MCP server for interacting with Azure DevOps | devtools | 0 |
| azure-mcp | Azure MCP Server - Model Context Protocol implementation for Azure | cloud | 0 |
| azure-mcp-darwin-arm64 | Azure MCP Server - Model Context Protocol implementation for Azure, for darwin on arm64 | cloud | 0 |
| azure-mcp-linux-x64 | Azure MCP Server - Model Context Protocol implementation for Azure, for linux on x64 | cloud | 0 |
| azure-mcp-win32-x64 | Azure MCP Server - Model Context Protocol implementation for Azure, for win32 on x64 | cloud | 0 |
| backlog-mcp-server | [![MCP Toplist](https://mcptoplist.com/badge/glama%2Fnulab%2Fbacklog-mcp-server.svg)](https://mcptoplist.com/server/glama%2Fnulab%2Fbacklog-mcp-server) ![MIT License](https://img.shields.io/badge/license-MIT-green.svg) ![Build](https://github.com/nulab/ba | devtools | 0 |
| baldim-mcp | Model Context Protocol server for Baldim documentation and databases. | database | 0 |
| bannerbear-mcp | Model Context Protocol server for the Bannerbear V5 API | utilities | 0 |
| basic-preact ⭐ | Basic MCP App Server example using Preact | utilities | 0 |
| basic-react ⭐ | Basic MCP App Server example using React | utilities | 0 |
| basic-solid ⭐ | Basic MCP App Server example using Solid | utilities | 0 |
| basic-svelte ⭐ | Basic MCP App Server example using Svelte | utilities | 0 |
| basic-vanillajs ⭐ | Basic MCP App Server example using vanilla JavaScript | utilities | 0 |
| basic-vue ⭐ | Basic MCP App Server example using Vue | utilities | 0 |
| battlegrid-mcp-server | BattleGrid MCP server — play crypto prediction games from AI agents | ai | 0 |
| bc-telemetry-buddy-mcp | Model Context Protocol server for Business Central telemetry | utilities | 0 |
| benchmark-mcp | Load test a Model Context Protocol server with random or scripted tools and parameters | ai | 0 |
| bennapp-modelcontextprotocol-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| berthojoris-mcp-mysql-server | Model Context Protocol server for MySQL database integration with dynamic per-project permissions | database | 0 |
| besales-mcp | Model Context Protocol server for Animaly / Besales | utilities | 0 |
| better-auth-mcp | Model Context Protocol (MCP) plugin for Better Auth | utilities | 0 |
| better-unraid-mcp | A complete, maintained Model Context Protocol server for the Unraid GraphQL API. | ai | 0 |
| big-whale-labs-modelcontextprotocol-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| bitrix24-tasks-mcp-server | Bitrix24 MCP server for tasks, projects, users, and CRM | project-management | 0 |
| bitwarden-mcp-server | Bitwarden MCP Server | utilities | 0 |
| bmad-mcp-server | Model Context Protocol server for BMAD methodology | ai | 0 |
| borodutch-modelcontextprotocol-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| brave-brave-search-mcp-server | Brave Search MCP Server: web results, images, videos, rich results, AI summaries, and more. | search | 0 |
| bretterer-forge-mcp-server | Laravel Forge MCP server for managing servers, sites, and deployments | utilities | 0 |
| brightspace-mcp-server | MCP server for Brightspace (D2L). Check grades, due dates, assignments, announcements, syllabus, rosters and more via Claude, ChatGPT, Cursor, Windsurf, or any MCP client. | communication | 0 |
| browserless.io-mcp | MCP (Model Context Protocol) server for the Browserless.io browser automation platform | browser | 0 |
| browsermcp-mcp | MCP server for browser automation using Browser MCP | browser | 0 |
| browserstack-mcp-server | BrowserStack's Official MCP Server | browser | 0 |
| budget-allocator ⭐ | Budget allocator MCP App Server with interactive visualization | utilities | 0 |
| bugsnag-mcp-server | A Bugsnag MCP server for interacting with Bugsnag API | ai | 0 |
| buildpad-mcp | Model Context Protocol server for Buildpad components - enables AI agents to discover and use Buildpad packages | ai | 0 |
| burtthecoder-mcp-shodan | A Model Context Protocol server for Shodan API queries. | ai | 0 |
| cap-js-mcp-server | Model Context Protocol (MCP) server for AI-assisted development of CAP applications. | devtools | 0 |
| cclsp | MCP server for accessing LSP functionality | utilities | 0 |
| centia-io-mcp-server | Centia MCP Server | utilities | 0 |
| chatwork-mcp-server | MCP (Model Context Protocol) server for operating Chatwork from AI | communication | 0 |
| chessceo-mcp | Model Context Protocol server for chess.ceo — 11.7M+ games, ~1.5M FIDE player profiles, opening preparation, live broadcasts. | ai | 0 |
| chrome-devtools-mcp | MCP server for Chrome DevTools | devtools | 0 |
| clado-ai-mcp | Clado Model Context Protocol Server | web | 0 |
| claude-flow-mcp | Standalone MCP (Model Context Protocol) server - stdio/http/websocket transports, connection pooling, tool registry | web | 0 |
| claudexor-mcp-server | MCP server exposing durable Claudexor run, status, cancel, result, and interaction tools. | utilities | 0 |
| clipform-mcp-server | MCP server for building and managing Clipform video forms | utilities | 0 |
| cls-mcp-server | [![npm version](https://img.shields.io/npm/v/cls-mcp-server)](https://www.npmjs.com/package/cls-mcp-server) [![license](https://img.shields.io/npm/l/cls-mcp-server)](https://github.com/Tencent/cls-mcp-server/blob/v1.2.1/LICENSE) | devtools | 0 |
| cmd8-excalidraw-mcp | Model Context Protocol server for Excalidraw diagrams. | utilities | 0 |
| cmssy-mcp-server | MCP server for Cmssy CMS — enables AI-driven page creation and management | ai | 0 |
| cocal-google-calendar-mcp | Google Calendar MCP Server with extensive support for calendar management | ai | 0 |
| coda-mcp | MCP Server for Coda | utilities | 0 |
| code-review-mcp-server | MCP Server with Code Review | devtools | 0 |
| code-runner | Code Runner MCP Server | utilities | 0 |
| codecov-mcp-server | A Codecov Model Context Protocol server | utilities | 0 |
| codex-mcp-server | MCP server wrapper for OpenAI Codex CLI | ai | 0 |
| cogenta-mcp | MCP (Model Context Protocol) server and client — the tool registry, exposed. | utilities | 0 |
| cognitionai-metabase-mcp-server | A Model Context Protocol server for Metabase integration | ai | 0 |
| cohort-heatmap ⭐ | Cohort heatmap MCP App Server for retention analysis | utilities | 0 |
| coinbase-cds-mcp-server | Coinbase Design System - MCP Server | utilities | 0 |
| composiohq-modelcontextprotocol-typescript-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| considered-harmful | Most [MCP servers](https://github.com/modelcontextprotocol/servers) suggest using `npx -y` as the recommended way to install a server. This downloads and executes arbitrary scripts from the internet. This is grossly insecure and I think the MCP authors sh | devtools | 0 |
| contentful-mcp-server | Contentful MCP Server - Model Context Protocol server for Contentful | utilities | 0 |
| contextflo-postgres-mcp | Read-only Postgres MCP server: a drop-in replacement for the archived @modelcontextprotocol/server-postgres, with schema context for correct answers. | database | 0 |
| contextstream-mcp-server | Verified npm launcher for the open-source ContextStream Rust MCP server | devtools | 0 |
| crewhaus-mcp-server | Project a compiled bundle's turn function as an MCP server (stdio + SSE) — a chat/invoke tool plus optional per-sub-agent tools delegating to an injected invoke fn, built on @modelcontextprotocol/sdk | communication | 0 |
| currents-mcp | Currents MCP server | browser | 0 |
| currikon-mcp | Model Context Protocol server for the Currikon curriculum API | utilities | 0 |
| customer-segmentation ⭐ | Customer segmentation MCP App Server with filtering | utilities | 0 |
| cyanheads-git-mcp-server | A secure and scalable Git MCP server enabling AI agents to perform comprehensive Git version control operations via STDIO and Streamable HTTP. | devtools | 0 |
| dakatan-mcp-mattermost | MCP (Model Context Protocol) server for Mattermost | utilities | 0 |
| dandeliongold-server-everything | Demo MCP server that exercises all the features of the MCP protocol. This server is a fork of @modelcontextprotocol/servers by Anthropic, PBC with extended functionality for testing MCP clients. | ai | 0 |
| dankelleher-modelcontextprotocol-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| dapp-local-mcp | A stdio MCP server using @modelcontextprotocol/sdk | utilities | 0 |
| datadog-mcp-server | MCP Server for Datadog API | monitoring | 0 |
| dataforseo-mcp-server | CLI and MCP server for DataForSEO API — browse documentation and make authenticated API requests | cloud | 0 |
| davewind-mysql-mcp-server | A Model Context Protocol server for MySQL | database | 0 |
| davinci-resolve-mcp | NPM bootstrapper for the DaVinci Resolve MCP Server. | utilities | 0 |
| dbx-app-mcp-server | MCP server for DBX — query databases from Claude Code, Cursor, and other AI agents | database | 0 |
| de-otio-repo-aegis-mcp | Model Context Protocol server wrapping repo-aegis as agent-readable tools | utilities | 0 |
| dealx-mcp-server | MCP Server for DealX platform | utilities | 0 |
| debug ⭐ | Debug MCP App Server for testing all SDK capabilities | utilities | 0 |
| decodo-mcp-server | Decodo MCP Server | utilities | 0 |
| deepl-mcp-server | MCP server for DeepL translation API | ai | 0 |
| deepseek | DeepSeek MCP Server - Model Context Protocol server for DeepSeek API | ai | 0 |
| delorenj-mcp-server-ticketmaster | A Model Context Protocol server for discovering events, venues, and attractions through the Ticketmaster Discovery API | utilities | 0 |
| delorenj-mcp-server-trello | An MCP server for Trello boards, powered by Bun for maximum performance. | productivity | 0 |
| democratize-technology-vikunja-mcp | Model Context Protocol server for Vikunja task management | ai | 0 |
| dennisk2025-text-alternating-case | Transforms input text so that letters alternately switch between uppercase and lowercase, starting with uppercase. MCP server for Claude Desktop and modelcontextprotocol. | utilities | 0 |
| depup-modelcontextprotocol--core | Model Context Protocol for TypeScript — public Zod schemas (spec + OAuth/OpenID) (with updated dependencies) | utilities | 0 |
| depup-modelcontextprotocol--sdk | Model Context Protocol implementation for TypeScript (with updated dependencies) | utilities | 0 |
| depup-modelcontextprotocol--server | Model Context Protocol implementation for TypeScript - Server package (with updated dependencies) | utilities | 0 |
| dev-boy-mcp-stdio-server | Native STDIO MCP server for Dev Boy - GitLab integration using @modelcontextprotocol/sdk | devtools | 0 |
| devflow-tools-mcp-server | Model Context Protocol server exposing DevFlow context, memory, knowledge, and workflow tools. | devtools | 0 |
| dexpaprika-mcp | A Model Context Protocol server for DexPaprika cryptocurrency data with network-specific pool queries | ai | 0 |
| diagrampilot-mcp | Model Context Protocol server for DiagramPilot. | devtools | 0 |
| dialpad-dialtone-mcp-server | MCP Server for Dialtone Design System | utilities | 0 |
| directus-content-mcp | Model Context Protocol server for Directus projects. | ai | 0 |
| djankies-vitest-mcp | A Model Context Protocol server for Vitest test execution and management | ai | 0 |
| dockbrain-mcp-filesystem-demo | Dies ist ein Demo-Paket für Dockbrain, das den `@modelcontextprotocol/server-filesystem` verwendet,  um Dokumente aus einem Dateisystem über das Model Context Protocol bereitzustellen. | ai | 0 |
| dockndevai-mcp-kubernetes | Model Context Protocol server for Kubernetes — multi-cluster access with security modes and access-control flags. | devtools | 0 |
| document-mcp | MCP (Model Context Protocol) server exposing documents.js's document-conversion, .odb, metadata, and font tooling as MCP tools. | database | 0 |
| documonster-mcp | Model Context Protocol server for documonster — lets AI assistants read, write and convert Excel, Word, PDF, CSV and ZIP documents. | ai | 0 |
| docusaurus-plugin-mcp-server | A Docusaurus plugin that exposes an MCP server endpoint for AI agents to search and retrieve documentation | search | 0 |
| doist-todoist-mcp | The official Todoist MCP server | ai | 0 |
| doitintl-doit-mcp-server | DoiT official MCP Server | utilities | 0 |
| dokploy-mcp | MCP Server for Dokploy API | utilities | 0 |
| dopplerhq-mcp-server | MCP server for Doppler API with auto-generated tools from OpenAPI specification | utilities | 0 |
| drawio-mcp | Official draw.io MCP server for LLMs - Open diagrams in draw.io editor | ai | 0 |
| driflyte-mcp-server | MCP Server for Driflyte | web | 0 |
| drip-apex-mcp-server | Model Context Protocol server for managing Apex experiments, goals, brand context, and QA previews. | utilities | 0 |
| dsh-plug-mcp | DeepSeek Harness 的 MCP 服务管理器：在 设置 → 插件 → MCP 标签页中发现 GitHub 上的 MCP 服务仓库（topic:mcp-server / modelcontextprotocol），探测 npm / PyPI 发布状态与 README 启动线索，详情查看后一键安装 / 移除。服务以 @deepseek-ai/dsh-mcp-client 行登记进 cordis.patch.yml，HMR 热重载，无需重启。支持 GitHub 代理。 | devtools | 0 |
| duckduckgo-mcp-server | A TypeScript-based MCP server that provides DuckDuckGo search functionality. | search | 0 |
| echo-server | A minimal MCP server template that echoes messages | utilities | 0 |
| edicarlos.lds-businessmap-mcp | Model Context Protocol server for BusinessMap (Kanbanize) integration | utilities | 0 |
| ee-mcp-server | Model Context Protocol server for Evolution Engineering | database | 0 |
| ehrocks-fe-mcp-server | MCP server for searching Hero Design System components | search | 0 |
| elgato-mcp-server | A Model Context Protocol (MCP) server that bridges AI assistants with Elgato apps. | ai | 0 |
| elijahtynes-reliefweb-mcp-server | ModelContextProtocol (MCP) server for ReliefWeb humanitarian information service | web | 0 |
| enfyra-mcp-server | MCP server for Enfyra - manage Enfyra instances from MCP-compatible coding tools | utilities | 0 |
| enhanced-postgres-mcp-server | Enhanced PostgreSQL MCP server with read and write capabilities. Based on @modelcontextprotocol/server-postgres by Anthropic. | database | 0 |
| epic-web-workshop-mcp | An MCP (Model Context Protocol) server intended for use inside Epic Workshop repositories. | web | 0 |
| ericthered926-duckduckgo-mcp-server | A Model Context Protocol (MCP) server for DuckDuckGo web and news search | search | 0 |
| esaio-esa-mcp-server | Official MCP server for esa.io - STDIO transport version | ai | 0 |
| eslint-mcp | MCP server for ESLint | utilities | 0 |
| euqns-nudge-mcp | Model Context Protocol server for the Nudge board (the in-house Trello). | utilities | 0 |
| european-parliament-mcp-server | Model Context Protocol server for European Parliament open data | ai | 0 |
| evals | GitHub Action for evaluating MCP server tool calls using LLM-based scoring | devtools | 0 |
| everything ⭐ | MCP server that exercises all the features of the MCP protocol | utilities | 0 |
| excalidraw-mcp | MCP server for Excalidraw | ai | 0 |
| expander-mcp-server | Model Context Protocol server for the Exmachine External API | utilities | 0 |
| expo-docs-mcp | Model Context Protocol server for Expo documentation | ai | 0 |
| ezmodo-mcp-server | MCP server for ezmodo - AI-first project management | ai | 0 |
| f4ww4z-mcp-mysql-server | A Model Context Protocol server for MySQL database operations | database | 0 |
| fangjunjie-ssh-mcp-server | SSH-based MCP Server (基于 SSH 的 MCP 服务器) | utilities | 0 |
| fanyangmeng-ghost-mcp | MCP server for using the Ghost API | utilities | 0 |
| feishu-mcp | Model Context Protocol server for Feishu integration | utilities | 0 |
| felores-airtable-mcp-server | An Airtable Model Context Protocol Server | ai | 0 |
| ferrfleet-mcp | Model Context Protocol server for FerrFleet: agents, runs, skills | utilities | 0 |
| fetch-typescript | A Model Context Protocol server that provides web content fetching and conversion capabilities | web | 0 |
| ffschrattenecker-tm1-mcp-server | Personal testing fork of flameY3T1/tm1-mcp-server (npm: tm1-mcp-server). Use the original. | utilities | 0 |
| fgv-ts-extras-mcp | Result-integration boundary over @modelcontextprotocol/sdk: connect to MCP servers, discover tools, and adapt them into @fgv/ts-extras ai-assist client tools | ai | 0 |
| figma-context-mcp | Model Context Protocol server for Figma integration with smart position info | utilities | 0 |
| figma-mcp-server | A local MCP server with full Figma REST API coverage. | utilities | 0 |
| flightradar-mcp-server | A Model Context Protocol server for flight tracking and status information | utilities | 0 |
| flint-chart-mcp | Model Context Protocol server for Flint — compile, validate, and render semantic chart specs across supported backends. | ai | 0 |
| forestadmin-mcp-server | Model Context Protocol server for Forest Admin with OAuth authentication | utilities | 0 |
| formfeed-mcp | Model Context Protocol server for Formfeed: list templates, read data schemas, validate and render documents from AI agents. | ai | 0 |
| foundryvtt-mcp | Model Context Protocol server for FoundryVTT integration | ai | 0 |
| frappe-mcp-server | Enhanced Model Context Protocol server for Frappe Framework with comprehensive API instructions and helper tools | ai | 0 |
| ftp | Model Context Protocol server for FTP access | utilities | 0 |
| galaxy-stack-orbit-mcp | Model Context Protocol server for Orbit framework — AI coding agents get framework knowledge, scaffolding, and security review tools | ai | 0 |
| gebrai-gebrai | Model Context Protocol server for GeoGebra mathematical visualization | ai | 0 |
| genkit-ai-mcp | A Genkit plugin that provides interoperability between Genkit and Model Context Protocol (MCP). Both client and server use cases are supported. | ai | 0 |
| geobio-google-workspace-server | A Model Context Protocol server | utilities | 0 |
| geocoding-ai-mcp | Model Context Protocol server for geocoding | ai | 0 |
| get-technology-inc-jamf-docs-mcp-server | MCP Server for accessing Jamf Documentation (learn.jamf.com) | utilities | 0 |
| getbourdon-mcp-server | Bourdon L6 MCP server (BUSL-1.1) — the facade over @getbourdon/federation that exposes the federation natively to any MCP-aware agent (Claude Code, Codex, Cursor). Faithful port of core/l6_server.py on @modelcontextprotocol/sdk. WIRE-COMPATIBLE with the P | ai | 0 |
| getnarro-mcp-server | MCP (Model Context Protocol) server for AI-assisted Narro presentation creation | ai | 0 |
| gezhe-mcp-server | gezhe ppt mcp server | utilities | 0 |
| git-mcp-server | A Model Context Protocol server | devtools | 0 |
| gitpagedocs-mcp | Model Context Protocol server for Git Page Docs (delegates to @gitpagedocs/tools). Ships TypeScript source; run via tsx. | devtools | 0 |
| godot-mcp-server | MCP server for Godot game engine integration | devtools | 0 |
| goke-mcp | Dynamically generate CLI commands from MCP server tools | utilities | 0 |
| gongrzhe-quickchart-mcp-server | A Model Context Protocol server for generating charts using QuickChart.io | utilities | 0 |
| gongrzhe-server-calendar-autoauth-mcp | A Model Context Protocol server for Google Calendar integration with auto authentication | utilities | 0 |
| gongrzhe-server-gmail-autoauth-mcp | Gmail MCP server with auto authentication support | communication | 0 |
| google-cloud-gcloud-mcp | Model Context Protocol (MCP) Server for interacting with GCP APIs | cloud | 0 |
| google-cloud-mcp | Model Context Protocol server for Google Cloud services | cloud | 0 |
| google-cloud-observability-mcp | MCP Server for GCP environment for interacting with various Observability APIs. | cloud | 0 |
| google-cloud-storage-mcp | Model Context Protocol (MCP) Server for interacting with GCS APIs | cloud | 0 |
| google-jules-mcp-server | Model Context Protocol server for Google's Jules AI coding agent | ai | 0 |
| google-pse-mcp | A Model Context Protocol server for Google Programmable Search Engine (PSE) | search | 0 |
| gorgias-mcp-server | MCP server exposing the full Gorgias helpdesk API to AI assistants | ai | 0 |
| gotillit-local-mcp-server | Local MCP server for Tillit API using @modelcontextprotocol/sdk. Provides 195+ tools and 48+ resources for complete Tillit API access with built-in documentation. | utilities | 0 |
| grackle-ai-mcp | MCP (Model Context Protocol) server for Grackle — translates MCP tool calls to ConnectRPC | ai | 0 |
| graphite-atlas-mcp-server | Model Context Protocol server for Graphite Atlas | memory | 0 |
| graphlit-mcp-server | Graphlit MCP Server | web | 0 |
| graphql-schema | Model Context Protocol server for GraphQL schemas | utilities | 0 |
| grpc-transport | Pluggable gRPC transport for Model Context Protocol (MCP) servers using @modelcontextprotocol/sdk. Protobuf surface aligned with the community mcp-python-sdk-grpc-poc reference. | utilities | 0 |
| gsc | Enhanced Model Context Protocol server for Google Search Console with 25K row limit, regex filters, and automatic quick wins detection | search | 0 |
| guyghost-swarm-dao-mcp | Swarm DAO Model Context Protocol server — exposes DAO governance tools to any MCP-compatible host (Copilot, Claude, Codex, …) | ai | 0 |
| handler | Framework-agnostic HTTP adapter for Model Context Protocol servers | web | 0 |
| hashi-mcp-server | MCP server for Hashi bridges. Wraps @modelcontextprotocol/sdk and exposes one or more bridges as a single MCP server (stdio). | ai | 0 |
| hasna-mementos | Universal memory system for AI agents - CLI + MCP server + library API | database | 0 |
| hasna-todos | Universal task management for AI coding agents - CLI + MCP server + interactive TUI | ai | 0 |
| healix-mcp | Model Context Protocol server for Healix — lets AI agents observe and control live wdio-healix-service test sessions | web | 0 |
| helicone-mcp | Model Context Protocol server for Helicone observability platform | ai | 0 |
| hello-world | A simple Hello World MCP server | utilities | 0 |
| heroku-mcp-server | Heroku Platform MCP Server | utilities | 0 |
| hisma-server-puppeteer | Fork and update (v0.6.5) of the original @modelcontextprotocol/server-puppeteer MCP server for browser automation using Puppeteer. | browser | 0 |
| honeycomb-mcp | Model Context Protocol server for Honeycomb | utilities | 0 |
| hono-mcp-server-sse-transport | Server-Sent Events transport for Hono and Model Context Protocol | utilities | 0 |
| hoppscotch-mcp-server | Model Context Protocol server for Hoppscotch API testing platform | ai | 0 |
| hostinger-api-mcp | MCP server for Hostinger API | utilities | 0 |
| hostinger-mcp | MCP server for Hostinger API | utilities | 0 |
| houndly-mcp-server | Houndly MCP Server - Model Context Protocol server for test management | utilities | 0 |
| hourei-mcp-server | MCP server for Japanese law information using e-Gov API | utilities | 0 |
| houtini-brevo-mcp | MCP (Model Context Protocol) server for Brevo email marketing platform with comprehensive analytics | communication | 0 |
| hubspot-mcp-server | MCP Server for developers building HubSpot Apps | devtools | 0 |
| hugeicons-mcp-server | MCP server for Hugeicons search and usage documentation | search | 0 |
| hyperbrowser-mcp | Hyperbrowser Model Context Protocol Server | web | 0 |
| hyperfixi-mcp-server | Model Context Protocol server for HyperFixi hyperscript development | devtools | 0 |
| hypothesi-tauri-mcp-server | A Model Context Protocol server for use with Tauri v2 applications | utilities | 0 |
| ibm-ibmi-mcp-server | A production-grade MCP server for IBM i | database | 0 |
| iconify-mcp-server | MCP server for Iconify | utilities | 0 |
| ifc-lite-mcp | Model Context Protocol server for ifc-lite — agent-native BIM via MCP (stdio + Streamable HTTP) | web | 0 |
| iflow-mcp-garethcott-enhanced-postgres-mcp-server | Enhanced PostgreSQL MCP server with read and write capabilities. Based on @modelcontextprotocol/server-postgres by Anthropic. | database | 0 |
| iflow-mcp-garethcott-enhanced-postgres-mcp-server | Enhanced PostgreSQL MCP server with read and write capabilities. Based on @modelcontextprotocol/server-postgres by Anthropic. | database | 0 |
| iflow-mcp-jageenshukla-hello-world-mcp-server | Welcome to the **Hello World MCP Server**! This project demonstrates how to set up a server using the [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/typescript-sdk) SDK. It includes tools, prompts, and endpoints for handling server | devtools | 0 |
| iflow-mcp-mailgun-mcp-server | [![MCP](https://img.shields.io/badge/MCP-Server-blue.svg)](https://github.com/modelcontextprotocol) | devtools | 0 |
| iflow-mcp-mbadkins-puppeteer-plus-martech | Puppeteer+ MarTech - Enhanced Puppeteer MCP server with specialized digital marketing analytics capabilities. This builds upon the official @modelcontextprotocol/server-puppeteer with tools for analyzing marketing technologies, analytics platforms, tag ma | devtools | 0 |
| iflow-mcp-minecraft-mcp-server | > ⚠️ **CLAUDE DESKTOP DUAL LAUNCH WARNING**: Claude Desktop may sometimes launch MCP servers twice ([known issue](https://github.com/modelcontextprotocol/servers/issues/812)), which can lead to incorrect behavior of this MCP server. If you experience issu | devtools | 0 |
| iflow-mcp-nataliapc-mcp-openmsx | Model context protocol server for openMSX automation and control | utilities | 0 |
| iflow-mcp-puppeteer-mcp-server | Experimental MCP server for browser automation using Puppeteer (inspired by @modelcontextprotocol/server-puppeteer) | browser | 0 |
| iflow-mcp-wizd-airylark-mcp-server | AiryLark的ModelContextProtocol(MCP)服务器，提供高精度翻译API | ai | 0 |
| iflowgate-mcp-server | Flowgate Model Context Protocol server. | utilities | 0 |
| ignex-mcp | Model Context Protocol server for Ignex — agent tooling for build/dev/route/info/openapi/doctor. | devtools | 0 |
| infisical-mcp | Official Infisical MCP Server | utilities | 0 |
| inkdropapp-mcp-server | Inkdrop Model Context Protocol Server | utilities | 0 |
| insforge-mcp | MCP (Model Context Protocol) server for Insforge backend-as-a-service | utilities | 0 |
| instawp-mcp-wp | A Model Context Protocol server for interacting with WordPress. | ai | 0 |
| intangle-mcp-server | Model Context Protocol server for Intangle - AI context that persists across conversations | ai | 0 |
| iobroker-mcp-server | MCP server for ioBroker | utilities | 0 |
| ios-simulator-mcp | MCP server for interacting with the iOS simulator | utilities | 0 |
| ironbee-ai-devtools | MCP Server and CLI for IronBee DevTools | devtools | 0 |
| iterable-mcp | Model Context Protocol server for Iterable API | utilities | 0 |
| ivotoby-openapi-mcp-server | An MCP server that exposes OpenAPI endpoints as resources | utilities | 0 |
| jobot-modelcontextprotocol-typescript-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| joplin-mcp-server | MCP server for Joplin | utilities | 0 |
| jupiterone-jupiterone-mcp | Model Context Protocol server for JupiterOne account rules and rule details | ai | 0 |
| jverneuer-beds24-mcp-server | MCP server + CLI host for Beds24. Depends on beds24-sdk-client (typed API client) and beds24-knowledge (hybrid vector+FTS search). Exposes tools, prompts, and resources for an LLM via @modelcontextprotocol/sdk. | search | 0 |
| karlangas12-mcp-auth-kit | Drop-in OAuthClientProvider wrapper for @modelcontextprotocol/sdk that fixes proactive token refresh, dynamic client registration retry, and trailing-slash resource normalization bugs seen across real MCP clients. | ai | 0 |
| kazuph-mcp-fetch | A Model Context Protocol server that provides web content fetching capabilities with automatic image saving and optional AI display | web | 0 |
| kazuph-mcp-taskmanager | Model Context Protocol server for Task Management | utilities | 0 |
| kekwanulabs-syncline-mcp-server | Model Context Protocol server for Syncline - AI-powered meeting scheduling | ai | 0 |
| kentico-management-api-mcp | Model Context Protocol server for Xperience by Kentico Management API | utilities | 0 |
| keygate | Monetize your MCP server in 60 seconds: API keys, plans, usage metering, and rate limits for any @modelcontextprotocol/sdk server — fully local, no cloud account required. | cloud | 0 |
| kibi-mcp | Model Context Protocol server for Kibi knowledge base | utilities | 0 |
| kintone-mcp-server | The official MCP Server for kintone | utilities | 0 |
| kkaminsk-modelcontextprotocol | MCP server for the Perplexity API Platform (fork of @perplexity-ai/mcp-server) | ai | 0 |
| knip-mcp | Knip MCP Server | utilities | 0 |
| knowledge01-mcp | Model Context Protocol server giving agents access to knowledge namespaces | memory | 0 |
| kolide-mcp-server | Model Context Protocol server for Kolide security platform | devtools | 0 |
| komodo-mcp-server | Model Context Protocol Server for Komodo (Container Manager) | devtools | 0 |
| korala-mcp | Model Context Protocol server for Korala: lets AI assistants prepare, send and track signing requests | ai | 0 |
| kubernetes-mcp-server | Model Context Protocol (MCP) server for Kubernetes and OpenShift | devtools | 0 |
| kubernetes-mcp-server-linux-amd64 | Model Context Protocol (MCP) server for Kubernetes and OpenShift | devtools | 0 |
| kubun-mcp | MCP server for Kubun | utilities | 0 |
| kya-os-mcp-i | The TypeScript MCP framework with identity features built-in | utilities | 0 |
| langsmith-mcp-server | LangSmith MCP Server - TypeScript implementation | utilities | 0 |
| last9-mcp-server | Last9 MCP Server - Model Context Protocol server implementation for Last9 | ai | 0 |
| launchsecure-launch-sdk | Typed server-side client for LaunchSecure's MCP. Wraps @modelcontextprotocol/sdk with PAT auth and typed helpers (feedback, work items, comments, etc.). | database | 0 |
| lazy-auth ⭐ | MCP App example demonstrating lazy (on-demand) OAuth: public tools work unauthenticated, protected tools return 401 + WWW-Authenticate so the host runs the OAuth flow only when needed | utilities | 0 |
| lerianstudio-matcher-mcp | Model Context Protocol server for the Matcher reconciliation engine | utilities | 0 |
| libtmux-mcp | Model Context Protocol server for tmux, built on libtmux. | devtools | 0 |
| lightsage-mcp-tracker | Track MCP tool calls from AI agents. Works with @modelcontextprotocol/sdk, FastMCP, and custom servers. | ai | 0 |
| likec4-mcp | Model Context Protocol server for LikeC4 | utilities | 0 |
| linea-mcp | A Model Context Protocol server for interacting with the Linea blockchain | ai | 0 |
| linear-mcp-server | A Model Context Protocol server for the Linear API. | project-management | 0 |
| linkd-mcp | Linkd Model Context Protocol Server | web | 0 |
| linkup-mcp-server | Linkup MCP server for web search | search | 0 |
| listmonk-ops-mcp | Listmonk Model Context Protocol Server using Hono | utilities | 0 |
| llmindset-hf-mcp-server | Official Hugging Face MCP Server | ai | 0 |
| logicmonitor-mcp-server | LogicMonitor Model Context Protocol Server | devtools | 0 |
| loopctl-mcp-server | MCP server for loopctl — structural trust for AI development loops | devtools | 0 |
| lostgradient-mcp | A Model Context Protocol server engine: registries, scope vocabularies, and an OAuth-ready request boundary. | utilities | 0 |
| lsp-mcp-server | MCP server bridging Claude Code to Language Server Protocol servers | utilities | 0 |
| luis-neira-mtn7-mcp-server | An MCP (modelcontextprotocol.io) server that serves a local, offline snapshot of the Mantine v7 documentation over stdio. Built on the official @modelcontextprotocol/sdk; reads its data from bundled local files instead of fetching from mantine.dev. | devtools | 0 |
| lumeo-ui-mcp-server | Model Context Protocol server for the Lumeo Blazor component library. Lets LLMs (Claude, Copilot, Cursor) author correct Lumeo markup. | ai | 0 |
| lunora-mcp | Model Context Protocol server exposing a Lunora deployment to AI agents | cloud | 0 |
| mackerel-mcp-server | A Model Context Protocol server for interacting with Mackerel | utilities | 0 |
| macula-io-mcp | Model Context Protocol server that exposes the Macula mesh to any agent harness | ai | 0 |
| magicpod-mcp-server | Model Context Protocol server for MagicPod integration | utilities | 0 |
| magneticwatermelon-mcp-toolkit | Build and ship **[Model Context Protocol](https://github.com/modelcontextprotocol)** (MCP) servers with zero-config ⚡️. | devtools | 0 |
| maildev-mcp | MCP (Model Context Protocol) server for Claude integration with MailDev | devtools | 0 |
| mailjet-mailjet-mcp-server | [![MCP](https://img.shields.io/badge/MCP-Server-blue.svg)](https://github.com/modelcontextprotocol) | devtools | 0 |
| makafeli-n8n-workflow-builder | Model Context Protocol server for n8n workflow management | utilities | 0 |
| mako10k-mcp-shell-server | Model Context Protocol server for shell command execution, terminal sessions, and retained output management | devtools | 0 |
| malicious-mcp-server | A deliberately malicious MCP server for E2E testing purposes | utilities | 0 |
| mantine-mcp-server | MCP server for Mantine documentation | ai | 0 |
| map ⭐ | MCP App Server example with CesiumJS 3D globe and geocoding | utilities | 0 |
| mapbox-mcp-server | Mapbox MCP server. | utilities | 0 |
| maple-kit-mcp | Model Context Protocol server that gives an agent Maple's review comments | utilities | 0 |
| markdownify-server | MCP Markdownify Server - Model Context Protocol Server for Converting Almost Anything to Markdown | utilities | 0 |
| markdy-mcp-server | Model Context Protocol server for Markdy diagram validation, transpilation, and generation. | utilities | 0 |
| markup-carve-carve-mcp | Model Context Protocol server for authoring and converting Carve documents | utilities | 0 |
| maroonedsoftware-mcp | Model Context Protocol (MCP) server dispatcher for ServerKit. | utilities | 0 |
| mastra-mcp-docs-server | MCP server for accessing Mastra.ai documentation, changelogs, and news. | ai | 0 |
| matillion-mcp-server | MCP Server for Matillion Data Productivity Cloud Public API integration | cloud | 0 |
| mcp-registry-mcp-obsidian-1 | A server implementation of the [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/protocol) for integrating with [Obsidian](https://obsidian.md/). This allows AI assistants to read, create, and manipulate notes in your Obsidian vault. | devtools | 0 |
| mcp-use-modelcontextprotocol-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| mcpflow.io-mcp | ModelContextProtocol server for enhancing JSON Resumes | ai | 0 |
| mcpjam-sdk | MCP server unit testing, end to end (e2e) testing, and server evals | utilities | 0 |
| mcpweb-org-sdk | Official TypeScript/JavaScript SDK for the MCPaaS platform - A wrapper around the official MCP Server using @modelcontextprotocol/sdk | web | 0 |
| mdavieds-mcp-tmp-files | A local MCP server stub built with the [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk). | devtools | 0 |
| mdedit-mcp-server | Model Context Protocol server for live mdedit.ai document collaboration. | ai | 0 |
| medic | Diagnose broken MCP (Model Context Protocol) server configs before they break your agent silently. | devtools | 0 |
| memberjunction-ai-mcp-server | MemberJunction: Model Context Protocol (MCP) - Server Implementation | ai | 0 |
| memofs-mcp-server | Model Context Protocol server for MemoFS agent integrations. | ai | 0 |
| merkl-mcp | MCP server exposing Merkl opportunities via @modelcontextprotocol/sdk | utilities | 0 |
| meshcpcom-pipe | MCP (Model Context Protocol) Server for MeshCP | utilities | 0 |
| meshy-ai-meshy-mcp-server | MCP server for Meshy AI 3D generation platform | ai | 0 |
| meta-ads-mcp | Model Context Protocol server for Meta Marketing API integration | utilities | 0 |
| mgcrea-mcp-appstore-connect | Model Context Protocol server for the Apple App Store Connect API | utilities | 0 |
| mgcrea-mcp-reddit | Model Context Protocol server for the Reddit API | utilities | 0 |
| mgcrea-mcp-shopify | Model Context Protocol server for the Shopify Admin GraphQL API | utilities | 0 |
| mgcrea-mcp-unifi-network | Model Context Protocol server for the UniFi Network API | utilities | 0 |
| mgcrea-mcp-unifi-protect | Model Context Protocol server for UniFi Protect | utilities | 0 |
| microsoft-clarity-mcp-server | MCP Server for Microsoft Clarity based on data export API | ai | 0 |
| microsoft-devbox-mcp | Model Context Protocol server for Microsoft Dev Box | devtools | 0 |
| microsoft-postgres-mcp | PostgreSQL MCP server for AI assistants over the Model Context Protocol. | database | 0 |
| microsoft-workiq | MCP server for Microsoft 365 Copilot | ai | 0 |
| middy-mcp | Middy middleware for Model Context Protocol server | cloud | 0 |
| mintmcp-slack-mcp-server | MCP server for interacting with Slack, with file upload and download tools | communication | 0 |
| mmxomni | Model Context Protocol server exposing MiniMax image, TTS, music, and video generation endpoints as MCP tools. | ai | 0 |
| modelcontextprotocol-cjs | Model Context Protocol implementation for TypeScript | utilities | 0 |
| modelcontextprotocol-client ⭐ | Model Context Protocol implementation for TypeScript - Client package | utilities | 0 |
| modelcontextprotocol-conformance ⭐ | A framework for testing MCP (Model Context Protocol) client and server implementations against the specification. | ai | 0 |
| modelcontextprotocol-core ⭐ | Model Context Protocol for TypeScript — public Zod schemas (spec + OAuth/OpenID) | utilities | 0 |
| modelcontextprotocol-eval | Model Context Protocol (MCP) evaluation framework and tools | ai | 0 |
| modelcontextprotocol-express ⭐ | Express adapters for the Model Context Protocol TypeScript server SDK - Express middleware | utilities | 0 |
| modelcontextprotocol-ext-apps ⭐ | MCP Apps SDK — Enable MCP servers to display interactive user interfaces in conversational clients. | utilities | 0 |
| modelcontextprotocol-fastify ⭐ | Fastify adapters for the Model Context Protocol TypeScript server SDK - Fastify middleware | utilities | 0 |
| modelcontextprotocol-gemini | Model Context Protocol implementation for TypeScript | utilities | 0 |
| modelcontextprotocol-hono ⭐ | Hono adapters for the Model Context Protocol TypeScript server SDK - Hono middleware | utilities | 0 |
| modelcontextprotocol-inspector ⭐ | The Model Context Protocol Inspector | utilities | 0 |
| modelcontextprotocol-node ⭐ | Model Context Protocol implementation for TypeScript - Node.js middleware | utilities | 0 |
| modelcontextprotocol-sdk ⭐ | Model Context Protocol implementation for TypeScript | utilities | 0 |
| modelcontextprotocol-server ⭐ | Model Context Protocol implementation for TypeScript - Server package | utilities | 0 |
| modelcontextprotocol-server-postgres | MCP server for interacting with PostgreSQL databases | database | 0 |
| modyo-mcp | Unified Modyo MCP Server - Model Context Protocol server for Modyo platform | utilities | 0 |
| mongo-server | A Model Context Protocol server for MongoDB connections | database | 0 |
| mongodb-js-mcp-tools-atlas | Atlas tools for MongoDB MCP server | database | 0 |
| mongodb-js-mcp-tools-mongodb | MongoDB tools for MongoDB MCP server | database | 0 |
| mongodb-mcp-server | MongoDB Model Context Protocol Server | database | 0 |
| monoes-mcp | Standalone MCP (Model Context Protocol) server - stdio/http/websocket transports, connection pooling, tool registry | web | 0 |
| mseep-airylark-mcp-server | AiryLark的ModelContextProtocol(MCP)服务器，提供高精度翻译API | ai | 0 |
| mseep-hyperbrowser-mcp | Hyperbrowser Model Context Protocol Server | web | 0 |
| mseep-mcp-smart-crawler | A command-line tool acting as an MCP (ModelContextProtocol) server, using Playwright to crawl web content for AI models. | web | 0 |
| mseep-mcp-typescript-server-starter | ModelContextProtocol typescript server starter | utilities | 0 |
| mseep-puppeteer-mcp-server | Experimental MCP server for browser automation using Puppeteer (inspired by @modelcontextprotocol/server-puppeteer) | browser | 0 |
| mseep-shadow-cljs-mcp | A Model Context Protocol server for monitoring shadow-cljs builds | monitoring | 0 |
| mseep-verodat-mcp-server | [![MCP](https://img.shields.io/badge/MCP-Server-blue.svg)](https://github.com/modelcontextprotocol) [![smithery badge](https://smithery.ai/badge/@Verodat/verodat-mcp-server)](https://smithery.ai/server/@Verodat/verodat-mcp-server) | devtools | 0 |
| mssql-mcp | MCP Server for MS SQL Server integration with Claude Desktop, Cursor, Windsurf and VS Code | database | 0 |
| mui-mcp | MUI MCP Server | utilities | 0 |
| multicluster-mcp-server | A Model Context Protocol server | utilities | 0 |
| myspec-mcp-server | MySpec MCP server — exposes MySpec platform projects, files and attachments to MCP-aware clients via OAuth-authenticated access tokens. | project-management | 0 |
| mysql-mcp-server | An MCP server that provides read-only access to MySQL databases. | database | 0 |
| mysql-server | A Model Context Protocol server for MySQL database operations | database | 0 |
| nataliapc-mcp-openmsx | Model context protocol server for openMSX automation and control | utilities | 0 |
| negokaz-excel-mcp-server | An MCP server that reads and writes spreadsheet data to MS Excel file | filesystem | 0 |
| neilinger-businessmap-mcp | Model Context Protocol server for BusinessMap (Kanbanize) integration | utilities | 0 |
| nestjs-mcp-server | Modular library for building scalable MCP servers with NestJS, providing decorators and integration patterns as a wrapper for the official MCP TypeScript SDK. | ai | 0 |
| nestm-mcp-auth | OAuth 2.1 authorization-server proxy, Client ID Metadata Documents, and token infrastructure for NestM MCP servers. | utilities | 0 |
| neurodivergent-memory | A Model Context Protocol server for knowledge graphs designed around neurodivergent thinking patterns | memory | 0 |
| nevescloud-mcp-rtc | Reference implementation of the MCP-over-WebRTC transport (see SPEC.md). Implements the @modelcontextprotocol/sdk Transport interface for both server and client, in Node and browser. | web | 0 |
| newrelic-mcp | Model Context Protocol server for New Relic observability platform integration | ai | 0 |
| next-devtools-mcp | Next.js development tools MCP server with stdio transport | devtools | 0 |
| nexus2520-bitbucket-mcp-server | MCP server for Bitbucket API integration - supports both Cloud and Server | cloud | 0 |
| nexus2520-jira-mcp-server | MCP server for Jira API integration - supports Jira Cloud | cloud | 0 |
| nipunibpaaris-modelcontextprotocol-typescript-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| nitrostack-cli | CLI for NitroStack - Create and manage MCP server projects | project-management | 0 |
| nocobase-plugin-mcp-server | An MCP server for building NocoBase systems and supporting business workflows. | ai | 0 |
| nocodb-mcp-server | Model Context Protocol server for nocodb | database | 0 |
| node-red-mcp-server | Model Context Protocol (MCP) server for interacting with Node-RED | ai | 0 |
| notebooklm-mcp-server | Node.js Model Context Protocol server for Google NotebookLM | ai | 0 |
| notionhq-notion-mcp-server | Official MCP server for Notion API | productivity | 0 |
| nozomtechs-grc-mcp | MCP server for the Nozom Cybersecurity GRC Platform â€” exposes GRC API endpoints as Model Context Protocol tools. R-EXTSPEC: @modelcontextprotocol/sdk v1.29.0 â€” https://modelcontextprotocol.io/specification/latest | web | 0 |
| nx-mcp | A Model Context Protocol server implementation for Nx | ai | 0 |
| obsidian | Model Context Protocol server for Obsidian Vaults | utilities | 0 |
| occirank-crazyserp-mcp | Model Context Protocol server for crazyserp API | utilities | 0 |
| occirank-haloscan-server | Model Context Protocol server for Haloscan SEO API | utilities | 0 |
| oevortex-ddg-search | A Model Context Protocol server for web search using DuckDuckGo, IAsk AI, and Monica AI | search | 0 |
| ohah-react-native-mcp-server | MCP server for React Native app automation and monitoring | monitoring | 0 |
| ohos-chrome-devtools-mcp | Thin wrapper that bridges OpenHarmony ArkWeb (via hdc fport) to chrome-devtools-mcp. The OHOS counterpart of @modelcontextprotocol/chrome-devtools. | devtools | 0 |
| okfit-mcp | Model Context Protocol server for okfit: query and understand Open Knowledge Format (OKF) bundles from an agent. | utilities | 0 |
| okx-ai-okx-trade-mcp | OKX MCP Server - Model Context Protocol server for OKX exchange | ai | 0 |
| olaservo-mcp-interceptors | TypeScript SDK for Model Context Protocol interceptors (temp publish — fork of @ext-modelcontextprotocol/interceptors) | utilities | 0 |
| onestep-puppeteer-mcp-server | Experimental MCP server for browser automation using Puppeteer (inspired by @modelcontextprotocol/server-puppeteer) | browser | 0 |
| onlyoffice-docspace-mcp | ONLYOFFICE DocSpace Model Context Protocol Server | utilities | 0 |
| onozaty-redmine-mcp-server | MCP server for Redmine | utilities | 0 |
| open-meteo-mcp-server | Model Context Protocol server for Open-Meteo weather APIs | ai | 0 |
| openai-mcp-extensions | OpenAI extensions for MCP servers and apps. | ai | 0 |
| openapi-mcp-generator | Generates MCP server code from OpenAPI specifications | ai | 0 |
| openapi-mcp-server | MCP server for interacting with openapisearch.com API | search | 0 |
| openbnb-mcp-server-airbnb | MCP server for Airbnb search and listing details | search | 0 |
| opendatalabs-personal-server-ts-mcp | MCP (Model Context Protocol) server for the Vana Personal Server | utilities | 0 |
| openrpc-mcp-server-updated | OpenRPC MCP server - Updated with latest @modelcontextprotocol/sdk for compatibility with newer clients | utilities | 0 |
| ophelio-mcp | Model Context Protocol server for the Ophel.io membership & entitlement API. | utilities | 0 |
| ouedyan-modelcontextprotocol-server-filesystem | MCP server for filesystem access | filesystem | 0 |
| pagespeed | A Model Context Protocol server for Google PageSpeed Insights | utilities | 0 |
| pandacss-mcp | MCP server for Panda CSS AI assistants | ai | 0 |
| paperclipai-mcp-server | Model Context Protocol server for Paperclip. | ai | 0 |
| parlayx-mcp | Model Context Protocol server for the ParlayX prediction-market API. | utilities | 0 |
| pascal-app-mcp | Model Context Protocol server for Pascal 3D editor | ai | 0 |
| pavindulakshan-modelcontextprotocol-typescript-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| pdf ⭐ | MCP server for loading and extracting text from PDF files with chunked pagination and interactive viewer | filesystem | 0 |
| pdf | A Model Context Protocol server for PDF manipulation and operations | ai | 0 |
| pdfgate-mcp-server | PDFGate MCP Server | utilities | 0 |
| penclipai-mcp-server | Model Context Protocol server for Paperclip. | ai | 0 |
| pennivo-mcp-server | Model Context Protocol server for the Pennivo markdown workspace | ai | 0 |
| pepk-mcp-memory-sqlite | Production-ready MCP memory server with SQLite WAL for thread-safe concurrent access. Drop-in replacement for @modelcontextprotocol/server-memory. Prevents race conditions and data loss in multi-session AI agent environments. ACID-compliant knowledge grap | database | 0 |
| perforce-p4plan-mcp | P4 Plan MCP (Model Context Protocol) Server | utilities | 0 |
| pg-mcp-server | A Model Context Protocol server for PostgreSQL databases | database | 0 |
| phantom-mcp-server | MCP Server for Phantom Wallet | utilities | 0 |
| picahq-mcp | A Model Context Protocol Server for Pica | utilities | 0 |
| pikku-modelcontextprotocol | A Pikku MCP server runtime using the official MCP SDK | utilities | 0 |
| pinecone-database-mcp | Model Context Protocol server for Pinecone - enables AI assistants to interact with Pinecone indexes and documentation | database | 0 |
| pinepaper.studio-mcp-server | MCP Server for PinePaper Studio - Create animated graphics with AI | ai | 0 |
| pipedrive-mcp-server | Model Context Protocol server for Pipedrive API integration | utilities | 0 |
| plantuml-mcp-server | MCP server for generating PlantUML diagrams | ai | 0 |
| playcanvas-editor-mcp-server | The PlayCanvas Editor MCP Server | utilities | 0 |
| playwright-mcp-server | MCP server for generating Playwright tests | browser | 0 |
| polygraph-mcp | A Model Context Protocol server for coordinating cross-repository changes via Polygraph | utilities | 0 |
| postgres-mcp-hardened | Secure read-only PostgreSQL MCP server in Rust — a maintained alternative to the deprecated @modelcontextprotocol/server-postgres. Blocks writes at the AST, not with regexes. | database | 0 |
| postman-postman-mcp-server | Postman MCP Server — connect AI agents (Claude Code, Cursor, VS Code Copilot, Gemini CLI) to your Postman collections, specifications, and environments via Model Context Protocol (MCP) | ai | 0 |
| powerplatform-mcp | PowerPlatform Model Context Protocol server | utilities | 0 |
| prefecthq-fastmcp-ts | 🏎️  The official FastMCP TypeScript library - build MCP servers and clients, fast 🏎️ | ai | 0 |
| primer-mcp | An MCP server that connects AI tools to the Primer Design System | ai | 0 |
| processon-mcp-server-processon-node | ProcessOn MCP Server - create mind maps from markdown | utilities | 0 |
| productbrain-mcp | Product Brain — MCP server for AI-assisted product knowledge management | ai | 0 |
| professional-wiki-mediawiki-mcp-server | Model Context Protocol (MCP) server for MediaWiki | utilities | 0 |
| prometheus-mcp | Prometheus MCP Server | utilities | 0 |
| puppeteer-mcp-server | Experimental MCP server for browser automation using Puppeteer (inspired by @modelcontextprotocol/server-puppeteer) | browser | 0 |
| puppeteer-mcp-server-ws | Experimental MCP server for browser automation using Puppeteer (inspired by @modelcontextprotocol/server-puppeteer) | browser | 0 |
| puppeteer-plus-martech | Puppeteer+ MarTech - Enhanced Puppeteer MCP server with specialized digital marketing analytics capabilities. This builds upon the official @modelcontextprotocol/server-puppeteer with tools for analyzing marketing technologies, analytics platforms, tag ma | devtools | 0 |
| qase-mcp-server | Official MCP server for Qase Test Management Platform | ai | 0 |
| questpie-mcp | Model Context Protocol server for QUESTPIE apps, under the app's own access rules | utilities | 0 |
| qwksearch-mcp-server | MCP server exposing web search and content extraction tools via stdio transport | search | 0 |
| razorpay-blade-mcp | Model Context Protocol server for Blade | ai | 0 |
| react-aria-mcp | MCP server for React Aria documentation | utilities | 0 |
| real-browser-mcp-server | MCP Server for Real Browser - Patchright Blocker. | browser | 0 |
| rebasepro-mcp | Model Context Protocol Server for Rebase — exposes schema, DB, document, and user management tools to AI assistants. | database | 0 |
| refrakt-md-mcp | Model Context Protocol server wrapping the refrakt CLI | utilities | 0 |
| regle-mcp-server | MCP Server for Regle | ai | 0 |
| relay-org-relay-mcp | Model Context Protocol server for Relay — deploy, inspect, and control apps from any MCP-aware AI tool | ai | 0 |
| relay-science-mcp | Model Context Protocol server for the Relay scientific platform | utilities | 0 |
| remnux-mcp-server | MCP server for using the REMnux malware analysis toolkit via AI assistants | ai | 0 |
| robinmordasiewicz-f5xc-terraform-mcp | MCP server for F5 Distributed Cloud Terraform provider - documentation, 270+ OpenAPI specs, subscription info, and addon activation workflows for AI assistants | cloud | 0 |
| rolino-mcp | Model Context Protocol server for Rolino | ai | 0 |
| rollbar-mcp-server | Model Context Protocol server for Rollbar | monitoring | 0 |
| roychri-mcp-server-asana | MCP Server for Asana | ai | 0 |
| rtorcato-api-mcp | Tiny result helpers for @modelcontextprotocol/sdk MCP servers. | utilities | 0 |
| runpod-mcp-server | MCP server for interacting with Runpod API | utilities | 0 |
| rushstack-mcp-server | A Model Context Protocol server implementation for Rush | utilities | 0 |
| salesforce-mcp | MCP Server for interacting with Salesforce instances | utilities | 0 |
| sap-mdk-mcp-server | Model Context Protocol (MCP) server for AI-assisted development of MDK applications. | devtools | 0 |
| sap-ux-fiori-mcp-server | SAP Fiori - Model Context Protocol (MCP) server | ai | 0 |
| scenario-modeler ⭐ | Financial scenario modeling MCP App Server | utilities | 0 |
| scitrera-memorylayer-mcp-server | MCP (Model Context Protocol) server for MemoryLayer.ai | ai | 0 |
| scryfall-mcp-server | MCP server for interacting with the Scryfall MTG API | utilities | 0 |
| search-mcp-server | MCP server for browser automation via Jan Browser extension - provides tools for web navigation, interaction, and search | search | 0 |
| searxng | MCP server for SearXNG integration | search | 0 |
| sebastienrousseau-noyalib-mcp | Model Context Protocol server for noyalib YAML tools — parse, format, get, set, validate over JSON-RPC stdio. | ai | 0 |
| sechel-mcp-mcp-server | MCP server factory for Sechel — registers all 24 persistent memory tools (`mem_*` + `ping`) on an [`@modelcontextprotocol/sdk`](https://github.com/modelcontextprotocol/typescript-sdk) server instance. | devtools | 0 |
| securestamp-mcp-guard | SecureStamp MCP Guard — a local stdio + remote MCP wrapper for the SecureStamp Agent Trust Layer. Lets MCP hosts (Claude Desktop, Cursor, any @modelcontextprotocol/sdk client) ask SecureStamp for Proof-of-Intent before sensitive tool calls. Authorizes/ver | utilities | 0 |
| sendlyapi-mcp | Model Context Protocol server for the Sendly API | communication | 0 |
| serper-search-scrape-mcp-server | Serper MCP Server supporting search and webpage scraping | search | 0 |
| server | mcp server | utilities | 0 |
| server-anthropic | A [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol) server that provides access to Anthropic's AI models through their official API. List available models and send messages to Claude using a secure, standardized interface. [More abou | devtools | 0 |
| servers | Welcome to the **Hello World MCP Server**! This project demonstrates how to set up a server using the [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/typescript-sdk) SDK. It includes tools, prompts, and endpoints for handling server | devtools | 0 |
| shadcn-ui-mcp-server | MCP server for shadcn/ui component references | utilities | 0 |
| shadertoy ⭐ | MCP App Server example for rendering ShaderToy-compatible GLSL shaders | utilities | 0 |
| sheet-music ⭐ | MCP App Server for rendering and playing sheet music from ABC notation | utilities | 0 |
| shopify-dev-mcp | A command line tool for setting up Shopify Dev MCP server | devtools | 0 |
| shortcut-mcp | Shortcut MCP Server | utilities | 0 |
| shrkcrft-mcp-server | SharkCraft MCP server: 25 tools over @modelcontextprotocol/sdk's stdio transport. | ai | 0 |
| siemens-element-mcp | Element MCP server | ai | 0 |
| siemens-ix-mcp | iX MCP server | ai | 0 |
| siemens-ix-mcp-angular | iX MCP server for Angular | ai | 0 |
| siemens-ix-mcp-react | iX MCP server for React | ai | 0 |
| sigmacomputing-slack-mcp-server | MCP server for interacting with Slack | communication | 0 |
| sit-onyx-modelcontextprotocol | MCP (Model Context Protocol) Server that provide onyx specific tools and resources. | utilities | 0 |
| sk-calculator-mcp-server | Initialize the project  npm init -y npx gitignore node  npm pkg set type=module npm install @modelcontextprotocol/sdk npm install | devtools | 0 |
| skanda-yutori-mcp-send-email | MCP server for sending emails via Resend API | communication | 0 |
| skyramp-mcp | Skyramp MCP (Model Context Protocol) Server - AI-powered test generation and execution | ai | 0 |
| slack-mcp-server | Model Context Protocol (MCP) server for Slack Workspaces. This integration supports both Stdio and SSE transports, proxy settings and does not require any permissions or bots being created or approved by Workspace admins | communication | 0 |
| slack-workspace-mcp-server | MCP server for Slack workspace integration | communication | 0 |
| slite-mcp-server | 'Slite MCP server' | search | 0 |
| smartbear-mcp | MCP server for interacting SmartBear Products | utilities | 0 |
| smithery-mcp-fetch | A Model Context Protocol server that provides web content fetching capabilities | web | 0 |
| snowflake-mcp-server | Model Context Protocol server for Snowflake database integration | database | 0 |
| softeria-ms-365-mcp-server |  A Model Context Protocol (MCP) server for interacting with Microsoft 365 and Office services through the Graph API | utilities | 0 |
| spartan-ng-mcp | Model Context Protocol server exposing Spartan Angular UI documentation, components, and blocks as AI-consumable tools. | ai | 0 |
| sqlite-npx | [![smithery badge](https://smithery.ai/badge/mcp-server-sqlite-npx)](https://smithery.ai/server/mcp-server-sqlite-npx) [![MseeP.ai Security Assessment Badge](https://mseep.net/mseep-audited.png)](https://mseep.ai/app/johnnyoshika-mcp-server-sqlite-npx) | database | 0 |
| square-mcp-server | MCP Server for Square API | utilities | 0 |
| stdio-oauth | Experimental MCP extension for proactive third-party OAuth readiness discovery on local stdio servers. | utilities | 0 |
| stepsecurity-stepsecurity-mcp | Model Context Protocol server for StepSecurity APIs | utilities | 0 |
| stigmer-mcp-server | Model Context Protocol server for the Stigmer platform — exposes Stigmer agents, skills, MCP servers, and workflows as MCP tools and resources | ai | 0 |
| storybook-mcp | MCP server that serves knowledge about your components based on your Storybook stories and documentation | utilities | 0 |
| stripe-mcp | A command line tool for setting up Stripe MCP server | payments | 0 |
| structured-world-gitlab-mcp | Advanced GitLab MCP server | devtools | 0 |
| sum-modelcontextprotocol-sum-number | MCP server for summing two numbers | utilities | 0 |
| supabase-mcp-server-postgrest | MCP server for PostgREST | database | 0 |
| supabase-mcp-server-supabase | MCP server for interacting with Supabase | utilities | 0 |
| superblocksteam-mcp-server | Superblocks MCP server | utilities | 0 |
| superdoc-mcp | Model Context Protocol server for SuperDoc, giving an AI agent tools to read and edit .docx files. | ai | 0 |
| suthio-redash-mcp | MCP server for Redash integration | ai | 0 |
| svn-agent-mcp | Strict SVN Model Context Protocol server for agent-safe SVN workflows. | utilities | 0 |
| sylphx-workflow-mcp | Stdio MCP server exposing @sylphx/workflow-engine's governed workflows as native MCP tools (official @modelcontextprotocol/sdk transport). A second-mind from outside the host's own model. | ai | 0 |
| system-monitor ⭐ | System monitor MCP App Server with real-time stats | utilities | 0 |
| szc-ft-mcp-szcd-component-helper | MCP server for szcd component library - built with @modelcontextprotocol/sdk, supports stdio/SSE/dual modes | ai | 0 |
| szjc-szjc-mcp-server | MCP Server for the Szjc API using @modelcontextprotocol/sdk | ai | 0 |
| taazkareem-clickup-mcp-server | ClickUp MCP Server - Powering AI Agents with full ClickUp task, document, and chat management capabilities. | communication | 0 |
| tada | Zero-runtime, compile-time typed tool calls derived from a live server's tools/list | utilities | 0 |
| taiga-ui-mcp | Model Context Protocol server providing Taiga UI documentation search and scaffolding tools. | search | 0 |
| tailwindcss-mcp-server | MCP server for TailwindCSS utility classes, documentation, and project assistance | ai | 0 |
| tanstack-ai-mcp | Host-side Model Context Protocol client for TanStack AI: discover and run MCP server tools, resources, and prompts in any adapter's chat() loop, with generated end-to-end types. | communication | 0 |
| tanstack-start | MCP (Model Context Protocol) integration for TanStack Start | ai | 0 |
| tea-color-to-vars-mcp-server | A basic MCP server example using @modelcontextprotocol/sdk | ai | 0 |
| tensor-cad-mcp | Model Context Protocol server for TensorCAD: design, validate, analyze and generate LLM architectures from an agent | ai | 0 |
| tenuo-mcp | Per-call, argument-level authorization for Model Context Protocol (MCP) servers: guard @modelcontextprotocol/server v2 tools with Tenuo warrants (beta). | ai | 0 |
| terraform-mcp-server | MCP server for Terraform Registry operations | utilities | 0 |
| testomatio-mcp | Model Context Protocol server for Testomatio API | utilities | 0 |
| testomatio-mcp-enterprise | Enterprise Model Context Protocol server for Testomat.io API with analytics tools | utilities | 0 |
| theia-ai-mcp-server | Theia - MCP Server | ai | 0 |
| thelabnyc-redmine-mcp | An MCP (Model Context Protocol) server that allows AI agents like Claude to interact with Redmine project management data. | ai | 0 |
| thirdstrandstudio-mcp-figma | MCP server for figma | utilities | 0 |
| threejs ⭐ | Three.js 3D visualization MCP App Server | utilities | 0 |
| thunder-ai-mcp-element-ui | Element Plus 的 ModelContextProtocol (MCP) 服务器 | ai | 0 |
| tickernelz-paperclip-pro-mcp-server | Model Context Protocol server for Paperclip. | utilities | 0 |
| timesheet-mcp | Model Context Protocol server for Timesheet API | utilities | 0 |
| tiny-http-mcp-server | Minimal MCP server over HTTP built on tiny-stdio-mcp-server | web | 0 |
| tiny-stdio-mcp-server | Minimal MCP server over stdio with typed tools and rich content helpers | utilities | 0 |
| titen-memory | Agent memory with no API key, no LLM, and no embedding provider. Serves MCP over stdio against a local SQLite store, or Cloudflare Workers + D1. Drop-in for @modelcontextprotocol/server-memory; every memory keeps its source, its scope, and the evidence th | database | 0 |
| tocharianou-mcp-server-kibana | Kibana MCP Server | devtools | 0 |
| todoforai-puppeteer-mcp-server | Experimental MCP server for browser automation using Puppeteer (inspired by @modelcontextprotocol/server-puppeteer) | browser | 0 |
| ton-mcp | TON MCP Server - Model Context Protocol server for TON blockchain wallet operations | ai | 0 |
| topolo-mcp | Model Context Protocol server for the Topolo platform. Exposes scope-gated tools that third-party agents (Claude, Codex, etc.) can call natively. | utilities | 0 |
| touchdesigner-mcp-server | MCP server for TouchDesigner | utilities | 0 |
| traceloop-instrumentation-mcp | MCP (Model Context Protocol) Instrumentation | utilities | 0 |
| transcend-io-mcp | Transcend MCP Server — unified server with all domain tools. | ai | 0 |
| transcend-io-mcp-server-admin | Transcend MCP Server — Admin tools. | utilities | 0 |
| transcend-io-mcp-server-assessment | Transcend MCP Server — Assessments tools. | utilities | 0 |
| transcend-io-mcp-server-base | Shared infrastructure for Transcend MCP Server packages. | utilities | 0 |
| transcend-io-mcp-server-consent | Transcend MCP Server — Consent Management tools. | utilities | 0 |
| transcend-io-mcp-server-custom-functions | Transcend MCP Server — Custom Functions tools. | utilities | 0 |
| transcend-io-mcp-server-discovery | Transcend MCP Server — Data Discovery tools. | utilities | 0 |
| transcend-io-mcp-server-docs | Transcend MCP Server — Documentation lookup tools. | utilities | 0 |
| transcend-io-mcp-server-dsr | Transcend MCP Server — DSR Automation tools. | utilities | 0 |
| transcend-io-mcp-server-inventory | Transcend MCP Server — Data Inventory tools. | utilities | 0 |
| transcend-io-mcp-server-policy | Transcend MCP Server — Policy Engine tools. | utilities | 0 |
| transcend-io-mcp-server-preferences | Transcend MCP Server — Preference Management tools. | utilities | 0 |
| transcend-io-mcp-server-workflows | Transcend MCP Server — Workflows tools. | utilities | 0 |
| transcript ⭐ | MCP App Server for live speech transcription | utilities | 0 |
| transloadit-mcp-server | Transloadit MCP server | ai | 0 |
| trello | A Model Context Protocol server for Trello | utilities | 0 |
| triliumnext-mcp | A model context protocol server for TriliumNext Notes | utilities | 0 |
| tsmztech-mcp-server-salesforce | A Salesforce connector MCP Server. | ai | 0 |
| turbopuffer-turbopuffer-mcp | The official MCP Server for the Turbopuffer API | utilities | 0 |
| twilio-alpha-mcp | This is a Model Context Protocol server that exposes all of Twilio APIs. | utilities | 0 |
| twilio-alpha-openapi-mcp-server | A Model Context Protocol server that to expose OpenAPI specs. | utilities | 0 |
| typeroll-mcp-server | Typeroll CMS MCP server – connect AI agents to the REST API to manage content and publish static websites. | web | 0 |
| ui5-mcp-server | MCP server for SAPUI5/OpenUI5 development | devtools | 0 |
| ui5-webcomponents-mcp-server | Model Context Protocol server for UI5 Web Components development assistance | devtools | 0 |
| umami-mcp | Model Context Protocol server for Umami analytics. | utilities | 0 |
| unthread-io-mcp-server | Unthread MCP Server | utilities | 0 |
| upstash-mcp-server | MCP server for Upstash | utilities | 0 |
| urbicon-ui-mcp-server | Model Context Protocol server exposing the Urbicon UI component catalog, recipes and design intelligence to LLM agents | ai | 0 |
| user-postgresql-mcp | A PostgreSQL MCP server built with @modelcontextprotocol/sdk. | database | 0 |
| ux-axioms-mcp | UX Axioms Model Context Protocol Server | utilities | 0 |
| vantageos-mcp-boilerplate | Clonable MCP server skeleton: dual-transport bootstrap (stdio + Streamable HTTP, stateless) on the official @modelcontextprotocol/sdk, ready to extend with protocol-kit, auth, tenant and UI layers. | web | 0 |
| vantasdk-vanta-mcp-server | Model Context Protocol server for Vanta's security compliance platform | utilities | 0 |
| variflight-ai-variflight-mcp | Variflight MCP Server | ai | 0 |
| vertex-ai-mcp-server | A Model Context Protocol server supporting Vertex AI and Gemini API | ai | 0 |
| viberevert-mcp | Model Context Protocol server for VibeRevert. | utilities | 0 |
| video-resource ⭐ | MCP App Server demonstrating video resources served as base64 blobs | utilities | 0 |
| villagemetrics-public-ask-anything-mcp | Model Context Protocol server for Village Metrics behavioral tracking data access | utilities | 0 |
| visulima-vis-mcp | MCP (Model Context Protocol) server for @visulima/vis — exposes vis tooling to AI agents over stdio | ai | 0 |
| vitest-agent-mcp | Model Context Protocol server for vitest-agent. Exposes 30 tools for agent access to test data, TDD lifecycle, and session management. | utilities | 0 |
| viyv-mcp-connect | Dial a Viyv MCP Gateway from any MCP server (official @modelcontextprotocol/sdk or otherwise): announce your tools over outbound WebSocket and serve tool calls locally. The TypeScript peer of viyv_mcp's connect mode. | web | 0 |
| vizejs-musea-mcp-server | MCP server for building Vue.js design systems - component analysis, documentation, variant generation, and design tokens | ai | 0 |
| voltagent-mcp-server | VoltAgent MCP server implementation for exposing agents, tools, and workflows via the Model Context Protocol. | utilities | 0 |
| vostride-agent-qa-mcp | Model Context Protocol server and tools for agent-qa authoring and triage. | utilities | 0 |
| vpr99-modelcontextprotocol-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| vuetify-mcp | Model Context Protocol server for Vuetify assistance | ai | 0 |
| web-qiang-aform-mcp | MCP server for @web_qiang/aform: 组件查询、配置生成与字典检索（stdio + Streamable HTTP 双传输，基于 @modelcontextprotocol/server v2）。 | web | 0 |
| weppy-roblox-mcp | MCP (Model Context Protocol) server for Roblox Studio integration - enables AI coding agents to interact with Roblox Studio in real-time | devtools | 0 |
| wiki-explorer ⭐ | Wikipedia link explorer MCP App Server with graph visualization | utilities | 0 |
| williamp29-project-mcp-server | A ModelContextProtocol server to let agents discover your project, such as APIs (using OpenAPI) or other resources. | database | 0 |
| winor30-mcp-server-datadog | MCP server for interacting with Datadog API | monitoring | 0 |
| withone-mcp | A Model Context Protocol Server for One | utilities | 0 |
| wix-mcp | A Model Context Protocol server for Wix AI tools | ai | 0 |
| wocha-mcp | Model Context Protocol server for the Wocha Management API | ai | 0 |
| wonderwhy-er-desktop-commander | MCP server for terminal operations and file editing | devtools | 0 |
| wopal-mcp-server-hotnews | A Model Context Protocol server that provides real-time hot trending topics from major Chinese social platforms and news sites | utilities | 0 |
| xcodebuildmcp | XcodeBuildMCP is a Model Context Protocol server that provides tools for Xcode project management, simulator management, and app utilities. | project-management | 0 |
| xeroapi-xero-mcp-server | MCP server implementation for Xero integration | utilities | 0 |
| xyd-js-mcp-server | MCP server for xyd | utilities | 0 |
| yapi-auto-mcp | YApi Auto MCP Server - Model Context Protocol server for YApi integration, enables AI tools like Cursor to interact with YApi API documentation | ai | 0 |
| yjzf-mcp-server-yjzf | MCP Server for YJZF | utilities | 0 |
| yoda.digital-gitlab-mcp-server | GitLab MCP Server - A Model Context Protocol server for GitLab integration | devtools | 0 |
| youtube-data-mcp-server | YouTube MCP Server Implementation | utilities | 0 |
| ytrynot-mcp-core | Generic MCP server factory + client — declarative tool registry (Standard Schema args: DNA, Zod, JSON Schema + pure handlers) over the @modelcontextprotocol SDK, plus in-process dispatch | utilities | 0 |
| z-ai-mcp-server | MCP Server for Z.AI - A Model Context Protocol server that provides AI capabilities | ai | 0 |
| zapier-zapier-sdk-mcp | MCP server for Zapier SDK | utilities | 0 |
| zd-mcp-server | Zendesk MCP Server - Model Context Protocol server for Zendesk Support integration | ai | 0 |
| zeddotdev-postgres-context-server | a model context protocol server for postgres | database | 0 |
| zencoderai-slack-mcp-server | MCP server for interacting with Slack | communication | 0 |
| zeplin-mcp-server | Zeplin’s official MCP server for AI-assisted UI development | devtools | 0 |
| zereight-mcp-gitlab | GitLab MCP server for projects, merge requests, issues, pipelines, wiki, releases, and more | devtools | 0 |
| zereight-sentry-server | A Model Context Protocol server | monitoring | 0 |
| zero-mcp | Zero-boilerplate, lightweight and fast MCP server toolkit. Skip the weight of `@modelcontextprotocol/sdk` and start shipping MCP servers in minutes with minimal code. | communication | 0 |
| znt-mcp | Model Context Protocol server for znt-core through @znt/sdk-nodejs | search | 0 |
| zubeid-youtube-mcp-server | YouTube MCP Server Implementation | ai | 0 |
| zudello-modelcontextprotocol | MCP server exposing 106 Zudello ERP automation tools for Claude Desktop and other MCP-compatible clients | ai | 0 |
| zuwiki-mcp | Model Context Protocol server for Zuwiki | utilities | 0 |

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
