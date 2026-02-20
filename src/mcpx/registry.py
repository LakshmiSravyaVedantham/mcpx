"""MCP server registry: search, browse, and get server info."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional


@dataclass
class ServerInfo:
    name: str
    description: str
    package: str
    install_type: str
    command: str
    args: list[str]
    env: dict[str, str]
    config_params: dict[str, Any]
    category: str
    tags: list[str]
    official: bool
    stars: int

    def build_config(self, params: Optional[dict[str, str]] = None) -> dict[str, Any]:
        """Build the MCP config entry for this server."""
        params = params or {}

        # Resolve args with params
        resolved_args = []
        for arg in self.args:
            resolved = arg
            for key, value in params.items():
                resolved = resolved.replace(f"{{{key}}}", value)
            # Remove unresolved placeholders with defaults from config_params
            for key, param_info in self.config_params.items():
                placeholder = f"{{{key}}}"
                if placeholder in resolved:
                    default = param_info.get("default", "")
                    resolved = resolved.replace(placeholder, default)
            resolved_args.append(resolved)

        # Resolve env vars with params
        resolved_env = {}
        for env_key, env_val in self.env.items():
            resolved = env_val
            for key, value in params.items():
                resolved = resolved.replace(f"{{{key}}}", value)
            for key, param_info in self.config_params.items():
                placeholder = f"{{{key}}}"
                if placeholder in resolved:
                    default = param_info.get("default", "")
                    resolved = resolved.replace(placeholder, default)
            resolved_env[env_key] = resolved

        config: dict[str, Any] = {
            "command": self.command,
            "args": resolved_args,
        }
        if resolved_env:
            config["env"] = resolved_env

        return config


class Registry:
    """MCP server registry backed by a JSON data file."""

    def __init__(self) -> None:
        self._servers: list[ServerInfo] = []
        self._categories: dict[str, Any] = {}
        self._load()

    def _load(self) -> None:
        data_path = Path(__file__).parent / "registry_data.json"
        with open(data_path, encoding="utf-8") as f:
            data = json.load(f)

        self._categories = data.get("categories", {})

        for entry in data.get("servers", []):
            self._servers.append(ServerInfo(
                name=entry["name"],
                description=entry["description"],
                package=entry["package"],
                install_type=entry["install_type"],
                command=entry["command"],
                args=entry["args"],
                env=entry.get("env", {}),
                config_params=entry.get("config_params", {}),
                category=entry["category"],
                tags=entry.get("tags", []),
                official=entry.get("official", False),
                stars=entry.get("stars", 0),
            ))

    @property
    def servers(self) -> list[ServerInfo]:
        return self._servers

    @property
    def categories(self) -> dict[str, Any]:
        return self._categories

    def get(self, name: str) -> Optional[ServerInfo]:
        """Get a server by exact name."""
        for server in self._servers:
            if server.name == name:
                return server
        return None

    def search(self, query: str) -> list[ServerInfo]:
        """Search servers by name, description, or tags."""
        query_lower = query.lower()
        results: list[ServerInfo] = []
        scored: list[tuple[int, ServerInfo]] = []

        for server in self._servers:
            score = 0
            if query_lower == server.name.lower():
                score = 100
            elif query_lower in server.name.lower():
                score = 80
            elif query_lower in server.description.lower():
                score = 50
            elif any(query_lower in tag for tag in server.tags):
                score = 40
            elif query_lower in server.category:
                score = 30

            if score > 0:
                scored.append((score, server))

        scored.sort(key=lambda x: (-x[0], -x[1].stars))
        return [s for _, s in scored]

    def by_category(self, category: str) -> list[ServerInfo]:
        """Get all servers in a category."""
        return [s for s in self._servers if s.category == category]

    def list_categories(self) -> list[str]:
        """Get all unique categories."""
        return sorted(set(s.category for s in self._servers))

    def top(self, n: int = 10) -> list[ServerInfo]:
        """Get the top N servers by popularity."""
        return sorted(self._servers, key=lambda s: -s.stars)[:n]
