#!/usr/bin/env python3
"""Validate Marcus Fleet spec-driven development gates."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


AGENTS_DIR = Path(__file__).resolve().parents[1]
SPECS_DIR = AGENTS_DIR / "specs"
CONSTITUTION = AGENTS_DIR / "memory" / "constitution.md"
REQUIRED_FILES = [
    "spec.md",
    "plan.md",
    "tasks.md",
    "verification.md",
    "agent-routing.md",
    "research.md",
    "data-model.md",
    "quickstart.md",
]

PLACEHOLDER_PATTERNS = [
    r"<role>",
    r"<capability>",
    r"<outcome>",
    r"<feature title>",
    r"<operator prompt>",
    r"\bTBD\b",
    r"\bpending\b",
    r"Describe the ",
    r"State the ",
    r"List files under ",
    r"Summarize ",
    r"Use this section only",
]

SPEC_REQUIRED_SECTIONS = [
    "## 1. Purpose",
    "## 2. User Stories",
    "## 3. Functional Requirements",
    "## 4. Non-Functional Requirements",
    "## 5. Acceptance Criteria",
    "## 6. Clarifications",
    "## 7. Constraints",
    "## 8. Risks",
    "## 9. Traceability",
    "## 10. Review Loop",
]

PLAN_REQUIRED_SECTIONS = [
    "## 1. Technical Summary",
    "## 2. Constitution Gates",
    "## 3. Architecture",
    "## 4. Contracts",
    "## 5. Data Model",
    "## 6. Agent Routing",
    "## 7. Migration and Rollback",
    "## 8. Complexity Tracking",
    "## 9. POC Slice and Review Cadence",
]

TASKS_REQUIRED_MARKERS = [
    "Owner:",
    "Write Scope:",
    "Verification:",
    "Docs:",
    "Sync:",
]

VERIFICATION_REQUIRED_SECTIONS = [
    "## Verification Plan",
    "## Execution Gates",
    "## Evidence",
    "## Review Rounds",
    "## Release Recommendation",
    "## Residual Risk",
]


def find_placeholder(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
            errors.append(f"{path}: contains placeholder or unfinished text matching `{pattern}`")
    return errors


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w/-]+\b", text))


def find_features(target: str | None) -> list[Path]:
    if target:
        path = Path(target)
        if not path.is_absolute():
            path = (Path.cwd() / path).resolve()
        return [path]

    if not SPECS_DIR.exists():
        return []
    return sorted(path for path in SPECS_DIR.iterdir() if path.is_dir())


def validate_feature(feature_dir: Path, allow_clarifications: bool) -> list[str]:
    errors: list[str] = []
    if not re.match(r"^\d{3,}-[a-z0-9-]+$", feature_dir.name):
        errors.append(f"{feature_dir}: feature directory must match NNN-slug")

    for filename in REQUIRED_FILES:
        path = feature_dir / filename
        if not path.exists():
            errors.append(f"{feature_dir}: missing {filename}")
        elif not path.read_text(encoding="utf-8").strip():
            errors.append(f"{feature_dir}: empty {filename}")

    contracts_dir = feature_dir / "contracts"
    if not contracts_dir.exists() or not contracts_dir.is_dir():
        errors.append(f"{feature_dir}: missing contracts/ directory")

    spec_path = feature_dir / "spec.md"
    spec = ""
    if spec_path.exists():
        spec = spec_path.read_text(encoding="utf-8")
        errors.extend(find_placeholder(spec_path, spec))
        if "[NEEDS CLARIFICATION:" in spec and not allow_clarifications:
            errors.append(f"{feature_dir}: unresolved [NEEDS CLARIFICATION] marker")
        for section in SPEC_REQUIRED_SECTIONS:
            if section not in spec:
                errors.append(f"{feature_dir}: spec.md missing section {section}")
        if spec.count("`FR-") < 3:
            errors.append(f"{feature_dir}: spec.md should define at least 3 functional requirements")
        if spec.count("`AC-") < 3:
            errors.append(f"{feature_dir}: spec.md should define at least 3 acceptance criteria")
        if "Out of scope" not in spec and "out of scope" not in spec.lower():
            errors.append(f"{feature_dir}: spec.md should explicitly state out-of-scope boundaries")
        if word_count(spec) < 250:
            errors.append(f"{feature_dir}: spec.md is too shallow; expected at least 250 words")

    plan_path = feature_dir / "plan.md"
    plan = ""
    if plan_path.exists():
        plan = plan_path.read_text(encoding="utf-8")
        errors.extend(find_placeholder(plan_path, plan))
        if "## 2. Constitution Gates" not in plan:
            errors.append(f"{feature_dir}: plan.md missing Constitution Gates")
        for section in PLAN_REQUIRED_SECTIONS:
            if section not in plan:
                errors.append(f"{feature_dir}: plan.md missing section {section}")
        if plan.count("- [ ]") > 7:
            errors.append(f"{feature_dir}: plan.md still contains too many unchecked gate placeholders")
        if "```mermaid" not in plan:
            errors.append(f"{feature_dir}: plan.md missing Mermaid architecture diagram")
        if word_count(plan) < 250:
            errors.append(f"{feature_dir}: plan.md is too shallow; expected at least 250 words")

    tasks_path = feature_dir / "tasks.md"
    tasks = ""
    if tasks_path.exists():
        tasks = tasks_path.read_text(encoding="utf-8")
        errors.extend(find_placeholder(tasks_path, tasks))
        for marker in TASKS_REQUIRED_MARKERS:
            if marker not in tasks:
                errors.append(f"{feature_dir}: tasks.md must include `{marker}` markers")
        if "## Parallel Groups" not in tasks:
            errors.append(f"{feature_dir}: tasks.md missing Parallel Groups section")
        if "## Execution Monitoring" not in tasks:
            errors.append(f"{feature_dir}: tasks.md missing Execution Monitoring section")
        if len(re.findall(r"- \[[ xX]\] `T\d{3}`", tasks)) < 4:
            errors.append(f"{feature_dir}: tasks.md should define at least 4 concrete tasks")
        if word_count(tasks) < 220:
            errors.append(f"{feature_dir}: tasks.md is too shallow; expected at least 220 words")

    verification_path = feature_dir / "verification.md"
    verification = ""
    if verification_path.exists():
        verification = verification_path.read_text(encoding="utf-8")
        errors.extend(find_placeholder(verification_path, verification))
        for section in VERIFICATION_REQUIRED_SECTIONS:
            if section not in verification:
                errors.append(f"{feature_dir}: verification.md missing section {section}")
        if "Command or Procedure" not in verification:
            errors.append(f"{feature_dir}: verification.md must define command or procedure evidence")
        if "Residual Risk" not in verification:
            errors.append(f"{feature_dir}: verification.md must record residual risk explicitly")
        if word_count(verification) < 180:
            errors.append(f"{feature_dir}: verification.md is too shallow; expected at least 180 words")

    quickstart_path = feature_dir / "quickstart.md"
    if quickstart_path.exists():
        quickstart = quickstart_path.read_text(encoding="utf-8")
        errors.extend(find_placeholder(quickstart_path, quickstart))
        for marker in [
            "## Local Preconditions",
            "## Validation Path",
            "## Expected Artifacts",
            "## POC Rehearsal",
            "## Rollback Check",
        ]:
            if marker not in quickstart:
                errors.append(f"{feature_dir}: quickstart.md missing section {marker}")

    agent_routing_path = feature_dir / "agent-routing.md"
    if agent_routing_path.exists():
        agent_routing = agent_routing_path.read_text(encoding="utf-8")
        errors.extend(find_placeholder(agent_routing_path, agent_routing))
        for marker in ["Write Scope", "Output", "Handoff Rules", "Review Topology", "Escalation Rules"]:
            if marker not in agent_routing:
                errors.append(f"{feature_dir}: agent-routing.md missing routing marker `{marker}`")

    current_contract = any(
        marker in text
        for marker, text in [
            ("## 10. Review Loop", spec),
            ("## 9. POC Slice and Review Cadence", plan),
            ("## Review Loop Tasks", tasks),
            ("## Review Rounds", verification),
        ]
    )

    if current_contract:
        if spec.count("`R") < 3:
            errors.append(f"{feature_dir}: spec.md should define at least 3 review loop rounds")
        for marker in ["POC slice boundary:", "Success evidence for the slice:", "Stop conditions:", "Proceed conditions:"]:
            if marker not in plan:
                errors.append(f"{feature_dir}: plan.md missing POC review marker `{marker}`")
        if "## Review Loop Tasks" not in tasks:
            errors.append(f"{feature_dir}: tasks.md missing Review Loop Tasks section")
        if "Recommendation:" not in verification:
            errors.append(f"{feature_dir}: verification.md must include a release recommendation")

        execution_brief_path = feature_dir / "execution-brief.md"
        if not execution_brief_path.exists():
            errors.append(f"{feature_dir}: missing execution-brief.md for current-contract feature")
        else:
            execution_brief = execution_brief_path.read_text(encoding="utf-8")
            errors.extend(find_placeholder(execution_brief_path, execution_brief))
        for marker in [
            "## 1. Operator Intent Snapshot",
            "## 2. Required Behavior",
            "## 3. Scope Boundaries",
            "## 4. Active Work Slice",
            "## 5. Development Ledger Context",
            "## 6. Verification Path",
            "## 7. Review and Release Signals",
            "## 8. Context Expansion Rules",
            "### Task Shape Decision",
            "### Required Reads",
            "### Forbidden Default Reads",
            "### Expansion Triggers",
        ]:
            if marker not in execution_brief:
                errors.append(f"{feature_dir}: execution-brief.md missing section {marker}")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Marcus Fleet feature specs.")
    parser.add_argument("--feature", help="Path to a single feature directory.")
    parser.add_argument(
        "--allow-clarifications",
        action="store_true",
        help="Allow unresolved [NEEDS CLARIFICATION] markers for draft specs.",
    )
    args = parser.parse_args()

    errors: list[str] = []
    if not CONSTITUTION.exists():
        errors.append(f"Missing constitution: {CONSTITUTION}")

    features = find_features(args.feature)
    if not features:
        errors.append(f"No feature specs found under {SPECS_DIR}")

    for feature_dir in features:
        errors.extend(validate_feature(feature_dir, args.allow_clarifications))

    if errors:
        print("SPEC VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print(f"SPEC VALIDATION PASSED: {len(features)} feature(s)")


if __name__ == "__main__":
    main()
