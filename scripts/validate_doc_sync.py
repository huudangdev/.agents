#!/usr/bin/env python3
"""Validate documentation synchronization after code changes."""

from __future__ import annotations

import argparse
import json
import re
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

GLOBAL_DOCS = {
    "docs/prd.md",
    "docs/tasks.md",
    "docs/knowledge.md",
    "docs/decisions.md",
    "docs/memory.md",
    "docs/planning/flows.md",
    "docs/planning/screens.md",
    "docs/planning/diagrams.md",
}

PLACEHOLDER_PATTERNS = [
    r"<[^>\n]+>",
    r"\bTBD\b",
    r"\bpending\b",
    r"no change needed / updated because",
    r"Changed file:",
    r"Reason:\s*$",
    r"Impacted behavior:\s*$",
    r"Pre-code docs read:\s*$",
    r"Pre-code docs updated:\s*$",
    r"Relationship map reviewed:\s*$",
    r"Related features checked:\s*$",
    r"Command:\s*$",
    r"Result:\s*$",
]


def run_git_diff(root: Path, args: list[str]) -> list[str]:
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", *args],
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


def git_changed_files(root: Path, base_ref: str) -> list[str]:
    if base_ref:
        return run_git_diff(root, [base_ref, "HEAD"])

    working_tree = run_git_diff(root, ["HEAD"])
    if working_tree:
        return working_tree

    previous_commit = subprocess.run(
        ["git", "rev-parse", "--verify", "HEAD~1"],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if previous_commit.returncode == 0:
        return run_git_diff(root, ["HEAD~1", "HEAD"])

    return []


def parse_changed_files(value: str, root: Path, base_ref: str) -> list[str]:
    if value:
        return [item.strip() for item in value.split(",") if item.strip()]
    return git_changed_files(root, base_ref)


def is_source_file(path: str) -> bool:
    return Path(path).suffix in SOURCE_SUFFIXES and not path.startswith(DOC_PREFIXES)


def is_doc_file(path: str) -> bool:
    return path.startswith(DOC_PREFIXES) and Path(path).suffix in {".md", ".json", ".jsonl"}


def load_manifest(root: Path) -> tuple[dict[str, Any], list[str]]:
    path = root / "docs/development/sync/sync_manifest.json"
    development_manifest = root / "docs/development/development_manifest.json"
    if not path.exists() and development_manifest.exists():
        path = development_manifest
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
    base = root / "docs/development"
    if not base.exists():
        return []
    root_sync = base / "sync"
    notes: list[Path] = []
    if root_sync.exists():
        notes.extend(item for item in root_sync.glob("*.md") if item.is_file())
    notes.extend(item for item in base.glob("E-*/sync/*.md") if item.is_file())
    return sorted(
        notes,
        key=lambda item: (item.stat().st_mtime, item.name),
    )


def validate(root: Path, changed_files: list[str], strict: bool) -> list[str]:
    errors: list[str] = []
    manifest, manifest_errors = load_manifest(root)
    errors.extend(manifest_errors)

    source_files = [path for path in changed_files if is_source_file(path)]
    doc_files = [path for path in changed_files if is_doc_file(path)]
    gates = manifest.get("quality_gates", {}) if manifest else {}

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

    if gates.get("require_global_docs_updated", True) and source_files and strict:
        changed_global_docs = [path for path in changed_files if path in GLOBAL_DOCS]
        if not changed_global_docs:
            errors.append("Source files changed but no required global /docs planning file was updated")

    if gates.get("require_no_unchecked_items", True) and "- [ ]" in latest_note:
        errors.append(f"Latest sync note still has unchecked documentation policy items: {notes[-1]}")

    if strict and source_files:
        for pattern in PLACEHOLDER_PATTERNS:
            if re.search(pattern, latest_note, flags=re.IGNORECASE | re.MULTILINE):
                errors.append(f"Latest sync note contains placeholder or unfinished text matching `{pattern}`")

        if len(re.findall(r"\b[\w/-]+\b", latest_note)) < 180:
            errors.append("Latest sync note is too shallow; expected at least 180 words of real rationale")

        lower_note = latest_note.lower()
        for marker in ["because", "impact", "evidence", "risk", "decision"]:
            if marker not in lower_note:
                errors.append(f"Latest sync note missing `{marker}` commentary")

    if gates.get("require_legacy_docs_decision", True) and source_files:
        for required in [
            *sorted(GLOBAL_DOCS),
        ]:
            if required not in latest_note:
                errors.append(f"Latest sync note missing legacy docs decision for {required}")

        if "updated because" not in latest_note.lower():
            errors.append("Latest sync note must include at least one `updated because` decision for a global doc")

    if gates.get("require_development_docs_decision", True) and source_files:
        for label in ["Epic notes", "Module notes", "Feature notes", "Page notes", "Task notes"]:
            if label not in latest_note:
                errors.append(f"Latest sync note missing development docs decision: {label}")

    if gates.get("require_docs_before_code", True) and source_files:
        for label in [
            "## Docs Before Code",
            "Pre-code docs read",
            "Pre-code docs updated",
            "Relationship map reviewed",
            "Related features checked",
        ]:
            if label not in latest_note:
                errors.append(f"Latest sync note missing docs-before-code evidence: {label}")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate documentation sync for changed code.")
    parser.add_argument("--root", default=".", help="Workspace root.")
    parser.add_argument("--changed-files", default="", help="Comma-separated changed files.")
    parser.add_argument(
        "--base-ref",
        default="",
        help="Optional git base ref for committed diffs, e.g. HEAD~1 or origin/main.",
    )
    parser.add_argument("--strict", action="store_true", help="Require docs changed and checklist completed.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    changed_files = parse_changed_files(args.changed_files, root, args.base_ref)
    errors = validate(root, changed_files, args.strict)
    if errors:
        print("DOC SYNC VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("DOC SYNC VALIDATION PASSED")


if __name__ == "__main__":
    main()
