#!/usr/bin/env python3
"""Validate documentation synchronization after code changes."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


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

DOC_PREFIXES = ("docs/", ".agents/specs/")


def git_changed_files(root: Path) -> list[str]:
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD"],
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


def is_source_file(path: str) -> bool:
    return Path(path).suffix in SOURCE_SUFFIXES and not path.startswith(DOC_PREFIXES)


def is_doc_file(path: str) -> bool:
    return path.startswith(DOC_PREFIXES) and Path(path).suffix in {".md", ".json", ".jsonl"}


def load_manifest(root: Path) -> tuple[dict[str, Any], list[str]]:
    path = root / "docs/development/sync/sync_manifest.json"
    if not path.exists():
        return {}, ["Missing doc sync manifest: docs/development/sync/sync_manifest.json"]
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {}, [f"Invalid doc sync manifest JSON: {exc}"]
    if not isinstance(value, dict):
        return {}, ["Doc sync manifest must be a JSON object"]
    return value, []


def sync_notes(root: Path) -> list[Path]:
    path = root / "docs/development/sync"
    if not path.exists():
        return []
    return sorted(
        (item for item in path.glob("*.md") if item.is_file()),
        key=lambda item: (item.stat().st_mtime, item.name),
    )


def validate(root: Path, changed_files: list[str], strict: bool) -> list[str]:
    errors: list[str] = []
    manifest, manifest_errors = load_manifest(root)
    errors.extend(manifest_errors)

    source_files = [path for path in changed_files if is_source_file(path)]
    doc_files = [path for path in changed_files if is_doc_file(path)]
    gates = manifest.get("quality_gates", {}) if manifest else {}

    if gates.get("require_changed_files", True) and strict and not changed_files:
        errors.append("No changed files supplied or detected")

    notes = sync_notes(root)
    if source_files and not notes:
        errors.append("Source files changed but no docs/development/sync/*.md note exists")
        return errors

    combined_notes = "\n".join(path.read_text(encoding="utf-8") for path in notes)
    latest_note = notes[-1].read_text(encoding="utf-8") if notes else ""

    for source_file in source_files:
        if source_file not in combined_notes:
            errors.append(f"Changed source file not referenced in sync notes: {source_file}")

    if gates.get("require_docs_reviewed", True) and source_files and not doc_files and strict:
        errors.append("Source files changed but no docs or spec files are in the changed set")

    if gates.get("require_no_unchecked_items", True) and "- [ ]" in latest_note:
        errors.append(f"Latest sync note still has unchecked documentation policy items: {notes[-1]}")

    if gates.get("require_legacy_docs_decision", True) and source_files:
        for required in [
            "docs/prd.md",
            "docs/tasks.md",
            "docs/knowledge.md",
            "docs/decisions.md",
            "docs/memory.md",
            "docs/planning/flows.md",
            "docs/planning/screens.md",
            "docs/planning/diagrams.md",
        ]:
            if required not in latest_note:
                errors.append(f"Latest sync note missing legacy docs decision for {required}")

    if gates.get("require_development_docs_decision", True) and source_files:
        for label in ["Epic notes", "Module notes", "Feature notes", "Page notes", "Task notes"]:
            if label not in latest_note:
                errors.append(f"Latest sync note missing development docs decision: {label}")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate documentation sync for changed code.")
    parser.add_argument("--root", default=".", help="Workspace root.")
    parser.add_argument("--changed-files", default="", help="Comma-separated changed files.")
    parser.add_argument("--strict", action="store_true", help="Require docs changed and checklist completed.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    changed_files = parse_changed_files(args.changed_files, root)
    errors = validate(root, changed_files, args.strict)
    if errors:
        print("DOC SYNC VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("DOC SYNC VALIDATION PASSED")


if __name__ == "__main__":
    main()
