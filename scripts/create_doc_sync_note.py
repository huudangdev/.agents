#!/usr/bin/env python3
"""Create an append-only documentation sync note for a code slice."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
from pathlib import Path


AGENTS_DIR = Path(__file__).resolve().parents[1]
TEMPLATE = AGENTS_DIR / "templates" / "development-sync-note-template.md"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "code-slice"


def git_changed_files(root: Path) -> list[str]:
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only"],
            cwd=root,
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return []
    if result.returncode != 0:
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def parse_changed_files(value: str, root: Path) -> list[str]:
    if value:
        return [item.strip() for item in value.split(",") if item.strip()]
    return git_changed_files(root)


def source_change_lines(changed_files: list[str]) -> str:
    if not changed_files:
        return "- Changed file:\n  - Reason:\n  - Impacted behavior:\n"

    lines: list[str] = []
    for path in changed_files:
        lines.extend(
            [
                f"- `{path}`",
                "  - Reason:",
                "  - Impacted behavior:",
            ]
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a development doc sync note.")
    parser.add_argument("--root", default=".", help="Workspace root.")
    parser.add_argument("--name", required=True, help="Code slice or feature name.")
    parser.add_argument(
        "--changed-files",
        default="",
        help="Comma-separated changed files. Defaults to git diff --name-only.",
    )
    parser.add_argument("--owner-skill", default="marcus-ai-orchestrator")
    parser.add_argument(
        "--mark-reviewed",
        action="store_true",
        help="Mark targeted patch policy checklist complete. Use only after docs were actually reviewed.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite the generated note if it exists.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    base = root / "docs" / "development" / "sync"
    base.mkdir(parents=True, exist_ok=True)

    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    slug = slugify(args.name)
    target = base / f"{timestamp}-{slug}.md"
    if target.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing sync note: {target}")

    changed_files = parse_changed_files(args.changed_files, root)
    text = TEMPLATE.read_text(encoding="utf-8")
    text = text.replace("id: sync-000", f"id: sync-{timestamp}-{slug}")
    text = text.replace("owner_skill: marcus-ai-orchestrator", f"owner_skill: {args.owner_skill}")
    text = text.replace("# Development Doc Sync: <Name>", f"# Development Doc Sync: {args.name}")
    text = text.replace(
        "- Changed file:\n  - Reason:\n  - Impacted behavior:\n",
        source_change_lines(changed_files),
    )
    if args.mark_reviewed:
        text = text.replace("- [ ]", "- [x]")

    target.write_text(text, encoding="utf-8")
    print(target.relative_to(root))


if __name__ == "__main__":
    main()
