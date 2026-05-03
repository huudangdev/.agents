#!/usr/bin/env python3
"""Validate the repo-wide harness contract between docs, workflows, and scripts."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from path_utils import resolve_from_root, resolve_script_path


CHECKS = [
    (
        ".agents/README.md",
        [
            "run_harness_preflight.py",
            "run_harness_postflight.py",
            "validate_harness_contract.py",
            ".agents/logs/harness/",
            "--changed-files",
            "--failing-evidence",
            "/init_brain",
            "/develop",
            "/quick_fix",
        ],
        "README documents the harness wrapper chain",
    ),
    (
        ".agents/USAGE_GUIDE.md",
        [
            "run_harness_preflight.py",
            "run_harness_postflight.py",
            "validate_harness_contract.py",
            ".agents/logs/harness/",
            "--changed-files",
            "--failing-evidence",
            "/init_brain",
            "/develop",
            "/quick_fix",
        ],
        "Usage guide documents the harness wrapper chain",
    ),
    (
        ".agents/workflows/init_brain.md",
        [
            "run_harness_preflight.py --root . --phase bootstrap",
            "sync_project_mcp.py",
            "check_mcp_health.py",
            "print_update_brief.py",
            ".agents/logs/harness/preflight.jsonl",
        ],
        "/init_brain wires bootstrap preflight",
    ),
    (
        ".agents/workflows/develop.md",
        [
            "run_harness_preflight.py --root . --phase execution --feature .agents/specs/<feature-id>",
            "run_harness_postflight.py --root . --phase execution --feature .agents/specs/<feature-id>",
            "validate_execution_readiness.py",
            ".agents/logs/harness/",
        ],
        "/develop wires execution preflight and postflight",
    ),
    (
        ".agents/workflows/quick_fix.md",
        [
            "run_harness_preflight.py --root . --phase execution --feature .agents/specs/<feature-id>",
            "execution-brief.md",
            "validate_doc_sync.py",
        ],
        "/quick_fix wires execution preflight",
    ),
    (
        ".agents/workflows/marcus_verify.md",
        [
            "run_harness_postflight.py --root . --phase execution --feature .agents/specs/<feature-id>",
            "validate_specs.py",
            "validate_doc_sync.py",
        ],
        "/marcus.verify wires execution postflight",
    ),
]

SCRIPT_NAMES = [
    "run_harness_preflight.py",
    "run_harness_postflight.py",
    "validate_harness_contract.py",
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate repo-wide harness contract freshness.")
    parser.add_argument("--root", default=".", help="Project root containing .agents/")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors: list[str] = []

    for script_name in SCRIPT_NAMES:
        script_path = resolve_script_path(root, script_name)
        if not script_path.exists():
            errors.append(f"Required harness script missing: {script_path}")

    for rel_path, markers, label in CHECKS:
        path = resolve_from_root(root, rel_path)
        if not path.exists():
            errors.append(f"{label}: missing file `{rel_path}`")
            continue
        text = path.read_text(encoding="utf-8")
        missing = [marker for marker in markers if marker not in text]
        if missing:
            errors.append(f"{label}: missing markers in `{rel_path}` -> {', '.join(missing)}")

    if errors:
        print("HARNESS CONTRACT VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("HARNESS CONTRACT VALIDATION PASSED")
    print("- README/USAGE mention the wrapper-based harness chain")
    print("- init/develop/quick_fix/verify workflows point to the same phases")
    print("- required harness wrapper scripts exist")


if __name__ == "__main__":
    main()
