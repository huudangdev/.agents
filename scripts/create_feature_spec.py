#!/usr/bin/env python3
"""Create a Marcus Fleet feature-spec workspace from templates."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


AGENTS_DIR = Path(__file__).resolve().parents[1]
SPECS_DIR = AGENTS_DIR / "specs"
TEMPLATES_DIR = AGENTS_DIR / "templates"

TEMPLATE_MAP = {
    "spec-template.md": "spec.md",
    "plan-template.md": "plan.md",
    "tasks-template.md": "tasks.md",
    "verification-template.md": "verification.md",
    "execution-brief-template.md": "execution-brief.md",
    "agent-routing-template.md": "agent-routing.md",
    "research-template.md": "research.md",
    "data-model-template.md": "data-model.md",
    "quickstart-template.md": "quickstart.md",
}


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower())
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "feature"


def next_feature_number() -> int:
    SPECS_DIR.mkdir(parents=True, exist_ok=True)
    numbers: list[int] = []
    for path in SPECS_DIR.iterdir():
        if not path.is_dir():
            continue
        match = re.match(r"^(\d+)-", path.name)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers, default=0) + 1


def render_template(template: str, replacements: dict[str, str]) -> str:
    output = template
    for key, value in replacements.items():
        output = output.replace("{{" + key + "}}", value)
    return output


def create_feature(title: str, prompt: str, force: bool = False) -> Path:
    feature_id = f"{next_feature_number():03d}-{slugify(title)}"
    feature_dir = SPECS_DIR / feature_id
    if feature_dir.exists() and not force:
        raise SystemExit(f"Feature directory already exists: {feature_dir}")

    feature_dir.mkdir(parents=True, exist_ok=True)
    (feature_dir / "contracts").mkdir(exist_ok=True)
    (feature_dir / "implementation-details").mkdir(exist_ok=True)

    replacements = {
        "FEATURE_ID": feature_id,
        "FEATURE_TITLE": title,
        "CREATED_DATE": date.today().isoformat(),
        "SOURCE_PROMPT": prompt,
    }

    for template_name, target_name in TEMPLATE_MAP.items():
        template_path = TEMPLATES_DIR / template_name
        target_path = feature_dir / target_name
        if target_path.exists() and not force:
            continue
        rendered = render_template(template_path.read_text(encoding="utf-8"), replacements)
        target_path.write_text(rendered, encoding="utf-8")

    readme = feature_dir / "README.md"
    if force or not readme.exists():
        readme.write_text(
            "\n".join(
                [
                    f"# {title}",
                    "",
                    f"Feature ID: `{feature_id}`",
                    "",
                    "Recommended order:",
                    "",
                    "1. Resolve `spec.md` clarifications.",
                    "2. Complete `research.md`, `data-model.md`, and `contracts/`.",
                    "3. Complete `plan.md` constitution gates.",
                    "4. Derive `tasks.md` ownership and parallel groups.",
                    "5. Build `execution-brief.md` from the package before `/develop`.",
                    "6. Implement tasks and record evidence in `verification.md`.",
                    "7. Do not begin execution until:",
                    f"   - `python3 .agents/scripts/validate_specs.py --feature .agents/specs/{feature_id}` passes",
                    f"   - `python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/{feature_id}` passes",
                    "",
                ]
            ),
            encoding="utf-8",
        )

    return feature_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a Marcus Fleet feature spec.")
    parser.add_argument("title", help="Feature title, e.g. 'Harden TrustGraph Config'")
    parser.add_argument(
        "--prompt",
        default="Created from local Marcus Fleet CLI.",
        help="Original operator prompt or context summary.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing generated files.")
    args = parser.parse_args()

    feature_dir = create_feature(args.title, args.prompt, args.force)
    print(feature_dir.relative_to(AGENTS_DIR.parent))


if __name__ == "__main__":
    main()
