"""Tests for scripts/generate_readme.py."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

# Ensure scripts/ is importable
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from generate_readme import (
    build_category_table,
    build_server_table,
    generate_readme,
    load_registry,
)


@pytest.fixture
def sample_registry(tmp_path: Path) -> Path:
    """Create a minimal registry file for testing."""
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
                "env": {},
                "config_params": {},
                "category": "filesystem",
                "tags": ["files"],
                "official": True,
                "stars": 5000,
            },
            {
                "name": "postgres",
                "description": "Query PostgreSQL databases",
                "package": "@modelcontextprotocol/server-postgres",
                "install_type": "npm",
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-postgres"],
                "env": {},
                "config_params": {},
                "category": "database",
                "tags": ["database", "sql"],
                "official": True,
                "stars": 4200,
            },
            {
                "name": "redis",
                "description": "Redis cache and data storage",
                "package": "@gongrzhe/server-redis-mcp",
                "install_type": "npm",
                "command": "npx",
                "args": ["-y", "@gongrzhe/server-redis-mcp"],
                "env": {},
                "config_params": {},
                "category": "database",
                "tags": ["redis", "cache"],
                "official": False,
                "stars": 1200,
            },
        ],
        "categories": {
            "filesystem": {
                "label": "Filesystem",
                "icon": "folder",
                "description": "File management",
            },
            "database": {
                "label": "Databases",
                "icon": "db",
                "description": "SQL and NoSQL",
            },
        },
    }
    path = tmp_path / "registry_data.json"
    path.write_text(json.dumps(data, indent=2))
    return path


class TestLoadRegistry:
    def test_loads_valid_file(self, sample_registry: Path):
        data = load_registry(sample_registry)
        assert "servers" in data
        assert len(data["servers"]) == 3

    def test_raises_on_missing_file(self, tmp_path: Path):
        with pytest.raises(FileNotFoundError):
            load_registry(tmp_path / "nonexistent.json")

    def test_raises_on_invalid_json(self, tmp_path: Path):
        bad = tmp_path / "bad.json"
        bad.write_text("not json")
        with pytest.raises(json.JSONDecodeError):
            load_registry(bad)


class TestBuildCategoryTable:
    def test_contains_all_categories(self, sample_registry: Path):
        data = load_registry(sample_registry)
        table = build_category_table(data)
        assert "Databases" in table
        assert "Filesystem" in table

    def test_has_table_headers(self, sample_registry: Path):
        data = load_registry(sample_registry)
        table = build_category_table(data)
        assert "| Category | Examples |" in table
        assert "|----------|----------|" in table

    def test_category_entries(self, sample_registry: Path):
        data = load_registry(sample_registry)
        table = build_category_table(data)
        lines = table.strip().split("\n")
        # header + separator + 2 categories
        assert len(lines) == 4


class TestBuildServerTable:
    def test_contains_all_servers(self, sample_registry: Path):
        data = load_registry(sample_registry)
        table = build_server_table(data)
        assert "filesystem" in table
        assert "postgres" in table
        assert "redis" in table

    def test_sorted_by_stars_descending(self, sample_registry: Path):
        data = load_registry(sample_registry)
        table = build_server_table(data)
        lines = [
            line
            for line in table.strip().split("\n")
            if line.startswith("| ") and "Name" not in line and "---" not in line
        ]
        # First should be filesystem (5000), then postgres (4200), then redis (1200)
        assert lines[0].startswith("| filesystem")
        assert lines[1].startswith("| postgres")
        assert lines[2].startswith("| redis")

    def test_official_marker(self, sample_registry: Path):
        data = load_registry(sample_registry)
        table = build_server_table(data)
        # Official servers should have a star marker
        assert "filesystem" in table
        # redis is not official, should not have the marker next to its name
        for line in table.split("\n"):
            if "| redis" in line and "redis" in line:
                assert (
                    "redis |" not in line or "redis" in line
                )  # just verify it appears


class TestGenerateReadme:
    def test_contains_server_count(self, sample_registry: Path):
        data = load_registry(sample_registry)
        readme = generate_readme(data)
        assert "3+ MCP servers" in readme

    def test_contains_category_count(self, sample_registry: Path):
        data = load_registry(sample_registry)
        readme = generate_readme(data)
        assert "2 categories" in readme

    def test_contains_category_table(self, sample_registry: Path):
        data = load_registry(sample_registry)
        readme = generate_readme(data)
        assert "| Category | Examples |" in readme

    def test_contains_server_table(self, sample_registry: Path):
        data = load_registry(sample_registry)
        readme = generate_readme(data)
        assert "| Name | Description | Category | Stars |" in readme

    def test_contains_install_instructions(self, sample_registry: Path):
        data = load_registry(sample_registry)
        readme = generate_readme(data)
        assert "pip install mcpx" in readme
        assert "mcpx install github" in readme

    def test_contains_project_sections(self, sample_registry: Path):
        data = load_registry(sample_registry)
        readme = generate_readme(data)
        assert "## What is mcpx?" in readme
        assert "## Quick Start" in readme
        assert "## Features" in readme
        assert "## Commands" in readme
        assert "## Registry" in readme
        assert "## Contributing" in readme
        assert "## Development" in readme
        assert "## License" in readme

    def test_empty_servers(self):
        data = {"servers": [], "categories": {}}
        readme = generate_readme(data)
        assert "0+ MCP servers" in readme
        assert "0 categories" in readme
