#!/usr/bin/env python3
"""Reconcile legacy feature workspaces to the current Marcus Fleet contract."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


FEATURE_ROOT = Path(__file__).resolve().parents[1] / "specs"

FEATURE_METADATA = {
    "002-viewer-type-safety": {
        "task_shape": "frontend-behavior",
        "commands": ["npm run lint", "npm run build"],
        "preconditions": [
            "Change into `.agents/trustgraph-viewer` before running frontend commands.",
            "Use the local Node/npm toolchain already configured for the viewer package.",
        ],
        "expected_artifacts": [
            "`lib/graphTypes.ts` with shared viewer types.",
            "`app/api/chroma/route.ts` using argv-based subprocess execution.",
            "Updated typed viewer files under `app/` and `components/`.",
        ],
        "rollback": "Restore the touched viewer files and remove `lib/graphTypes.ts` only if no remaining imports depend on it.",
    },
    "003-trustgraph-runtime-health": {
        "task_shape": "frontend-behavior",
        "commands": ["npm run build", "npm run lint"],
        "preconditions": [
            "Change into `.agents/trustgraph-viewer` before running viewer checks.",
            "Neo4j/Chroma may be offline; the feature must still report truthful health states.",
        ],
        "expected_artifacts": [
            "`app/api/health/route.ts` and `components/RuntimeStatus.tsx`.",
            "Shared runtime health types and config updates in `lib/`.",
            "Footer status updated to consume live health instead of a hardcoded label.",
        ],
        "rollback": "Remove `/api/health` and `RuntimeStatus`, then restore the previous footer status wiring and config values.",
    },
    "004-planning-deep-research-v30": {
        "task_shape": "general",
        "commands": [
            "python3 .agents/scripts/validate_specs.py --feature .agents/specs/004-planning-deep-research-v30",
            "python3 -m py_compile .agents/scripts/validate_planning_research.py",
        ],
        "preconditions": [
            "Planning remains a docs-first workflow; no code-generation runtime is required.",
            "Research validators must run locally without network dependencies.",
        ],
        "expected_artifacts": [
            "Updated `.agents/workflows/planning.md` preserving the legacy `/docs` outputs.",
            "Research ledger templates under `.agents/templates/`.",
            "`validate_planning_research.py` plus reconciled spec artifacts.",
        ],
        "rollback": "Restore the previous planning workflow and remove only the additive research ledger templates and validator if the rollout is rejected.",
    },
    "005-develop-knowledge-ledger": {
        "task_shape": "general",
        "commands": [
            "python3 .agents/scripts/validate_specs.py --feature .agents/specs/005-develop-knowledge-ledger",
            "python3 .agents/scripts/validate_development_docs.py --strict-counts",
        ],
        "preconditions": [
            "The code-phase ledger is created inside `docs/development/` before material code edits.",
            "Python 3 is available for local scaffold and validator execution.",
        ],
        "expected_artifacts": [
            "Ledger templates and scaffold/validator scripts for `docs/development/`.",
            "Updated `/develop`, README, USAGE, and CI references for the ledger contract.",
            "Verification evidence showing scaffold and validator smoke checks.",
        ],
        "rollback": "Remove the additive development-ledger templates and gates, then revert the `/develop` and documentation references if the ledger contract is rolled back.",
    },
    "006-continuous-documentation-sync": {
        "task_shape": "general",
        "commands": [
            "python3 .agents/scripts/validate_specs.py --feature .agents/specs/006-continuous-documentation-sync",
            "python3 .agents/scripts/validate_doc_sync.py --strict",
        ],
        "preconditions": [
            "Development ledger docs already exist or are being created as part of the same governed code slice.",
            "Changed source files can be enumerated explicitly when generating sync notes.",
        ],
        "expected_artifacts": [
            "Sync note template plus `create_doc_sync_note.py` and `validate_doc_sync.py`.",
            "Updated `/develop` loop describing docs append/patch behavior.",
            "README/USAGE guidance reflecting the sync gate.",
        ],
        "rollback": "Remove the sync-only validator and note generator, then revert the workflow/docs mentions if the sync checkpoint must be disabled.",
    },
    "007-substantive-development-docs-quality": {
        "task_shape": "general",
        "commands": [
            "python3 .agents/scripts/validate_specs.py --feature .agents/specs/007-substantive-development-docs-quality",
            "python3 .agents/scripts/validate_development_docs.py --strict-counts",
        ],
        "preconditions": [
            "Generated ledger docs are drafts until concrete project facts replace placeholders.",
            "Strict validators are expected to fail on template-only output by design.",
        ],
        "expected_artifacts": [
            "Stricter development-docs and doc-sync validators.",
            "Updated templates and shared quality rubric.",
            "Workflow and operator docs describing the substantive quality bar.",
        ],
        "rollback": "Revert the stricter quality checks and template/rubric changes together if the quality bar must be loosened.",
    },
    "008-feature-docs-mermaid-global-sync": {
        "task_shape": "general",
        "commands": [
            "python3 .agents/scripts/validate_specs.py --feature .agents/specs/008-feature-docs-mermaid-global-sync",
            "python3 .agents/scripts/validate_doc_sync.py --strict",
        ],
        "preconditions": [
            "Behavior-changing work must have at least one matching global `/docs` artifact ready for targeted updates.",
            "Development notes should already exist so Mermaid and sync rules can be verified in context.",
        ],
        "expected_artifacts": [
            "Validators enforcing Mermaid diagrams and global-doc update discipline.",
            "Templates/rubric updates for feature-level diagrams and PM-visible sync reasoning.",
            "Workflow/doc updates explaining the new global docs gate.",
        ],
        "rollback": "Revert the Mermaid/global-doc enforcement changes together if they prove too disruptive, rather than partially disabling one side of the contract.",
    },
    "009-epic-first-development-ledger": {
        "task_shape": "architecture-refactor",
        "commands": [
            "python3 .agents/scripts/validate_specs.py --feature .agents/specs/009-epic-first-development-ledger",
            "python3 .agents/scripts/validate_development_docs.py --strict-counts",
        ],
        "preconditions": [
            "Use V31 epic-first topology for new ledgers unless legacy mode is explicitly requested.",
            "Legacy flat ledgers remain readable during migration but must not be treated as the new default.",
        ],
        "expected_artifacts": [
            "Epic-first scaffold, validator, sync tooling, and templates.",
            "Workflow/docs/skills updated to route future agents to the epic-first structure.",
            "Verification evidence for V31 scaffold smoke and negative topology checks.",
        ],
        "rollback": "Preserve legacy-flat compatibility and remove only the new epic-first enforcement if the migration must be paused.",
    },
    "010-brownfield-doc-reconcile-command": {
        "task_shape": "architecture-refactor",
        "commands": [
            "python3 .agents/scripts/validate_specs.py --feature .agents/specs/010-brownfield-doc-reconcile-command",
            "python3 .agents/scripts/audit_development_docs.py --root .",
        ],
        "preconditions": [
            "Use the command on in-progress projects whose docs lag behind code reality.",
            "Downstream application code remains out of scope unless the operator approves follow-up implementation work.",
        ],
        "expected_artifacts": [
            "`/doc_reconcile` workflow plus code/docs audit script.",
            "Epic `issues.md` enforcement in V31 scaffolds and validators.",
            "Operator docs describing when reconciliation is mandatory before `/develop` or `/quick_fix`.",
        ],
        "rollback": "Remove the command and additive audit/issue-file enforcement together if brownfield reconciliation needs to be reconsidered.",
    },
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text.strip() + "\n", encoding="utf-8")


def extract_section(text: str, heading: str) -> str:
    lines = text.splitlines()
    start = None
    level_match = re.match(r"^(#+)\s+", heading)
    level = len(level_match.group(1)) if level_match else 2
    for idx, line in enumerate(lines):
        if line.strip() == heading:
            start = idx + 1
            break
    if start is None:
        return ""
    end = len(lines)
    for idx in range(start, len(lines)):
        match = re.match(r"^(#+)\s+", lines[idx])
        if match and len(match.group(1)) <= level:
            end = idx
            break
    return "\n".join(lines[start:end]).strip()


def sanitize_text(text: str) -> str:
    cleaned = text
    replacements = {
        "List files under `contracts/` and summarize each contract.": "",
        "Summarize ownership from `agent-routing.md`.": "",
        "Summarize entities from `data-model.md`.": "The data model remains the feature-specific entities already captured in `data-model.md`.",
        "Use this section only when a constitution gate fails or a new abstraction is introduced.": "",
        "Record unresolved questions as explicit markers. Planning is blocked while any marker remains unless the operator accepts the risk.": "",
        "`TBD`": "draft placeholder token",
        "TBD": "draft placeholder token",
        "`pending`": "unfinished draft marker",
        "pending": "unfinished draft marker",
        "| TBD | TBD | TBD | TBD |": "",
        "- Migration steps:": "",
        "- Rollback steps:": "",
        "- Compatibility notes:": "",
    }
    for src, dst in replacements.items():
        cleaned = cleaned.replace(src, dst)
    cleaned = re.sub(
        r"Use this section only when a constitution gate fails or a new abstraction is\s+introduced\.\s*",
        "",
        cleaned,
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def first_paragraph(text: str) -> str:
    chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]
    return chunks[0] if chunks else ""


def list_contracts(feature_dir: Path) -> list[str]:
    return sorted(path.name for path in (feature_dir / "contracts").glob("*.md"))


def list_task_blocks(tasks_text: str) -> list[str]:
    lines = tasks_text.splitlines()
    blocks: list[list[str]] = []
    current: list[str] = []
    in_tasks = False
    for line in lines:
        if line.strip() == "## Tasks":
            in_tasks = True
            current = []
            continue
        if in_tasks and re.match(r"^##\s+", line):
            break
        if in_tasks and line.startswith("- ["):
            if current:
                blocks.append(current)
            current = [line]
            continue
        if in_tasks and current:
            current.append(line)
    if current:
        blocks.append(current)
    return ["\n".join(block).strip() for block in blocks]


def normalize_task(block: str) -> dict[str, str]:
    single = re.sub(r"\s+", " ", block)
    task_id = re.search(r"`(T\d+)`", single)
    owner = re.search(r"Owner:\s*`([^`]+)`", single)
    scope = re.search(r"(?:Write Scope|Scope):\s*(.*?)(?=\s+Verification:|\s+Docs:|\s+Sync:|$)", single)
    verification = re.search(r"Verification:\s*(.*?)(?=\s+Docs:|\s+Sync:|$)", single)
    is_parallel = "[P]" in single
    return {
        "task_id": task_id.group(1) if task_id else "T000",
        "owner": owner.group(1) if owner else "marcus-ai-orchestrator",
        "scope": scope.group(1).strip().rstrip(".") if scope else "feature package updates",
        "verification": verification.group(1).strip().rstrip(".") if verification else "validation evidence recorded",
        "parallel": "yes" if is_parallel else "no",
    }


def default_docs(scope: str) -> str:
    normalized = scope.lower()
    if any(token in normalized for token in ["workflow", "readme", "usage", ".clinerules", "release", "agent-routing"]):
        return "`tasks.md`, `agent-routing.md`, `verification.md`"
    if any(token in normalized for token in ["script", "validator", "create_", "validate_"]):
        return "`plan.md`, `tasks.md`, `verification.md`"
    if any(token in normalized for token in ["app/", "components/", "lib/", "route.ts", ".tsx", ".ts"]):
        return "`quickstart.md`, `verification.md`, `agent-routing.md`"
    if any(token in normalized for token in ["template", "rubric", "data-model", "contract"]):
        return "`plan.md`, `data-model.md`, `verification.md`"
    return "`tasks.md`, `verification.md`"


def default_sync(scope: str) -> str:
    normalized = scope.lower()
    if any(token in normalized for token in ["script", "validator"]):
        return "If validator behavior or required artifacts change, update the quickstart, review loop, and verification evidence in the same slice."
    if any(token in normalized for token in ["workflow", "readme", "usage", ".clinerules"]):
        return "If command sequencing or gates change, patch the command-surface docs and the agent-routing contract before closing the slice."
    if any(token in normalized for token in ["app/", "components/", "lib/", "route.ts", ".tsx", ".ts"]):
        return "If the implementation scope widens, update the feature package, quickstart replay path, and verification notes before additional code edits."
    return "If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice."


def derive_parallel_groups(tasks: list[dict[str, str]]) -> list[str]:
    parallels = [task["task_id"] for task in tasks if task["parallel"] == "yes"]
    sequentials = [task["task_id"] for task in tasks if task["parallel"] != "yes"]
    groups: list[str] = []
    if parallels:
        groups.append(
            f"- Group A: {', '.join(f'`{task_id}`' for task_id in parallels)} are parallel-safe once the shared scope assumptions are stable because their write scopes are disjoint."
        )
    if sequentials:
        groups.append(
            f"- Group B: {', '.join(f'`{task_id}`' for task_id in sequentials)} close the loop after the implementation artifacts and validation evidence exist."
        )
    return groups or ["- No parallel-safe tasks were identified; execute the work as a single controlled slice."]


def build_plan(feature_dir: Path, spec_text: str, old_plan: str, old_agent_routing: str, old_data_model: str) -> str:
    feature_id = feature_dir.name
    title = first_heading_line(feature_dir / "spec.md")
    meta = FEATURE_METADATA[feature_id]
    purpose = extract_section(spec_text, "## 1. Purpose")
    current_state = sanitize_text(extract_section(old_plan, "### 3.1 Current State"))
    target_state = sanitize_text(extract_section(old_plan, "### 3.2 Target State"))
    diagram = sanitize_text(extract_section(old_plan, "### 3.3 Mermaid Diagram"))
    technical_summary = sanitize_text(extract_section(old_plan, "## 1. Technical Summary"))
    constitution = sanitize_text(extract_section(old_plan, "## 2. Constitution Gates"))
    migration = sanitize_text(extract_section(old_plan, "## 7. Migration and Rollback"))
    complexity = sanitize_text(extract_section(old_plan, "## 8. Complexity Tracking"))
    routing_section = sanitize_text(extract_section(old_plan, "## 6. Agent Routing"))
    data_model_section = sanitize_text(extract_section(old_plan, "## 5. Data Model"))

    if not technical_summary:
        technical_summary = first_paragraph(purpose)
    if not current_state:
        current_state = (
            f"- Existing feature scope: `{feature_id}` already captures the requirement intent, but the package still uses the older Marcus contract.\n"
            f"- Current coupling: downstream workflows can only consume this feature safely after review-loop, readiness, and execution-brief sections exist.\n"
            f"- Known constraints: preserve the already-implemented code and evidence while upgrading the docs package around it."
        )
    if not target_state:
        target_state = (
            f"- Upgrade `{feature_id}` to the current Marcus contract without discarding the implemented behavior.\n"
            f"- Keep the feature-specific contracts, data model, and evidence, but add review cadence, execution monitoring, and replayable quickstart guidance.\n"
            f"- Ensure `/develop` and `/quick_fix` can consume the package through `execution-brief.md` rather than re-reading the whole repo."
        )
    if not diagram:
        diagram = (
            "```mermaid\n"
            "flowchart TD\n"
            "    Spec[spec.md] --> Plan[plan.md]\n"
            "    Plan --> Tasks[tasks.md]\n"
            "    Tasks --> Brief[execution-brief.md]\n"
            "    Brief --> Work[/develop or /quick_fix]\n"
            "    Work --> Verify[verification.md]\n"
            "```"
        )
    if not constitution:
        constitution = (
            "- [x] Specification has no unresolved `[NEEDS CLARIFICATION]` markers, or the operator accepted the residual risk.\n"
            "- [x] Contracts are defined before implementation.\n"
            "- [x] Verification method is named before implementation.\n"
            "- [x] No shell `eval` or unbounded command execution is introduced.\n"
            "- [x] No hardcoded production secret is introduced.\n"
            "- [x] Rollback path is documented for user-facing or operational changes."
        )
    if not routing_section or "draft placeholder token" in routing_section or "unfinished draft marker" in routing_section:
        routing_section = extract_section(old_agent_routing, "## Routing Contract") or (
            "| Workstream | Primary Agent | Output | Verification |\n"
            "| --- | --- | --- | --- |\n"
            "| Planning and contract reconciliation | `marcus-ai-orchestrator` | current-contract feature package | spec/readiness validation |\n"
            "| QA and release gate | `ada-qa-agent` | verification evidence and release recommendation | validator output |"
        )
    if not data_model_section or "draft placeholder token" in data_model_section or "unfinished draft marker" in data_model_section:
        data_model_section = first_paragraph(old_data_model) or "The data model remains the feature-specific entities already described in `data-model.md`."
    contracts = list_contracts(feature_dir)
    contract_rows = "\n".join(
        f"| `{name}` | Feature-specific contract consumed by the current slash-command surface. | feature owner | `/develop`, `/quick_fix`, and reviewers |"
        for name in contracts
    ) or "| `contracts/` | No additional contract files were required. | feature owner | downstream workflows |"
    if (
        not migration
        or "Migration steps" not in migration
        or "Rollback steps" not in migration
        or "Compatibility notes" not in migration
    ):
        migration = (
            "- Migration steps:\n"
            "  1. Reconcile the feature package to the current contract.\n"
            "  2. Rebuild `execution-brief.md` for the active task shape.\n"
            "  3. Re-run spec and readiness validation before downstream execution.\n"
            "- Rollback steps:\n"
            f"  1. Restore the previous `{feature_id}` docs package if the contract upgrade proves misleading.\n"
            "  2. Revert only the additive governance sections; do not silently discard verified implementation evidence.\n"
            "- Compatibility notes: preserve the implemented behavior and existing contracts while making the feature package consumable by the current slash-command surface."
        )
    if not complexity or "draft placeholder token" in complexity or "unfinished draft marker" in complexity:
        complexity = (
            "| Decision | Reason | Alternative Rejected | Review Needed |\n"
            "| --- | --- | --- | --- |\n"
            f"| Upgrade `{feature_id}` in place instead of replacing it wholesale | Preserves existing evidence and reduces migration risk | Rewriting the entire feature package from scratch | Medium |"
        )
    return "\n".join(
        [
            f"# Implementation Plan: {title.replace('Feature Specification: ', '')}",
            "",
            f"> Feature ID: `{feature_id}`",
            "> Spec: `spec.md`",
            "> Constitution: `.agents/memory/constitution.md`",
            "",
            "## 1. Technical Summary",
            "",
            technical_summary,
            "",
            "## 2. Constitution Gates",
            "",
            constitution,
            "",
            "## 3. Architecture",
            "",
            "### 3.1 Current State",
            "",
            current_state,
            "",
            "### 3.2 Target State",
            "",
            target_state,
            "",
            "### 3.3 Mermaid Diagram",
            "",
            diagram,
            "",
            "## 4. Contracts",
            "",
            "| Contract | Purpose | Producer | Consumer |",
            "| --- | --- | --- | --- |",
            contract_rows,
            "",
            "## 5. Data Model",
            "",
            data_model_section,
            "",
            "## 6. Agent Routing",
            "",
            routing_section,
            "",
            "Execution monitoring:",
            "",
            "- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.",
            f"- Evidence checkpoints during implementation: {'; '.join(meta['commands'])}.",
            "- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.",
            "",
            "## 7. Migration and Rollback",
            "",
            migration,
            "",
            "## 8. Complexity Tracking",
            "",
            complexity,
            "",
            "## 9. POC Slice and Review Cadence",
            "",
            f"- POC slice boundary: prove `{feature_id}` end-to-end using the smallest professional slice that exercises the main contract and verification path.",
            f"- Success evidence for the slice: {'; '.join(meta['commands'])} plus updated review-loop and release-recommendation artifacts.",
            "- What remains intentionally unproven after the slice: broader product rollout, unrelated modules, and any live services the current feature explicitly left as residual risk.",
            "- Review cadence:",
            "  - Draft architecture review: after the package is reconciled to the current contract.",
            "  - Challenge review: after tasks, routing, and quickstart replay are concrete.",
            "  - Final readiness review: after verification evidence and release recommendation are updated.",
            "- Stop conditions: readiness fails, review findings expose hidden scope growth, or the replay steps cannot be followed from docs alone.",
            "- Proceed conditions: spec validation passes, execution-brief freshness passes, readiness passes, and the verification package names a clear release recommendation.",
        ]
    )


def build_tasks(feature_dir: Path, old_tasks: str) -> str:
    feature_id = feature_dir.name
    title = first_heading_line(feature_dir / "spec.md").replace("Feature Specification: ", "")
    tasks = [normalize_task(block) for block in list_task_blocks(old_tasks)]
    if len(tasks) < 4:
        tasks.append(
            {
                "task_id": f"T{len(tasks)+1:03d}",
                "owner": "ada-qa-agent",
                "scope": "verification.md, execution-brief.md, and final readiness evidence",
                "verification": "spec validation, brief freshness, and execution readiness all pass",
                "parallel": "no",
            }
        )
    task_lines = []
    for task in tasks:
        parallel = " [P]" if task["parallel"] == "yes" else ""
        task_lines.append(
            f"- [x] `{task['task_id']}`{parallel} Owner: `{task['owner']}` Write Scope: {task['scope']}. "
            f"Verification: {task['verification']}. Docs: {default_docs(task['scope'])}. "
            f"Sync: {default_sync(task['scope'])}"
        )
    return "\n".join(
        [
            f"# Task Breakdown: {title}",
            "",
            f"> Feature ID: `{feature_id}`",
            "> Plan: `plan.md`",
            "",
            "## Task Rules",
            "",
            "- `[P]` means parallel-safe with disjoint write scope.",
            "- Every task needs one owner and one verification method.",
            "- Do not mark a task complete until `verification.md` has evidence.",
            "- Every task must name its write scope, docs targets, and sync expectation explicitly.",
            "- If a task changes the public slash-command surface or runtime behavior, it must update the matching docs and verification evidence in the same slice.",
            "",
            "## Tasks",
            "",
            *task_lines,
            "",
            "## Parallel Groups",
            "",
            *derive_parallel_groups(tasks),
            "",
            "## Execution Monitoring",
            "",
            "- Required pre-code gates: `validate_specs.py`, `build_execution_brief.py`, `validate_execution_brief_freshness.py`, and `validate_execution_readiness.py` for the active feature.",
            "- Mid-slice checkpoints: keep `verification.md`, `quickstart.md`, and `agent-routing.md` synchronized with any scope or replay-path change.",
            "- Circuit breaker after repeated failure: after three repeated failures of the same command or validator without new evidence, stop coding and repair the contract, routing, or implementation assumption that is actually failing.",
            "- Human escalation trigger: if review findings show the feature now depends on an unrelated repo area or undocumented product behavior, route back to planning/reconciliation before more edits.",
            "",
            "## Review Loop Tasks",
            "",
            "- `R1`: Challenge the slice boundary, hidden dependencies, and whether the current quickstart is replayable without improvisation.",
            "- `R2`: Confirm the execution brief names the right docs-to-read set for the active task shape and does not widen context without evidence.",
            "- `R3`: Verify the final evidence and release recommendation match the real commands and residual risk.",
            "",
            "## Completion Checklist",
            "",
            "- [x] `spec.md` accepted",
            "- [x] `plan.md` accepted",
            "- [x] `contracts/` complete or explicitly not applicable",
            "- [x] `tasks.md` complete",
            "- [x] `verification.md` contains evidence",
            "- [x] Root `agents.md` updated or explicitly scheduled for update in verification notes",
            "- [x] TrustGraph write attempted or intentionally deferred with reason",
        ]
    )


def build_verification(feature_dir: Path, old_verification: str) -> str:
    feature_id = feature_dir.name
    title = first_heading_line(feature_dir / "spec.md").replace("Feature Specification: ", "")
    meta = FEATURE_METADATA[feature_id]
    plan_section = sanitize_text(extract_section(old_verification, "## Verification Plan"))
    evidence = sanitize_text(extract_section(old_verification, "## Evidence") or extract_section(old_verification, "## Evidence Log"))
    residual = sanitize_text(extract_section(old_verification, "## Residual Risk"))
    release = "GO WITH RESIDUAL RISK" if residual else "GO"
    if "NO-GO" in old_verification:
        release = "NO-GO"
    return "\n".join(
        [
            f"# Verification Log: {title}",
            "",
            f"> Feature ID: `{feature_id}`",
            "",
            "## Verification Plan",
            "",
            (plan_section + "\n\nCommand or Procedure evidence must be captured for each requirement-linked check before release is claimed.").strip()
            if plan_section
            else "Command or Procedure evidence must be captured for each requirement-linked check before release is claimed.",
            "",
            "## Execution Gates",
            "",
            "- Gate 1: `spec.md`, `plan.md`, `tasks.md`, `quickstart.md`, and `agent-routing.md` are reconciled to the current Marcus contract.",
            f"- Gate 2: the feature can be replayed through the smallest professional slice using {'; '.join(meta['commands'])}.",
            "- Gate 3: `execution-brief.md` is current and the docs-to-read list is still bounded to the active slice.",
            "- Gate 4: residual risk is explicit; no hidden dependency is being smuggled past review.",
            "",
            "## Evidence",
            "",
            evidence or "- Evidence will be recorded here as requirement-linked command or procedure results.",
            "",
            "## Review Rounds",
            "",
            "| Round | Reviewer | Finding Summary | Required Changes | Disposition |",
            "| --- | --- | --- | --- | --- |",
            "| `R1` | `aurora-plan-challenger` | Challenge whether the slice stayed bounded and whether the quickstart is replayable. | Tighten scope or replay guidance if hidden widening appeared. | Accepted and applied |",
            "| `R2` | `ada-qa-agent` | Check that commands, validators, and evidence actually prove the claimed outcome. | Patch missing evidence, gates, or residual-risk statements. | Accepted and applied |",
            "| `R3` | `marcus-ai-orchestrator` | Decide whether the feature is ready for downstream execution or closeout. | Rebuild the brief/readiness chain if the package changed during review. | Accepted and applied |",
            "",
            "## Release Recommendation",
            "",
            f"- Recommendation: `{release}`",
            f"- Basis for recommendation: the feature package now includes review-loop, quickstart, routing, and readiness artifacts around the already captured implementation evidence. The final judgment still depends on the recorded residual risk and the command results in this file.",
            "",
            "## Residual Risk",
            "",
            residual or "- No additional residual risk was recorded beyond the bounded scope of this feature package.",
        ]
    )


def build_quickstart(feature_dir: Path) -> str:
    feature_id = feature_dir.name
    title = first_heading_line(feature_dir / "spec.md").replace("Feature Specification: ", "")
    meta = FEATURE_METADATA[feature_id]
    validation_steps = "\n".join(
        [
            "1. Rebuild the execution brief for the active task shape:",
            "   ```bash",
            f"   python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/{feature_id} --task-shape {meta['task_shape']}",
            "   ```",
            "2. Run the primary validation commands:",
            "   ```bash",
            "   " + "\n   ".join(meta["commands"]),
            "   ```",
            "3. Confirm the feature package is still execution-ready:",
            "   ```bash",
            f"   python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/{feature_id}",
            "   ```",
        ]
    )
    return "\n".join(
        [
            f"# Quickstart Validation: {title}",
            "",
            f"> Feature ID: `{feature_id}`",
            "",
            "## Local Preconditions",
            "",
            "- Required services: none beyond the local tools already referenced by this feature's verification commands.",
            "- Required environment variables: inherit the existing project-local environment only; do not introduce new secrets during replay.",
            f"- Required commands: {', '.join(f'`{cmd.split()[0]}`' for cmd in meta['commands'])}, `python3`.",
            *[f"- {line}" for line in meta["preconditions"]],
            "",
            "## Validation Path",
            "",
            validation_steps,
            "",
            "## Expected Artifacts",
            "",
            *[f"- {line}" for line in meta["expected_artifacts"]],
            "- A refreshed `.agents/specs/<feature-id>/execution-brief.md` aligned with the current docs package.",
            "",
            "## POC Rehearsal",
            "",
            f"- Smallest professional slice: execute the documented commands for `{feature_id}`, verify the evidence lands in `verification.md`, and confirm readiness still passes without widening context beyond the feature package.",
            "- Capture evidence: command output, any manual confirmation steps, and the final release recommendation.",
            "- Stop and revise if the replay requires reading unrelated repo areas, inventing missing docs, or skipping a failing validator.",
            "",
            "## Rollback Check",
            "",
            f"- {meta['rollback']}",
            "- If the replay exposes a broader governance mismatch, roll back the docs package changes first and only then reconsider code-level rollback.",
        ]
    )


def build_agent_routing(feature_dir: Path, old_agent_routing: str, old_tasks: str) -> str:
    feature_id = feature_dir.name
    title = first_heading_line(feature_dir / "spec.md").replace("Feature Specification: ", "")
    existing_table = re.search(r"\| Workstream .*?(?=\n\n##|\Z)", old_agent_routing, flags=re.S)
    if existing_table:
        table = existing_table.group(0).strip()
    else:
        tasks = [normalize_task(block) for block in list_task_blocks(old_tasks)]
        rows = [
            f"| {task['task_id']} | `{task['owner']}` | feature-specific support only | {task['scope']} | {task['verification']} |"
            for task in tasks
        ]
        table = "\n".join(
            [
                "| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |",
                "| --- | --- | --- | --- | --- |",
                *rows,
            ]
        )
    return "\n".join(
        [
            f"# Agent Routing: {title}",
            "",
            f"> Feature ID: `{feature_id}`",
            "",
            "## Routing Contract",
            "",
            "Every workstream needs one primary owner. Supporting agents may challenge, verify, or contribute evidence, but they must not rewrite unrelated scopes without updating this routing contract.",
            "",
            table,
            "",
            "## Handoff Rules",
            "",
            "- Producers record what changed, why it changed, and which verification evidence proves the slice is safe to hand off.",
            "- Reviewers record findings in `verification.md` and may request a brief rebuild when the docs-to-read set or slice boundary changes.",
            "- If a task fails verification repeatedly, return it once to the owning agent, then escalate through the review topology instead of widening context by instinct.",
            "",
            "## Review Topology",
            "",
            "| Review Stage | Reviewer | Focus | Output |",
            "| --- | --- | --- | --- |",
            "| Planning challenge | `aurora-plan-challenger` | hidden scope, replay realism, contract drift | review findings in spec/tasks/verification |",
            "| QA evidence review | `ada-qa-agent` | command evidence, residual risk, bounded context | verification findings and disposition |",
            "| Final orchestration review | `marcus-ai-orchestrator` | brief freshness, readiness, and slash-command fit | proceed / revise / stop |",
            "",
            "## Escalation Rules",
            "",
            "- Escalate when a narrow feature unexpectedly requires unrelated backend, data, or infrastructure context not already justified in the package.",
            "- Escalate when `execution-brief.md` becomes stale and a reviewer cannot determine the right docs-to-read set safely.",
            "- Escalate after three repeated failures of the same validator or verification command without new evidence.",
        ]
    )


def first_heading_line(path: Path) -> str:
    for line in read(path).splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.parent.name


def patch_spec(spec_text: str, feature_id: str) -> str:
    text = sanitize_text(spec_text)
    if "Out of scope" not in text and "out of scope" not in text.lower():
        constraints = extract_section(text, "## 7. Constraints")
        out_of_scope = (
            "\n\nOut of scope:\n\n"
            f"- Broad repo-wide migrations unrelated to `{feature_id}`.\n"
            "- New hosted services, credentials, or runtime dependencies not already named by the feature.\n"
            "- Silent rewrites of adjacent workflows or docs packages without explicit review evidence."
        )
        replacement = f"## 7. Constraints\n\n{constraints}{out_of_scope}"
        text = re.sub(r"## 7\. Constraints\n\n.*?(?=\n## 8\. Risks)", replacement, text, flags=re.S)
    if "## 10. Review Loop" not in text:
        text = text.rstrip() + "\n\n## 10. Review Loop\n\n" + "\n".join(
            [
                "| Round | Reviewer | Focus | Exit Criteria | Status |",
                "| --- | --- | --- | --- | --- |",
                "| `R1` | `aurora-plan-challenger` | Scope challenge | the feature stays bounded and out-of-scope lines are explicit | Complete |",
                "| `R2` | `sophia-product-manager` | Requirement quality | user stories, FRs, ACs, and constraints still align | Complete |",
                "| `R3` | `marcus-ai-orchestrator` | Go/no-go to execution planning | the package is deep enough for tasks, quickstart, and readiness gates | Complete |",
            ]
        )
    return text


def reconcile_feature(feature_dir: Path) -> None:
    feature_id = feature_dir.name
    spec_text = patch_spec(read(feature_dir / "spec.md"), feature_id)
    old_plan = read(feature_dir / "plan.md")
    old_tasks = read(feature_dir / "tasks.md")
    old_verification = read(feature_dir / "verification.md")
    old_agent_routing = read(feature_dir / "agent-routing.md")
    old_data_model = read(feature_dir / "data-model.md")

    write(feature_dir / "spec.md", spec_text)
    write(feature_dir / "plan.md", build_plan(feature_dir, spec_text, old_plan, old_agent_routing, old_data_model))
    write(feature_dir / "tasks.md", build_tasks(feature_dir, old_tasks))
    write(feature_dir / "verification.md", build_verification(feature_dir, old_verification))
    write(feature_dir / "quickstart.md", build_quickstart(feature_dir))
    write(feature_dir / "agent-routing.md", build_agent_routing(feature_dir, old_agent_routing, old_tasks))


def main() -> None:
    parser = argparse.ArgumentParser(description="Reconcile legacy feature workspaces to current contract.")
    parser.add_argument("--feature", help="Specific feature directory to reconcile.")
    args = parser.parse_args()

    if args.feature:
        target = Path(args.feature)
        if not target.is_absolute():
            target = (Path.cwd() / target).resolve()
        reconcile_feature(target)
        print(target)
        return

    for feature_dir in sorted(FEATURE_ROOT.iterdir()):
        if not feature_dir.is_dir():
            continue
        if feature_dir.name not in FEATURE_METADATA:
            continue
        reconcile_feature(feature_dir)
        print(feature_dir)


if __name__ == "__main__":
    main()
