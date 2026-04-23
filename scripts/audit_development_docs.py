#!/usr/bin/env python3
"""Create a brownfield code/docs reconciliation audit for /doc_reconcile."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path


SOURCE_SUFFIXES = {
    ".ts",
    ".tsx",
    ".js",
    ".jsx",
    ".py",
    ".go",
    ".rs",
    ".java",
    ".kt",
    ".swift",
    ".dart",
    ".cs",
    ".php",
    ".rb",
    ".vue",
    ".svelte",
    ".css",
    ".scss",
    ".sql",
}

SKIP_PARTS = {
    ".git",
    ".agents",
    "node_modules",
    ".next",
    "dist",
    "build",
    "coverage",
    ".venv",
    "venv",
    "__pycache__",
}


def should_skip(path: Path, root: Path) -> bool:
    try:
        rel = path.relative_to(root)
    except ValueError:
        return True
    return any(part in SKIP_PARTS for part in rel.parts)


def source_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if should_skip(path, root) or not path.is_file():
            continue
        if path.suffix in SOURCE_SUFFIXES:
            files.append(path)
    return sorted(files)


def docs_files(root: Path) -> list[Path]:
    docs = root / "docs"
    if not docs.exists():
        return []
    return sorted(path for path in docs.rglob("*") if path.is_file() and path.suffix in {".md", ".json", ".jsonl"})


def classify(path: Path, root: Path) -> str:
    rel = path.relative_to(root).as_posix()
    if "/app/" in f"/{rel}" or rel.startswith("app/") or "/pages/" in f"/{rel}" or rel.startswith("pages/"):
        return "page-or-route"
    if "/components/" in f"/{rel}" or rel.startswith("components/"):
        return "component"
    if "/api/" in f"/{rel}" or "route.ts" in rel or "route.js" in rel:
        return "api"
    if "/lib/" in f"/{rel}" or rel.startswith("lib/"):
        return "module-or-service"
    if "/test" in f"/{rel}" or ".test." in rel or ".spec." in rel:
        return "test"
    if path.suffix == ".sql":
        return "data-migration"
    return "source"


def lines_for_inventory(paths: list[Path], root: Path, limit: int) -> list[str]:
    lines: list[str] = []
    for path in paths[:limit]:
        rel = path.relative_to(root).as_posix()
        lines.append(f"- `{rel}` - {classify(path, root)}")
    if len(paths) > limit:
        lines.append(f"- ... {len(paths) - limit} more files omitted from display; full count recorded above.")
    return lines


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit code/docs before V31 development docs reconciliation.")
    parser.add_argument("--root", default=".", help="Project root.")
    parser.add_argument("--output", default="", help="Output markdown path. Defaults to docs/development/audits/<timestamp>-code-docs-audit.md")
    parser.add_argument("--limit", type=int, default=250, help="Displayed file limit per inventory section.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    output = Path(args.output).resolve() if args.output else root / "docs/development/audits" / f"{timestamp}-code-docs-audit.md"
    output.parent.mkdir(parents=True, exist_ok=True)

    sources = source_files(root)
    docs = docs_files(root)
    by_kind: dict[str, int] = {}
    for path in sources:
        kind = classify(path, root)
        by_kind[kind] = by_kind.get(kind, 0) + 1

    manifest = root / "docs/development/development_manifest.json"
    topology = "missing"
    if manifest.exists():
        try:
            value = json.loads(manifest.read_text(encoding="utf-8"))
            topology = str(value.get("topology", value.get("ledger_topology", "legacy_flat")))
        except json.JSONDecodeError:
            topology = "invalid-json"

    lines = [
        "---",
        f"id: audit-{timestamp}-code-docs-reconcile",
        "type: development-docs-audit",
        "status: draft",
        "owner_skill: development-ledger-architect",
        "source_trace:",
        "  - docs/development/development_manifest.json",
        "verification:",
        "  - pending",
        "---",
        "",
        f"# Code and Docs Reconciliation Audit - {timestamp}",
        "",
        "## Purpose",
        "",
        "This audit is mandatory evidence for `/doc_reconcile`. It proves the agent",
        "created a whole-codebase inventory before restructuring or enriching",
        "development docs.",
        "",
        "## Summary",
        "",
        f"- Project root: `{root}`",
        f"- Development docs topology: `{topology}`",
        f"- Source files inventoried: {len(sources)}",
        f"- Docs files inventoried: {len(docs)}",
        "",
        "## Source Classification",
        "",
    ]

    for kind, count in sorted(by_kind.items()):
        lines.append(f"- {kind}: {count}")

    lines.extend(
        [
            "",
            "## Source Inventory",
            "",
            *lines_for_inventory(sources, root, args.limit),
            "",
            "## Documentation Inventory",
            "",
            *lines_for_inventory(docs, root, args.limit),
            "",
            "## Reconciliation Checklist",
            "",
            "- [ ] Map every source cluster to an epic, feature, module, page, or task.",
            "- [ ] Create or migrate V31 epic-first docs with canonical IDs.",
            "- [ ] Create `issues.md` for every epic using QA skill reasoning.",
            "- [ ] Fill Story, Priority, Relationship Map, Work Log, Mermaid, verification, and Change Log.",
            "- [ ] Update global docs when source behavior differs from existing planning docs.",
            "- [ ] Run `validate_development_docs.py --strict-counts` and `validate_doc_sync.py --strict`.",
            "",
            "## Relationship Labels To Use",
            "",
            "- `DEPENDS_ON`",
            "- `BLOCKS`",
            "- `ENABLES`",
            "- `IMPLEMENTS`",
            "- `USES`",
            "- `EXTENDS`",
            "- `CONFLICTS_WITH`",
            "- `SUPERSEDES`",
            "- `DUPLICATES`",
            "- `RELATES_TO`",
            "",
        ]
    )

    output.write_text("\n".join(lines), encoding="utf-8")
    print(output.relative_to(root))


if __name__ == "__main__":
    main()
