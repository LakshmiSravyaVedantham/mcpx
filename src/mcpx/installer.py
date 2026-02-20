"""Installer: install and uninstall MCP servers."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import Any, Optional

from mcpx.config import add_server_to_config, remove_server_from_config
from mcpx.registry import ServerInfo


def check_npx_available() -> bool:
    """Check if npx is available on the system."""
    return shutil.which("npx") is not None


def check_npm_available() -> bool:
    """Check if npm is available on the system."""
    return shutil.which("npm") is not None


def check_pip_available() -> bool:
    """Check if pip is available on the system."""
    return shutil.which("pip") is not None or shutil.which("pip3") is not None


def install_server(
    server: ServerInfo,
    config_path: Path,
    params: Optional[dict[str, str]] = None,
) -> tuple[bool, str]:
    """
    Install an MCP server into the config.

    Returns (success, message).
    """
    # Build the config entry
    config_entry = server.build_config(params)

    # Add to config
    try:
        add_server_to_config(config_path, server.name, config_entry)
    except OSError as e:
        return False, f"Failed to write config: {e}"

    return True, f"Server '{server.name}' installed successfully"


def uninstall_server(
    server_name: str,
    config_path: Path,
) -> tuple[bool, str]:
    """
    Uninstall an MCP server from the config.

    Returns (success, message).
    """
    removed = remove_server_from_config(config_path, server_name)
    if removed:
        return True, f"Server '{server_name}' uninstalled successfully"
    return False, f"Server '{server_name}' not found in config"


def verify_server_deps(server: ServerInfo) -> list[str]:
    """Check if dependencies for a server are met. Returns list of issues."""
    issues = []

    if server.install_type == "npm":
        if not check_npx_available():
            issues.append("npx is not installed. Install Node.js: https://nodejs.org")
    elif server.install_type == "pip":
        if not check_pip_available():
            issues.append("pip is not installed")

    return issues
