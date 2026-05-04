#!/usr/bin/env python3
"""Run the mandatory documentation gates for planning/execution closeout."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from path_utils import resolve_script_path


PLANNING_DOCS = (
    "docs/prd.md",
    "docs/tasks.md",
    "docs/knowledge.md",
    "docs/decisions.md",
    "docs/memory.md",
    "docs/planning/flows.md",
    "docs/planning/screens.md",
    "docs/planning/diagrams.md",
)


def run(command: list[str], cwd: Path) -> int:
    print("$ " + " ".join(command))
    result = subprocess.run(command, cwd=cwd, check=False)
    if result.returncode != 0:
        print(f"FAILED: {' '.join(command)}")
    return result.returncode


def py(root: Path, script_name: str, *args: str) -> list[str]:
    return [sys.executable, str(resolve_script_path(root, script_name)), *args]


def has_any(root: Path, relpaths: tuple[str, ...]) -> bool:
    return any((root / relpath).exists() for relpath in relpaths)


def has_development_docs(root: Path) -> bool:
    return (root / "docs" / "development").exists()


def has_research_docs(root: Path) -> bool:
    return (root / "docs" / "research").exists()


def command_chain(root: Path, mode: str) -> list[list[str]]:
    commands: list[list[str]] = []
    planning_present = has_any(root, PLANNING_DOCS)
    development_present = has_development_docs(root)
    research_present = has_research_docs(root)

    execution_requested = mode in {"execution", "all"} or (mode == "auto" and development_present)

    if mode in {"planning", "all"} or (mode == "auto" and (planning_present or research_present)):
        commands.append(py(root, "validate_docs_substance.py", "--root", str(root), "--strict-planning", "--require-docs"))
        if research_present:
            commands.append(py(root, "validate_planning_research.py", "--root", str(root), "--strict-outputs"))
    elif not execution_requested:
        commands.append(py(root, "validate_docs_substance.py", "--root", str(root), "--include-development"))

    if execution_requested:
        if development_present:
            commands.append(py(root, "validate_development_docs.py", "--strict-counts"))
            commands.append(py(root, "validate_doc_sync.py", "--strict"))
        commands.append(py(root, "validate_docs_substance.py", "--root", str(root), "--include-development"))

    return commands


def main() -> None:
    parser = argparse.ArgumentParser(description="Run mandatory docs gates.")
    parser.add_argument("--root", default=".", help="Project root containing .agents/ and docs/")
    parser.add_argument(
        "--mode",
        choices=["auto", "planning", "execution", "all"],
        default="auto",
        help="Gate profile to run. auto infers from docs present.",
    )
    parser.add_argument(
        "--require-development-docs",
        action="store_true",
        help="Fail closed when docs/development/ is missing.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    print(f"REQUIRED DOCS GATES: {args.mode}")
    print(f"- Root: {root}")
    if args.require_development_docs and not has_development_docs(root):
        print("FAILED: docs/development/ is required for this closeout but is missing")
        sys.exit(1)
    for command in command_chain(root, args.mode):
        exit_code = run(command, root)
        if exit_code != 0:
            sys.exit(exit_code)

    print("REQUIRED DOCS GATES PASSED")


if __name__ == "__main__":
    main()
