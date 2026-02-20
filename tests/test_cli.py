"""Tests for the CLI interface."""

from typer.testing import CliRunner

from mcpx.cli import app

runner = CliRunner()


class TestCLI:
    def test_version(self):
        result = runner.invoke(app, ["--version"])
        assert result.exit_code == 0
        assert "0.1.0" in result.output

    def test_no_args(self):
        result = runner.invoke(app, [])
        # typer returns 2 for no-args with no_args_is_help=True
        assert result.exit_code in (0, 2)

    def test_search(self):
        result = runner.invoke(app, ["search", "github"])
        assert result.exit_code == 0
        assert "github" in result.output.lower()

    def test_search_no_results(self):
        result = runner.invoke(app, ["search", "zzzznonexistentzzzz"])
        assert result.exit_code == 1

    def test_top(self):
        result = runner.invoke(app, ["top"])
        assert result.exit_code == 0

    def test_top_custom_count(self):
        result = runner.invoke(app, ["top", "--count", "5"])
        assert result.exit_code == 0

    def test_categories(self):
        result = runner.invoke(app, ["categories"])
        assert result.exit_code == 0
        assert "database" in result.output.lower()

    def test_browse(self):
        result = runner.invoke(app, ["browse", "database"])
        assert result.exit_code == 0

    def test_browse_invalid(self):
        result = runner.invoke(app, ["browse", "nonexistent-category"])
        assert result.exit_code == 1

    def test_info(self):
        result = runner.invoke(app, ["info", "filesystem"])
        assert result.exit_code == 0
        assert "filesystem" in result.output.lower()

    def test_info_not_found(self):
        result = runner.invoke(app, ["info", "nonexistent-server"])
        assert result.exit_code == 1

    def test_list_empty(self, tmp_path):
        config = tmp_path / "mcp.json"
        config.write_text('{"mcpServers": {}}')
        result = runner.invoke(app, ["list", "--config", str(config)])
        assert result.exit_code == 0
        assert "No MCP servers installed" in result.output

    def test_install_and_uninstall(self, tmp_path):
        config = tmp_path / "mcp.json"
        config.write_text('{"mcpServers": {}}')

        # Install
        result = runner.invoke(
            app,
            ["install", "filesystem", "--config", str(config), "--param", "path=/tmp"],
        )
        assert result.exit_code == 0
        assert "Installed" in result.output

        # List
        result = runner.invoke(app, ["list", "--config", str(config)])
        assert "filesystem" in result.output

        # Uninstall
        result = runner.invoke(
            app, ["uninstall", "filesystem", "--config", str(config)]
        )
        assert result.exit_code == 0

    def test_install_not_found(self, tmp_path):
        config = tmp_path / "mcp.json"
        config.write_text('{"mcpServers": {}}')
        result = runner.invoke(
            app, ["install", "nonexistent-server-xyz", "--config", str(config)]
        )
        assert result.exit_code == 1

    def test_doctor(self, tmp_path):
        config = tmp_path / "mcp.json"
        config.write_text('{"mcpServers": {}}')
        result = runner.invoke(app, ["doctor", "--config", str(config)])
        assert result.exit_code == 0

    def test_init(self, tmp_path):
        config = tmp_path / "new_config.json"
        result = runner.invoke(app, ["init", "--config", str(config)])
        assert result.exit_code == 0
        assert config.exists()

    def test_platforms(self):
        result = runner.invoke(app, ["platforms"])
        assert result.exit_code == 0
