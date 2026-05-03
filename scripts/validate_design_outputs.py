#!/usr/bin/env python3
"""Validate that `/design` produced the expected design documents."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_OUTPUTS = (
    "docs/BRAND_GUIDELINES.md",
    "docs/UI_COMPONENTS_STATE.md",
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate `/design` output artifacts.")
    parser.add_argument("--root", default=".", help="Project root that contains docs/")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors: list[str] = []

    for relpath in REQUIRED_OUTPUTS:
        path = root / relpath
        if not path.exists():
            errors.append(f"Missing required design output: {path}")
            continue
        if not path.read_text(encoding="utf-8").strip():
            errors.append(f"Empty required design output: {path}")

    if errors:
        print("DESIGN OUTPUT VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("DESIGN OUTPUT VALIDATION PASSED")
    print(f"- Root: {root}")
    print("- `/design` output artifacts exist and are non-empty")


if __name__ == "__main__":
    main()
