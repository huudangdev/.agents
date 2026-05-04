#!/usr/bin/env python3
"""Scaffold /develop execution knowledge artifacts."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path


AGENTS_DIR = Path(__file__).resolve().parents[1]
TEMPLATES_DIR = AGENTS_DIR / "templates"

LEGACY_TEMPLATE_MAP = {
    "index.md": "development-index-template.md",
    "development_manifest.json": "development-manifest-template.json",
    "epics/epic-000.md": "development-epic-template.md",
    "modules/module-000.md": "development-module-template.md",
    "features/feature-000.md": "development-feature-template.md",
    "pages/page-000.md": "development-page-template.md",
    "tasks/task-000.md": "development-task-template.md",
    "sync/sync_manifest.json": "development-sync-manifest-template.json",
}

EPIC_FIRST_TEMPLATE_MAP = {
    "index.md": "development-index-template.md",
    "development_manifest.json": "development-manifest-template.json",
    "{epic_dir}/epic.md": "development-epic-template.md",
    "{epic_dir}/issues.md": "development-issues-template.md",
    "{epic_dir}/features/{feature_id}.md": "development-feature-template.md",
    "{epic_dir}/modules/{module_id}.md": "development-module-template.md",
    "{epic_dir}/pages/{page_id}.md": "development-page-template.md",
    "{epic_dir}/tasks/{task_id}.md": "development-task-template.md",
    "sync/sync_manifest.json": "development-sync-manifest-template.json",
    "{epic_dir}/sync/sync_manifest.json": "development-sync-manifest-template.json",
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


def render_template(target: Path, template_name: str, replacements: dict[str, str], force: bool) -> bool:
    if target.exists() and not force:
        return False
    target.parent.mkdir(parents=True, exist_ok=True)
    text = (TEMPLATES_DIR / template_name).read_text(encoding="utf-8")
    for old, new in replacements.items():
        text = text.replace(old, new)
    target.write_text(text, encoding="utf-8")
    return True


def padded(value: str) -> str:
    digits = re.sub(r"\D+", "", value)
    return (digits or "1").zfill(3)[-3:]


def existing_topology(base: Path) -> str:
    manifest = base / "development_manifest.json"
    if not manifest.exists():
        return "epic-first"
    try:
        value = json.loads(manifest.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return "legacy-flat"
    topology = str(value.get("topology", value.get("ledger_topology", "legacy-flat")))
    return topology.replace("_", "-")


def scaffold_legacy(base: Path, root: Path, slug: str, feature_id: str, force: bool) -> list[Path]:
    created: list[Path] = []

    for rel_path, template_name in LEGACY_TEMPLATE_MAP.items():
        target = base / rel_path
        if rel_path.endswith("-000.md"):
            target = target.with_name(target.name.replace("000", slug))
        if copy_template(target, template_name, force):
            if target.suffix == ".md":
                text = target.read_text(encoding="utf-8")
                text = text.replace("id: epic-000", f"id: epic-{slug}")
                text = text.replace("id: module-000", f"id: module-{slug}")
                text = text.replace("id: feature-000", f"id: feature-{slug}")
                text = text.replace("id: page-000", f"id: page-{slug}")
                text = text.replace("id: task-000", f"id: task-{slug}")
                text = text.replace("parent_epic: E-000-placeholder\n", "")
                text = text.replace("# Epic: <Name>", f"# Epic: {slug.replace('-', ' ').title()}")
                text = text.replace("# Module: <Name>", f"# Module: {slug.replace('-', ' ').title()}")
                text = text.replace("# Feature: <Name>", f"# Feature: {slug.replace('-', ' ').title()}")
                text = text.replace("# Page: <Name>", f"# Page: {slug.replace('-', ' ').title()}")
                text = text.replace("# Task: <Name>", f"# Task: {slug.replace('-', ' ').title()}")
                text = text.replace("`feature-000`", f"`feature-{slug}`")
                target.write_text(text, encoding="utf-8")
            created.append(target)

    manifest = base / "development_manifest.json"
    if manifest.exists():
        text = manifest.read_text(encoding="utf-8")
        text = text.replace('"version": "31.0"', '"version": "30.4"')
        text = text.replace('"topology": "epic_first"', '"topology": "legacy_flat"')
        text = text.replace('"ledger_topology": "epic_first"', '"ledger_topology": "legacy_flat"')
        text = text.replace('"require_epic_first_topology": true', '"require_epic_first_topology": false')
        text = text.replace('"require_canonical_ids": true', '"require_canonical_ids": false')
        text = text.replace('"require_parent_child_trace": true', '"require_parent_child_trace": false')
        text = text.replace('"forbid_orphan_development_docs": true', '"forbid_orphan_development_docs": false')
        if feature_id:
            text = text.replace('"feature_id": ""', f'"feature_id": "{feature_id}"')
        manifest.write_text(text, encoding="utf-8")

    return created


def scaffold_epic_first(
    base: Path,
    root: Path,
    slug: str,
    feature_id: str,
    force: bool,
    epic_number: str,
    child_number: str,
    task_number: str,
) -> list[Path]:
    created: list[Path] = []
    epic_num = padded(epic_number)
    child_num = padded(child_number)
    task_num = padded(task_number)
    epic_id = f"E-{epic_num}-{slug}"
    feature_doc_id = f"F-{epic_num}-{child_num}-{slug}"
    module_doc_id = f"M-{epic_num}-{child_num}-{slug}"
    page_doc_id = f"P-{epic_num}-{child_num}-{slug}"
    task_doc_id = f"T-{epic_num}-{child_num}-{task_num}-{slug}"

    replacements = {
        "id: epic-000": f"id: {epic_id}",
        "id: ISSUES-E-000-placeholder": f"id: ISSUES-{epic_id}",
        "id: module-000": f"id: {module_doc_id}",
        "id: feature-000": f"id: {feature_doc_id}",
        "id: page-000": f"id: {page_doc_id}",
        "id: task-000": f"id: {task_doc_id}",
        "`feature-000`": f"`{feature_doc_id}`",
        "parent_epic: E-000-placeholder": f"parent_epic: {epic_id}",
        "# Epic: <Name>": f"# Epic: {slug.replace('-', ' ').title()}",
        "# Epic Issues: <Name>": f"# Epic Issues: {slug.replace('-', ' ').title()}",
        "# Module: <Name>": f"# Module: {slug.replace('-', ' ').title()}",
        "# Feature: <Name>": f"# Feature: {slug.replace('-', ' ').title()}",
        "# Page: <Name>": f"# Page: {slug.replace('-', ' ').title()}",
        "# Task: <Name>": f"# Task: {slug.replace('-', ' ').title()}",
        '"feature_id": ""': f'"feature_id": "{feature_id}"',
    }

    format_values = {
        "epic_dir": epic_id,
        "feature_id": feature_doc_id,
        "module_id": module_doc_id,
        "page_id": page_doc_id,
        "task_id": task_doc_id,
    }

    for rel_template, template_name in EPIC_FIRST_TEMPLATE_MAP.items():
        rel_path = rel_template.format(**format_values)
        target = base / rel_path
        if render_template(target, template_name, replacements, force):
            created.append(target)

    manifest = base / "development_manifest.json"
    if manifest.exists():
        text = manifest.read_text(encoding="utf-8")
        text = text.replace('"topology": "legacy_flat"', '"topology": "epic_first"')
        text = text.replace('"version": "1.0"', '"version": "31.0"')
        text = text.replace('"ledger_topology": "legacy_flat"', '"ledger_topology": "epic_first"')
        text = text.replace(
            '"epics": {}',
            (
                '"epics": {\n'
                f'    "{epic_id}": {{\n'
                f'      "path": "docs/development/{epic_id}",\n'
                '      "status": "draft",\n'
                f'      "children": ["ISSUES-{epic_id}", "{feature_doc_id}", "{module_doc_id}", "{page_doc_id}", "{task_doc_id}"]\n'
                "    }\n"
                "  }"
            ),
        )
        manifest.write_text(text, encoding="utf-8")

    return created


def main() -> None:
    parser = argparse.ArgumentParser(description="Create /develop documentation scaffold.")
    parser.add_argument("--root", default=".", help="Workspace root.")
    parser.add_argument("--name", default="Implementation", help="Implementation or feature name.")
    parser.add_argument("--feature-id", default="", help="Related .agents/specs/<feature-id>.")
    parser.add_argument(
        "--topology",
        choices=["auto", "epic-first", "legacy-flat"],
        default="auto",
        help="Scaffold topology. auto preserves an existing manifest topology; new ledgers use epic-first.",
    )
    parser.add_argument("--epic-number", default="001", help="Three-digit epic number, e.g. 001.")
    parser.add_argument("--child-number", default="001", help="Three-digit feature/module/page number within the epic.")
    parser.add_argument("--task-number", default="001", help="Three-digit task number within the child scope.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing scaffold files.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    base = root / "docs" / "development"
    slug = slugify(args.name)
    topology = args.topology
    if topology == "auto":
        topology = existing_topology(base) if base.exists() else "epic-first"

    if topology == "legacy-flat":
        created = scaffold_legacy(base, root, slug, args.feature_id, args.force)
    else:
        created = scaffold_epic_first(
            base,
            root,
            slug,
            args.feature_id,
            args.force,
            args.epic_number,
            args.child_number,
            args.task_number,
        )

    print(f"Development docs scaffold created ({topology}): {base}")
    print("DRAFT SCAFFOLD ONLY: these files are invalid until filled with code-derived facts.")
    print("Required closeout:")
    print("- python3 .agents/scripts/validate_development_docs.py --strict-counts")
    print("- python3 .agents/scripts/validate_docs_substance.py --root . --include-development")
    for path in created:
        print(f"- {path.relative_to(root)}")


if __name__ == "__main__":
    main()
