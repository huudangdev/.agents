#!/usr/bin/env python3
"""Validate that `/refactor-planning` produced its required closeout artifacts."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from validate_docs_substance import validate_docs


REQUIRED_OUTPUTS = (
    "agents.md",
    "docs/ADR_REFACTOR_LOG.md",
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate `/refactor-planning` closeout artifacts.")
    parser.add_argument("--root", default=".", help="Project root to validate.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors: list[str] = []

    for relpath in REQUIRED_OUTPUTS:
        path = root / relpath
        if not path.exists():
            errors.append(f"Missing required refactor-planning output: {path}")
            continue
        if path.is_file() and not path.read_text(encoding="utf-8").strip():
            errors.append(f"Empty required refactor-planning output: {path}")

    for issue in validate_docs(root, targets=("docs/ADR_REFACTOR_LOG.md",)):
        errors.append(f"{issue.relpath}: {issue.message}")

    if errors:
        print("REFACTOR PLANNING OUTPUT VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("REFACTOR PLANNING OUTPUT VALIDATION PASSED")
    print(f"- Root: {root}")
    print("- Required refactor-planning closeout artifacts exist and are non-empty")


if __name__ == "__main__":
    main()
