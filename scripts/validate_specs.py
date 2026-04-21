#!/usr/bin/env python3
"""Validate Marcus Fleet spec-driven development gates."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


AGENTS_DIR = Path(__file__).resolve().parents[1]
SPECS_DIR = AGENTS_DIR / "specs"
CONSTITUTION = AGENTS_DIR / "memory" / "constitution.md"
REQUIRED_FILES = [
    "spec.md",
    "plan.md",
    "tasks.md",
    "verification.md",
    "agent-routing.md",
    "research.md",
    "data-model.md",
    "quickstart.md",
]


def find_features(target: str | None) -> list[Path]:
    if target:
        path = Path(target)
        if not path.is_absolute():
            path = (Path.cwd() / path).resolve()
        return [path]

    if not SPECS_DIR.exists():
        return []
    return sorted(path for path in SPECS_DIR.iterdir() if path.is_dir())


def validate_feature(feature_dir: Path, allow_clarifications: bool) -> list[str]:
    errors: list[str] = []
    if not re.match(r"^\d{3,}-[a-z0-9-]+$", feature_dir.name):
        errors.append(f"{feature_dir}: feature directory must match NNN-slug")

    for filename in REQUIRED_FILES:
        path = feature_dir / filename
        if not path.exists():
            errors.append(f"{feature_dir}: missing {filename}")
        elif not path.read_text(encoding="utf-8").strip():
            errors.append(f"{feature_dir}: empty {filename}")

    contracts_dir = feature_dir / "contracts"
    if not contracts_dir.exists() or not contracts_dir.is_dir():
        errors.append(f"{feature_dir}: missing contracts/ directory")

    spec_path = feature_dir / "spec.md"
    if spec_path.exists():
        spec = spec_path.read_text(encoding="utf-8")
        if "[NEEDS CLARIFICATION:" in spec and not allow_clarifications:
            errors.append(f"{feature_dir}: unresolved [NEEDS CLARIFICATION] marker")
        for section in [
            "## 1. Purpose",
            "## 2. User Stories",
            "## 3. Functional Requirements",
            "## 5. Acceptance Criteria",
        ]:
            if section not in spec:
                errors.append(f"{feature_dir}: spec.md missing section {section}")

    plan_path = feature_dir / "plan.md"
    if plan_path.exists():
        plan = plan_path.read_text(encoding="utf-8")
        if "## 2. Constitution Gates" not in plan:
            errors.append(f"{feature_dir}: plan.md missing Constitution Gates")

    tasks_path = feature_dir / "tasks.md"
    if tasks_path.exists():
        tasks = tasks_path.read_text(encoding="utf-8")
        if "Owner:" not in tasks:
            errors.append(f"{feature_dir}: tasks.md must include Owner markers")
        if "Verification:" not in tasks:
            errors.append(f"{feature_dir}: tasks.md must include Verification markers")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Marcus Fleet feature specs.")
    parser.add_argument("--feature", help="Path to a single feature directory.")
    parser.add_argument(
        "--allow-clarifications",
        action="store_true",
        help="Allow unresolved [NEEDS CLARIFICATION] markers for draft specs.",
    )
    args = parser.parse_args()

    errors: list[str] = []
    if not CONSTITUTION.exists():
        errors.append(f"Missing constitution: {CONSTITUTION}")

    features = find_features(args.feature)
    if not features:
        errors.append(f"No feature specs found under {SPECS_DIR}")

    for feature_dir in features:
        errors.extend(validate_feature(feature_dir, args.allow_clarifications))

    if errors:
        print("SPEC VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print(f"SPEC VALIDATION PASSED: {len(features)} feature(s)")


if __name__ == "__main__":
    main()
