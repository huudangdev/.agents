#!/usr/bin/env python3
"""Validate that `.agents/index/` exists and is fresh enough for routing.

This is a lightweight guardrail to prevent models from skipping the index and
falling back to reading huge doc/code trees.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from path_utils import resolve_agents_root


REQUIRED_OUTPUTS = (
    "index/docs_index.md",
    "index/skills_index.md",
    "index/code_index.md",
    "index/architecture_graph.mmd",
    "index/index_manifest.json",
)


def parse_time(value: str) -> datetime | None:
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate `.agents/index/` context index artifacts.")
    parser.add_argument("--root", default=".", help="Project root containing `.agents/`.")
    parser.add_argument("--max-age-hours", type=int, default=24, help="Max allowed age for the index manifest.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    agents_root = resolve_agents_root(root)
    errors: list[str] = []

    for rel in REQUIRED_OUTPUTS:
        path = agents_root / rel.replace("index/", "index/")
        if not path.exists():
            errors.append(f"Missing required context-index artifact: {path}")
        elif path.is_file() and not path.read_text(encoding="utf-8", errors="ignore").strip():
            errors.append(f"Empty context-index artifact: {path}")

    manifest_path = agents_root / "index" / "index_manifest.json"
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"Invalid JSON in index manifest: {exc}")
            manifest = {}
        generated_at = str(manifest.get("generated_at", "")).strip()
        stamp = parse_time(generated_at) if generated_at else None
        if not stamp:
            errors.append("Index manifest missing a valid `generated_at` ISO timestamp")
        else:
            age = datetime.now(timezone.utc) - stamp.astimezone(timezone.utc)
            if age.total_seconds() > args.max_age_hours * 3600:
                errors.append(
                    f"Context index is stale ({age.total_seconds() / 3600:.1f}h old, max {args.max_age_hours}h). "
                    "Rebuild with `python3 .agents/scripts/build_context_index.py --root .`."
                )

    if errors:
        print("CONTEXT INDEX VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("CONTEXT INDEX VALIDATION PASSED")
    print(f"- Root: {root}")
    print(f"- Agents root: {agents_root}")


if __name__ == "__main__":
    main()

