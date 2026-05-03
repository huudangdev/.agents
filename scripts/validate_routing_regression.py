#!/usr/bin/env python3
"""Validate Marcus Fleet routing regression guardrails."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from path_utils import resolve_agents_root


def missing_markers(path: Path, markers: list[str]) -> list[str]:
    if not path.exists():
        return [f"Missing file: {path}"]
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    for marker in markers:
        if marker not in text:
            errors.append(f"{path.name}: missing `{marker}`")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate routing regression guardrails.")
    parser.add_argument("--root", default=".", help="Project root containing .agents/")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    agents = resolve_agents_root(root)

    develop = agents / "workflows" / "develop.md"
    skills_index = agents / "skills" / "SKILLS_INDEX.md"
    checklist = agents / "ROUTING_REGRESSION_CHECKLIST.md"
    usage = agents / "USAGE_GUIDE.md"
    readme = agents / "README.md"

    errors: list[str] = []

    errors.extend(
        missing_markers(
            develop,
            [
                "MINIMUM VIABLE CONTEXT",
                "SCOPE ROUTING GATE",
                "SKILL BUDGET GATE",
                "ROUTING REGRESSION GATE",
                "UI-only",
                "Forbidden Default Reads",
                "Do not route all work through backend scaffolding by default.",
            ],
        )
    )

    errors.extend(
        missing_markers(
            skills_index,
            [
                "## Context Budget Rules",
                "Default budget: read `SKILL.md` for 2 to 4 skills only.",
                "Never inspect databases, Supabase, SQL, analytics, or infrastructure",
                "## Recommended Routing by Task Shape",
            ],
        )
    )

    errors.extend(
        missing_markers(
            checklist,
            [
                "## 1. UI-only",
                "## 2. Frontend Behavior",
                "## 3. Backend/API",
                "## 4. Data/Contract",
                "## 5. Architecture/Refactor",
                "UI-only task reads Supabase, SQL, analytics, or infra by default",
            ],
        )
    )

    errors.extend(
        missing_markers(
            usage,
            [
                "ROUTING_REGRESSION_CHECKLIST.md",
                "a UI-only task reads Supabase/SQL/analytics/infra by default",
            ],
        )
    )

    errors.extend(
        missing_markers(
            readme,
            [
                "ROUTING_REGRESSION_CHECKLIST.md",
                "narrow UI task drifts into Supabase, SQL,",
            ],
        )
    )

    if errors:
        print("ROUTING REGRESSION VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("ROUTING REGRESSION VALIDATION PASSED")
    print("- develop workflow guardrails: present")
    print("- skills index routing budget: present")
    print("- regression checklist task shapes: present")
    print("- operator docs mention regression gate: present")


if __name__ == "__main__":
    main()
