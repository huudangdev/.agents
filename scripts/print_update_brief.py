#!/usr/bin/env python3
"""Print release highlights and onboarding steps for install/update/bootstrap."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise SystemExit(f"Expected JSON object at {path}")
    return value


def main() -> None:
    parser = argparse.ArgumentParser(description="Print release highlights and onboarding suggestions.")
    parser.add_argument("--root", default=".", help="Project root.")
    parser.add_argument("--manifest", default=".agents/release_manifest.json", help="Release manifest path relative to root.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    manifest = load_json((root / args.manifest).resolve())

    print(f"Release version: {manifest.get('version', 'unknown')}")
    print(f"Headline: {manifest.get('headline', '')}")

    highlights = manifest.get("highlights", [])
    if highlights:
        print("\nWhat's new:")
        for item in highlights:
            print(f"- {item}")

    steps = manifest.get("post_update_steps", [])
    if steps:
        print("\nSuggested next steps:")
        for item in steps:
            print(f"- {item}")

    prompts = manifest.get("onboarding_prompts", [])
    if prompts:
        print("\nFeature onboarding suggestions:")
        for item in prompts:
            print(f"- {item}")


if __name__ == "__main__":
    main()
