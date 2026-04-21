#!/usr/bin/env python3
"""Validate /develop execution knowledge artifacts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_BUCKETS = {
    "epics": {"path": "docs/development/epics", "minimum_count": 1},
    "modules": {"path": "docs/development/modules", "minimum_count": 1},
    "features": {"path": "docs/development/features", "minimum_count": 1},
    "pages": {"path": "docs/development/pages", "minimum_count": 0},
    "tasks": {"path": "docs/development/tasks", "minimum_count": 1},
}

REQUIRED_FRONTMATTER_FIELDS = [
    "id:",
    "type:",
    "status:",
    "owner_skill:",
    "source_trace:",
    "verification:",
]

REQUIRED_BODY_SECTIONS = {
    "epics": ["## Outcome", "## Acceptance Criteria", "## Evidence"],
    "modules": ["## Responsibility", "## Code Scope", "## Verification"],
    "features": ["## User Value", "## Requirements Trace", "## Code Scope", "## Verification"],
    "pages": ["## Route / Surface", "## States", "## Verification"],
    "tasks": ["## Objective", "## Write Scope", "## Verification", "## Handoff"],
}


def load_manifest(root: Path) -> tuple[dict[str, Any] | None, list[str]]:
    path = root / "docs/development/development_manifest.json"
    if not path.exists():
        return None, ["Missing development manifest: docs/development/development_manifest.json"]
    if not path.read_text(encoding="utf-8").strip():
        return None, ["Empty development manifest: docs/development/development_manifest.json"]
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return None, [f"Invalid development manifest JSON: {exc}"]
    if not isinstance(value, dict):
        return None, ["Development manifest must be a JSON object"]
    return value, []


def has_frontmatter(text: str) -> bool:
    return text.startswith("---\n") and "\n---\n" in text[4:]


def validate_markdown(path: Path, bucket_name: str, gates: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    rel = path.as_posix()

    if not text.strip():
        return [f"Empty development artifact: {rel}"]

    if gates.get("require_frontmatter", True):
        if not has_frontmatter(text):
            errors.append(f"{rel}: missing YAML frontmatter")
        else:
            frontmatter = text.split("---", 2)[1]
            for field in REQUIRED_FRONTMATTER_FIELDS:
                if field not in frontmatter:
                    errors.append(f"{rel}: frontmatter missing {field}")

    if gates.get("require_owner_skill", True) and "owner_skill:" not in text:
        errors.append(f"{rel}: missing owner_skill")

    if gates.get("require_source_trace", True) and "source_trace:" not in text:
        errors.append(f"{rel}: missing source_trace")

    if gates.get("require_verification", True) and "verification:" not in text and "## Verification" not in text:
        errors.append(f"{rel}: missing verification")

    if gates.get("require_code_scope", True) and bucket_name in {"modules", "features", "tasks"}:
        if "## Code Scope" not in text and "## Write Scope" not in text:
            errors.append(f"{rel}: missing Code Scope or Write Scope")

    for section in REQUIRED_BODY_SECTIONS.get(bucket_name, []):
        if section not in text:
            errors.append(f"{rel}: missing section {section}")

    return errors


def validate(root: Path, strict_counts: bool) -> list[str]:
    errors: list[str] = []
    manifest, manifest_errors = load_manifest(root)
    errors.extend(manifest_errors)

    index_path = root / "docs/development/index.md"
    if not index_path.exists():
        errors.append("Missing development index: docs/development/index.md")
    elif not index_path.read_text(encoding="utf-8").strip():
        errors.append("Empty development index: docs/development/index.md")

    buckets = DEFAULT_BUCKETS
    gates: dict[str, Any] = {
        "require_frontmatter": True,
        "require_owner_skill": True,
        "require_verification": True,
        "require_source_trace": True,
        "require_code_scope": True,
    }

    if manifest:
        raw_buckets = manifest.get("buckets", DEFAULT_BUCKETS)
        if isinstance(raw_buckets, dict):
            buckets = raw_buckets
        raw_gates = manifest.get("quality_gates", gates)
        if isinstance(raw_gates, dict):
            gates.update(raw_gates)

    for bucket_name, config in buckets.items():
        if not isinstance(config, dict):
            errors.append(f"Bucket {bucket_name} config must be an object")
            continue

        rel_path = str(config.get("path", f"docs/development/{bucket_name}"))
        bucket_path = root / rel_path
        if not bucket_path.exists() or not bucket_path.is_dir():
            errors.append(f"Missing development bucket: {rel_path}")
            continue

        docs = sorted(bucket_path.glob("*.md"))
        minimum_count = int(config.get("minimum_count", 0))
        if strict_counts and len(docs) < minimum_count:
            errors.append(
                f"Bucket {bucket_name} has {len(docs)} markdown file(s), expected at least {minimum_count}"
            )

        for doc_path in docs:
            errors.extend(validate_markdown(doc_path, bucket_name, gates))

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate /develop documentation artifacts.")
    parser.add_argument("--root", default=".", help="Workspace root containing docs/")
    parser.add_argument(
        "--strict-counts",
        action="store_true",
        help="Require bucket minimum_count values from the manifest.",
    )
    args = parser.parse_args()

    errors = validate(Path(args.root).resolve(), args.strict_counts)
    if errors:
        print("DEVELOPMENT DOCS VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("DEVELOPMENT DOCS VALIDATION PASSED")


if __name__ == "__main__":
    main()
