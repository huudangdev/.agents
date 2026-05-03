# Execution Brief: Feature Specification: Substantive Development Docs Quality

> Feature ID: `007-substantive-development-docs-quality`
> Task Shape: `general`
> Generated From: `spec.md`, `plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, `agent-routing.md`

## 1. Operator Intent Snapshot

## 1. Purpose

Raise `/develop` documentation from "files exist" to "PM-grade implementation
knowledge exists". Agents must not close code work with template-only notes.
Development docs must contain concrete project facts, rationale, PM impact,
evidence, risks, and exact code paths.


## 2. Required Behavior

## 3. Functional Requirements

- `FR-001`: Development docs validation MUST reject placeholders, draft placeholder token,
  unfinished draft marker, unchecked boxes, and generic template prose.
- `FR-002`: Development docs MUST include PM-visible commentary, rationale,
  tradeoffs, evidence, risk, and concrete code paths.
- `FR-003`: Sync note validation MUST reject shallow or unfinished notes.
- `FR-004`: Development templates MUST explain the quality bar directly.
- `FR-005`: A shared quality rubric MUST define accepted and rejected docs.


## 5. Acceptance Criteria

- `AC-001`: Given a scaffolded template with placeholders, when strict
  development docs validation runs, then it fails.
- `AC-002`: Given a real development doc with code path, rationale, evidence,
  risk, and sufficient depth, when strict validation runs, then it passes.
- `AC-003`: Given a sync note with unfinished placeholders, when strict doc sync
  validation runs, then it fails.


## 3. Scope Boundaries

## 7. Constraints

- Constitution articles that apply: Evidence Before Completion, Human-Visible
  Handoff, Context Before Construction.
- Existing files or modules in scope: development templates, sync templates,
  validators, `/develop`, `.clinerules`, README, USAGE, release notes.
- Files or modules out of scope: application code in downstream projects.
- Compatibility requirements: stricter docs should fail shallow output rather
  than silently accepting it.


## 4. Active Work Slice

## 1. Technical Summary

Add hard quality gates to development documentation. The implementation updates
validators, templates, workflow rules, and PM-facing docs so scaffolded template
output fails until agents provide concrete implementation knowledge.


## 6. Agent Routing

Every workstream needs one primary owner. Supporting agents may challenge, verify, or contribute evidence, but they must not rewrite unrelated scopes without updating this routing contract.

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| Quality rubric | `knowledge-work-architecture` | `sophia-product-manager` | `.agents/DEVELOPMENT_DOCS_QUALITY_RUBRIC.md` | PM-grade documentation bar |
| Development validator | `ada-qa-agent` | `alan-tech-lead` | `.agents/scripts/validate_development_docs.py` | Strict content validation |
| Sync validator | `ada-qa-agent` | `knowledge-work-architecture` | `.agents/scripts/validate_doc_sync.py` | Strict sync note validation |
| Templates | `knowledge-work-architecture` | `marcus-ai-orchestrator` | `.agents/templates/development-*` | Quality-bar prompts |
| Workflow/docs | `marcus-ai-orchestrator` | `sophia-product-manager` | `/develop`, README, USAGE, `.clinerules` | Visible enforcement |

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: python3 .agents/scripts/validate_specs.py --feature .agents/specs/007-substantive-development-docs-quality; python3 .agents/scripts/validate_development_docs.py --strict-counts.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.


## Tasks

- [x] `T001` Owner: `ada-qa-agent` Write Scope: strengthen `validate_development_docs.py`. Verification: rejects placeholders, shallow notes, missing rationale, and missing code paths. Docs: `plan.md`, `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T002` Owner: `ada-qa-agent` Write Scope: strengthen `validate_doc_sync.py`. Verification: rejects shallow unfinished sync notes. Docs: `plan.md`, `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T003` Owner: `knowledge-work-architecture` Write Scope: add quality rubric and improve templates. Verification: templates include PM notes, commentary, change logs, evidence, and risk prompts. Docs: `plan.md`, `data-model.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T004` Owner: `marcus-ai-orchestrator` Write Scope: update `/develop`, `.clinerules`, README, USAGE, and release notes. Verification: quality gate is visible to future agents. Docs: `tasks.md`, `agent-routing.md`, `verification.md`. Sync: If command sequencing or gates change, patch the command-surface docs and the agent-routing contract before closing the slice.


## Execution Monitoring

- Required pre-code gates: `validate_specs.py`, `build_execution_brief.py`, `validate_execution_brief_freshness.py`, and `validate_execution_readiness.py` for the active feature.
- Mid-slice checkpoints: keep `verification.md`, `quickstart.md`, and `agent-routing.md` synchronized with any scope or replay-path change.
- Circuit breaker after repeated failure: after three repeated failures of the same command or validator without new evidence, stop coding and repair the contract, routing, or implementation assumption that is actually failing.
- Human escalation trigger: if review findings show the feature now depends on an unrelated repo area or undocumented product behavior, route back to planning/reconciliation before more edits.


## 5. Development Ledger Context

Read these development-ledger notes before source edits for the active slice:

No `docs/development/` notes matched this feature workspace.
Before behavior-changing code work, create or reconcile the development ledger for this feature slice.
Preferred paths:
- If the feature is new: run `python3 .agents/scripts/create_development_docs.py --name "<epic-or-feature-name>" --feature-id "<feature-id>" --epic-number 001 --child-number 001 --task-number 001`.
- If the project is brownfield or docs are stale: route to `/doc_reconcile` and repair the ledger before source edits.

## 6. Verification Path

## Verification Plan

| Check | Command / Method | Expected Result | Evidence |
| --- | --- | --- | --- |
| Spec validation | `python3 .agents/scripts/validate_specs.py` | Pass | `SPEC VALIDATION PASSED: 7 feature(s)` |
| Python compile | `PYTHONPYCACHEPREFIX=/tmp/marcus-pycache python3 -m py_compile .agents/scripts/validate_development_docs.py .agents/scripts/validate_doc_sync.py .agents/scripts/create_development_docs.py .agents/scripts/create_doc_sync_note.py .agents/scripts/validate_specs.py` | Pass | Exit 0 |
| Negative quality smoke | Scaffold docs then run strict validation | Fail on placeholders/shallow docs | `DEVELOPMENT DOCS VALIDATION FAILED` with placeholder, unfinished draft marker, and shallow-depth errors |
| Positive quality smoke | Validate filled fixture | Pass | Deferred to first real downstream `/develop` slice |

Command or Procedure evidence must be captured for each requirement-linked check before release is claimed.


## Execution Gates

- Gate 1: `spec.md`, `plan.md`, `tasks.md`, `quickstart.md`, and `agent-routing.md` are reconciled to the current Marcus contract.
- Gate 2: the feature can be replayed through the smallest professional slice using python3 .agents/scripts/validate_specs.py --feature .agents/specs/007-substantive-development-docs-quality; python3 .agents/scripts/validate_development_docs.py --strict-counts.
- Gate 3: `execution-brief.md` is current and the docs-to-read list is still bounded to the active slice.
- Gate 4: residual risk is explicit; no hidden dependency is being smuggled past review.


## Local Preconditions

- Required services: none beyond the local tools already referenced by this feature's verification commands.
- Required environment variables: inherit the existing project-local environment only; do not introduce new secrets during replay.
- Required commands: `python3`, `python3`, `python3`.
- Generated ledger docs are drafts until concrete project facts replace placeholders.
- Strict validators are expected to fail on template-only output by design.


## Validation Path

1. Rebuild the execution brief for the active task shape:
   ```bash
   python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/007-substantive-development-docs-quality --task-shape general
   ```
2. Run the primary validation commands:
   ```bash
   python3 .agents/scripts/validate_specs.py --feature .agents/specs/007-substantive-development-docs-quality
   python3 .agents/scripts/validate_development_docs.py --strict-counts
   ```
3. Confirm the feature package is still execution-ready:
   ```bash
   python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/007-substantive-development-docs-quality
   ```


## POC Rehearsal

- Smallest professional slice: execute the documented commands for `007-substantive-development-docs-quality`, verify the evidence lands in `verification.md`, and confirm readiness still passes without widening context beyond the feature package.
- Capture evidence: command output, any manual confirmation steps, and the final release recommendation.
- Stop and revise if the replay requires reading unrelated repo areas, inventing missing docs, or skipping a failing validator.


## 7. Review and Release Signals

## 10. Review Loop

| Round | Reviewer | Focus | Exit Criteria | Status |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Scope challenge | the feature stays bounded and out-of-scope lines are explicit | Complete |
| `R2` | `sophia-product-manager` | Requirement quality | user stories, FRs, ACs, and constraints still align | Complete |
| `R3` | `marcus-ai-orchestrator` | Go/no-go to execution planning | the package is deep enough for tasks, quickstart, and readiness gates | Complete |


## Review Loop Tasks

- `R1`: Challenge the slice boundary, hidden dependencies, and whether the current quickstart is replayable without improvisation.
- `R2`: Confirm the execution brief names the right docs-to-read set for the active task shape and does not widen context without evidence.
- `R3`: Verify the final evidence and release recommendation match the real commands and residual risk.


## Review Rounds

| Round | Reviewer | Finding Summary | Required Changes | Disposition |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Challenge whether the slice stayed bounded and whether the quickstart is replayable. | Tighten scope or replay guidance if hidden widening appeared. | Accepted and applied |
| `R2` | `ada-qa-agent` | Check that commands, validators, and evidence actually prove the claimed outcome. | Patch missing evidence, gates, or residual-risk statements. | Accepted and applied |
| `R3` | `marcus-ai-orchestrator` | Decide whether the feature is ready for downstream execution or closeout. | Rebuild the brief/readiness chain if the package changed during review. | Accepted and applied |


## Release Recommendation

- Recommendation: `GO WITH RESIDUAL RISK`
- Basis for recommendation: the feature package now includes review-loop, quickstart, routing, and readiness artifacts around the already captured implementation evidence. The final judgment still depends on the recorded residual risk and the command results in this file.


## 8. Context Expansion Rules

### Task Shape Decision

- Selected task shape: `general`
- Why this shape: Start from the active feature workspace and only expand context when the write scope demands it.

### Required Reads

- Required read: `agents.md`
- Required read: `.agents/memory/constitution.md`
- Required read: `.agents/specs/007-substantive-development-docs-quality/execution-brief.md`
- Required read: `.agents/specs/007-substantive-development-docs-quality/spec.md` only if the brief or failing evidence says deeper requirement context is needed.
- Required read: `.agents/specs/007-substantive-development-docs-quality/plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, and `agent-routing.md` only when the current write scope or failing evidence requires the deeper artifact.
- Required read: create or reconcile the missing `docs/development/` notes before behavior-changing source edits.

