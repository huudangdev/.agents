#!/usr/bin/env python3
"""Validate that a feature workspace is ready for behavior-changing execution."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from path_utils import resolve_agents_root


def run_spec_validation(root: Path, feature: Path) -> tuple[int, str]:
    agents_root = resolve_agents_root(root)
    script = agents_root / "scripts/validate_specs.py"
    result = subprocess.run(
        [sys.executable, str(script), "--feature", str(feature)],
        cwd=agents_root,
        check=False,
        capture_output=True,
        text=True,
    )
    output = (result.stdout or "") + (result.stderr or "")
    return result.returncode, output.strip()


def run_brief_freshness_validation(root: Path, feature: Path) -> tuple[int, str]:
    agents_root = resolve_agents_root(root)
    script = agents_root / "scripts/validate_execution_brief_freshness.py"
    result = subprocess.run(
        [sys.executable, str(script), "--root", str(root), "--feature", str(feature)],
        cwd=agents_root,
        check=False,
        capture_output=True,
        text=True,
    )
    output = (result.stdout or "") + (result.stderr or "")
    return result.returncode, output.strip()


def check_file_contains(path: Path, markers: list[str]) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"Missing file: {path}"]
    text = path.read_text(encoding="utf-8")
    for marker in markers:
        if marker not in text:
            errors.append(f"{path.name}: missing `{marker}`")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Marcus Fleet execution readiness.")
    parser.add_argument("--root", default=".", help="Project root containing .agents/")
    parser.add_argument("--feature", required=True, help="Feature directory or path to feature workspace.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    feature = Path(args.feature)
    if not feature.is_absolute():
        feature = (root / feature).resolve()

    errors: list[str] = []

    if not feature.exists():
        errors.append(f"Feature workspace not found: {feature}")
    if not feature.is_dir():
        errors.append(f"Feature workspace is not a directory: {feature}")

    if errors:
        print("EXECUTION READINESS FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    spec_code, spec_output = run_spec_validation(root, feature)
    if spec_code != 0:
        print("EXECUTION READINESS FAILED")
        print("- Spec validation did not pass")
        if spec_output:
            for line in spec_output.splitlines():
                print(f"  {line}")
        sys.exit(1)

    brief_code, brief_output = run_brief_freshness_validation(root, feature)
    if brief_code != 0:
        print("EXECUTION READINESS FAILED")
        print("- Execution brief freshness validation did not pass")
        if brief_output:
            for line in brief_output.splitlines():
                print(f"  {line}")
        sys.exit(1)

    errors.extend(
        check_file_contains(
            feature / "tasks.md",
            ["## Execution Monitoring", "## Review Loop Tasks", "Write Scope:", "Verification:", "Docs:", "Sync:"],
        )
    )
    errors.extend(
        check_file_contains(
            feature / "verification.md",
            ["## Verification Plan", "## Execution Gates", "## Evidence", "## Review Rounds", "## Release Recommendation", "## Residual Risk"],
        )
    )
    errors.extend(
        check_file_contains(
            feature / "execution-brief.md",
            [
                "## 1. Operator Intent Snapshot",
                "## 4. Active Work Slice",
                "## 5. Development Ledger Context",
                "## 6. Verification Path",
                "## 8. Context Expansion Rules",
                "### Task Shape Decision",
                "### Required Reads",
                "### Forbidden Default Reads",
                "### Expansion Triggers",
            ],
        )
    )
    errors.extend(
        check_file_contains(
            feature / "agent-routing.md",
            ["## Routing Contract", "## Handoff Rules", "## Review Topology", "## Escalation Rules"],
        )
    )

    if errors:
        print("EXECUTION READINESS FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("EXECUTION READINESS PASSED")
    print(f"- Feature: {feature.relative_to(root)}")
    print("- Spec validation: passed")
    print("- Execution brief freshness: passed")
    print("- Task monitoring contract: present")
    print("- Verification execution gates: present")
    print("- Routing escalation rules: present")


if __name__ == "__main__":
    main()
