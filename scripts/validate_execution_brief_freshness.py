#!/usr/bin/env python3
"""Validate that execution-brief.md is newer than its source artifacts."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from build_execution_brief import find_relevant_development_docs  # noqa: E402


SOURCE_FILES = [
    "spec.md",
    "plan.md",
    "tasks.md",
    "verification.md",
    "quickstart.md",
    "agent-routing.md",
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate execution-brief freshness.")
    parser.add_argument("--root", default=".", help="Project root containing .agents/")
    parser.add_argument("--feature", required=True, help="Feature directory or path to feature workspace.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    feature = Path(args.feature)
    if not feature.is_absolute():
        feature = (root / feature).resolve()

    brief = feature / "execution-brief.md"
    if not brief.exists():
        print("EXECUTION BRIEF FRESHNESS FAILED")
        print(f"- Missing file: {brief}")
        sys.exit(1)

    stale_sources: list[Path] = []
    brief_mtime = brief.stat().st_mtime

    for name in SOURCE_FILES:
        path = feature / name
        if path.exists() and path.stat().st_mtime > brief_mtime:
            stale_sources.append(path)

    for path in find_relevant_development_docs(feature):
        if path.exists() and path.stat().st_mtime > brief_mtime:
            stale_sources.append(path)

    if stale_sources:
        print("EXECUTION BRIEF FRESHNESS FAILED")
        print("- execution-brief.md is older than these source artifacts:")
        for path in stale_sources:
            print(f"  - {path.relative_to(root)}")
        print("- Rebuild with `python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/<feature-id> --task-shape <shape>` before /develop.")
        sys.exit(1)

    print("EXECUTION BRIEF FRESHNESS PASSED")
    print(f"- Feature: {feature.relative_to(root)}")
    print("- execution-brief.md is at least as recent as spec, plan, tasks, verification, quickstart, agent-routing, and matched development docs")


if __name__ == "__main__":
    main()
