"""CLI interface for mcpx — the MCP server package manager."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from mcpx import __version__
from mcpx.config import (
    detect_platforms,
    get_default_config_path,
    get_installed_servers,
    write_config,
)
from mcpx.doctor import run_diagnostics
from mcpx.installer import install_server, uninstall_server, verify_server_deps
from mcpx.registry import Registry

app = typer.Typer(
    name="mcpx",
    help="The package manager for MCP servers.",
    no_args_is_help=True,
    rich_markup_mode="rich",
)
console = Console()

STATUS_ICONS = {
    "ok": "[green]✓[/green]",
    "warning": "[yellow]![/yellow]",
    "error": "[red]✗[/red]",
}


def _get_config_path(config: Optional[str]) -> Path:
    if config:
        return Path(config)
    return get_default_config_path()


def _get_registry() -> Registry:
    return Registry()


def version_callback(value: bool) -> None:
    if value:
        console.print(f"mcpx [bold cyan]{__version__}[/bold cyan]")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        False,
        "--version",
        "-v",
        help="Show version and exit.",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    """mcpx — The package manager for MCP servers."""


@app.command()
def search(
    query: str = typer.Argument(..., help="Search query (name, description, or tag)"),
    config: Optional[str] = typer.Option(
        None, "--config", "-c", help="Config file path"
    ),
) -> None:
    """Search the MCP server registry."""
    registry = _get_registry()
    results = registry.search(query)

    if not results:
        console.print(f"[yellow]No servers found for '{query}'[/yellow]")
        console.print(
            "Try a broader search or run [bold]mcpx top[/bold] to see popular servers."
        )
        raise typer.Exit(1)

    table = Table(title=f"Search results for '{query}'", show_lines=False)
    table.add_column("Name", style="cyan bold", min_width=15)
    table.add_column("Description", min_width=30)
    table.add_column("Category", style="magenta")
    table.add_column("Stars", style="yellow", justify="right")

    # Check installed
    config_path = _get_config_path(config)
    installed = get_installed_servers(config_path)

    for server in results[:20]:
        name = server.name
        if name in installed:
            name = f"{name} [green](installed)[/green]"
        stars = f"★ {server.stars}" if server.stars else ""
        table.add_row(name, server.description, server.category, stars)

    console.print(table)
    console.print(
        f"\n[dim]Found {len(results)} server(s). Install with:[/dim] [bold]mcpx install <name>[/bold]"
    )


@app.command()
def install(
    name: str = typer.Argument(..., help="Server name to install"),
    config: Optional[str] = typer.Option(
        None, "--config", "-c", help="Config file path"
    ),
    param: Optional[list[str]] = typer.Option(
        None, "--param", "-p", help="Parameters as key=value"
    ),
) -> None:
    """Install an MCP server."""
    registry = _get_registry()
    server = registry.get(name)

    if not server:
        console.print(f"[red]Server '{name}' not found.[/red]")
        # Suggest similar
        suggestions = registry.search(name)[:3]
        if suggestions:
            console.print("\n[yellow]Did you mean:[/yellow]")
            for s in suggestions:
                console.print(f"  [cyan]{s.name}[/cyan] — {s.description}")
        raise typer.Exit(1)

    # Check deps
    issues = verify_server_deps(server)
    if issues:
        console.print("[yellow]Dependency warnings:[/yellow]")
        for issue in issues:
            console.print(f"  [yellow]![/yellow] {issue}")

    # Parse params
    params: dict[str, str] = {}
    if param:
        for p in param:
            if "=" not in p:
                console.print(f"[red]Invalid param format: '{p}'. Use key=value[/red]")
                raise typer.Exit(1)
            key, value = p.split("=", 1)
            params[key] = value

    # Check for required params
    required_params = {
        k: v
        for k, v in server.config_params.items()
        if v.get("required", False) and k not in params
    }
    if required_params:
        console.print(f"\n[bold]Server '{name}' requires configuration:[/bold]")
        for key, info in required_params.items():
            desc = info.get("description", key)
            value = typer.prompt(f"  {desc}")
            params[key] = value

    config_path = _get_config_path(config)
    success, message = install_server(server, config_path, params)

    if success:
        console.print(
            Panel(
                f"[green]✓[/green] {message}\n\n"
                f"[dim]Config:[/dim] {config_path}\n"
                f"[dim]Restart your AI tool to activate.[/dim]",
                title="[bold green]Installed[/bold green]",
                border_style="green",
            )
        )
    else:
        console.print(f"[red]✗ {message}[/red]")
        raise typer.Exit(1)


@app.command()
def uninstall(
    name: str = typer.Argument(..., help="Server name to uninstall"),
    config: Optional[str] = typer.Option(
        None, "--config", "-c", help="Config file path"
    ),
) -> None:
    """Uninstall an MCP server."""
    config_path = _get_config_path(config)
    success, message = uninstall_server(name, config_path)

    if success:
        console.print(f"[green]✓[/green] {message}")
    else:
        console.print(f"[red]✗ {message}[/red]")
        raise typer.Exit(1)


@app.command(name="list")
def list_servers(
    config: Optional[str] = typer.Option(
        None, "--config", "-c", help="Config file path"
    ),
) -> None:
    """List installed MCP servers."""
    config_path = _get_config_path(config)
    servers = get_installed_servers(config_path)

    if not servers:
        console.print("[yellow]No MCP servers installed.[/yellow]")
        console.print(
            "Run [bold]mcpx search <query>[/bold] or [bold]mcpx top[/bold] to find servers."
        )
        return

    table = Table(title=f"Installed MCP Servers ({config_path})", show_lines=False)
    table.add_column("Name", style="cyan bold")
    table.add_column("Command", style="green")
    table.add_column("Args", style="dim")

    for name, cfg in servers.items():
        cmd = cfg.get("command", "?")
        args = " ".join(cfg.get("args", []))
        # Truncate long args
        if len(args) > 60:
            args = args[:57] + "..."
        table.add_row(name, cmd, args)

    console.print(table)
    console.print(f"\n[dim]{len(servers)} server(s) installed[/dim]")


@app.command()
def info(
    name: str = typer.Argument(..., help="Server name"),
) -> None:
    """Show detailed info about an MCP server."""
    registry = _get_registry()
    server = registry.get(name)

    if not server:
        console.print(f"[red]Server '{name}' not found.[/red]")
        raise typer.Exit(1)

    official = " [green](Official)[/green]" if server.official else ""
    stars = f" ★ {server.stars}" if server.stars else ""

    content = (
        f"[bold]{server.description}[/bold]\n\n"
        f"[dim]Package:[/dim]      {server.package}\n"
        f"[dim]Type:[/dim]         {server.install_type}\n"
        f"[dim]Command:[/dim]      {server.command}\n"
        f"[dim]Category:[/dim]     {server.category}\n"
        f"[dim]Tags:[/dim]         {', '.join(server.tags)}\n"
    )

    if server.config_params:
        content += "\n[bold]Configuration Parameters:[/bold]\n"
        for key, param_info in server.config_params.items():
            required = " [red](required)[/red]" if param_info.get("required") else ""
            desc = param_info.get("description", key)
            content += f"  [cyan]{key}[/cyan]: {desc}{required}\n"

    if server.env:
        content += "\n[bold]Environment Variables:[/bold]\n"
        for env_key, env_val in server.env.items():
            content += f"  [cyan]{env_key}[/cyan] = {env_val}\n"

    console.print(
        Panel(
            content,
            title=f"[bold cyan]{server.name}[/bold cyan]{official}{stars}",
            border_style="cyan",
        )
    )

    console.print(f"\nInstall: [bold]mcpx install {server.name}[/bold]")


@app.command()
def doctor(
    config: Optional[str] = typer.Option(
        None, "--config", "-c", help="Config file path"
    ),
) -> None:
    """Diagnose MCP configuration issues."""
    config_path = _get_config_path(config)

    console.print(Panel("[bold]MCP Configuration Doctor[/bold]", border_style="blue"))
    console.print(f"[dim]Checking config: {config_path}[/dim]\n")

    results = run_diagnostics(config_path)

    for result in results:
        icon = STATUS_ICONS.get(result.status, "?")
        console.print(f"  {icon} [bold]{result.check}[/bold]: {result.message}")
        if result.fix:
            console.print(f"      [dim]Fix: {result.fix}[/dim]")

    # Summary
    errors = sum(1 for r in results if r.status == "error")
    warnings = sum(1 for r in results if r.status == "warning")
    ok = sum(1 for r in results if r.status == "ok")

    console.print()
    if errors:
        console.print(
            f"[red bold]{errors} error(s)[/red bold], {warnings} warning(s), {ok} ok"
        )
    elif warnings:
        console.print(f"[yellow]{warnings} warning(s)[/yellow], {ok} ok")
    else:
        console.print(f"[green bold]All {ok} checks passed![/green bold]")


@app.command()
def top(
    count: int = typer.Option(10, "--count", "-n", help="Number of servers to show"),
) -> None:
    """Show the most popular MCP servers."""
    registry = _get_registry()
    servers = registry.top(count)

    table = Table(title=f"Top {count} MCP Servers", show_lines=False)
    table.add_column("#", style="dim", width=3)
    table.add_column("Name", style="cyan bold", min_width=15)
    table.add_column("Description", min_width=30)
    table.add_column("Category", style="magenta")
    table.add_column("Stars", style="yellow", justify="right")

    for i, server in enumerate(servers, 1):
        official = " ✓" if server.official else ""
        stars = f"★ {server.stars}" if server.stars else ""
        table.add_row(
            str(i),
            f"{server.name}{official}",
            server.description,
            server.category,
            stars,
        )

    console.print(table)
    console.print("\nInstall: [bold]mcpx install <name>[/bold]")


@app.command()
def categories() -> None:
    """List all server categories."""
    registry = _get_registry()
    cats = registry.list_categories()

    table = Table(title="MCP Server Categories", show_lines=False)
    table.add_column("Category", style="magenta bold")
    table.add_column("Servers", style="cyan", justify="right")

    for cat in cats:
        count = len(registry.by_category(cat))
        table.add_row(cat, str(count))

    console.print(table)
    console.print("\nBrowse: [bold]mcpx browse <category>[/bold]")


@app.command()
def browse(
    category: str = typer.Argument(..., help="Category to browse"),
) -> None:
    """Browse servers by category."""
    registry = _get_registry()
    servers = registry.by_category(category)

    if not servers:
        console.print(f"[yellow]No servers in category '{category}'[/yellow]")
        console.print("Run [bold]mcpx categories[/bold] to see available categories.")
        raise typer.Exit(1)

    table = Table(title=f"Category: {category}", show_lines=False)
    table.add_column("Name", style="cyan bold", min_width=15)
    table.add_column("Description", min_width=30)
    table.add_column("Stars", style="yellow", justify="right")

    for server in sorted(servers, key=lambda s: -s.stars):
        official = " [green]✓[/green]" if server.official else ""
        stars = f"★ {server.stars}" if server.stars else ""
        table.add_row(f"{server.name}{official}", server.description, stars)

    console.print(table)


@app.command()
def init(
    config: Optional[str] = typer.Option(
        None, "--config", "-c", help="Config file path"
    ),
) -> None:
    """Initialize a new MCP config file."""
    config_path = _get_config_path(config)

    if config_path.exists():
        console.print(f"[yellow]Config already exists at {config_path}[/yellow]")
        overwrite = typer.confirm("Overwrite?", default=False)
        if not overwrite:
            raise typer.Exit()

    write_config(config_path, {"mcpServers": {}})
    console.print(f"[green]✓[/green] Created MCP config at [bold]{config_path}[/bold]")
    console.print("\nNext steps:")
    console.print("  [bold]mcpx search filesystem[/bold]  — Find servers")
    console.print("  [bold]mcpx install github[/bold]     — Install a server")
    console.print("  [bold]mcpx doctor[/bold]             — Check your setup")


@app.command()
def platforms() -> None:
    """Detect installed AI platforms."""
    detected = detect_platforms()

    table = Table(title="AI Platforms", show_lines=False)
    table.add_column("Platform", style="bold")
    table.add_column("Status")
    table.add_column("Config Path", style="dim")

    for p in detected:
        status = "[green]✓ Detected[/green]" if p.exists else "[dim]Not found[/dim]"
        table.add_row(p.name, status, str(p.config_path))

    console.print(table)


if __name__ == "__main__":
    app()
