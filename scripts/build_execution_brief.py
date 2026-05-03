#!/usr/bin/env python3
"""Build a distilled execution brief from a Marcus Fleet feature workspace."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SECTION_SPECS = {
    "spec.md": [
        "## 1. Purpose",
        "## 3. Functional Requirements",
        "## 5. Acceptance Criteria",
        "## 7. Constraints",
        "## 10. Review Loop",
    ],
    "plan.md": [
        "## 1. Technical Summary",
        "## 6. Agent Routing",
        "## 9. POC Slice and Review Cadence",
    ],
    "tasks.md": [
        "## Tasks",
        "## Execution Monitoring",
        "## Review Loop Tasks",
    ],
    "verification.md": [
        "## Verification Plan",
        "## Execution Gates",
        "## Review Rounds",
        "## Release Recommendation",
    ],
    "quickstart.md": [
        "## Local Preconditions",
        "## Validation Path",
        "## POC Rehearsal",
    ],
    "agent-routing.md": [
        "## Routing Contract",
        "## Review Topology",
        "## Escalation Rules",
    ],
}

TASK_SHAPE_RULES = {
    "ui-only": [
        "Read UI-specific docs, target components, and QA expectations first.",
        "Do not inspect Supabase, SQL, migrations, analytics, or infrastructure by default.",
        "Load frontend/design/QA skills only unless failing evidence proves wider scope.",
    ],
    "frontend-behavior": [
        "Read page, feature, hook, and browser-interaction artifacts first.",
        "Do not widen into data-contract or infrastructure context without failing evidence.",
        "Load frontend, technical lead, and QA skills unless the spec explicitly says otherwise.",
    ],
    "backend-api": [
        "Read contracts, data-model, affected service docs, and rollback notes first.",
        "Do not pull visual-design or animation context unless user-facing evidence requires it.",
        "Load backend/architecture/QA skills first.",
    ],
    "data-contract": [
        "Read contracts, schema/model docs, rollback notes, and affected modules first.",
        "Do not inspect unrelated page/component docs by default.",
        "Load data/architecture/security skills first.",
    ],
    "architecture-refactor": [
        "Read decisions, diagrams, affected modules, and execution boundaries first.",
        "Do not scan the full repo without a bounded module list.",
        "Load architecture/refactor skills first.",
    ],
    "general": [
        "Start from the active feature workspace and only expand context when the write scope demands it.",
        "Record any scope widening in verification evidence.",
        "Do not read broad repo areas just to feel safe.",
    ],
}

FORBIDDEN_DEFAULT_READS = {
    "ui-only": [
        "Supabase",
        "SQL",
        "migrations",
        "analytics",
        "cloud configs",
        "unrelated backend services",
    ],
    "frontend-behavior": [
        "schema and migration files",
        "analytics stacks",
        "cloud orchestration",
        "unrelated persistence layers",
    ],
    "backend-api": [
        "unrelated brand/theme docs",
        "visual polish docs",
        "animation-only assets",
    ],
    "data-contract": [
        "unrelated page/component docs",
        "visual design systems",
        "animation or branding-only assets",
    ],
    "architecture-refactor": [
        "full repo scans without a bounded module list",
        "random DB exploration unrelated to the refactor boundary",
        "random UI exploration unrelated to the refactor boundary",
    ],
    "general": [
        "broad repo areas not justified by the active write scope",
        "unrelated infrastructure surfaces",
        "unrelated analytics or database areas",
    ],
}

DEV_SECTION_MARKERS = [
    "## PM Notes",
    "## Code Scope",
    "## Write Scope",
    "## Verification",
    "## Handoff",
    "## Issues",
    "## Relationship Map",
]


def extract_sections(path: Path, headings: list[str]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    heading_to_index: dict[str, int] = {}
    for idx, line in enumerate(lines):
        if line.startswith("## "):
            heading_to_index[line.strip()] = idx

    extracted: dict[str, str] = {}
    for heading in headings:
        start = heading_to_index.get(heading)
        if start is None:
            extracted[heading] = f"{heading}\n\nMissing from {path.name}.\n"
            continue
        end = len(lines)
        for idx in range(start + 1, len(lines)):
            if re.match(r"^##\s+", lines[idx]):
                end = idx
                break
        extracted[heading] = "\n".join(lines[start:end]).strip() + "\n"
    return extracted


def first_heading_line(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.parent.name


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_changed_files(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def build_dynamic_signal_section(changed_files: list[str], failing_evidence: str) -> list[str]:
    lines = ["## 4.1 Dynamic Execution Signals", ""]
    lines.append("### Changed Files")
    lines.append("")
    if changed_files:
        lines.extend(f"- `{path}`" for path in changed_files)
    else:
        lines.append("- No changed files were provided for this brief rebuild.")
    lines.append("")
    lines.append("### Failing Evidence")
    lines.append("")
    if failing_evidence.strip():
        lines.append(f"- {failing_evidence.strip()}")
    else:
        lines.append("- No failing evidence was provided for this brief rebuild.")
    lines.append("")
    return lines


def summarize_dev_note(path: Path) -> str:
    text = load_text(path)
    lines = text.splitlines()
    title = first_heading_line(path)
    sections = extract_sections(path, DEV_SECTION_MARKERS)
    chosen: list[str] = [f"- Required read: `{path.as_posix()}`", f"  - Title: {title}"]
    for marker in ["## PM Notes", "## Code Scope", "## Write Scope", "## Verification", "## Handoff", "## Issues"]:
        body = sections.get(marker, "")
        if "Missing from" in body:
            continue
        snippet_lines = [line for line in body.splitlines()[1:] if line.strip()]
        if not snippet_lines:
            continue
        snippet = " ".join(snippet_lines[:3]).strip()
        chosen.append(f"  - {marker[3:]}: {snippet}")
    return "\n".join(chosen)


def find_relevant_development_docs(feature_dir: Path) -> list[Path]:
    root = feature_dir.parents[2]
    dev_root = root / "docs" / "development"
    if not dev_root.exists():
        return []

    feature_id = feature_dir.name
    feature_slug = feature_id.split("-", 1)[1] if "-" in feature_id else feature_id
    candidates: list[Path] = []

    manifest = dev_root / "development_manifest.json"
    if manifest.exists():
        try:
            manifest_data = json.loads(load_text(manifest))
        except json.JSONDecodeError:
            manifest_data = {}
        if str(manifest_data.get("feature_id", "")).strip() == feature_id:
            epics = manifest_data.get("epics", {})
            for _, meta in epics.items():
                rel = meta.get("path")
                if rel:
                    epic_dir = root / rel
                    if epic_dir.exists():
                        candidates.extend(sorted(epic_dir.rglob("*.md")))

    if not candidates:
        for path in sorted(dev_root.rglob("*.md")):
            rel = path.relative_to(dev_root).as_posix().lower()
            text = load_text(path).lower()
            if feature_id.lower() in text or feature_slug.lower() in rel or feature_slug.lower() in text:
                candidates.append(path)

    unique: list[Path] = []
    seen: set[Path] = set()
    for path in candidates:
        if path in seen:
            continue
        seen.add(path)
        unique.append(path)
    return unique


def build_brief(feature_dir: Path, task_shape: str, changed_files: list[str], failing_evidence: str) -> str:
    feature_title = first_heading_line(feature_dir / "spec.md")
    feature_id = feature_dir.name

    extracted: dict[str, dict[str, str]] = {}
    for filename, headings in SECTION_SPECS.items():
        extracted[filename] = extract_sections(feature_dir / filename, headings)

    rules = TASK_SHAPE_RULES.get(task_shape, TASK_SHAPE_RULES["general"])
    forbidden_reads = FORBIDDEN_DEFAULT_READS.get(task_shape, FORBIDDEN_DEFAULT_READS["general"])
    dev_docs = find_relevant_development_docs(feature_dir)
    required_reads = [
        "- Required read: `agents.md`",
        "- Required read: `.agents/memory/constitution.md`",
        f"- Required read: `.agents/specs/{feature_id}/execution-brief.md`",
        f"- Required read: `.agents/specs/{feature_id}/spec.md` only if the brief or failing evidence says deeper requirement context is needed.",
        f"- Required read: `.agents/specs/{feature_id}/plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, and `agent-routing.md` only when the current write scope or failing evidence requires the deeper artifact.",
    ]
    if dev_docs:
        required_reads.extend(f"- Required read: `{path.as_posix()}`" for path in dev_docs)
    else:
        required_reads.append("- Required read: create or reconcile the missing `docs/development/` notes before behavior-changing source edits.")
    if changed_files:
        required_reads.append("- Required read: start with the changed files listed under `## 4.1 Dynamic Execution Signals` before widening to adjacent artifacts.")
    dev_context = (
        "\n\n".join(summarize_dev_note(path) for path in dev_docs)
        if dev_docs
        else "\n".join(
            [
                "No `docs/development/` notes matched this feature workspace.",
                "Before behavior-changing code work, create or reconcile the development ledger for this feature slice.",
                "Preferred paths:",
                "- If the feature is new: run `python3 .agents/scripts/create_development_docs.py --name \"<epic-or-feature-name>\" --feature-id \"<feature-id>\" --epic-number 001 --child-number 001 --task-number 001`.",
                "- If the project is brownfield or docs are stale: route to `/doc_reconcile` and repair the ledger before source edits.",
            ]
        )
    )

    return "\n".join(
        [
            f"# Execution Brief: {feature_title}",
            "",
            f"> Feature ID: `{feature_id}`",
            f"> Task Shape: `{task_shape}`",
            "> Generated From: `spec.md`, `plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, `agent-routing.md`",
            "",
            "## 1. Operator Intent Snapshot",
            "",
            extracted["spec.md"]["## 1. Purpose"],
            "",
            "## 2. Required Behavior",
            "",
            extracted["spec.md"]["## 3. Functional Requirements"],
            "",
            extracted["spec.md"]["## 5. Acceptance Criteria"],
            "",
            "## 3. Scope Boundaries",
            "",
            extracted["spec.md"]["## 7. Constraints"],
            "",
            "## 4. Active Work Slice",
            "",
            extracted["plan.md"]["## 1. Technical Summary"],
            "",
            extracted["plan.md"]["## 6. Agent Routing"],
            "",
            extracted["tasks.md"]["## Tasks"],
            "",
            *build_dynamic_signal_section(changed_files, failing_evidence),
            extracted["tasks.md"]["## Execution Monitoring"],
            "",
            "## 5. Development Ledger Context",
            "",
            "Read these development-ledger notes before source edits for the active slice:",
            "",
            dev_context,
            "",
            "## 6. Verification Path",
            "",
            extracted["verification.md"]["## Verification Plan"],
            "",
            extracted["verification.md"]["## Execution Gates"],
            "",
            extracted["quickstart.md"]["## Local Preconditions"],
            "",
            extracted["quickstart.md"]["## Validation Path"],
            "",
            extracted["quickstart.md"]["## POC Rehearsal"],
            "",
            "## 7. Review and Release Signals",
            "",
            extracted["spec.md"]["## 10. Review Loop"],
            "",
            extracted["tasks.md"]["## Review Loop Tasks"],
            "",
            extracted["verification.md"]["## Review Rounds"],
            "",
            extracted["verification.md"]["## Release Recommendation"],
            "",
            "## 8. Context Expansion Rules",
            "",
            "### Task Shape Decision",
            "",
            f"- Selected task shape: `{task_shape}`",
            f"- Why this shape: {rules[0]}",
            "",
            "### Required Reads",
            "",
            *required_reads,
            "",
            "### Forbidden Default Reads",
            "",
            *[f"- Forbidden by default: {item}" for item in forbidden_reads],
            "",
            "### Expansion Triggers",
            "",
            *[f"- {rule}" for rule in rules],
            "- Read the `docs/development/` notes listed in this brief before widening beyond the current work slice.",
            "- If the required epic/feature/module/page/task note is missing, stop and reconcile the development ledger instead of improvising from code alone.",
            "",
            extracted["agent-routing.md"]["## Review Topology"],
            "",
            extracted["agent-routing.md"]["## Escalation Rules"],
        ]
    ).strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build execution brief for a feature workspace.")
    parser.add_argument("--feature", required=True, help="Feature directory path.")
    parser.add_argument(
        "--task-shape",
        default="general",
        choices=sorted(TASK_SHAPE_RULES.keys()),
        help="Execution task shape to bias context expansion rules.",
    )
    parser.add_argument("--changed-files", default="", help="Comma-separated changed files to foreground in the brief.")
    parser.add_argument("--failing-evidence", default="", help="Optional bounded failing-evidence summary to foreground in the brief.")
    args = parser.parse_args()

    feature_dir = Path(args.feature)
    if not feature_dir.is_absolute():
        feature_dir = (Path.cwd() / feature_dir).resolve()

    output = build_brief(
        feature_dir,
        args.task_shape,
        parse_changed_files(args.changed_files),
        args.failing_evidence,
    )
    target = feature_dir / "execution-brief.md"
    target.write_text(output, encoding="utf-8")
    print(target)


if __name__ == "__main__":
    main()
