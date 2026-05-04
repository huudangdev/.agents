#!/usr/bin/env python3
"""Validate that `/marcus_init` produced the expected scaffold artifacts."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from validate_docs_substance import validate_docs


REQUIRED_PATHS = (
    "docs",
    ".agents",
    ".clinerules",
    "agents.md",
    ".agents/agents.md",
    "docs/prd_draft.md",
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate `/marcus_init` scaffold outputs.")
    parser.add_argument("--root", required=True, help="Scaffolded project root to validate.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors: list[str] = []

    for relpath in REQUIRED_PATHS:
        path = root / relpath
        if not path.exists():
            errors.append(f"Missing required marcus_init output: {path}")
            continue
        if path.is_file() and not path.read_text(encoding="utf-8").strip():
            errors.append(f"Empty required marcus_init output: {path}")

    for issue in validate_docs(root, targets=("docs/prd_draft.md",)):
        errors.append(f"{issue.relpath}: {issue.message}")

    if errors:
        print("MARCUS INIT OUTPUT VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("MARCUS INIT OUTPUT VALIDATION PASSED")
    print(f"- Root: {root}")
    print("- Required scaffold outputs exist and are non-empty")


if __name__ == "__main__":
    main()
