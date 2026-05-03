#!/usr/bin/env python3
"""Validate that `/design` has the planning inputs it depends on."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from path_utils import resolve_agents_root


REQUIRED_INPUTS = (
    "agents.md",
    "docs/prd.md",
    "docs/planning/screens.md",
    "docs/planning/flows.md",
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate `/design` readiness inputs.")
    parser.add_argument("--root", default=".", help="Project root that contains docs/ and optionally .agents/")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    agents_root = resolve_agents_root(root)
    errors: list[str] = []

    for relpath in REQUIRED_INPUTS:
        path = root / relpath
        if not path.exists():
            errors.append(f"Missing required design input: {path}")
            continue
        if path.is_file() and not path.read_text(encoding="utf-8").strip():
            errors.append(f"Empty required design input: {path}")

    workflow = agents_root / "workflows" / "design.md"
    if not workflow.exists():
        errors.append(f"Missing `/design` workflow: {workflow}")

    if errors:
        print("DESIGN READINESS FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("DESIGN READINESS PASSED")
    print(f"- Root: {root}")
    print("- Required planning inputs are present for `/design`")
    print("- `/design` workflow is available")


if __name__ == "__main__":
    main()
