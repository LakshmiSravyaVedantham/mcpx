"""Tests for scripts/scan_registry.py."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock

import httpx
import pytest

import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from scan_registry import (
    build_new_entry,
    get_existing_packages,
    guess_category,
    is_mcp_server_package,
    load_registry,
    scan_for_new_packages,
    search_npm,
)


@pytest.fixture
def sample_registry(tmp_path: Path) -> Path:
    """Create a minimal registry for testing."""
    data = {
        "version": "1.0.0",
        "servers": [
            {
                "name": "filesystem",
                "description": "Read and write files",
                "package": "@modelcontextprotocol/server-filesystem",
                "install_type": "npm",
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-filesystem"],
                "category": "filesystem",
                "tags": ["files"],
                "official": True,
                "stars": 5000,
            },
        ],
        "categories": {},
    }
    path = tmp_path / "registry_data.json"
    path.write_text(json.dumps(data, indent=2))
    return path


@pytest.fixture
def mock_npm_response() -> dict:
    """A mock npm search API response."""
    return {
        "objects": [
            {
                "package": {
                    "name": "mcp-server-new-tool",
                    "description": "A new MCP server for some tool",
                    "version": "1.0.0",
                    "date": "2026-01-01T00:00:00.000Z",
                    "keywords": ["mcp", "server"],
                    "links": {
                        "npm": "https://www.npmjs.com/package/mcp-server-new-tool"
                    },
                    "publisher": {"username": "testuser"},
                },
                "score": {"final": 0.85},
            },
            {
                "package": {
                    "name": "totally-unrelated-package",
                    "description": "Nothing to do with MCP",
                    "version": "2.0.0",
                    "date": "2026-01-01T00:00:00.000Z",
                    "keywords": ["widget"],
                    "links": {},
                    "publisher": {"username": "other"},
                },
                "score": {"final": 0.5},
            },
            {
                "package": {
                    "name": "@modelcontextprotocol/server-filesystem",
                    "description": "Filesystem MCP server",
                    "version": "1.0.0",
                    "date": "2026-01-01T00:00:00.000Z",
                    "keywords": ["mcp", "server"],
                    "links": {},
                    "publisher": {},
                },
                "score": {"final": 0.9},
            },
        ]
    }


class TestGetExistingPackages:
    def test_extracts_package_names(self, sample_registry: Path):
        data = load_registry(sample_registry)
        packages = get_existing_packages(data)
        assert "@modelcontextprotocol/server-filesystem" in packages

    def test_empty_registry(self):
        packages = get_existing_packages({"servers": []})
        assert packages == set()


class TestIsMcpServerPackage:
    def test_name_with_mcp_server(self):
        pkg = {"name": "mcp-server-postgres", "keywords": [], "description": ""}
        assert is_mcp_server_package(pkg) is True

    def test_official_package(self):
        pkg = {
            "name": "@modelcontextprotocol/server-fetch",
            "keywords": [],
            "description": "",
        }
        assert is_mcp_server_package(pkg) is True

    def test_keyword_mcp_server(self):
        pkg = {
            "name": "some-random-tool",
            "keywords": ["mcp", "server"],
            "description": "",
        }
        assert is_mcp_server_package(pkg) is True

    def test_description_mcp_server(self):
        pkg = {
            "name": "cool-tool",
            "keywords": [],
            "description": "An MCP server for cool things",
        }
        assert is_mcp_server_package(pkg) is True

    def test_unrelated_package(self):
        pkg = {
            "name": "express",
            "keywords": ["web", "framework"],
            "description": "Fast web framework for Node.js",
        }
        assert is_mcp_server_package(pkg) is False

    def test_empty_fields(self):
        pkg = {"name": "", "keywords": [], "description": ""}
        assert is_mcp_server_package(pkg) is False


class TestGuessCategory:
    def test_database_keywords(self):
        pkg = {
            "name": "mcp-server-postgres",
            "keywords": ["database"],
            "description": "",
        }
        assert guess_category(pkg) == "database"

    def test_ai_keywords(self):
        pkg = {"name": "mcp-openai", "keywords": ["openai", "llm"], "description": ""}
        assert guess_category(pkg) == "ai"

    def test_cloud_description(self):
        pkg = {
            "name": "mcp-server-aws",
            "keywords": [],
            "description": "AWS cloud services",
        }
        assert guess_category(pkg) == "cloud"

    def test_unknown_defaults_to_utilities(self):
        pkg = {
            "name": "mcp-server-xyz",
            "keywords": [],
            "description": "Does something",
        }
        assert guess_category(pkg) == "utilities"


class TestBuildNewEntry:
    def test_basic_entry(self):
        pkg = {
            "name": "mcp-server-postgres",
            "description": "PostgreSQL MCP server",
            "keywords": ["database", "sql"],
        }
        entry = build_new_entry(pkg)
        assert entry["name"] == "postgres"
        assert entry["package"] == "mcp-server-postgres"
        assert entry["install_type"] == "npm"
        assert entry["command"] == "npx"
        assert entry["args"] == ["-y", "mcp-server-postgres"]

    def test_scoped_package(self):
        pkg = {
            "name": "@modelcontextprotocol/server-fetch",
            "description": "Fetch MCP server",
            "keywords": [],
        }
        entry = build_new_entry(pkg)
        assert entry["name"] == "fetch"
        assert entry["official"] is True

    def test_non_official_package(self):
        pkg = {
            "name": "mcp-server-custom",
            "description": "Custom server",
            "keywords": [],
        }
        entry = build_new_entry(pkg)
        assert entry["official"] is False
        assert entry["stars"] == 0

    def test_tags_limited(self):
        pkg = {
            "name": "mcp-server-test",
            "description": "Test",
            "keywords": [f"tag{i}" for i in range(20)],
        }
        entry = build_new_entry(pkg)
        assert len(entry["tags"]) <= 10


class TestSearchNpm:
    def test_parses_response(self, mock_npm_response: dict):
        mock_client = MagicMock(spec=httpx.Client)
        mock_response = MagicMock()
        mock_response.json.return_value = mock_npm_response
        mock_response.raise_for_status = MagicMock()
        mock_client.get.return_value = mock_response

        results = search_npm("mcp-server", client=mock_client)
        assert len(results) == 3
        assert results[0]["name"] == "mcp-server-new-tool"
        assert results[0]["score"] == 0.85

    def test_empty_response(self):
        mock_client = MagicMock(spec=httpx.Client)
        mock_response = MagicMock()
        mock_response.json.return_value = {"objects": []}
        mock_response.raise_for_status = MagicMock()
        mock_client.get.return_value = mock_response

        results = search_npm("mcp-server", client=mock_client)
        assert results == []


class TestScanForNewPackages:
    def test_filters_existing_and_non_mcp(
        self, sample_registry: Path, mock_npm_response: dict
    ):
        mock_client = MagicMock(spec=httpx.Client)
        mock_response = MagicMock()
        mock_response.json.return_value = mock_npm_response
        mock_response.raise_for_status = MagicMock()
        mock_client.get.return_value = mock_response

        new_entries = scan_for_new_packages(
            registry_path=sample_registry, client=mock_client
        )
        # Should find mcp-server-new-tool (new, is MCP)
        # Should NOT find: totally-unrelated-package (not MCP),
        # @modelcontextprotocol/server-filesystem (already in registry)
        names = [e["name"] for e in new_entries]
        assert "new-tool" in names
        assert "filesystem" not in names

    def test_handles_network_errors(self, sample_registry: Path):
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.get.side_effect = httpx.ConnectError("network down")

        new_entries = scan_for_new_packages(
            registry_path=sample_registry, client=mock_client
        )
        # Should return empty on network errors (graceful degradation)
        assert new_entries == []
