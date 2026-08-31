# mcpx

> The package manager for MCP servers. Discover, install, and manage Model Context Protocol servers for Claude Code, Cursor, and VS Code.

[![PyPI version](https://img.shields.io/pypi/v/mcpx.svg)](https://pypi.org/project/mcpx/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/LakshmiSravyaVedantham/mcpx/actions/workflows/ci.yml/badge.svg)](https://github.com/LakshmiSravyaVedantham/mcpx/actions)

---

## What is mcpx?

**mcpx** is like `npm` or `brew` -- but for MCP servers. It provides a curated registry of **716+ MCP servers** and lets you install them into Claude Code, Cursor, or VS Code with a single command.

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

- **716+ curated MCP servers** across 21 categories (database, devtools, cloud, AI, etc.)
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

The built-in registry includes 716+ servers across these categories:

| Category | Examples |
|----------|----------|
| AI & ML | Openai, Pinecone, Anthropic, 1Mcp Agent, Abhiz123 Todoist Mcp Server, ... |
| Browser Automation | Puppeteer, Playwright, Agent Infra Mcp Server Browser, Browserless.Io Mcp, Browsermcp Mcp, ... |
| Cloud Providers | Aws, Cloudflare, Azure, Gcp, Azure Mcp, ... |
| Communication | Slack, Twilio, Discord, Gmail, Aipost Mcp Server, ... |
| CRM | Hubspot |
| Databases | Postgres, Sqlite, Redis, Mysql, Mongodb, ... |
| Deployment | Vercel |
| Design | Figma |
| Developer Tools | Github, Docker, Kubernetes, Terminal, Context7, ... |
| E-Commerce | Shopify |
| Filesystem | Filesystem, Adpharm Mcp Server Filesystem Ro, Agent Infra Mcp Server Filesystem, Agent Install, Negokaz Excel Mcp Server, ... |
| Location & Maps | Google Maps |
| Memory & Context | Memory, Agentage Server Memory, Graphite Atlas Mcp Server, Infranodus Mcp Server, Neurodivergent Memory |
| Monitoring | Sentry, Grafana, Datadog, Autotel Mcp Instrumentation, Datadog Mcp Server, ... |
| Payments | Stripe, Stripe Mcp |
| Productivity | Notion, Todoist, Confluence, Google Drive, Delorenj Mcp Server Trello, ... |
| Project Management | Linear, Jira, Fractalizer Mcp Server Yandex Tracker, Linear Mcp Server, Mseep Linear Mcp Server, ... |
| Reasoning | Sequential Thinking |
| Search | Brave Search, Tavily, Adenot Mcp Google Search, Agent Ready Mcp, Ai Mentora Mcp Server, ... |
| Utilities | Time, 0Xmonaco Mcp Server, Aborruso Ckan Mcp Server, Adrkit Mcp, Agent5Ive Mcp, ... |
| Web & Scraping | Fetch, Firecrawl, Agenticpay Mcp Bridge, Agentproto Driver Mcp, Arcote.Tech Arc Mcp, ... |

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
| abhiz123-todoist-mcp-server | MCP server for Todoist API integration | ai | 0 |
| aborruso-ckan-mcp-server | MCP server for interacting with CKAN open data portals | utilities | 0 |
| adamhancock-bullmq-mcp | Model Context Protocol server for BullMQ job queue management | database | 0 |
| adamik-signer-mcp-server | This is an [MCP (Model Context Protocol)](https://github.com/modelcontextprotocol/spec) server that provides digital signature capabilities for blockchain transactions. It is designed to work **in tandem with** the `adamik-mcp-server`, which handles trans | devtools | 0 |
| adenot-mcp-google-search | A Model Context Protocol server for Google Search | search | 0 |
| adisuryanathanael-mcp-server-filesystem2 | MCP-compatible server tool for filesystem access from https://github.com/adisuryanathan/modelcontextprotocol-servers.git | devtools | 0 |
| adpharm-mcp-server-filesystem-ro | Read-only MCP server for filesystem access (fork of @modelcontextprotocol/server-filesystem) | filesystem | 0 |
| adrkit-mcp | Local, read-only Model Context Protocol server exposing adrkit decision retrieval over stdio. | utilities | 0 |
| affine-mcp-server | Model Context Protocol server for AFFiNE - enables AI assistants to interact with AFFiNE workspaces, documents, and collaboration features. | ai | 0 |
| agent-infra-mcp-server-browser | MCP server for browser use access | browser | 0 |
| agent-infra-mcp-server-filesystem | MCP server for filesystem access | filesystem | 0 |
| agent-install | Install SKILL.md files, MCP servers, and AGENTS.md guidance for any coding agent. Ships both a Node API and a CLI. | filesystem | 0 |
| agent-ready-mcp | MCP server for Agent Ready — scan any URL for AI-readability against the Vercel Agent Readability Spec, the llmstxt.org standard, and agent-protocol manifests (MCP server cards, A2A, agents.json, agent-permissions.json, UCP, x402, NLWeb). 70 checks with p | search | 0 |
| agent5ive-mcp | An MCP server for Agent5ive, built with the official @modelcontextprotocol/sdk. | utilities | 0 |
| agentage-server-memory | The agentage Memory MCP server: exposes your local vaults as the frozen 6 memory__* tools over stdio. The open, cross-vendor counterpart to @modelcontextprotocol/server-memory. | memory | 0 |
| agentation-mcp | MCP server for Agentation - visual feedback for AI coding agents | database | 0 |
| agentcat | Analytics tool for MCP (Model Context Protocol) servers and AI agents - tracks tool usage patterns and provides insights | ai | 0 |
| agenticpay-mcp-bridge | Real MCP server (stdio + @modelcontextprotocol/sdk) that exposes x402-paywalled HTTP endpoints as MCP tools. Drop into Claude Desktop, Cursor, or any MCP client. | web | 0 |
| agentmail-mcp | stdio compatibility bridge for the hosted AgentMail MCP server | ai | 0 |
| agentproto-driver-mcp | agentproto/mcp-runtime — AIP-32 MCP provider specialisation. Sugar over @agentproto/driver for Model Context Protocol servers (stdio/SSE/HTTP transports). v0.1 ships frontmatter-driven dispatch; full MCP client wraps @modelcontextprotocol/sdk in v0.2. | web | 0 |
| ai-mentora-mcp-server | MCP server for AI Mentora, compatible with ModelContextProtocol. Provides es-fulltext-retrieve tool for Canadian case law search. | search | 0 |
| aigentyc-mcp | Model Context Protocol server for aiGentyc — content & authoring tools for LLM agents | ai | 0 |
| aikidosec-mcp | Aikido MCP server | ai | 0 |
| ainative-memory-mcp | Enhanced MCP server-memory with ZeroDB cloud persistence and semantic vector search. Drop-in replacement for @modelcontextprotocol/server-memory that stores your knowledge graph in the cloud instead of local JSONL files. | database | 0 |
| ainative-postgres-mcp | Zero-config Postgres MCP server with auto-provisioning. Drop-in replacement for @modelcontextprotocol/server-postgres — no DATABASE_URL needed. Auto-provisions a managed PostgreSQL instance with pgvector on first run. | database | 0 |
| aiondadotcom-mcp-ssh | MCP Agent for managing SSH hosts - A Model Context Protocol server for SSH operations | ai | 0 |
| aipost-mcp-server | MCP Server for AIPost.email — typed, structured messaging for AI agents with Ed25519 identities | communication | 0 |
| airtable-mcp-server | A Model Context Protocol server that provides read and write access to Airtable databases. This server enables LLMs to inspect database schemas, then read and write records. | database | 0 |
| akoskomuves-appstoreconnect-mcp | Model Context Protocol server for the Apple App Store Connect API. | ai | 0 |
| akutishevsky-lunchmoney-mcp | Model Context Protocol server for LunchMoney personal finance management | ai | 0 |
| alchemy-mcp-server | MCP server for using Alchemy APIs | ai | 0 |
| alcyone-labs-modelcontextprotocol-sdk | Upgrade to Zod V4 for Model Context Protocol implementation for TypeScript | utilities | 0 |
| alfe.ai-github-mcp | GitHub MCP proxy server — bridges the official @modelcontextprotocol/server-github with Alfe OAuth credentials (Pattern A multi-account) | devtools | 0 |
| amap-amap-maps-mcp-server | MCP server for using the AMap Maps API | utilities | 0 |
| amcjt-mcp-server | amcjt MCP server with stdio transport | utilities | 0 |
| aml-modelcontextprotocol-aml-watcher-mcp | MCP server for AML Watcher API search | search | 0 |
| ampersend-ai-modelcontextprotocol-sdk | Model Context Protocol implementation for TypeScript | ai | 0 |
| amplitude-mcp-analytics | Amplitude MCP Analytics SDK - MCP server usage tracking for Amplitude Analytics | utilities | 0 |
| anaisbetts-mcp-installer | A MCP server to install other MCP servers | ai | 0 |
| anki-mcp-http | Model Context Protocol server for Anki - enables AI assistants to interact with your Anki flashcards | communication | 0 |
| ankimcp-anki-mcp-server | Model Context Protocol server for Anki - enables AI assistants to interact with your Anki flashcards | communication | 0 |
| antonytm-mcp-sitecore-server | A Model Context Protocol server for Sitecore | utilities | 0 |
| antv-mcp-server-chart | A Model Context Protocol server for generating charts using AntV. This is a TypeScript-based MCP server that provides chart generation capabilities. It allows you to create various types of charts through MCP tools. | utilities | 0 |
| api-now-mcp | API Now Model Context Protocol Server | utilities | 0 |
| apicity-mcp-server | Optional MCP (Model Context Protocol) server that exposes every @apicity provider endpoint as a tool. | ai | 0 |
| apify-actors-mcp-server | Apify MCP Server | utilities | 0 |
| appium-mcp-server | Claude-compatible MCP server for Appium (Android + iOS) | utilities | 0 |
| apple-shortcuts | MCP server for automation using Apple Shortcuts | utilities | 0 |
| arabold-docs-mcp-server | MCP server for fetching and searching documentation | search | 0 |
| arc-mcp-xsuaa-auth | XSUAA / OAuth authentication + BTP principal propagation for Model Context Protocol (MCP) servers built on Express and @modelcontextprotocol/sdk. | utilities | 0 |
| arcote.tech-arc-mcp | Model Context Protocol server for Arc framework — exposes Arc tools over streamable HTTP | web | 0 |
| argocd-mcp | Argo CD MCP Server | devtools | 0 |
| arikusi-deepseek-mcp-server | MCP Server for DeepSeek API integration - enables Claude Code to use DeepSeek Chat and Reasoner models | devtools | 0 |
| arizeai-phoenix-mcp | A MCP server for Arize Phoenix | ai | 0 |
| atlassian | MCP server for Atlassian (Confluence and Jira) integration | ai | 0 |
| atom8n-inspector | Model Context Protocol inspector | utilities | 0 |
| atomgit.com-atomgit-mcp-server | AtomGit MCP Server - Model Context Protocol server for AtomGit code hosting platform | devtools | 0 |
| atomicmail-mcp-modelcontextprotocol | Atomic Mail MCP server — local stdio proxy with PoW auth and JMAP, for AI agents. (modelcontextprotocol install channel) | communication | 0 |
| auth | Plug and play auth for Model Context Protocol (MCP) servers | utilities | 0 |
| auth0-auth0-mcp-server | Auth0 Model Context Protocol (MCP) Server (Beta) — A secure and extendable implementation of an MCP server that provides AI assistants with controlled access to the Auth0 Management API through natural language. This project is in beta and not intended fo | ai | 0 |
| autotel-mcp-instrumentation | OpenTelemetry instrumentation for Model Context Protocol (MCP) with distributed tracing support | monitoring | 0 |
| awesome-copilot-mcp | Model Context Protocol server for awesome-copilot agents and collections | devtools | 0 |
| aws-nx-plugin-mcp | A lightweight, standalone MCP (Model Context Protocol) server for the [Nx Plugin for AWS](https://github.com/awslabs/nx-plugin-for-aws). | devtools | 0 |
| axe-mcp-server | Axe DevTools accessibility analysis and remediation MCP Server for AI coding agents | devtools | 0 |
| axiom | An MCP server implementation for Axiom that enables AI agents to query data using Axiom Processing Language (APL) | ai | 0 |
| azure-devops-mcp | MCP server for interacting with Azure DevOps | devtools | 0 |
| azure-mcp | Azure MCP Server - Model Context Protocol implementation for Azure | cloud | 0 |
| azure-mcp-darwin-arm64 | Azure MCP Server - Model Context Protocol implementation for Azure, for darwin on arm64 | cloud | 0 |
| azure-mcp-linux-x64 | Azure MCP Server - Model Context Protocol implementation for Azure, for linux on x64 | cloud | 0 |
| azure-mcp-win32-x64 | Azure MCP Server - Model Context Protocol implementation for Azure, for win32 on x64 | cloud | 0 |
| backlog-mcp-server | [![MCP Toplist](https://mcptoplist.com/badge/glama%2Fnulab%2Fbacklog-mcp-server.svg)](https://mcptoplist.com/server/glama%2Fnulab%2Fbacklog-mcp-server) ![MIT License](https://img.shields.io/badge/license-MIT-green.svg) ![Build](https://github.com/nulab/ba | devtools | 0 |
| bannerbear-mcp | Model Context Protocol server for the Bannerbear V5 API | utilities | 0 |
| basic-preact ⭐ | Basic MCP App Server example using Preact | utilities | 0 |
| basic-react ⭐ | Basic MCP App Server example using React | utilities | 0 |
| basic-solid ⭐ | Basic MCP App Server example using Solid | utilities | 0 |
| basic-svelte ⭐ | Basic MCP App Server example using Svelte | utilities | 0 |
| basic-vanillajs ⭐ | Basic MCP App Server example using vanilla JavaScript | utilities | 0 |
| basic-vue ⭐ | Basic MCP App Server example using Vue | utilities | 0 |
| bc-telemetry-buddy-mcp | Model Context Protocol server for Business Central telemetry | utilities | 0 |
| beautyfree-modelcontextprotocol-server-github | MCP server for using the GitHub API | devtools | 0 |
| behavioros-mcp-server | BehaviorOS MCP Server — Model Context Protocol server for BehaviorOS | ai | 0 |
| bennapp-modelcontextprotocol-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| berthojoris-mcp-mysql-server | Model Context Protocol server for MySQL database integration with dynamic per-project permissions | database | 0 |
| besales-mcp | Model Context Protocol server for Animaly / Besales | utilities | 0 |
| better-auth-mcp | Model Context Protocol (MCP) plugin for Better Auth | utilities | 0 |
| big-whale-labs-modelcontextprotocol-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| bitwarden-mcp-server | Bitwarden MCP Server | utilities | 0 |
| bmad-mcp-server | Model Context Protocol server for BMAD methodology | ai | 0 |
| borodutch-modelcontextprotocol-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| bossbench-mcp | Model Context Protocol server for Bossbench. | utilities | 0 |
| brave-brave-search-mcp-server | Brave Search MCP Server: web results, images, videos, rich results, AI summaries, and more. | search | 0 |
| breadstone-archipel-platform-mcp | Reusable MCP (Model Context Protocol) server module for NestJS applications | ai | 0 |
| bretterer-forge-mcp-server | Laravel Forge MCP server for managing servers, sites, and deployments | utilities | 0 |
| browserless.io-mcp | MCP (Model Context Protocol) server for the Browserless.io browser automation platform | browser | 0 |
| browsermcp-mcp | MCP server for browser automation using Browser MCP | browser | 0 |
| browserstack-mcp-server | BrowserStack's Official MCP Server | browser | 0 |
| budget-allocator ⭐ | Budget allocator MCP App Server with interactive visualization | utilities | 0 |
| bugsnag-mcp-server | A Bugsnag MCP server for interacting with Bugsnag API | ai | 0 |
| burtthecoder-mcp-shodan | A Model Context Protocol server for Shodan API queries. | ai | 0 |
| caiquebrito-nodum-mcp | Model Context Protocol server for Nodum — integrate code knowledge graphs with Claude AI | ai | 0 |
| cap-js-mcp-server | Model Context Protocol (MCP) server for AI-assisted development of CAP applications. | devtools | 0 |
| cclsp | MCP server for accessing LSP functionality | utilities | 0 |
| channel.io-tolgee-mcp | Model Context Protocol server for Tolgee integration | utilities | 0 |
| chatwork-mcp-server | MCP (Model Context Protocol) server for operating Chatwork from AI | communication | 0 |
| chrome-devtools-mcp | MCP server for Chrome DevTools | devtools | 0 |
| claude-flow-mcp | Standalone MCP (Model Context Protocol) server - stdio/http/websocket transports, connection pooling, tool registry | web | 0 |
| claudexor-mcp-server | MCP server exposing durable Claudexor run, status, cancel, result, and interaction tools. | utilities | 0 |
| clearlist-mcp-server | ClearList MCP Server — AI agent interface to the ClearList API | ai | 0 |
| clipform-mcp-server | MCP server for building and managing Clipform video forms | utilities | 0 |
| cloudwerxlab-gpt-image-1-mcp | A Model Context Protocol server for OpenAI's gpt-image-1 model, supports Image Generation and Editing/Masks. | cloud | 0 |
| cmd8-excalidraw-mcp | Model Context Protocol server for Excalidraw diagrams. | utilities | 0 |
| codacy-codacy-mcp | Codacy MCP server | ai | 0 |
| code-runner | Code Runner MCP Server | utilities | 0 |
| codecov-mcp-server | A Codecov Model Context Protocol server | utilities | 0 |
| codefuturist-email-mcp | Email MCP server with IMAP + SMTP support | communication | 0 |
| codex-mcp-server | MCP server wrapper for OpenAI Codex CLI | ai | 0 |
| cognigy-mcp-server | Model Context Protocol server for Cognigy.AI REST API | ai | 0 |
| cognitionai-metabase-mcp-server | A Model Context Protocol server for Metabase integration | ai | 0 |
| cognium-ai-mcp-server | MCP server exposing Cognium spec-conformance, spec-drift, and pattern-search tools over stdio | search | 0 |
| cohort-heatmap ⭐ | Cohort heatmap MCP App Server for retention analysis | utilities | 0 |
| coinbase-cds-mcp-server | Coinbase Design System - MCP Server | utilities | 0 |
| commercetools-commerce-mcp | A command line tool for setting up commercetools MCP server | utilities | 0 |
| composiohq-modelcontextprotocol-typescript-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| considered-harmful | Most [MCP servers](https://github.com/modelcontextprotocol/servers) suggest using `npx -y` as the recommended way to install a server. This downloads and executes arbitrary scripts from the internet. This is grossly insecure and I think the MCP authors sh | devtools | 0 |
| content-island-mcp | Content Island - MCP (Model Context Protocol) server | utilities | 0 |
| contentful-mcp-server | Contentful MCP Server - Model Context Protocol server for Contentful | utilities | 0 |
| crewhaus-mcp-server | Project a compiled bundle's turn function as an MCP server (stdio + SSE) — a chat/invoke tool plus optional per-sub-agent tools delegating to an injected invoke fn, built on @modelcontextprotocol/sdk | communication | 0 |
| currents-mcp | Currents MCP server | browser | 0 |
| customer-segmentation ⭐ | Customer segmentation MCP App Server with filtering | utilities | 0 |
| cyanheads-git-mcp-server | A secure and scalable Git MCP server enabling AI agents to perform comprehensive Git version control operations via STDIO and Streamable HTTP. | devtools | 0 |
| dandeliongold-server-everything | Demo MCP server that exercises all the features of the MCP protocol. This server is a fork of @modelcontextprotocol/servers by Anthropic, PBC with extended functionality for testing MCP clients. | ai | 0 |
| dankelleher-modelcontextprotocol-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| dapp-local-mcp | A stdio MCP server using @modelcontextprotocol/sdk | utilities | 0 |
| datadog-mcp-server | MCP Server for Datadog API | monitoring | 0 |
| dataforseo-mcp-server | CLI and MCP server for DataForSEO API — browse documentation and make authenticated API requests | cloud | 0 |
| davewind-mysql-mcp-server | A Model Context Protocol server for MySQL | database | 0 |
| davinci-resolve-mcp | NPM bootstrapper for the DaVinci Resolve MCP Server. | utilities | 0 |
| dbx-app-mcp-server | MCP server for DBX — query databases from Claude Code, Cursor, and other AI agents | database | 0 |
| debug ⭐ | Debug MCP App Server for testing all SDK capabilities | utilities | 0 |
| deepl-mcp-server | MCP server for DeepL translation API | ai | 0 |
| deepseek | DeepSeek MCP Server - Model Context Protocol server for DeepSeek API | ai | 0 |
| deepseek-mcp-server | Model Context Protocol server for DeepSeek V4 Chat, Responses, FIM, models, and balance APIs. | communication | 0 |
| delorenj-mcp-server-ticketmaster | A Model Context Protocol server for discovering events, venues, and attractions through the Ticketmaster Discovery API | utilities | 0 |
| delorenj-mcp-server-trello | An MCP server for Trello boards, powered by Bun for maximum performance. | productivity | 0 |
| democratize-technology-vikunja-mcp | Model Context Protocol server for Vikunja task management | ai | 0 |
| dennisk2025-text-alternating-case | Transforms input text so that letters alternately switch between uppercase and lowercase, starting with uppercase. MCP server for Claude Desktop and modelcontextprotocol. | utilities | 0 |
| depup-modelcontextprotocol--sdk | Model Context Protocol implementation for TypeScript (with updated dependencies) | utilities | 0 |
| desktop-automation | Model Context Protocol server for desktop automation | utilities | 0 |
| dev-boy-mcp-stdio-server | Native STDIO MCP server for Dev Boy - GitLab integration using @modelcontextprotocol/sdk | devtools | 0 |
| devflow-tools-mcp-server | Model Context Protocol server exposing DevFlow context, memory, knowledge, and workflow tools. | devtools | 0 |
| dexpaprika-mcp | A Model Context Protocol server for DexPaprika cryptocurrency data with network-specific pool queries | ai | 0 |
| diagrampilot-mcp | Model Context Protocol server for DiagramPilot. | devtools | 0 |
| dialpad-dialtone-mcp-server | MCP Server for Dialtone Design System | utilities | 0 |
| directus-content-mcp | Model Context Protocol server for Directus projects. | ai | 0 |
| djankies-vitest-mcp | A Model Context Protocol server for Vitest test execution and management | ai | 0 |
| dockbrain-mcp-filesystem-demo | Dies ist ein Demo-Paket für Dockbrain, das den `@modelcontextprotocol/server-filesystem` verwendet,  um Dokumente aus einem Dateisystem über das Model Context Protocol bereitzustellen. | ai | 0 |
| document-mcp | MCP (Model Context Protocol) server exposing documents.js's document-conversion, .odb, metadata, and font tooling as MCP tools. | database | 0 |
| docusaurus-plugin-mcp-server | A Docusaurus plugin that exposes an MCP server endpoint for AI agents to search and retrieve documentation | search | 0 |
| doist-todoist-mcp | The official Todoist MCP server | ai | 0 |
| doitintl-doit-mcp-server | DoiT official MCP Server | utilities | 0 |
| dokploy-mcp | MCP Server for Dokploy API | utilities | 0 |
| doppler-server | Model Context Protocol server for Doppler secret management | utilities | 0 |
| dopplerhq-mcp-server | MCP server for Doppler API with auto-generated tools from OpenAPI specification | utilities | 0 |
| drawio-mcp | Official draw.io MCP server for LLMs - Open diagrams in draw.io editor | ai | 0 |
| driflyte-mcp-server | MCP Server for Driflyte | web | 0 |
| dsh-plug-mcp | DeepSeek Harness 的 MCP 服务管理器：在 设置 → 插件 → MCP 标签页中发现 GitHub 上的 MCP 服务仓库（topic:mcp-server / modelcontextprotocol），探测 npm / PyPI 发布状态与 README 启动线索，详情查看后一键安装 / 移除。服务以 @deepseek-ai/dsh-mcp-client 行登记进 cordis.patch.yml，HMR 热重载，无需重启。支持 GitHub 代理。 | devtools | 0 |
| duckduckgo-mcp-server | A TypeScript-based MCP server that provides DuckDuckGo search functionality. | search | 0 |
| dunx-mcp | A Model Context Protocol server for dunx apps - bunx @dunx/mcp ./src/app.module.ts | utilities | 0 |
| echo-server | A minimal MCP server template that echoes messages | utilities | 0 |
| edicarlos.lds-businessmap-mcp | Model Context Protocol server for BusinessMap (Kanbanize) integration | utilities | 0 |
| ee-mcp-server | Model Context Protocol server for Evolution Engineering | database | 0 |
| ehrocks-fe-mcp-server | MCP server for searching Hero Design System components | search | 0 |
| elementor-angie-sdk | TypeScript SDK for Angie AI assistant | ai | 0 |
| elgato-mcp-server | A Model Context Protocol (MCP) server that bridges AI assistants with Elgato apps. | ai | 0 |
| elijahtynes-reliefweb-mcp-server | ModelContextProtocol (MCP) server for ReliefWeb humanitarian information service | web | 0 |
| enfyra-mcp-server | MCP server for Enfyra - manage Enfyra instances from MCP-compatible coding tools | utilities | 0 |
| enhanced-postgres-mcp-server | Enhanced PostgreSQL MCP server with read and write capabilities. Based on @modelcontextprotocol/server-postgres by Anthropic. | database | 0 |
| epic-web-workshop-mcp | An MCP (Model Context Protocol) server intended for use inside Epic Workshop repositories. | web | 0 |
| ericthered926-duckduckgo-mcp-server | A Model Context Protocol (MCP) server for DuckDuckGo web and news search | search | 0 |
| esaio-esa-mcp-server | Official MCP server for esa.io - STDIO transport version | ai | 0 |
| eslint-mcp | MCP server for ESLint | utilities | 0 |
| eslint-plugin-mcp-sdk-security | ESLint plugin for Model Context Protocol (MCP) SDK security — catches tools registered without an input schema, handlers reading arguments the schema never declared, model-visible descriptions built from dynamic text, and tool arguments reaching a shell. | ai | 0 |
| euqns-nudge-mcp | Model Context Protocol server for the Nudge board (the in-house Trello). | utilities | 0 |
| european-parliament-mcp-server | Model Context Protocol server for European Parliament open data | ai | 0 |
| evals | GitHub Action for evaluating MCP server tool calls using LLM-based scoring | devtools | 0 |
| everything ⭐ | MCP server that exercises all the features of the MCP protocol | utilities | 0 |
| excalidraw-mcp | MCP server for Excalidraw | ai | 0 |
| expander-mcp-server | Model Context Protocol server for the Exmachine External API | utilities | 0 |
| expo-docs-mcp | Model Context Protocol server for Expo documentation | ai | 0 |
| extentos-mcp-server | Extentos MCP server â€” deterministic tools for building smart-glasses apps with AI agents. | ai | 0 |
| f4ww4z-mcp-mysql-server | A Model Context Protocol server for MySQL database operations | database | 0 |
| fangjunjie-ssh-mcp-server | SSH-based MCP Server (基于 SSH 的 MCP 服务器) | utilities | 0 |
| fanyangmeng-ghost-mcp | MCP server for using the Ghost API | utilities | 0 |
| fdx-mcp-server | A Model Context Protocol server — Bun-first, Deno-compatible. | utilities | 0 |
| feishu-mcp | Model Context Protocol server for Feishu integration | utilities | 0 |
| felixallistar-coolify-mcp | Model Context Protocol server for Coolify API integration | utilities | 0 |
| felores-airtable-mcp-server | An Airtable Model Context Protocol Server | ai | 0 |
| fetch-typescript | A Model Context Protocol server that provides web content fetching and conversion capabilities | web | 0 |
| fetcher-mcp | MCP server for fetching web content using Playwright browser | web | 0 |
| fgv-ts-extras-mcp | Result-integration boundary over @modelcontextprotocol/sdk: connect to MCP servers, discover tools, and adapt them into @fgv/ts-extras ai-assist client tools | ai | 0 |
| figma-context-mcp | Model Context Protocol server for Figma integration with smart position info | utilities | 0 |
| figma-mcp-server | A local MCP server with full Figma REST API coverage. | utilities | 0 |
| figura-mcp | Model Context Protocol server for the Figura visualization SaaS | utilities | 0 |
| financial-modeling-prep-mcp-server | Model Context Protocol server for Financial Modeling Prep (FMP) API, exposing 250+ tools for financial data, market insights, and analysis. | ai | 0 |
| flightradar-mcp-server | A Model Context Protocol server for flight tracking and status information | utilities | 0 |
| flint-chart-mcp | Model Context Protocol server for Flint — compile, validate, and render semantic chart specs across supported backends. | ai | 0 |
| flor3z-github-mcp-server-redmine | Model Context Protocol server for Redmine integration | devtools | 0 |
| forestadmin-mcp-server | Model Context Protocol server for Forest Admin with OAuth authentication | utilities | 0 |
| foundryvtt-mcp | Model Context Protocol server for FoundryVTT integration | ai | 0 |
| fractalizer-mcp-server-yandex-tracker | MCP Server for Yandex Tracker API integration | project-management | 0 |
| fractalizer-mcp-server-yandex-wiki | MCP Server for Yandex Wiki API integration | utilities | 0 |
| freee-mcp | Model Context Protocol (MCP) server for freee API integration | utilities | 0 |
| freestyle | A Model Context Protocol server that reads data from a FreeStyle glucose sensor. | utilities | 0 |
| ftp | Model Context Protocol server for FTP access | utilities | 0 |
| futuretea-redis-mcp-server | Redis Model Context Protocol server | database | 0 |
| gebrai-gebrai | Model Context Protocol server for GeoGebra mathematical visualization | ai | 0 |
| gently-mcp-server | gently MCP server — repo-first graph tools for agents | utilities | 0 |
| geobio-google-workspace-server | A Model Context Protocol server | utilities | 0 |
| geocoding-ai-mcp | Model Context Protocol server for geocoding | ai | 0 |
| get-technology-inc-jamf-docs-mcp-server | MCP Server for accessing Jamf Documentation (learn.jamf.com) | utilities | 0 |
| getbourdon-mcp-server | Bourdon L6 MCP server (BUSL-1.1) — the facade over @getbourdon/federation that exposes the federation natively to any MCP-aware agent (Claude Code, Codex, Cursor). Faithful port of core/l6_server.py on @modelcontextprotocol/sdk. WIRE-COMPATIBLE with the P | ai | 0 |
| getnarro-mcp-server | MCP (Model Context Protocol) server for AI-assisted Narro presentation creation | ai | 0 |
| gezhe-mcp-server | gezhe ppt mcp server | utilities | 0 |
| git-mcp-server | A Model Context Protocol server | devtools | 0 |
| gitbook-mcp | GitBook Model Context Protocol server - read and search GitBook documentation with AI assistants | devtools | 0 |
| github-mcp-server-js | A GitHub MCP server built on octokit.js and the MCP TypeScript SDK v2 — 100+ tools across 16 toolsets, packaged as npm and .mcpb Claude Desktop Extension. | devtools | 0 |
| gleanwork-configure-mcp-server | MCP server configurator for Glean | utilities | 0 |
| gmlee-ncurity-mcp-server-redmine | Model Context Protocol server for Redmine integration | ai | 0 |
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
| gorgias-mcp-server | MCP server exposing the full Gorgias helpdesk API to AI assistants | ai | 0 |
| gotillit-local-mcp-server | Local MCP server for Tillit API using @modelcontextprotocol/sdk. Provides 195+ tools and 48+ resources for complete Tillit API access with built-in documentation. | utilities | 0 |
| grackle-ai-mcp | MCP (Model Context Protocol) server for Grackle — translates MCP tool calls to ConnectRPC | ai | 0 |
| graphite-atlas-mcp-server | Model Context Protocol server for Graphite Atlas | memory | 0 |
| graphlit-mcp-server | Graphlit MCP Server | web | 0 |
| graphql-schema | Model Context Protocol server for GraphQL schemas | utilities | 0 |
| greenline-works-mcp-server | Model Context Protocol server for the GreenLine public API | ai | 0 |
| groq-compound-mcp-server | MCP server for interacting with Groq models | utilities | 0 |
| growth-labs-mcp-server | Server framework for Growth Labs MCP services. Provides defineMcpTool primitive, createMcpServer composition, audit/metrics interfaces, error envelopes, role-based authorization, and a hand-rolled JSON-RPC HTTP transport behind a swappable Transport abstr | web | 0 |
| grpc-transport | Pluggable gRPC transport for Model Context Protocol (MCP) servers using @modelcontextprotocol/sdk. Protobuf surface aligned with the community mcp-python-sdk-grpc-poc reference. | utilities | 0 |
| gsc | Enhanced Model Context Protocol server for Google Search Console with 25K row limit, regex filters, and automatic quick wins detection | search | 0 |
| handler | Framework-agnostic HTTP adapter for Model Context Protocol servers | web | 0 |
| hashi-mcp-server | MCP server for Hashi bridges. Wraps @modelcontextprotocol/sdk and exposes one or more bridges as a single MCP server (stdio). | ai | 0 |
| helicone-mcp | Model Context Protocol server for Helicone observability platform | ai | 0 |
| hello-world | A simple Hello World MCP server | utilities | 0 |
| henkey-postgres-mcp-server | A Model Context Protocol (MCP) server that provides comprehensive PostgreSQL database management capabilities for AI assistants | database | 0 |
| heroku-mcp-server | Heroku Platform MCP Server | utilities | 0 |
| hisma-server-puppeteer | Fork and update (v0.6.5) of the original @modelcontextprotocol/server-puppeteer MCP server for browser automation using Puppeteer. | browser | 0 |
| honeycomb-mcp | Model Context Protocol server for Honeycomb | utilities | 0 |
| hono-mcp-server-sse-transport | Server-Sent Events transport for Hono and Model Context Protocol | utilities | 0 |
| hostinger-api-mcp | MCP server for Hostinger API | utilities | 0 |
| hourei-mcp-server | MCP server for Japanese law information using e-Gov API | utilities | 0 |
| houtini-brevo-mcp | MCP (Model Context Protocol) server for Brevo email marketing platform with comprehensive analytics | communication | 0 |
| hubspot-mcp-server | MCP Server for developers building HubSpot Apps | devtools | 0 |
| hugeicons-mcp-server | MCP server for Hugeicons search and usage documentation | search | 0 |
| hyperbrowser-mcp | Hyperbrowser Model Context Protocol Server | web | 0 |
| hyperfixi-mcp-server | Model Context Protocol server for HyperFixi hyperscript development | devtools | 0 |
| hypothesi-tauri-mcp-server | A Model Context Protocol server for use with Tauri v2 applications | utilities | 0 |
| ibm-ibmi-mcp-server | A production-grade MCP server for IBM i | database | 0 |
| iflow-mcp-garethcott-enhanced-postgres-mcp-server | Enhanced PostgreSQL MCP server with read and write capabilities. Based on @modelcontextprotocol/server-postgres by Anthropic. | database | 0 |
| iflow-mcp-garethcott-enhanced-postgres-mcp-server | Enhanced PostgreSQL MCP server with read and write capabilities. Based on @modelcontextprotocol/server-postgres by Anthropic. | database | 0 |
| iflow-mcp-google-workspace-mcp-server | A Model Context Protocol server | utilities | 0 |
| iflow-mcp-jageenshukla-hello-world-mcp-server | Welcome to the **Hello World MCP Server**! This project demonstrates how to set up a server using the [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/typescript-sdk) SDK. It includes tools, prompts, and endpoints for handling server | devtools | 0 |
| iflow-mcp-mailgun-mcp-server | [![MCP](https://img.shields.io/badge/MCP-Server-blue.svg)](https://github.com/modelcontextprotocol) | devtools | 0 |
| iflow-mcp-mbadkins-puppeteer-plus-martech | Puppeteer+ MarTech - Enhanced Puppeteer MCP server with specialized digital marketing analytics capabilities. This builds upon the official @modelcontextprotocol/server-puppeteer with tools for analyzing marketing technologies, analytics platforms, tag ma | devtools | 0 |
| iflow-mcp-minecraft-mcp-server | > ⚠️ **CLAUDE DESKTOP DUAL LAUNCH WARNING**: Claude Desktop may sometimes launch MCP servers twice ([known issue](https://github.com/modelcontextprotocol/servers/issues/812)), which can lead to incorrect behavior of this MCP server. If you experience issu | devtools | 0 |
| iflow-mcp-puppeteer-mcp-server | Experimental MCP server for browser automation using Puppeteer (inspired by @modelcontextprotocol/server-puppeteer) | browser | 0 |
| iflow-mcp-wizd-airylark-mcp-server | AiryLark的ModelContextProtocol(MCP)服务器，提供高精度翻译API | ai | 0 |
| ignex-mcp | Model Context Protocol server for Ignex — agent tooling for build/dev/route/info/openapi/doctor. | devtools | 0 |
| impetik-xeer-mcp | Model Context Protocol server for Xeer project context, diagnostics, scaffold, check, test, dev, build, and preview deployment. | devtools | 0 |
| imqueue-mcp | Model Context Protocol server for @imqueue — lets AI coding agents search the docs and scaffold typed services & clients. | search | 0 |
| infranodus-mcp-server | InfraNodus MCP server - A Model Context Protocol server for network thinking and graph analysis | memory | 0 |
| inkdropapp-mcp-server | Inkdrop Model Context Protocol Server | utilities | 0 |
| insforge-mcp | MCP (Model Context Protocol) server for Insforge backend-as-a-service | utilities | 0 |
| instawp-mcp-wp | A Model Context Protocol server for interacting with WordPress. | ai | 0 |
| intangle-mcp-server | Model Context Protocol server for Intangle - AI context that persists across conversations | ai | 0 |
| iobroker-mcp-server | MCP server for ioBroker | utilities | 0 |
| ios-simulator-mcp | MCP server for interacting with the iOS simulator | utilities | 0 |
| iqai-mcp-polymarket | Polymarket MCP Server - Model Context Protocol server for Polymarket trading | ai | 0 |
| ironbee-ai-devtools | MCP Server and CLI for IronBee DevTools | devtools | 0 |
| iterable-mcp | Model Context Protocol server for Iterable API | utilities | 0 |
| iterm-mcp | A Model Context Protocol server that provides access to the currently active tab of iTerm | utilities | 0 |
| ivotoby-openapi-mcp-server | An MCP server that exposes OpenAPI endpoints as resources | utilities | 0 |
| jobot-modelcontextprotocol-typescript-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| json-render-mcp | MCP Apps integration for @json-render/core. Serve json-render UIs as interactive MCP Apps in Claude, ChatGPT, Cursor, and VS Code. | communication | 0 |
| jupiterone-jupiterone-mcp | Model Context Protocol server for JupiterOne account rules and rule details | ai | 0 |
| kanban-zone-mcp-server | Model Context Protocol server for the Kanban Zone public API | ai | 0 |
| kazuph-mcp-fetch | A Model Context Protocol server that provides web content fetching capabilities with automatic image saving and optional AI display | web | 0 |
| kazuph-mcp-taskmanager | Model Context Protocol server for Task Management | utilities | 0 |
| kekwanulabs-syncline-mcp-server | Model Context Protocol server for Syncline - AI-powered meeting scheduling | ai | 0 |
| kentico-management-api-mcp | Model Context Protocol server for Xperience by Kentico Management API | utilities | 0 |
| keygate | Monetize your MCP server in 60 seconds: API keys, plans, usage metering, and rate limits for any @modelcontextprotocol/sdk server — fully local, no cloud account required. | cloud | 0 |
| kibi-mcp | Model Context Protocol server for Kibi knowledge base | utilities | 0 |
| kickflow-mcp-server | MCP Server for kickflow API | utilities | 0 |
| kintone-mcp-server | The official MCP Server for kintone | utilities | 0 |
| kkaminsk-modelcontextprotocol | MCP server for the Perplexity API Platform (fork of @perplexity-ai/mcp-server) | ai | 0 |
| knip-mcp | Knip MCP Server | utilities | 0 |
| kolide-mcp-server | Model Context Protocol server for Kolide security platform | devtools | 0 |
| komodo-mcp-server | Model Context Protocol Server for Komodo (Container Manager) | devtools | 0 |
| kubernetes-mcp-server | Model Context Protocol (MCP) server for Kubernetes and OpenShift | devtools | 0 |
| kubernetes-mcp-server-linux-amd64 | Model Context Protocol (MCP) server for Kubernetes and OpenShift | devtools | 0 |
| kya-os-mcp-i | The TypeScript MCP framework with identity features built-in | utilities | 0 |
| lambda-solutions-mcp-server-sheriff | Model Context Protocol server for Sheriff | utilities | 0 |
| langsmith-mcp-server | LangSmith MCP Server - TypeScript implementation | utilities | 0 |
| lannzo-mcp | Local Model Context Protocol server for Lannzo | utilities | 0 |
| launchsecure-launch-sdk | Typed server-side client for LaunchSecure's MCP. Wraps @modelcontextprotocol/sdk with PAT auth and typed helpers (feedback, work items, comments, etc.). | database | 0 |
| lazy-auth ⭐ | MCP App example demonstrating lazy (on-demand) OAuth: public tools work unauthenticated, protected tools return 401 + WWW-Authenticate so the host runs the OAuth flow only when needed | utilities | 0 |
| lazyants-hetzner-mcp-server | MCP server for the Hetzner Cloud API — manage servers, networks, volumes, and more | cloud | 0 |
| lazyants-lexware-mcp-server | MCP server for the Lexware Office API — manage invoices, contacts, articles, vouchers, and more | utilities | 0 |
| lerianstudio-matcher-mcp | Model Context Protocol server for the Matcher reconciliation engine | utilities | 0 |
| libtmux-mcp | Model Context Protocol server for tmux, built on libtmux. | devtools | 0 |
| lightsage-mcp-tracker | Track MCP tool calls from AI agents. Works with @modelcontextprotocol/sdk, FastMCP, and custom servers. | ai | 0 |
| likec4-mcp | Model Context Protocol server for LikeC4 | utilities | 0 |
| line-line-bot-mcp-server | MCP server for interacting with your LINE Official Account | utilities | 0 |
| linear-mcp-server | A Model Context Protocol server for the Linear API. | project-management | 0 |
| linkup-mcp-server | Linkup MCP server for web search | search | 0 |
| listmonk-ops-mcp | Listmonk Model Context Protocol Server using Hono | utilities | 0 |
| llmindset-hf-mcp-server | Official Hugging Face MCP Server | ai | 0 |
| logicmonitor-mcp-server | LogicMonitor Model Context Protocol Server | devtools | 0 |
| loopctl-mcp-server | MCP server for loopctl — structural trust for AI development loops | devtools | 0 |
| lostgradient-cinder-mcp | Model Context Protocol server exposing Cinder component discovery, comparison, and best-practice guidance to MCP clients. | utilities | 0 |
| lsp-mcp-server | MCP server bridging Claude Code to Language Server Protocol servers | utilities | 0 |
| lucairn-mcp-server | Model Context Protocol server for Lucairn — privacy-preserving AI gateway | ai | 0 |
| luis-neira-mtn7-mcp-server | An MCP (modelcontextprotocol.io) server that serves a local, offline snapshot of the Mantine v7 documentation over stdio. Built on the official @modelcontextprotocol/sdk; reads its data from bundled local files instead of fetching from mantine.dev. | devtools | 0 |
| lumiastream-mcp | Model Context Protocol server for Lumia Stream | utilities | 0 |
| lunora-mcp | Model Context Protocol server exposing a Lunora deployment to AI agents | cloud | 0 |
| lynx-js-docs-mcp-server-canary | A MCP Server providing Lynx documentation resources for LLMs, with carefully designed prompting. | ai | 0 |
| magicpod-mcp-server | Model Context Protocol server for MagicPod integration | utilities | 0 |
| magneticwatermelon-mcp-toolkit | Build and ship **[Model Context Protocol](https://github.com/modelcontextprotocol)** (MCP) servers with zero-config ⚡️. | devtools | 0 |
| maildev-mcp | MCP (Model Context Protocol) server for Claude integration with MailDev | devtools | 0 |
| mailjet-mailjet-mcp-server | [![MCP](https://img.shields.io/badge/MCP-Server-blue.svg)](https://github.com/modelcontextprotocol) | devtools | 0 |
| makafeli-n8n-workflow-builder | Model Context Protocol server for n8n workflow management | utilities | 0 |
| malicious-mcp-server | A deliberately malicious MCP server for E2E testing purposes | utilities | 0 |
| mantine-mcp-server | MCP server for Mantine documentation | ai | 0 |
| map ⭐ | MCP App Server example with CesiumJS 3D globe and geocoding | utilities | 0 |
| mapbox-mcp-server | Mapbox MCP server. | utilities | 0 |
| markdownify-server | MCP Markdownify Server - Model Context Protocol Server for Converting Almost Anything to Markdown | utilities | 0 |
| markdy-mcp-server | Model Context Protocol server for Markdy diagram validation, transpilation, and generation. | utilities | 0 |
| mastra-mcp-docs-server | MCP server for accessing Mastra.ai documentation, changelogs, and news. | ai | 0 |
| mathis1m-gmod-mcp | Model Context Protocol server for Garry's Mod | utilities | 0 |
| matillion-mcp-server | MCP Server for Matillion Data Productivity Cloud Public API integration | cloud | 0 |
| mcp-registry-mcp-obsidian-1 | A server implementation of the [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/protocol) for integrating with [Obsidian](https://obsidian.md/). This allows AI assistants to read, create, and manipulate notes in your Obsidian vault. | devtools | 0 |
| mcp-use-modelcontextprotocol-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| mcpflow.io-mcp | ModelContextProtocol server for enhancing JSON Resumes | ai | 0 |
| mcpmarket-mcp-auto-install | MCP server that helps install other MCP servers automatically | ai | 0 |
| mcpweb-org-sdk | Official TypeScript/JavaScript SDK for the MCPaaS platform - A wrapper around the official MCP Server using @modelcontextprotocol/sdk | web | 0 |
| mdavieds-mcp-tmp-files | A local MCP server stub built with the [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk). | devtools | 0 |
| mdedit-mcp-server | Model Context Protocol server for live mdedit.ai document collaboration. | ai | 0 |
| mealie-mcp-server | MCP server for Mealie recipe management | utilities | 0 |
| memberjunction-ai-mcp-server | MemberJunction: Model Context Protocol (MCP) - Server Implementation | ai | 0 |
| memofs-mcp-server | Model Context Protocol server for MemoFS agent integrations. | ai | 0 |
| merkl-mcp | MCP server exposing Merkl opportunities via @modelcontextprotocol/sdk | utilities | 0 |
| meshcpcom-pipe | MCP (Model Context Protocol) Server for MeshCP | utilities | 0 |
| meshy-ai-meshy-mcp-server | MCP server for Meshy AI 3D generation platform | ai | 0 |
| meta-ads-mcp | Model Context Protocol server for Meta Marketing API integration | utilities | 0 |
| metamask-device-mcp | MCP server for mobile device interaction — iOS (IDB), Android (ADB), and Appium/BrowserStack | database | 0 |
| mgcrea-mcp-appstore-connect | Model Context Protocol server for the Apple App Store Connect API | utilities | 0 |
| mgsoftwarebv-mcp-server-bridge | MCP Server bridge for MG Tickets - connects Cursor to HTTP MCP server with image support and GitHub code exploration | devtools | 0 |
| microsoft-clarity-mcp-server | MCP Server for Microsoft Clarity based on data export API | ai | 0 |
| microsoft-devbox-mcp | Model Context Protocol server for Microsoft Dev Box | devtools | 0 |
| microsoft-powerbi-modeling-mcp | Power BI Modeling MCP Server - Node.js client package for installing and running the Power BI Modeling MCP server | utilities | 0 |
| microsoft-workiq | MCP server for Microsoft 365 Copilot | ai | 0 |
| middy-mcp | Middy middleware for Model Context Protocol server | cloud | 0 |
| miemiegy-mysql | A Model Context Protocol server for MySQL operations | database | 0 |
| mimo-mcp-server | MCP Server for MiMo multimodal capabilities (image, audio, video understanding, ASR, TTS) | utilities | 0 |
| mindstone-mcp-server-openai-image | OpenAI image generation MCP server for Model Context Protocol hosts | ai | 0 |
| mmtr-tech-confluence-mcp | Model Context Protocol server for Confluence Server/Data Center REST API | productivity | 0 |
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
| mongo-server | A Model Context Protocol server for MongoDB connections | database | 0 |
| mongodb-mcp-server | MongoDB Model Context Protocol Server | database | 0 |
| motiffcom-motiff-mcp-server | MCP server for motiff | utilities | 0 |
| mseep-airylark-mcp-server | AiryLark的ModelContextProtocol(MCP)服务器，提供高精度翻译API | ai | 0 |
| mseep-linear-mcp-server | A Model Context Protocol server for the Linear API. | project-management | 0 |
| mseep-mcp-smart-crawler | A command-line tool acting as an MCP (ModelContextProtocol) server, using Playwright to crawl web content for AI models. | web | 0 |
| mseep-mcp-typescript-server-starter | ModelContextProtocol typescript server starter | utilities | 0 |
| mseep-puppeteer-mcp-server | Experimental MCP server for browser automation using Puppeteer (inspired by @modelcontextprotocol/server-puppeteer) | browser | 0 |
| mseep-verodat-mcp-server | [![MCP](https://img.shields.io/badge/MCP-Server-blue.svg)](https://github.com/modelcontextprotocol) [![smithery badge](https://smithery.ai/badge/@Verodat/verodat-mcp-server)](https://smithery.ai/server/@Verodat/verodat-mcp-server) | devtools | 0 |
| mssql-mcp-server | MCP server for Microsoft SQL Server database access and comprehensive schema exploration using tedious. Includes enhanced stored procedure tools for complete SQL source code access. | database | 0 |
| mui-mcp | MUI MCP Server | utilities | 0 |
| multicluster-mcp-server | A Model Context Protocol server | utilities | 0 |
| negokaz-excel-mcp-server | An MCP server that reads and writes spreadsheet data to MS Excel file | filesystem | 0 |
| neilinger-businessmap-mcp | Model Context Protocol server for BusinessMap (Kanbanize) integration | utilities | 0 |
| nekzus-mcp-server | NPM Sentinel MCP - A powerful Model Context Protocol (MCP) server that revolutionizes NPM package analysis through AI. Built to integrate with Claude and Anthropic AI, it provides real-time intelligence on package security, dependencies, and performance. | devtools | 0 |
| nestjs-mcp-server | Modular library for building scalable MCP servers with NestJS, providing decorators and integration patterns as a wrapper for the official MCP TypeScript SDK. | ai | 0 |
| nestm-mcp-auth | OAuth 2.1 authorization-server proxy, Client ID Metadata Documents, and token infrastructure for NestM MCP servers. | utilities | 0 |
| neurodivergent-memory | A Model Context Protocol server for knowledge graphs designed around neurodivergent thinking patterns | memory | 0 |
| nevescloud-mcp-rtc | Reference implementation of the MCP-over-WebRTC transport (see SPEC.md). Implements the @modelcontextprotocol/sdk Transport interface for both server and client, in Node and browser. | web | 0 |
| newrelic-mcp | Model Context Protocol server for New Relic observability platform integration | ai | 0 |
| nexbrowser-mcp | Model Context Protocol server for NexBrowser environment management and browser automation | devtools | 0 |
| next-devtools-mcp | Next.js development tools MCP server with stdio transport | devtools | 0 |
| nexus2520-bitbucket-mcp-server | MCP server for Bitbucket API integration - supports both Cloud and Server | cloud | 0 |
| nexus2520-jira-mcp-server | MCP server for Jira API integration - supports Jira Cloud | cloud | 0 |
| nipunibpaaris-modelcontextprotocol-typescript-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| nocobase-plugin-mcp-server | An MCP server for building NocoBase systems and supporting business workflows. | ai | 0 |
| nocodb-mcp-server | Model Context Protocol server for nocodb | database | 0 |
| notdone-mcp | Model Context Protocol server for NotDone | ai | 0 |
| notebooklm-mcp-server | Node.js Model Context Protocol server for Google NotebookLM | ai | 0 |
| notionhq-notion-mcp-server | Official MCP server for Notion API | productivity | 0 |
| nozomtechs-grc-mcp | MCP server for the Nozom Cybersecurity GRC Platform â€” exposes GRC API endpoints as Model Context Protocol tools. R-EXTSPEC: @modelcontextprotocol/sdk v1.29.0 â€” https://modelcontextprotocol.io/specification/latest | web | 0 |
| nx-mcp | A Model Context Protocol server implementation for Nx | ai | 0 |
| obsidian | Model Context Protocol server for Obsidian Vaults | utilities | 0 |
| oevortex-ddg-search | A Model Context Protocol server for web search using DuckDuckGo, IAsk AI, and Monica AI | search | 0 |
| ohah-react-native-mcp-server | MCP server for React Native app automation and monitoring | monitoring | 0 |
| ohos-chrome-devtools-mcp | Thin wrapper that bridges OpenHarmony ArkWeb (via hdc fport) to chrome-devtools-mcp. The OHOS counterpart of @modelcontextprotocol/chrome-devtools. | devtools | 0 |
| okx-ai-okx-trade-mcp | OKX MCP Server - Model Context Protocol server for OKX exchange | ai | 0 |
| olaservo-mcp-interceptors | TypeScript SDK for Model Context Protocol interceptors (temp publish — fork of @ext-modelcontextprotocol/interceptors) | utilities | 0 |
| onestep-puppeteer-mcp-server | Experimental MCP server for browser automation using Puppeteer (inspired by @modelcontextprotocol/server-puppeteer) | browser | 0 |
| oneuptime-mcp-server | OneUptime MCP Server | utilities | 0 |
| onlyoffice-docspace-mcp | ONLYOFFICE DocSpace Model Context Protocol Server | utilities | 0 |
| onozaty-redmine-mcp-server | MCP server for Redmine | utilities | 0 |
| open-meteo-mcp-server | Model Context Protocol server for Open-Meteo weather APIs | utilities | 0 |
| openai-mcp-server | MCP server for interacting with OpenAI | ai | 0 |
| openai-vision-mcp-server | MCP server for secure, bounded OpenAI-compatible vision analysis | ai | 0 |
| openapi-mcp-generator | Generates MCP server code from OpenAPI specifications | ai | 0 |
| openapi-mcp-server | MCP server for interacting with openapisearch.com API | search | 0 |
| openapi-schema | A Model Context Protocol server that exposes OpenAPI schema information to Large Language Models | ai | 0 |
| openbnb-mcp-server-airbnb | MCP server for Airbnb search and listing details | search | 0 |
| openephemeris-mcp-server | Model Context Protocol server for the Open Ephemeris astronomical computation API | ai | 0 |
| openrpc-mcp-server-updated | OpenRPC MCP server - Updated with latest @modelcontextprotocol/sdk for compatibility with newer clients | utilities | 0 |
| orengrinker-jira-mcp-server | A comprehensive Model Context Protocol server for Jira integration with issue management, board operations, time tracking, and project management capabilities | ai | 0 |
| ouedyan-modelcontextprotocol-server-filesystem | MCP server for filesystem access | filesystem | 0 |
| outline-mcp-server | An MCP server for interacting with Outline's API | utilities | 0 |
| pagespeed | A Model Context Protocol server for Google PageSpeed Insights | utilities | 0 |
| pandacss-mcp | MCP server for Panda CSS AI assistants | ai | 0 |
| paperclipai-mcp-server | Model Context Protocol server for Paperclip. | ai | 0 |
| parseable-parseable-mcp-server | Model Context Protocol server for Parseable. Lets LLMs discover and query Parseable datasets. | ai | 0 |
| pascal-app-mcp | Model Context Protocol server for Pascal 3D editor | ai | 0 |
| pavindulakshan-modelcontextprotocol-typescript-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| pdf ⭐ | MCP server for loading and extracting text from PDF files with chunked pagination and interactive viewer | filesystem | 0 |
| pdf | A Model Context Protocol server for PDF manipulation and operations | ai | 0 |
| penclipai-mcp-server | Model Context Protocol server for Paperclip. | ai | 0 |
| pepk-mcp-memory-sqlite | Production-ready MCP memory server with SQLite WAL for thread-safe concurrent access. Drop-in replacement for @modelcontextprotocol/server-memory. Prevents race conditions and data loss in multi-session AI agent environments. ACID-compliant knowledge grap | database | 0 |
| pg-mcp-server | A Model Context Protocol server for PostgreSQL databases | database | 0 |
| phantom-mcp-server | MCP Server for Phantom Wallet | utilities | 0 |
| picahq-mcp | A Model Context Protocol Server for Pica | utilities | 0 |
| pikku-modelcontextprotocol | A Pikku MCP server runtime using the official MCP SDK | utilities | 0 |
| pinecone-database-mcp | Model Context Protocol server for Pinecone - enables AI assistants to interact with Pinecone indexes and documentation | database | 0 |
| pipedrive-mcp-server | Model Context Protocol server for Pipedrive API integration | utilities | 0 |
| playwright-mcp-server | MCP server for generating Playwright tests | browser | 0 |
| playwright-stealth-mcp-server | Local implementation of Playwright Stealth MCP server | browser | 0 |
| polygraph-mcp | A Model Context Protocol server for coordinating cross-repository changes via Polygraph | utilities | 0 |
| postgres-mcp-hardened | Secure read-only PostgreSQL MCP server in Rust — a maintained alternative to the deprecated @modelcontextprotocol/server-postgres. Blocks writes at the AST, not with regexes. | database | 0 |
| postgres-server | A Model Context Protocol server for PostgreSQL database operations | database | 0 |
| postman-postman-mcp-server | Postman MCP Server — connect AI agents (Claude Code, Cursor, VS Code Copilot, Gemini CLI) to your Postman collections, specifications, and environments via Model Context Protocol (MCP) | ai | 0 |
| powerplatform-mcp | PowerPlatform Model Context Protocol server | utilities | 0 |
| prefecthq-fastmcp-ts | 🏎️  The official FastMCP TypeScript library - build MCP servers and clients, fast 🏎️ | ai | 0 |
| professional-wiki-mediawiki-mcp-server | Model Context Protocol (MCP) server for MediaWiki | utilities | 0 |
| prometheus-mcp | Prometheus MCP Server | utilities | 0 |
| public-ui-mcp | Model Context Protocol server providing AI agents access to 136+ KoliBri component examples, source code, and template repositories. | ai | 0 |
| puppeteer-mcp-server | Experimental MCP server for browser automation using Puppeteer (inspired by @modelcontextprotocol/server-puppeteer) | browser | 0 |
| puppeteer-mcp-server-ws | Experimental MCP server for browser automation using Puppeteer (inspired by @modelcontextprotocol/server-puppeteer) | browser | 0 |
| puppeteer-plus-martech | Puppeteer+ MarTech - Enhanced Puppeteer MCP server with specialized digital marketing analytics capabilities. This builds upon the official @modelcontextprotocol/server-puppeteer with tools for analyzing marketing technologies, analytics platforms, tag ma | devtools | 0 |
| qase-mcp-server | Official MCP server for Qase Test Management Platform | ai | 0 |
| qdrant-api-mcp | Model Context Protocol server for Qdrant Collections & Points APIs | ai | 0 |
| questpie-mcp | Model Context Protocol server for QUESTPIE apps, under the app's own access rules | utilities | 0 |
| rad-security-mcp-server | RAD Security MCP Server for AI-powered security insights | devtools | 0 |
| ramarivera-gpt-image-mcp | A Model Context Protocol server for OpenAI's gpt-image-2 model | ai | 0 |
| razorpay-blade-mcp | Model Context Protocol server for Blade | ai | 0 |
| react-aria-mcp | MCP server for React Aria documentation | utilities | 0 |
| real-browser-mcp-server | MCP Server for Real Browser - Patchright Blocker. | browser | 0 |
| rebasepro-mcp | Model Context Protocol Server for Rebase — exposes schema, DB, document, and user management tools to AI assistants. | database | 0 |
| regle-mcp-server | MCP Server for Regle | ai | 0 |
| rekey.dev-mcp | Model Context Protocol server for Rekey — lets Claude Desktop / Cursor / Claude Code introspect a deployment. | devtools | 0 |
| relay-science-mcp | Model Context Protocol server for the Relay scientific platform | utilities | 0 |
| remnux-mcp-server | MCP server for using the REMnux malware analysis toolkit via AI assistants | ai | 0 |
| retell-ai-mcp-server | The official MCP Server for the Retell API | ai | 0 |
| robinmordasiewicz-f5xc-terraform-mcp | MCP server for F5 Distributed Cloud Terraform provider - documentation, 270+ OpenAPI specs, subscription info, and addon activation workflows for AI assistants | cloud | 0 |
| rockhopper-co-mcp-server | Rockhopper MCP server — expose file metadata, versions, reviews, and comments to AI tools | ai | 0 |
| rolino-mcp | Model Context Protocol server for Rolino | ai | 0 |
| rollbar-mcp-server | Model Context Protocol server for Rollbar | monitoring | 0 |
| roychri-mcp-server-asana | MCP Server for Asana | ai | 0 |
| rtorcato-api-mcp | Tiny result helpers for @modelcontextprotocol/sdk MCP servers. | utilities | 0 |
| runpod-mcp-server | MCP server for interacting with Runpod API | utilities | 0 |
| rushstack-mcp-server | A Model Context Protocol server implementation for Rush | utilities | 0 |
| s3-mcp-server | A Model Context Protocol server that interfaces with S3-compatible storage (like Cloudflare R2). | cloud | 0 |
| saasflow-mcp | Model Context Protocol server for the SaaSFlow public API. | ai | 0 |
| salesforce-mcp | MCP Server for interacting with Salesforce instances | utilities | 0 |
| sap-mdk-mcp-server | Model Context Protocol (MCP) server for AI-assisted development of MDK applications. | devtools | 0 |
| sap-ux-fiori-mcp-server | SAP Fiori - Model Context Protocol (MCP) server | ai | 0 |
| scenario-modeler ⭐ | Financial scenario modeling MCP App Server | utilities | 0 |
| scorecard | Grade any MCP server's agent-readiness in one command — stdio (10 protocol checks) AND hosted/remote servers (10 security + web agent-readiness checks). Open source, local-first, no credentials. | web | 0 |
| scrapeless-mcp-server | Scrapeless Mcp Server | communication | 0 |
| scraper | MCP server for MCP Scraper web intelligence tools | web | 0 |
| search-mcp-server | MCP server for browser automation via Jan Browser extension - provides tools for web navigation, interaction, and search | search | 0 |
| searxng | MCP server for SearXNG integration | search | 0 |
| sechel-mcp-mcp-server | MCP server factory for Sechel — registers all 24 persistent memory tools (`mem_*` + `ping`) on an [`@modelcontextprotocol/sdk`](https://github.com/modelcontextprotocol/typescript-sdk) server instance. | devtools | 0 |
| securestamp-mcp-guard | SecureStamp MCP Guard — a local stdio + remote MCP wrapper for the SecureStamp Agent Trust Layer. Lets MCP hosts (Claude Desktop, Cursor, any @modelcontextprotocol/sdk client) ask SecureStamp for Proof-of-Intent before sensitive tool calls. Authorizes/ver | utilities | 0 |
| serper-search-scrape-mcp-server | Serper MCP Server supporting search and webpage scraping | search | 0 |
| server | mcp server | utilities | 0 |
| server-anthropic | A [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol) server that provides access to Anthropic's AI models through their official API. List available models and send messages to Claude using a secure, standardized interface. [More abou | devtools | 0 |
| servers | Welcome to the **Hello World MCP Server**! This project demonstrates how to set up a server using the [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/typescript-sdk) SDK. It includes tools, prompts, and endpoints for handling server | devtools | 0 |
| sfmc | SFMC AMPscript/SSJS/GTL tools + searchable MCE and MCN developer docs, with full MCN platform support. | devtools | 0 |
| shadcn-ui-mcp-server | MCP server for shadcn/ui component references | utilities | 0 |
| shadertoy ⭐ | MCP App Server example for rendering ShaderToy-compatible GLSL shaders | utilities | 0 |
| sheet-music ⭐ | MCP App Server for rendering and playing sheet music from ABC notation | utilities | 0 |
| shortcut-mcp | Shortcut MCP Server | utilities | 0 |
| shrkcrft-mcp-server | SharkCraft MCP server: 25 tools over @modelcontextprotocol/sdk's stdio transport. | ai | 0 |
| siemens-element-mcp | Element MCP server | ai | 0 |
| siemens-ix-mcp | iX MCP server | ai | 0 |
| siemens-ix-mcp-react | iX MCP server for React | ai | 0 |
| sigmacomputing-slack-mcp-server | MCP server for interacting with Slack | communication | 0 |
| sit-onyx-modelcontextprotocol | MCP (Model Context Protocol) Server that provide onyx specific tools and resources. | utilities | 0 |
| sk-calculator-mcp-server | Initialize the project  npm init -y npx gitignore node  npm pkg set type=module npm install @modelcontextprotocol/sdk npm install | devtools | 0 |
| skillsmp-mcp-server | MCP server for SkillsMP - Search, discover, and install AI coding skills | devtools | 0 |
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
| stableperp-mcp | Model Context Protocol Server for Stableperp on Solana | utilities | 0 |
| stigmer-mcp-server | Model Context Protocol server for the Stigmer platform — exposes Stigmer agents, skills, MCP servers, and workflows as MCP tools and resources | ai | 0 |
| storybook-mcp | MCP server that serves knowledge about your components based on your Storybook stories and documentation | utilities | 0 |
| storybook-mcp-server | MCP server for Storybook - provides AI assistants access to components, stories, properties and screenshots | browser | 0 |
| stripe-mcp | A command line tool for setting up Stripe MCP server | payments | 0 |
| structured-world-gitlab-mcp | Advanced GitLab MCP server | devtools | 0 |
| sum-modelcontextprotocol-sum-number | MCP server for summing two numbers | utilities | 0 |
| supabase-mcp | MCP server for Supabase CRUD operations | ai | 0 |
| supabase-mcp-server-postgrest | MCP server for PostgREST | database | 0 |
| supabase-mcp-server-supabase | MCP server for interacting with Supabase | utilities | 0 |
| superblocksteam-mcp-server | Superblocks MCP server | utilities | 0 |
| suthio-redash-mcp | MCP server for Redash integration | ai | 0 |
| svn-agent-mcp | Strict SVN Model Context Protocol server for agent-safe SVN workflows. | utilities | 0 |
| sylphx-workflow-mcp | Stdio MCP server exposing @sylphx/workflow-engine's governed workflows as native MCP tools (official @modelcontextprotocol/sdk transport). A second-mind from outside the host's own model. | ai | 0 |
| system-monitor ⭐ | System monitor MCP App Server with real-time stats | utilities | 0 |
| szc-ft-mcp-szcd-component-helper | MCP server for szcd component library - built with @modelcontextprotocol/sdk, supports stdio/SSE/dual modes | ai | 0 |
| szjc-szjc-mcp-server | MCP Server for the Szjc API using @modelcontextprotocol/sdk | ai | 0 |
| taazkareem-clickup-mcp-server | ClickUp MCP Server - Powering AI Agents with full ClickUp task, document, and chat management capabilities. | communication | 0 |
| taiga-ui-mcp | Model Context Protocol server providing Taiga UI documentation search and scaffolding tools. | search | 0 |
| tailwindcss-mcp-server | MCP server for TailwindCSS utility classes, documentation, and project assistance | ai | 0 |
| tanstack-start | MCP (Model Context Protocol) integration for TanStack Start | ai | 0 |
| taptap-maker | TapTap Maker local development CLI and MCP server | devtools | 0 |
| targetprocess-mcp-server | MCP server for Tartget Process | utilities | 0 |
| tea-color-to-vars-mcp-server | A basic MCP server example using @modelcontextprotocol/sdk | ai | 0 |
| teolin-mcp-jira | Model Context Protocol server for Doctari Jira integration | project-management | 0 |
| terraform-mcp-server | MCP server for Terraform Registry operations | utilities | 0 |
| testomatio-mcp | Model Context Protocol server for Testomatio API | utilities | 0 |
| testomatio-mcp-enterprise | Enterprise Model Context Protocol server for Testomat.io API with analytics tools | utilities | 0 |
| theia-ai-mcp-server | Theia - MCP Server | ai | 0 |
| thelabnyc-redmine-mcp | An MCP (Model Context Protocol) server that allows AI agents like Claude to interact with Redmine project management data. | ai | 0 |
| theme-registry-refract-mcp | Model Context Protocol server for refract — query + validate a project's theme from an AI agent. | ai | 0 |
| thenomadinorbit-vision-mcp-server | MCP server for AI vision analysis via OpenRouter | ai | 0 |
| therealchristhomas-gitlab-mcp-server | MCP Server for GitLab API operations | devtools | 0 |
| thirdstrandstudio-mcp-figma | MCP server for figma | utilities | 0 |
| threejs ⭐ | Three.js 3D visualization MCP App Server | utilities | 0 |
| thunder-ai-mcp-element-ui | Element Plus 的 ModelContextProtocol (MCP) 服务器 | ai | 0 |
| titen-memory | Agent memory with no API key, no LLM, and no embedding provider. Serves MCP over stdio against a local SQLite store, or Cloudflare Workers + D1. Drop-in for @modelcontextprotocol/server-memory; every memory keeps its source, its scope, and the evidence th | database | 0 |
| tocharianou-mcp-server-kibana | Kibana MCP Server | devtools | 0 |
| todoforai-puppeteer-mcp-server | Experimental MCP server for browser automation using Puppeteer (inspired by @modelcontextprotocol/server-puppeteer) | browser | 0 |
| tokportal-mcp | Public MCP server for the TokPortal API. | ai | 0 |
| ton-mcp | TON MCP Server - Model Context Protocol server for TON blockchain wallet operations | ai | 0 |
| topolo-mcp | Model Context Protocol server for the Topolo platform. Exposes scope-gated tools that third-party agents (Claude, Codex, etc.) can call natively. | utilities | 0 |
| toriihq-torii-mcp | Model Context Protocol server for Torii API | utilities | 0 |
| touchdesigner-mcp-server | MCP server for TouchDesigner | utilities | 0 |
| traceloop-instrumentation-mcp | MCP (Model Context Protocol) Instrumentation | utilities | 0 |
| transcend-io-mcp | Transcend MCP Server — unified server with all domain tools. | ai | 0 |
| transcend-io-mcp-server-admin | Transcend MCP Server — Admin tools. | utilities | 0 |
| transcend-io-mcp-server-assessment | Transcend MCP Server — Assessments tools. | utilities | 0 |
| transcend-io-mcp-server-base | Shared infrastructure for Transcend MCP Server packages. | utilities | 0 |
| transcend-io-mcp-server-consent | Transcend MCP Server — Consent Management tools. | utilities | 0 |
| transcend-io-mcp-server-discovery | Transcend MCP Server — Data Discovery tools. | utilities | 0 |
| transcend-io-mcp-server-docs | Transcend MCP Server — Documentation lookup tools. | utilities | 0 |
| transcend-io-mcp-server-dsr | Transcend MCP Server — DSR Automation tools. | utilities | 0 |
| transcend-io-mcp-server-inventory | Transcend MCP Server — Data Inventory tools. | utilities | 0 |
| transcend-io-mcp-server-preferences | Transcend MCP Server — Preference Management tools. | utilities | 0 |
| transcend-io-mcp-server-workflows | Transcend MCP Server — Workflows tools. | utilities | 0 |
| transcript ⭐ | MCP App Server for live speech transcription | utilities | 0 |
| transloadit-mcp-server | Transloadit MCP server | ai | 0 |
| trello | A Model Context Protocol server for Trello | utilities | 0 |
| triliumnext-mcp | A model context protocol server for TriliumNext Notes | utilities | 0 |
| trycompai-mcp-server | Model Context Protocol (MCP) Server for the *@trycompai/mcp-server* API. | ai | 0 |
| tsmztech-mcp-server-salesforce | A Salesforce connector MCP Server. | ai | 0 |
| tugudush-bitbucket-mcp | A Model Context Protocol server for Bitbucket with read-only operations | ai | 0 |
| twilio-alpha-mcp | This is a Model Context Protocol server that exposes all of Twilio APIs. | utilities | 0 |
| twilio-alpha-openapi-mcp-server | A Model Context Protocol server that to expose OpenAPI specs. | utilities | 0 |
| u-space-mcp | Model Context Protocol server for u-space documentation. | web | 0 |
| ui5-mcp-server | MCP server for SAPUI5/OpenUI5 development | devtools | 0 |
| ui5-webcomponents-mcp-server | Model Context Protocol server for UI5 Web Components development assistance | devtools | 0 |
| unthread-io-mcp-server | Unthread MCP Server | utilities | 0 |
| upstash-mcp-server | MCP server for Upstash | utilities | 0 |
| urbicon-ui-mcp-server | Model Context Protocol server exposing the Urbicon UI component catalog, recipes and design intelligence to LLM agents | ai | 0 |
| usearete-mcp | Arete MCP server (a4-mcp) - Model Context Protocol server for Arete streams | ai | 0 |
| user-postgresql-mcp | A PostgreSQL MCP server built with @modelcontextprotocol/sdk. | database | 0 |
| utcp-mcp | Model Context Protocol integration for UTCP | ai | 0 |
| vaneui-mcp | Model Context Protocol server that exposes VaneUI component documentation as resources for MCP-aware clients. | ai | 0 |
| vantageos-mcp-boilerplate | Clonable MCP server skeleton: dual-transport bootstrap (stdio + Streamable HTTP, stateless) on the official @modelcontextprotocol/sdk, ready to extend with protocol-kit, auth, tenant and UI layers. | web | 0 |
| vantasdk-vanta-mcp-server | Model Context Protocol server for Vanta's security compliance platform | utilities | 0 |
| variflight-ai-variflight-mcp | Variflight MCP Server | ai | 0 |
| viberevert-mcp | Model Context Protocol server for VibeRevert. | utilities | 0 |
| video-resource ⭐ | MCP App Server demonstrating video resources served as base64 blobs | utilities | 0 |
| vikunja-fastmcp | Clean-room, v2-only Vikunja Model Context Protocol server (rebuilt from scratch; no legacy code). | utilities | 0 |
| visulima-vis-mcp | MCP (Model Context Protocol) server for @visulima/vis — exposes vis tooling to AI agents over stdio | ai | 0 |
| vitest-agent-mcp | Model Context Protocol server for vitest-agent. Exposes 53 tools for agent access to test data, TDD lifecycle, and session management. | utilities | 0 |
| viyv-mcp-connect | Dial a Viyv MCP Gateway from any MCP server (official @modelcontextprotocol/sdk or otherwise): announce your tools over outbound WebSocket and serve tool calls locally. The TypeScript peer of viyv_mcp's connect mode. | web | 0 |
| vizejs-musea-mcp-server | MCP server for building Vue.js design systems - component analysis, documentation, variant generation, and design tokens | ai | 0 |
| vk-mcp-server | Model Context Protocol server for VK (VKontakte) social network API | ai | 0 |
| voltagent-mcp-server | VoltAgent MCP server implementation for exposing agents, tools, and workflows via the Model Context Protocol. | utilities | 0 |
| vostride-agent-qa-mcp | Model Context Protocol server and tools for agent-qa authoring and triage. | utilities | 0 |
| vpr99-modelcontextprotocol-sdk | Model Context Protocol implementation for TypeScript | utilities | 0 |
| vuetify-mcp | Model Context Protocol server for Vuetify assistance | ai | 0 |
| weppy-roblox-mcp | MCP (Model Context Protocol) server for Roblox Studio integration - enables AI coding agents to interact with Roblox Studio in real-time | devtools | 0 |
| wiki-explorer ⭐ | Wikipedia link explorer MCP App Server with graph visualization | utilities | 0 |
| williamp29-project-mcp-server | A ModelContextProtocol server to let agents discover your project, such as APIs (using OpenAPI) or other resources. | database | 0 |
| winor30-mcp-server-datadog | MCP server for interacting with Datadog API | monitoring | 0 |
| withone-mcp | A Model Context Protocol Server for One | utilities | 0 |
| wix-mcp | A Model Context Protocol server for Wix AI tools | ai | 0 |
| wonderwhy-er-desktop-commander | MCP server for terminal operations and file editing | devtools | 0 |
| wopal-mcp-server-hotnews | A Model Context Protocol server that provides real-time hot trending topics from major Chinese social platforms and news sites | utilities | 0 |
| wuying-agentbay-mcp-server | Wuying AgentBay MCP Server is a Node.js package that provides seamless integration with Alibaba Cloud's Wuying AgentBay | cloud | 0 |
| xcodebuildmcp | XcodeBuildMCP is a Model Context Protocol server that provides tools for Xcode project management, simulator management, and app utilities. | project-management | 0 |
| xeroapi-xero-mcp-server | MCP server implementation for Xero integration | utilities | 0 |
| xs-shlink-mcp | A Model Context Protocol server for Shlink | utilities | 0 |
| xyd-js-mcp-server | MCP server for xyd | utilities | 0 |
| yamanoku-aria-validate-mcp-server | Model context protocol server for validating ARIA (Accessible Rich Internet Applications) | ai | 0 |
| yandex-tracker | MCP Server for Yandex Tracker API integration. This is a convenience wrapper for @fractalizer/mcp-server-yandex-tracker. | project-management | 0 |
| yandex-wiki | MCP Server for Yandex Wiki API integration. This is a convenience wrapper for @fractalizer/mcp-server-yandex-wiki. | utilities | 0 |
| yapi-auto-mcp | YApi Auto MCP Server - Model Context Protocol server for YApi integration, enables AI tools like Cursor to interact with YApi API documentation | ai | 0 |
| yawlabs-postgres-mcp | PostgreSQL MCP server - query, schema introspection, explain, and health checks for AI assistants | database | 0 |
| yjzf-mcp-server-yjzf | MCP Server for YJZF | utilities | 0 |
| yoda.digital-gitlab-mcp-server | GitLab MCP Server - A Model Context Protocol server for GitLab integration | devtools | 0 |
| yoryoboy-bi-connectif-mcp | A minimal Model Context Protocol server for the Connectif HTTP API | web | 0 |
| youtube-data-mcp-server | YouTube MCP Server Implementation | utilities | 0 |
| yungle-mcp | Model Context Protocol server for Yungle. | filesystem | 0 |
| z-ai-mcp-server | MCP Server for Z.AI - A Model Context Protocol server that provides AI capabilities | ai | 0 |
| zapier-zapier-sdk-mcp | MCP server for Zapier SDK | utilities | 0 |
| zd-mcp-server | Zendesk MCP Server - Model Context Protocol server for Zendesk Support integration | ai | 0 |
| zeddotdev-postgres-context-server | a model context protocol server for postgres | database | 0 |
| zencoderai-slack-mcp-server | MCP server for interacting with Slack | communication | 0 |
| zenixsolutions-netbox-mcp | Model Context Protocol server for the NetBox REST API | utilities | 0 |
| zereight-mcp-gitlab | GitLab MCP server for projects, merge requests, issues, pipelines, wiki, releases, and more | devtools | 0 |
| zereight-sentry-server | A Model Context Protocol server | monitoring | 0 |
| zero-mcp | Zero-boilerplate, lightweight and fast MCP server toolkit. Skip the weight of `@modelcontextprotocol/sdk` and start shipping MCP servers in minutes with minimal code. | communication | 0 |
| zubeid-youtube-mcp-server | YouTube MCP Server Implementation | ai | 0 |
| zudello-modelcontextprotocol | MCP server exposing 106 Zudello ERP automation tools for Claude Desktop and other MCP-compatible clients | ai | 0 |

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
