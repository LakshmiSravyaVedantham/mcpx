"""Config manager: auto-detect and manage MCP configs for Claude Code, Cursor, VS Code."""

from __future__ import annotations

import json
import os
import platform
from dataclasses import dataclass
from pathlib import Path
from typing import Any

CONFIG_FILE_NAME = ".mcp.json"


@dataclass
class Platform:
    name: str
    config_path: Path
    exists: bool = False


def _home() -> Path:
    return Path.home()


def _detect_os() -> str:
    system = platform.system()
    if system == "Darwin":
        return "macos"
    elif system == "Windows":
        return "windows"
    return "linux"


def get_claude_code_config_path() -> Path:
    return _home() / ".claude.json"


def get_cursor_config_path() -> Path:
    os_name = _detect_os()
    if os_name == "macos":
        return (
            _home()
            / "Library"
            / "Application Support"
            / "Cursor"
            / "User"
            / "globalStorage"
            / "cursor.mcp"
            / "mcp.json"
        )
    elif os_name == "windows":
        return (
            Path(os.environ.get("APPDATA", ""))
            / "Cursor"
            / "User"
            / "globalStorage"
            / "cursor.mcp"
            / "mcp.json"
        )
    return (
        _home()
        / ".config"
        / "Cursor"
        / "User"
        / "globalStorage"
        / "cursor.mcp"
        / "mcp.json"
    )


def get_vscode_config_path() -> Path:
    os_name = _detect_os()
    if os_name == "macos":
        return (
            _home()
            / "Library"
            / "Application Support"
            / "Code"
            / "User"
            / "globalStorage"
            / "vscode.mcp"
            / "mcp.json"
        )
    elif os_name == "windows":
        return (
            Path(os.environ.get("APPDATA", ""))
            / "Code"
            / "User"
            / "globalStorage"
            / "vscode.mcp"
            / "mcp.json"
        )
    return (
        _home()
        / ".config"
        / "Code"
        / "User"
        / "globalStorage"
        / "vscode.mcp"
        / "mcp.json"
    )


def get_project_config_path() -> Path:
    return Path.cwd() / ".mcp.json"


def detect_platforms() -> list[Platform]:
    """Detect which AI platforms are installed."""
    platforms = []

    claude_path = get_claude_code_config_path()
    platforms.append(
        Platform(
            name="Claude Code",
            config_path=claude_path,
            exists=claude_path.exists(),
        )
    )

    cursor_path = get_cursor_config_path()
    platforms.append(
        Platform(
            name="Cursor",
            config_path=cursor_path,
            exists=cursor_path.parent.exists(),
        )
    )

    project_path = get_project_config_path()
    platforms.append(
        Platform(
            name="Project (.mcp.json)",
            config_path=project_path,
            exists=project_path.exists(),
        )
    )

    return platforms


def read_config(config_path: Path) -> dict[str, Any]:
    """Read MCP config from a file."""
    if not config_path.exists():
        return {"mcpServers": {}}
    try:
        text = config_path.read_text(encoding="utf-8")
        data = json.loads(text)
        if "mcpServers" not in data:
            data["mcpServers"] = {}
        return data
    except (json.JSONDecodeError, OSError):
        return {"mcpServers": {}}


def write_config(config_path: Path, config: dict[str, Any]) -> None:
    """Write MCP config to a file."""
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(
        json.dumps(config, indent=2) + "\n",
        encoding="utf-8",
    )


def get_installed_servers(config_path: Path) -> dict[str, Any]:
    """Get all installed MCP servers from a config file."""
    config = read_config(config_path)
    return config.get("mcpServers", {})


def add_server_to_config(
    config_path: Path,
    server_name: str,
    server_config: dict[str, Any],
) -> None:
    """Add an MCP server to the config file."""
    config = read_config(config_path)
    config["mcpServers"][server_name] = server_config
    write_config(config_path, config)


def remove_server_from_config(config_path: Path, server_name: str) -> bool:
    """Remove an MCP server from the config file. Returns True if removed."""
    config = read_config(config_path)
    if server_name in config.get("mcpServers", {}):
        del config["mcpServers"][server_name]
        write_config(config_path, config)
        return True
    return False


def get_default_config_path() -> Path:
    """Get the best default config path (prefer Claude Code, then project)."""
    claude_path = get_claude_code_config_path()
    if claude_path.exists():
        return claude_path

    project_path = get_project_config_path()
    if project_path.exists():
        return project_path

    # Default to Claude Code
    return claude_path
