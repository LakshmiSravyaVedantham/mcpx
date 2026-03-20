"""Tests for scripts/check_freshness.py."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock

import httpx
import pytest

import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from check_freshness import (
    apply_star_updates,
    check_all_packages,
    check_npm_package,
    extract_github_repo,
    get_github_stars,
    save_registry,
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
            {
                "name": "removed-pkg",
                "description": "This package was removed from npm",
                "package": "mcp-server-removed",
                "install_type": "npm",
                "command": "npx",
                "args": ["-y", "mcp-server-removed"],
                "category": "utilities",
                "tags": [],
                "official": False,
                "stars": 100,
            },
        ],
        "categories": {},
    }
    path = tmp_path / "registry_data.json"
    path.write_text(json.dumps(data, indent=2))
    return path


class TestExtractGithubRepo:
    def test_https_url(self):
        url = "https://github.com/modelcontextprotocol/servers"
        assert extract_github_repo(url) == "modelcontextprotocol/servers"

    def test_git_plus_https(self):
        url = "git+https://github.com/owner/repo.git"
        assert extract_github_repo(url) == "owner/repo"

    def test_git_protocol(self):
        url = "git://github.com/owner/repo.git"
        assert extract_github_repo(url) == "owner/repo"

    def test_github_shorthand(self):
        url = "github:owner/repo"
        assert extract_github_repo(url) == "owner/repo"

    def test_empty_string(self):
        assert extract_github_repo("") is None

    def test_non_github_url(self):
        assert extract_github_repo("https://gitlab.com/owner/repo") is None

    def test_ssh_url(self):
        url = "git@github.com:owner/repo.git"
        assert extract_github_repo(url) == "owner/repo"


class TestCheckNpmPackage:
    def test_existing_package(self):
        mock_client = MagicMock(spec=httpx.Client)
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = {
            "dist-tags": {"latest": "1.0.0"},
            "versions": {"1.0.0": {"deprecated": None}},
            "repository": {"url": "https://github.com/owner/repo"},
        }
        mock_client.get.return_value = mock_response

        result = check_npm_package("test-pkg", client=mock_client)
        assert result["exists"] is True
        assert result["version"] == "1.0.0"
        assert result["deprecated"] is None

    def test_missing_package(self):
        mock_client = MagicMock(spec=httpx.Client)
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_client.get.return_value = mock_response

        result = check_npm_package("nonexistent-pkg", client=mock_client)
        assert result["exists"] is False

    def test_deprecated_package(self):
        mock_client = MagicMock(spec=httpx.Client)
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.raise_for_status = MagicMock()
        mock_response.json.return_value = {
            "dist-tags": {"latest": "2.0.0"},
            "versions": {"2.0.0": {"deprecated": "Use new-package instead"}},
            "repository": {},
        }
        mock_client.get.return_value = mock_response

        result = check_npm_package("old-pkg", client=mock_client)
        assert result["exists"] is True
        assert result["deprecated"] == "Use new-package instead"

    def test_network_error(self):
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.get.side_effect = httpx.ConnectError("connection failed")

        result = check_npm_package("test-pkg", client=mock_client)
        assert result["exists"] is None
        assert result.get("error") == "network_error"


class TestGetGithubStars:
    def test_returns_star_count(self):
        mock_client = MagicMock(spec=httpx.Client)
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"stargazers_count": 1234}
        mock_client.get.return_value = mock_response

        stars = get_github_stars("owner/repo", client=mock_client)
        assert stars == 1234

    def test_with_token(self):
        mock_client = MagicMock(spec=httpx.Client)
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"stargazers_count": 500}
        mock_client.get.return_value = mock_response

        stars = get_github_stars(
            "owner/repo", client=mock_client, github_token="ghp_test"
        )
        assert stars == 500
        # Verify token was passed in headers
        call_kwargs = mock_client.get.call_args
        headers = call_kwargs.kwargs.get("headers", {})
        assert "Authorization" in headers

    def test_repo_not_found(self):
        mock_client = MagicMock(spec=httpx.Client)
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_client.get.return_value = mock_response

        stars = get_github_stars("owner/nonexistent", client=mock_client)
        assert stars is None

    def test_network_error(self):
        mock_client = MagicMock(spec=httpx.Client)
        mock_client.get.side_effect = httpx.ConnectError("timeout")

        stars = get_github_stars("owner/repo", client=mock_client)
        assert stars is None


class TestCheckAllPackages:
    def test_detects_removed_packages(self, sample_registry: Path):
        def npm_side_effect(url, **kwargs):
            mock_response = MagicMock()
            if "mcp-server-removed" in url:
                mock_response.status_code = 404
            else:
                mock_response.status_code = 200
                mock_response.raise_for_status = MagicMock()
                mock_response.json.return_value = {
                    "dist-tags": {"latest": "1.0.0"},
                    "versions": {"1.0.0": {}},
                    "repository": {},
                }
            return mock_response

        npm_client = MagicMock(spec=httpx.Client)
        npm_client.get.side_effect = npm_side_effect

        results = check_all_packages(
            registry_path=sample_registry,
            npm_client=npm_client,
        )
        assert "removed-pkg" in results["removed"]
        assert "filesystem" not in results["removed"]

    def test_detects_star_updates(self, sample_registry: Path):
        def npm_side_effect(url, **kwargs):
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.raise_for_status = MagicMock()
            mock_response.json.return_value = {
                "dist-tags": {"latest": "1.0.0"},
                "versions": {"1.0.0": {}},
                "repository": {"url": "https://github.com/owner/repo"},
            }
            return mock_response

        def github_side_effect(url, headers=None, **kwargs):
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"stargazers_count": 9999}
            return mock_response

        npm_client = MagicMock(spec=httpx.Client)
        npm_client.get.side_effect = npm_side_effect

        github_client = MagicMock(spec=httpx.Client)
        github_client.get.side_effect = github_side_effect

        results = check_all_packages(
            registry_path=sample_registry,
            npm_client=npm_client,
            github_client=github_client,
        )
        assert "filesystem" in results["star_updates"]
        assert results["star_updates"]["filesystem"] == 9999


class TestApplyStarUpdates:
    def test_updates_stars_in_file(self, sample_registry: Path):
        updates = {"filesystem": 7777}
        data = apply_star_updates(updates, registry_path=sample_registry)

        # Verify in-memory
        fs_server = next(s for s in data["servers"] if s["name"] == "filesystem")
        assert fs_server["stars"] == 7777

        # Verify on disk
        saved = json.loads(sample_registry.read_text())
        fs_saved = next(s for s in saved["servers"] if s["name"] == "filesystem")
        assert fs_saved["stars"] == 7777

    def test_no_updates_preserves_file(self, sample_registry: Path):
        apply_star_updates({}, registry_path=sample_registry)
        # File is rewritten but content should be equivalent
        saved = json.loads(sample_registry.read_text())
        assert len(saved["servers"]) == 2


class TestSaveRegistry:
    def test_saves_valid_json(self, tmp_path: Path):
        path = tmp_path / "test_registry.json"
        data = {"version": "1.0.0", "servers": []}
        save_registry(data, path)

        loaded = json.loads(path.read_text())
        assert loaded == data
