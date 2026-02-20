"""Tests for the config manager."""

import json
from pathlib import Path

from mcpx.config import (
    add_server_to_config,
    get_installed_servers,
    read_config,
    remove_server_from_config,
    write_config,
)


class TestReadConfig:
    def test_read_existing(self, tmp_config: Path):
        config = read_config(tmp_config)
        assert "mcpServers" in config

    def test_read_missing(self, tmp_path: Path):
        config = read_config(tmp_path / "nonexistent.json")
        assert config == {"mcpServers": {}}

    def test_read_invalid_json(self, tmp_path: Path):
        bad = tmp_path / "bad.json"
        bad.write_text("not json at all")
        config = read_config(bad)
        assert config == {"mcpServers": {}}

    def test_read_missing_servers_key(self, empty_config: Path):
        config = read_config(empty_config)
        assert "mcpServers" in config


class TestWriteConfig:
    def test_write_creates_file(self, tmp_path: Path):
        config_path = tmp_path / "subdir" / "mcp.json"
        write_config(config_path, {"mcpServers": {"test": {}}})
        assert config_path.exists()
        data = json.loads(config_path.read_text())
        assert "test" in data["mcpServers"]


class TestGetInstalledServers:
    def test_empty(self, tmp_config: Path):
        servers = get_installed_servers(tmp_config)
        assert servers == {}

    def test_with_servers(self, tmp_config_with_servers: Path):
        servers = get_installed_servers(tmp_config_with_servers)
        assert "filesystem" in servers
        assert "github" in servers


class TestAddServer:
    def test_add_new(self, tmp_config: Path):
        add_server_to_config(tmp_config, "test-server", {"command": "npx", "args": []})
        servers = get_installed_servers(tmp_config)
        assert "test-server" in servers

    def test_add_overwrites(self, tmp_config_with_servers: Path):
        add_server_to_config(
            tmp_config_with_servers,
            "filesystem",
            {"command": "npx", "args": ["new-args"]},
        )
        servers = get_installed_servers(tmp_config_with_servers)
        assert servers["filesystem"]["args"] == ["new-args"]


class TestRemoveServer:
    def test_remove_existing(self, tmp_config_with_servers: Path):
        result = remove_server_from_config(tmp_config_with_servers, "filesystem")
        assert result is True
        servers = get_installed_servers(tmp_config_with_servers)
        assert "filesystem" not in servers

    def test_remove_missing(self, tmp_config: Path):
        result = remove_server_from_config(tmp_config, "nonexistent")
        assert result is False
