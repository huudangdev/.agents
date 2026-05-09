#!/usr/bin/env python3
"""Validate Marcus Fleet skill packaging and routing contracts."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from path_utils import resolve_agents_root


REQUIRED_SECTIONS = (
    "## Required Reads",
    "## Operating Rules",
    "## Output Expectations",
)

REFERENCE_LINK_RE = re.compile(r"\]\((references/[^)]+\.md)\)")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def validate_skill(skill_file: Path, skills_index_text: str) -> list[str]:
    errors: list[str] = []
    text = read_text(skill_file)
    skill_dir = skill_file.parent
    rel = skill_file.as_posix()
    frontmatter = parse_frontmatter(text)

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")

    if not name:
        errors.append(f"{rel}: missing frontmatter `name`")
    elif name != skill_dir.name:
        errors.append(f"{rel}: frontmatter name `{name}` does not match directory `{skill_dir.name}`")

    if not description:
        errors.append(f"{rel}: missing frontmatter `description`")

    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"{rel}: missing `{section}`")

    refs_dir = skill_dir / "references"
    reference_files = sorted(refs_dir.glob("*.md")) if refs_dir.exists() else []
    if not reference_files:
        errors.append(f"{rel}: missing local `references/*.md` contract")

    for match in REFERENCE_LINK_RE.finditer(text):
        target = skill_dir / match.group(1)
        if not target.exists():
            errors.append(f"{rel}: broken reference link `{match.group(1)}`")

    if name and f"`{name}`" not in skills_index_text and f"**{name}**" not in skills_index_text:
        errors.append(f"{rel}: `{name}` is not discoverable in skills/SKILLS_INDEX.md")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate `.agents/skills` contracts.")
    parser.add_argument("--root", default=".", help="Project root containing `.agents/`.")
    parser.add_argument("--max-skill-lines", type=int, default=40, help="Maximum preferred line count for SKILL.md files.")
    parser.add_argument("--max-reference-lines", type=int, default=40, help="Maximum preferred line count for reference contracts.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    agents_root = resolve_agents_root(root)
    skills_root = agents_root / "skills"
    skills_index = skills_root / "SKILLS_INDEX.md"
    errors: list[str] = []

    if not skills_root.exists():
        errors.append(f"Missing skills directory: {skills_root}")
    if not skills_index.exists():
        errors.append(f"Missing skills index: {skills_index}")

    skills_index_text = read_text(skills_index) if skills_index.exists() else ""

    if skills_root.exists():
        for skill_file in sorted(skills_root.glob("*/SKILL.md")):
            errors.extend(validate_skill(skill_file, skills_index_text))

            line_count = len(read_text(skill_file).splitlines())
            if line_count > args.max_skill_lines:
                errors.append(f"{skill_file.as_posix()}: too long ({line_count} lines, max {args.max_skill_lines})")

            for ref_file in sorted((skill_file.parent / "references").glob("*.md")):
                ref_lines = len(read_text(ref_file).splitlines())
                if ref_lines > args.max_reference_lines:
                    errors.append(f"{ref_file.as_posix()}: too long ({ref_lines} lines, max {args.max_reference_lines})")

    if errors:
        print("SKILL CONTRACT VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    skill_count = len(list(skills_root.glob("*/SKILL.md"))) if skills_root.exists() else 0
    reference_count = len(list(skills_root.glob("*/references/*.md"))) if skills_root.exists() else 0
    print("SKILL CONTRACT VALIDATION PASSED")
    print(f"- skills: {skill_count}")
    print(f"- references: {reference_count}")
    print("- required sections: present")
    print("- reference links: valid")
    print("- skills index discoverability: present")


if __name__ == "__main__":
    main()
