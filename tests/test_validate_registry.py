"""Tests for registry_data.json validation logic.

Mirrors the validation that runs in the validate-registry.yml workflow,
so we can catch issues locally before pushing.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

REGISTRY_PATH = (
    Path(__file__).resolve().parent.parent / "src" / "mcpx" / "registry_data.json"
)

REQUIRED_FIELDS = [
    "name",
    "description",
    "package",
    "install_type",
    "command",
    "args",
    "category",
    "tags",
]


@pytest.fixture
def registry_data() -> dict:
    """Load the actual registry data."""
    with open(REGISTRY_PATH, encoding="utf-8") as f:
        return json.load(f)


class TestRegistryValidation:
    def test_registry_is_valid_json(self):
        """Registry file must be valid JSON."""
        with open(REGISTRY_PATH, encoding="utf-8") as f:
            data = json.load(f)
        assert "servers" in data

    def test_servers_not_empty(self, registry_data: dict):
        """Registry must contain at least one server."""
        assert len(registry_data["servers"]) > 0

    def test_all_required_fields_present(self, registry_data: dict):
        """Every server must have all required fields."""
        for server in registry_data["servers"]:
            for field in REQUIRED_FIELDS:
                assert field in server, (
                    f"Server '{server.get('name', 'UNKNOWN')}' "
                    f"missing required field '{field}'"
                )

    def test_no_empty_required_fields(self, registry_data: dict):
        """Required fields (except tags) must not be empty."""
        for server in registry_data["servers"]:
            for field in REQUIRED_FIELDS:
                if field == "tags":
                    continue  # tags can be empty list
                value = server.get(field)
                assert value, f"Server '{server['name']}' has empty field '{field}'"

    def test_no_duplicate_names(self, registry_data: dict):
        """Server names must be unique."""
        names = [s["name"] for s in registry_data["servers"]]
        duplicates = [n for n in names if names.count(n) > 1]
        assert len(duplicates) == 0, f"Duplicate server names: {set(duplicates)}"

    def test_no_duplicate_packages(self, registry_data: dict):
        """Package names must be unique."""
        packages = [s["package"] for s in registry_data["servers"]]
        duplicates = [p for p in packages if packages.count(p) > 1]
        assert len(duplicates) == 0, f"Duplicate packages: {set(duplicates)}"

    def test_args_is_list(self, registry_data: dict):
        """The args field must be a list."""
        for server in registry_data["servers"]:
            assert isinstance(
                server["args"], list
            ), f"Server '{server['name']}' args is not a list"

    def test_tags_is_list(self, registry_data: dict):
        """The tags field must be a list."""
        for server in registry_data["servers"]:
            assert isinstance(
                server["tags"], list
            ), f"Server '{server['name']}' tags is not a list"

    def test_valid_install_type(self, registry_data: dict):
        """install_type must be npm, pip, or binary."""
        valid_types = {"npm", "pip", "binary"}
        for server in registry_data["servers"]:
            assert server["install_type"] in valid_types, (
                f"Server '{server['name']}' has invalid "
                f"install_type '{server['install_type']}'"
            )

    def test_categories_have_info(self, registry_data: dict):
        """Each server category should exist in the categories dict."""
        categories = registry_data.get("categories", {})
        for server in registry_data["servers"]:
            cat = server["category"]
            assert cat in categories, (
                f"Server '{server['name']}' has category '{cat}' "
                f"not defined in categories dict"
            )
