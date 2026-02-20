"""Shared test fixtures for mcpx."""

import json
from pathlib import Path

import pytest


@pytest.fixture
def tmp_config(tmp_path: Path) -> Path:
    """Create a temporary MCP config file."""
    config_path = tmp_path / "mcp.json"
    config_path.write_text(json.dumps({"mcpServers": {}}, indent=2))
    return config_path


@pytest.fixture
def tmp_config_with_servers(tmp_path: Path) -> Path:
    """Create a temporary MCP config with some servers."""
    config_path = tmp_path / "mcp.json"
    config_path.write_text(json.dumps({
        "mcpServers": {
            "filesystem": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"],
            },
            "github": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-github"],
                "env": {"GITHUB_TOKEN": "test-token"},
            },
        }
    }, indent=2))
    return config_path


@pytest.fixture
def empty_config(tmp_path: Path) -> Path:
    """Create a temporary empty config file."""
    config_path = tmp_path / "mcp.json"
    config_path.write_text("{}")
    return config_path
