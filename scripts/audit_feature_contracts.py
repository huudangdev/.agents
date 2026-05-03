#!/usr/bin/env python3
"""Audit feature workspaces against the current Marcus Fleet contract."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from path_utils import resolve_agents_root

CURRENT_CONTRACT_MARKERS = [
    ("spec.md", "## 10. Review Loop"),
    ("plan.md", "## 9. POC Slice and Review Cadence"),
    ("tasks.md", "## Review Loop Tasks"),
    ("verification.md", "## Review Rounds"),
]


def run_validation(script: Path, feature: Path) -> tuple[int, str]:
    result = subprocess.run(
        [sys.executable, str(script), "--feature", str(feature)],
        cwd=script.parent.parent,
        check=False,
        capture_output=True,
        text=True,
    )
    output = (result.stdout or "") + (result.stderr or "")
    return result.returncode, output.strip()


def contract_mode(feature: Path) -> str:
    for filename, marker in CURRENT_CONTRACT_MARKERS:
        path = feature / filename
        if not path.exists():
            return "legacy"
        if marker not in path.read_text(encoding="utf-8"):
            return "legacy"
    return "current"


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit .agents/specs feature contracts.")
    parser.add_argument("--root", default=".", help="Project root containing .agents/")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    agents_root = resolve_agents_root(root)
    specs_dir = agents_root / "specs"
    validate_specs = agents_root / "scripts" / "validate_specs.py"

    if not specs_dir.exists():
        print("FEATURE CONTRACT AUDIT FAILED")
        print(f"- Missing specs directory: {specs_dir}")
        sys.exit(1)

    rows: list[tuple[str, str, str]] = []
    failed = 0

    for feature in sorted(path for path in specs_dir.iterdir() if path.is_dir()):
        mode = contract_mode(feature)
        code, _ = run_validation(validate_specs, feature)
        status = "pass" if code == 0 else "fail"
        if status == "fail":
            failed += 1
        rows.append((feature.name, mode, status))

    print("FEATURE CONTRACT AUDIT")
    print("")
    print("| Feature | Contract | Validation |")
    print("| --- | --- | --- |")
    for feature_name, mode, status in rows:
        print(f"| `{feature_name}` | `{mode}` | `{status}` |")

    print("")
    print(f"- Total features: {len(rows)}")
    print(f"- Current-contract features: {sum(1 for _, mode, _ in rows if mode == 'current')}")
    print(f"- Legacy features: {sum(1 for _, mode, _ in rows if mode == 'legacy')}")
    print(f"- Validation failures: {failed}")

    if failed:
        print("- Recommended next step: migrate legacy or failing packages before claiming repo-wide spec readiness.")
        sys.exit(1)


if __name__ == "__main__":
    main()
