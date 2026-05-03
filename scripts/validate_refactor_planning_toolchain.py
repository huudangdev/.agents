#!/usr/bin/env python3
"""Validate that `/refactor-planning` has the local toolchain prerequisites available.

This gate is intentionally non-invasive:
- It does not run `npx understand-anything`, `tsc`, or `npm run dev`.
- It only checks that the required executables are discoverable and that ESLint
  is available either globally or via local `node_modules/.bin`.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


REQUIRED_BINARIES = ("node", "npm", "npx")


def which(name: str) -> str | None:
    return shutil.which(name)


def run_version(binary: str) -> str:
    try:
        result = subprocess.run(
            [binary, "--version"],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError as exc:
        return f"<error: {exc}>"
    output = (result.stdout + result.stderr).strip()
    return output.splitlines()[0].strip() if output else "<no output>"


def has_local_eslint(root: Path) -> bool:
    # Support POSIX and Windows layouts.
    candidates = [
        root / "node_modules" / ".bin" / "eslint",
        root / "node_modules" / ".bin" / "eslint.cmd",
        root / "node_modules" / ".bin" / "eslint.ps1",
    ]
    return any(path.exists() for path in candidates)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate local toolchain prerequisites for `/refactor-planning`.")
    parser.add_argument("--root", default=".", help="Project root to validate.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors: list[str] = []

    found: dict[str, str] = {}
    for binary in REQUIRED_BINARIES:
        resolved = which(binary)
        if not resolved:
            errors.append(f"Missing required executable in PATH: {binary}")
        else:
            found[binary] = resolved

    eslint_global = which("eslint")
    eslint_local = has_local_eslint(root)
    if not eslint_global and not eslint_local:
        errors.append(
            "Missing ESLint: expected either `eslint` in PATH or `node_modules/.bin/eslint` under the project root"
        )

    if errors:
        print("REFACTOR PLANNING TOOLCHAIN VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("REFACTOR PLANNING TOOLCHAIN VALIDATION PASSED")
    print(f"- Root: {root}")
    for binary in REQUIRED_BINARIES:
        resolved = found.get(binary, "<missing>")
        print(f"- {binary}: {resolved} ({run_version(binary)})")
    if eslint_global:
        print(f"- eslint: {eslint_global} ({run_version('eslint')})")
    elif eslint_local:
        rel = (root / 'node_modules' / '.bin' / 'eslint').as_posix()
        print(f"- eslint: {rel} (local project dependency)")


if __name__ == "__main__":
    main()
