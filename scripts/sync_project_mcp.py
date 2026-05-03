#!/usr/bin/env python3
"""Sync .agents/mcp/mcp.json into project-root .mcp.json safely.

Bundled MCP servers should stay aligned with the source-controlled config in
.agents/mcp/mcp.json, but project-local secrets and env overrides should not be
destroyed during sync. This script refreshes managed server definitions from the
source while preserving destination env values when possible.
"""

from __future__ import annotations

import argparse
import json
import sys
from copy import deepcopy
from pathlib import Path

from path_utils import resolve_from_root


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON at {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise SystemExit(f"Expected JSON object at {path}")
    return value


def merge_server_config(source_config: object, existing_config: object) -> object:
    if not isinstance(source_config, dict):
        return deepcopy(source_config)

    merged = deepcopy(source_config)
    if not isinstance(existing_config, dict):
        return merged

    source_env = source_config.get("env", {})
    existing_env = existing_config.get("env", {})
    if isinstance(source_env, dict) and isinstance(existing_env, dict):
        preserved_env = dict(source_env)
        preserved_env.update(existing_env)
        merged["env"] = preserved_env

    return merged


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Merge .agents MCP servers into a project-root .mcp.json file."
    )
    parser.add_argument("--root", default=".", help="Project root containing .agents/")
    parser.add_argument(
        "--source",
        default=".agents/mcp/mcp.json",
        help="Source MCP JSON relative to --root.",
    )
    parser.add_argument(
        "--dest",
        default=".mcp.json",
        help="Destination MCP JSON relative to --root.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    source_path = resolve_from_root(root, args.source).resolve()
    dest_path = resolve_from_root(root, args.dest).resolve()

    if not source_path.exists():
        raise SystemExit(f"Source MCP config not found: {source_path}")

    source = load_json(source_path)
    source_servers = source.get("mcpServers", {})
    if not isinstance(source_servers, dict):
        raise SystemExit(f"Invalid mcpServers object in {source_path}")

    existing = load_json(dest_path) if dest_path.exists() else {}
    existing_servers = existing.get("mcpServers", {})
    if existing_servers is None:
        existing_servers = {}
    if not isinstance(existing_servers, dict):
        raise SystemExit(f"Invalid mcpServers object in {dest_path}")

    merged_servers = dict(existing_servers)
    added: list[str] = []
    refreshed: list[str] = []
    kept: list[str] = []
    for name, config in source_servers.items():
        if name not in merged_servers:
            merged_servers[name] = deepcopy(config)
            added.append(name)
            continue

        merged_config = merge_server_config(config, merged_servers[name])
        if merged_servers[name] != merged_config:
            merged_servers[name] = merged_config
            refreshed.append(name)
        else:
            kept.append(name)

    payload = dict(existing)
    payload["mcpServers"] = merged_servers
    dest_path.write_text(f"{json.dumps(payload, indent=2)}\n", encoding="utf-8")

    print(f"Synced project MCP config: {dest_path.relative_to(root)}")
    if added:
        print(f"Added MCP servers: {', '.join(sorted(added))}")
    if refreshed:
        print(f"Refreshed MCP servers: {', '.join(sorted(refreshed))}")
    if kept:
        print(f"Kept existing MCP servers: {', '.join(sorted(kept))}")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:  # pragma: no cover - defensive CLI guard
        print(f"Failed to sync project MCP config: {exc}", file=sys.stderr)
        sys.exit(1)
