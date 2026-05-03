#!/usr/bin/env python3
"""Validate that `/refactor-planning` can start on the current project root."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from path_utils import resolve_agents_root


REQUIRED_DOCS = (
    "agents.md",
    "docs/prd.md",
    "docs/tasks.md",
    "docs/knowledge.md",
    "docs/decisions.md",
    "docs/memory.md",
    "docs/planning/flows.md",
    "docs/planning/screens.md",
    "docs/planning/diagrams.md",
    "docs/development/development_manifest.json",
    "docs/development/index.md",
)


def run_validator(root: Path, script_name: str, *args: str) -> tuple[int, str]:
    command = [sys.executable, str(Path(__file__).resolve().parent / script_name), *args]
    result = subprocess.run(command, cwd=root, capture_output=True, text=True, check=False)
    output = (result.stdout + result.stderr).strip()
    return result.returncode, output


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate `/refactor-planning` brownfield readiness.")
    parser.add_argument("--root", default=".", help="Project root to validate.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    agents_root = resolve_agents_root(root)
    errors: list[str] = []

    for relpath in REQUIRED_DOCS:
        path = root / relpath
        if not path.exists():
            errors.append(f"Missing required brownfield input: {path}")
            continue
        if path.is_file() and not path.read_text(encoding="utf-8").strip():
            errors.append(f"Empty required brownfield input: {path}")

    workflow = agents_root / "workflows" / "refactor-planning.md"
    if not workflow.exists():
        errors.append(f"Missing `/refactor-planning` workflow: {workflow}")

    if not errors:
        rc, output = run_validator(root, "validate_development_docs.py", "--strict-counts")
        if rc != 0:
            errors.append("Development docs gate failed under `/refactor-planning` readiness.")
            if output:
                errors.append(output)

    if errors:
        print("REFACTOR PLANNING READINESS FAILED")
        for error in errors:
            for line in str(error).splitlines():
                print(f"- {line}")
        sys.exit(1)

    print("REFACTOR PLANNING READINESS PASSED")
    print(f"- Root: {root}")
    print("- Brownfield docs package exists and passes development-doc quality gate")
    print("- `/refactor-planning` workflow is available")


if __name__ == "__main__":
    main()
