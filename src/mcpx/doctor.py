"""Doctor: diagnose MCP configuration issues."""

from __future__ import annotations

import json
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from mcpx.config import (
    detect_platforms,
    get_installed_servers,
    read_config,
)


@dataclass
class DiagnosticResult:
    check: str
    status: str  # "ok", "warning", "error"
    message: str
    fix: str = ""


def run_diagnostics(config_path: Path) -> list[DiagnosticResult]:
    """Run all diagnostic checks."""
    results: list[DiagnosticResult] = []

    # Check 1: Config file exists
    if config_path.exists():
        results.append(DiagnosticResult(
            check="Config file",
            status="ok",
            message=f"Found at {config_path}",
        ))
    else:
        results.append(DiagnosticResult(
            check="Config file",
            status="warning",
            message=f"No config at {config_path}",
            fix="Run 'mcpx init' to create a config file",
        ))
        return results  # Can't check further without config

    # Check 2: Config is valid JSON
    try:
        config = read_config(config_path)
        results.append(DiagnosticResult(
            check="Valid JSON",
            status="ok",
            message="Config file is valid JSON",
        ))
    except Exception as e:
        results.append(DiagnosticResult(
            check="Valid JSON",
            status="error",
            message=f"Invalid JSON: {e}",
            fix="Fix the JSON syntax in your config file",
        ))
        return results

    # Check 3: mcpServers key exists
    if "mcpServers" in config:
        server_count = len(config["mcpServers"])
        results.append(DiagnosticResult(
            check="MCP servers section",
            status="ok",
            message=f"Found {server_count} server(s) configured",
        ))
    else:
        results.append(DiagnosticResult(
            check="MCP servers section",
            status="error",
            message="Missing 'mcpServers' key in config",
            fix="Add '\"mcpServers\": {}' to your config file",
        ))

    # Check 4: npx available
    if shutil.which("npx"):
        results.append(DiagnosticResult(
            check="npx available",
            status="ok",
            message="npx found in PATH",
        ))
    else:
        results.append(DiagnosticResult(
            check="npx available",
            status="error",
            message="npx not found — most MCP servers need it",
            fix="Install Node.js from https://nodejs.org",
        ))

    # Check 5: Node.js version
    if shutil.which("node"):
        import subprocess
        try:
            result = subprocess.run(
                ["node", "--version"],
                capture_output=True, text=True, timeout=5,
            )
            version = result.stdout.strip()
            results.append(DiagnosticResult(
                check="Node.js version",
                status="ok",
                message=f"Node.js {version}",
            ))
        except Exception:
            results.append(DiagnosticResult(
                check="Node.js version",
                status="warning",
                message="Could not determine Node.js version",
            ))
    else:
        results.append(DiagnosticResult(
            check="Node.js version",
            status="error",
            message="Node.js not installed",
            fix="Install Node.js from https://nodejs.org",
        ))

    # Check 6: Each configured server has valid structure
    servers = config.get("mcpServers", {})
    for name, server_config in servers.items():
        if "command" not in server_config:
            results.append(DiagnosticResult(
                check=f"Server '{name}'",
                status="error",
                message="Missing 'command' field",
                fix=f"Add a 'command' field to the '{name}' server config",
            ))
        elif not shutil.which(server_config["command"]):
            results.append(DiagnosticResult(
                check=f"Server '{name}'",
                status="warning",
                message=f"Command '{server_config['command']}' not found in PATH",
                fix=f"Install {server_config['command']} or check your PATH",
            ))
        else:
            # Check for empty env vars that look like placeholders
            env = server_config.get("env", {})
            empty_vars = [k for k, v in env.items() if not v or v.startswith("{")]
            if empty_vars:
                results.append(DiagnosticResult(
                    check=f"Server '{name}'",
                    status="warning",
                    message=f"Unconfigured env vars: {', '.join(empty_vars)}",
                    fix=f"Set values for: {', '.join(empty_vars)}",
                ))
            else:
                results.append(DiagnosticResult(
                    check=f"Server '{name}'",
                    status="ok",
                    message="Configuration looks valid",
                ))

    # Check 7: Platforms detected
    platforms = detect_platforms()
    active = [p for p in platforms if p.exists]
    if active:
        names = ", ".join(p.name for p in active)
        results.append(DiagnosticResult(
            check="AI platforms",
            status="ok",
            message=f"Detected: {names}",
        ))
    else:
        results.append(DiagnosticResult(
            check="AI platforms",
            status="warning",
            message="No AI platforms detected",
            fix="Install Claude Code, Cursor, or create a .mcp.json",
        ))

    return results
