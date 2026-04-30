#!/usr/bin/env python3
"""Validate project MCP readiness without blocking on optional servers."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_json(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"Missing JSON file: {path}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON at {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise SystemExit(f"Expected JSON object at {path}")
    return value


def is_placeholder(value: str) -> bool:
    stripped = value.strip()
    return not stripped or (stripped.startswith("<") and stripped.endswith(">"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Check project MCP readiness.")
    parser.add_argument("--root", default=".", help="Project root containing .mcp.json")
    parser.add_argument("--catalog", default=".agents/mcp/mcp_catalog.json", help="Catalog path relative to root")
    parser.add_argument("--config", default=".mcp.json", help="Project MCP config path relative to root")
    parser.add_argument("--strict-core", action="store_true", help="Exit non-zero if a core MCP server is missing.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    catalog = load_json((root / args.catalog).resolve())
    config = load_json((root / args.config).resolve())

    catalog_servers = catalog.get("servers", {})
    config_servers = config.get("mcpServers", {})
    if not isinstance(catalog_servers, dict) or not isinstance(config_servers, dict):
        raise SystemExit("Invalid MCP catalog or config structure.")

    warnings: list[str] = []
    errors: list[str] = []

    print("MCP Health Check")
    print(f"- Catalog version: {catalog.get('version', 'unknown')}")
    print(f"- Config file: {(root / args.config).resolve()}")

    for name, meta in sorted(catalog_servers.items()):
        tier = meta.get("tier", "optional")
        required_env = meta.get("required_env", [])
        present = name in config_servers
        if not present:
            message = f"{name}: missing from .mcp.json ({tier})"
            if tier == "core":
                errors.append(message)
            else:
                warnings.append(message)
            continue

        server = config_servers.get(name, {})
        env = server.get("env", {}) if isinstance(server, dict) else {}
        missing_env = []
        for key in required_env:
            value = env.get(key, "") if isinstance(env, dict) else ""
            if not isinstance(value, str) or is_placeholder(value):
                missing_env.append(key)

        if missing_env:
            message = f"{name}: missing env -> {', '.join(missing_env)} ({tier})"
            if tier == "core":
                errors.append(message)
            else:
                warnings.append(message)
        else:
            print(f"- {name}: ready ({tier})")

    if warnings:
        print("\nWarnings:")
        for item in warnings:
            print(f"- {item}")

    if errors:
        print("\nErrors:")
        for item in errors:
            print(f"- {item}")
        if args.strict_core:
            sys.exit(1)


if __name__ == "__main__":
    main()
