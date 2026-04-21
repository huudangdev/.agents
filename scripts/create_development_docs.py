#!/usr/bin/env python3
"""Scaffold /develop execution knowledge artifacts."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


AGENTS_DIR = Path(__file__).resolve().parents[1]
TEMPLATES_DIR = AGENTS_DIR / "templates"

TEMPLATE_MAP = {
    "index.md": "development-index-template.md",
    "development_manifest.json": "development-manifest-template.json",
    "epics/epic-000.md": "development-epic-template.md",
    "modules/module-000.md": "development-module-template.md",
    "features/feature-000.md": "development-feature-template.md",
    "pages/page-000.md": "development-page-template.md",
    "tasks/task-000.md": "development-task-template.md",
    "sync/sync_manifest.json": "development-sync-manifest-template.json",
}


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "implementation"


def copy_template(target: Path, template_name: str, force: bool) -> bool:
    if target.exists() and not force:
        return False
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(TEMPLATES_DIR / template_name, target)
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Create /develop documentation scaffold.")
    parser.add_argument("--root", default=".", help="Workspace root.")
    parser.add_argument("--name", default="Implementation", help="Implementation or feature name.")
    parser.add_argument("--feature-id", default="", help="Related .agents/specs/<feature-id>.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing scaffold files.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    base = root / "docs" / "development"
    slug = slugify(args.name)
    created: list[Path] = []

    for rel_path, template_name in TEMPLATE_MAP.items():
        target = base / rel_path
        if rel_path.endswith("-000.md"):
            target = target.with_name(target.name.replace("000", slug))
        if copy_template(target, template_name, args.force):
            created.append(target)

    manifest = base / "development_manifest.json"
    if manifest.exists() and args.feature_id:
        text = manifest.read_text(encoding="utf-8")
        text = text.replace('"feature_id": ""', f'"feature_id": "{args.feature_id}"')
        manifest.write_text(text, encoding="utf-8")

    print(f"Development docs scaffold ready: {base}")
    for path in created:
        print(f"- {path.relative_to(root)}")


if __name__ == "__main__":
    main()
