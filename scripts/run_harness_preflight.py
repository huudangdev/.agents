#!/usr/bin/env python3
"""Run deterministic harness preflight checks for bootstrap or execution."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from path_utils import append_jsonl, resolve_agents_root, resolve_harness_logs_dir, resolve_script_path, utc_timestamp


def run_command(command: list[str], cwd: Path) -> dict[str, object]:
    printable = " ".join(command)
    print(f"$ {printable}")
    result = subprocess.run(command, cwd=cwd, check=False)
    if result.returncode != 0:
        print(f"Command failed with exit code {result.returncode}: {printable}")
    return {
        "command": printable,
        "exit_code": result.returncode,
        "status": "pass" if result.returncode == 0 else "fail",
    }


def python_command(root: Path, script_name: str, *args: str) -> list[str]:
    return [sys.executable, str(resolve_script_path(root, script_name)), *args]


def bootstrap_commands(root: Path) -> list[list[str]]:
    return [
        python_command(root, "sync_project_mcp.py", "--root", str(root)),
        python_command(root, "check_mcp_health.py", "--root", str(root)),
        python_command(root, "print_update_brief.py", "--root", str(root)),
        python_command(root, "validate_harness_contract.py", "--root", str(root)),
        ["bash", str(resolve_script_path(root, "check_repo_setup.sh")), str(root)],
    ]


def execution_commands(root: Path, feature: str | None) -> list[list[str]]:
    commands = [
        python_command(root, "build_context_index.py", "--root", str(root)),
        python_command(root, "validate_context_index.py", "--root", str(root)),
        python_command(root, "validate_command_surface.py", "--root", str(root)),
        python_command(root, "validate_routing_regression.py", "--root", str(root)),
        python_command(root, "validate_harness_contract.py", "--root", str(root)),
    ]
    if feature:
        commands.append(
            python_command(
                root,
                "validate_execution_readiness.py",
                "--root",
                str(root),
                "--feature",
                feature,
            )
        )
    return commands


def write_log(root: Path, phase: str, feature: str, results: list[dict[str, object]]) -> None:
    failing = next((str(item["command"]) for item in results if item["status"] == "fail"), "")
    payload = {
        "timestamp": utc_timestamp(),
        "phase": phase,
        "stage": "preflight",
        "feature": feature,
        "status": "fail" if failing else "pass",
        "failing_command": failing,
        "commands": results,
    }
    append_jsonl(resolve_harness_logs_dir(root) / "preflight.jsonl", payload)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run harness preflight checks.")
    parser.add_argument("--root", default=".", help="Project root containing .agents/")
    parser.add_argument("--phase", choices=["bootstrap", "execution"], required=True)
    parser.add_argument("--feature", default="", help="Optional feature path for execution phase.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    agents_root = resolve_agents_root(root)
    print(f"HARNESS PREFLIGHT: {args.phase}")
    print(f"- Root: {root}")
    print(f"- Agents root: {agents_root}")

    commands = bootstrap_commands(root) if args.phase == "bootstrap" else execution_commands(root, args.feature or None)

    results: list[dict[str, object]] = []
    for command in commands:
        result = run_command(command, agents_root)
        results.append(result)
        if result["status"] == "fail":
            write_log(root, args.phase, args.feature, results)
            sys.exit(int(result["exit_code"]))

    write_log(root, args.phase, args.feature, results)
    print("HARNESS PREFLIGHT PASSED")
    print(f"- Phase: {args.phase}")
    if args.feature:
        print(f"- Feature: {args.feature}")


if __name__ == "__main__":
    main()
