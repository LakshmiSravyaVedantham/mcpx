"""Tests for the MCP server registry."""

from mcpx.registry import Registry, ServerInfo


class TestRegistry:
    def test_load(self):
        registry = Registry()
        assert len(registry.servers) > 0

    def test_get_existing(self):
        registry = Registry()
        server = registry.get("filesystem")
        assert server is not None
        assert server.name == "filesystem"

    def test_get_missing(self):
        registry = Registry()
        assert registry.get("nonexistent-server-xyz") is None

    def test_search_by_name(self):
        registry = Registry()
        results = registry.search("github")
        assert len(results) > 0
        assert results[0].name == "github"

    def test_search_by_description(self):
        registry = Registry()
        results = registry.search("database")
        assert len(results) > 0

    def test_search_no_results(self):
        registry = Registry()
        results = registry.search("zzzznonexistentzzzz")
        assert len(results) == 0

    def test_by_category(self):
        registry = Registry()
        servers = registry.by_category("database")
        assert len(servers) > 0
        assert all(s.category == "database" for s in servers)

    def test_list_categories(self):
        registry = Registry()
        cats = registry.list_categories()
        assert len(cats) > 0
        assert "database" in cats

    def test_top(self):
        registry = Registry()
        top = registry.top(5)
        assert len(top) == 5
        # Should be sorted by stars descending
        for i in range(len(top) - 1):
            assert top[i].stars >= top[i + 1].stars


class TestServerInfo:
    def test_build_config_basic(self):
        server = ServerInfo(
            name="test",
            description="Test server",
            package="test-pkg",
            install_type="npm",
            command="npx",
            args=["-y", "test-pkg"],
            env={},
            config_params={},
            category="test",
            tags=["test"],
            official=False,
            stars=0,
        )
        config = server.build_config()
        assert config["command"] == "npx"
        assert config["args"] == ["-y", "test-pkg"]
        assert "env" not in config

    def test_build_config_with_params(self):
        server = ServerInfo(
            name="test",
            description="Test server",
            package="test-pkg",
            install_type="npm",
            command="npx",
            args=["-y", "test-pkg", "{path}"],
            env={"TOKEN": "{token}"},
            config_params={
                "path": {"description": "Path", "required": True},
                "token": {"description": "Token", "required": True},
            },
            category="test",
            tags=[],
            official=False,
            stars=0,
        )
        config = server.build_config({"path": "/home", "token": "abc123"})
        assert config["args"] == ["-y", "test-pkg", "/home"]
        assert config["env"]["TOKEN"] == "abc123"

    def test_build_config_with_defaults(self):
        server = ServerInfo(
            name="test",
            description="Test server",
            package="test-pkg",
            install_type="npm",
            command="npx",
            args=["-y", "test-pkg", "{path}"],
            env={},
            config_params={
                "path": {"description": "Path", "default": "/tmp"},
            },
            category="test",
            tags=[],
            official=False,
            stars=0,
        )
        config = server.build_config()
        assert config["args"] == ["-y", "test-pkg", "/tmp"]
