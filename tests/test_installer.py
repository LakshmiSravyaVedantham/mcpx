"""Tests for the installer module."""

import json
from pathlib import Path

from mcpx.installer import install_server, uninstall_server, verify_server_deps
from mcpx.registry import ServerInfo


def _make_server(**kwargs) -> ServerInfo:
    defaults = dict(
        name="test-server",
        description="A test server",
        package="test-pkg",
        install_type="npm",
        command="npx",
        args=["-y", "test-pkg"],
        env={},
        config_params={},
        category="test",
        tags=[],
        official=False,
        stars=0,
    )
    defaults.update(kwargs)
    return ServerInfo(**defaults)


class TestInstallServer:
    def test_install(self, tmp_config: Path):
        server = _make_server()
        success, msg = install_server(server, tmp_config)
        assert success
        data = json.loads(tmp_config.read_text())
        assert "test-server" in data["mcpServers"]

    def test_install_with_params(self, tmp_config: Path):
        server = _make_server(
            args=["-y", "test-pkg", "{path}"],
            env={"TOKEN": "{token}"},
            config_params={
                "path": {"description": "Path"},
                "token": {"description": "Token"},
            },
        )
        success, msg = install_server(
            server, tmp_config, {"path": "/data", "token": "xyz"}
        )
        assert success
        data = json.loads(tmp_config.read_text())
        entry = data["mcpServers"]["test-server"]
        assert "/data" in entry["args"]
        assert entry["env"]["TOKEN"] == "xyz"


class TestUninstallServer:
    def test_uninstall_existing(self, tmp_config_with_servers: Path):
        success, msg = uninstall_server("filesystem", tmp_config_with_servers)
        assert success

    def test_uninstall_missing(self, tmp_config: Path):
        success, msg = uninstall_server("nonexistent", tmp_config)
        assert not success


class TestVerifyDeps:
    def test_npm_server(self):
        server = _make_server(install_type="npm")
        issues = verify_server_deps(server)
        # npx might or might not be available in test env — just check it returns a list
        assert isinstance(issues, list)

    def test_unknown_type(self):
        server = _make_server(install_type="binary")
        issues = verify_server_deps(server)
        assert issues == []
