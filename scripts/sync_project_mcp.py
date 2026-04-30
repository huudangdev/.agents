#!/usr/bin/env python3
"""Sync .agents/mcp/mcp.json into project-root .mcp.json non-destructively."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


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
    source_path = (root / args.source).resolve()
    dest_path = (root / args.dest).resolve()

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
    kept: list[str] = []
    for name, config in source_servers.items():
        if name in merged_servers:
            kept.append(name)
            continue
        merged_servers[name] = config
        added.append(name)

    payload = dict(existing)
    payload["mcpServers"] = merged_servers
    dest_path.write_text(f"{json.dumps(payload, indent=2)}\n", encoding="utf-8")

    print(f"Synced project MCP config: {dest_path.relative_to(root)}")
    if added:
        print(f"Added MCP servers: {', '.join(sorted(added))}")
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