### Forbidden Default Reads

- Forbidden by default: broad repo areas not justified by the active write scope
- Forbidden by default: unrelated infrastructure surfaces
- Forbidden by default: unrelated analytics or database areas

### Expansion Triggers

- Start from the active feature workspace and only expand context when the write scope demands it.
- Record any scope widening in verification evidence.
- Do not read broad repo areas just to feel safe.
- Read the `docs/development/` notes listed in this brief before widening beyond the current work slice.
- If the required epic/feature/module/page/task note is missing, stop and reconcile the development ledger instead of improvising from code alone.

## Review Topology

| Review Stage | Reviewer | Focus | Output |
| --- | --- | --- | --- |
| Planning challenge | `aurora-plan-challenger` | hidden scope, replay realism, contract drift | review findings in spec/tasks/verification |
| QA evidence review | `ada-qa-agent` | command evidence, residual risk, bounded context | verification findings and disposition |
| Final orchestration review | `marcus-ai-orchestrator` | brief freshness, readiness, and slash-command fit | proceed / revise / stop |


## Escalation Rules

- Escalate when a narrow feature unexpectedly requires unrelated backend, data, or infrastructure context not already justified in the package.
- Escalate when `execution-brief.md` becomes stale and a reviewer cannot determine the right docs-to-read set safely.
- Escalate after three repeated failures of the same validator or verification command without new evidence.
