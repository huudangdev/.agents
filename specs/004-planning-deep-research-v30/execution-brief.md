# Execution Brief: Feature Specification: Planning Deep Research V30

> Feature ID: `004-planning-deep-research-v30`
> Task Shape: `general`
> Generated From: `spec.md`, `plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, `agent-routing.md`

## 1. Operator Intent Snapshot

## 1. Purpose

The existing `/planning` workflow must keep its historical output contract while
becoming meaningfully deeper: research should be evidence-backed, claims should
trace to sources, contradictions should be explicit, and diagrams should be
supported by architectural reasoning instead of shallow sketches.

The workflow must not discard the current `/docs` file structure. It should add
research ledgers and validation gates around that structure.


## 2. Required Behavior

## 3. Functional Requirements

- `FR-001`: `/planning` MUST preserve the existing 8 output files.
- `FR-002`: `/planning` MUST add research ledgers under `/docs/research/`.
- `FR-003`: `/planning` MUST require source, evidence, claim, contradiction,
  and research manifest artifacts for deep planning runs.
- `FR-004`: `/planning` MUST include clarify, outline refinement, synthesis, and
  validation gates.
- `FR-005`: The repo MUST include templates for the research ledger files.
- `FR-006`: The repo MUST include a local validator for planning research
  artifacts.


## 5. Acceptance Criteria

- `AC-001`: Given `.agents/workflows/planning.md`, when inspected, then it lists
  all 8 legacy output files unchanged.
- `AC-002`: Given `.agents/templates/`, when inspected, then planning research
  templates exist for sources, evidence, claims, contradictions, and manifest.
- `AC-003`: Given `.agents/scripts/validate_planning_research.py`, when parsed
  by Python AST validation, then it has no syntax errors.
- `AC-004`: Given the repo specs, when `validate_specs.py` runs, then all feature
  specs pass.


## 3. Scope Boundaries

## 7. Constraints

- Constitution articles that apply: Articles I, II, III, IV, VI, VIII.
- Existing files or modules in scope: `.agents/workflows/planning.md`,
  `.agents/templates/`, `.agents/scripts/`, `.agents/specs/004-*`.
- Files or modules out of scope: installing third-party search tools, changing
  `/design` or `/develop`, removing `/docs` outputs.
- Compatibility requirements: existing `/planning` users still receive the same
  file count and names as before.


## 4. Active Work Slice

## 1. Technical Summary

Upgrade `/planning` as an additive V30 workflow:

- Replace shallow map-reduce instructions with a deep-research evidence pipeline.
- Preserve the 8 legacy `/docs` outputs exactly.
- Add `/docs/research/*` ledgers and templates.
- Add `validate_planning_research.py` for local validation.
- Keep code generation forbidden and preserve human oversight halt.


## 6. Agent Routing

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| Workflow rewrite | `marcus-ai-orchestrator` | V30 `planning.md` | spec validation |
| Research templates | `sage-research-synthesis` | planning ledger templates | file checks |
| Validator | `ada-qa-agent` | `validate_planning_research.py` | AST parse |

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: python3 .agents/scripts/validate_specs.py --feature .agents/specs/004-planning-deep-research-v30; python3 -m py_compile .agents/scripts/validate_planning_research.py.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: python3 .agents/scripts/validate_specs.py --feature .agents/specs/004-planning-deep-research-v30; python3 -m py_compile .agents/scripts/validate_planning_research.py.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: python3 .agents/scripts/validate_specs.py --feature .agents/specs/004-planning-deep-research-v30; python3 -m py_compile .agents/scripts/validate_planning_research.py.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.


## Tasks

- [x] `T001` Owner: `marcus-ai-orchestrator` Write Scope: `.agents/workflows/planning.md`. Verification: workflow preserves all 8 legacy outputs and adds V30 gates. Docs: `tasks.md`, `agent-routing.md`, `verification.md`. Sync: If command sequencing or gates change, patch the command-surface docs and the agent-routing contract before closing the slice.
- [x] `T002` [P] Owner: `sage-research-synthesis` Write Scope: `.agents/templates/planning-*-template.*`. Verification: source/evidence/ claim/contradiction/manifest templates exist. Docs: `plan.md`, `data-model.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T003` [P] Owner: `ada-qa-agent` Write Scope: `.agents/scripts/validate_planning_research.py`. Verification: Python AST parse passes. Docs: `plan.md`, `tasks.md`, `verification.md`. Sync: If validator behavior or required artifacts change, update the quickstart, review loop, and verification evidence in the same slice.
- [x] `T004` Owner: `david-systems-architect` Write Scope: `contracts/planning-output-contract.md`, `data-model.md`. Verification: output contract documents legacy and extra files. Docs: `plan.md`, `data-model.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.


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

| Requirement | Method | Command or Procedure | Expected Result |
| --- | --- | --- | --- |
| `FR-001` | Static review | Inspect `.agents/workflows/planning.md` | All 8 legacy outputs listed |
| `FR-002` | Static review | Inspect templates and workflow | `/docs/research` files defined |
| `FR-003` | Static review | Inspect templates | sources/evidence/claims/contradictions/manifest templates exist |
| `FR-004` | Static review | Inspect workflow | clarify, outline refinement, synthesis, validation gates exist |
| `FR-005` | File check | `find .agents/templates -name 'planning-*'` | Planning templates exist |
| `FR-006` | AST parse | Python AST parse for scripts | Validator syntax passes |

Command or Procedure evidence must be captured for each requirement-linked check before release is claimed.

Command or Procedure evidence must be captured for each requirement-linked check before release is claimed.


## Execution Gates

- Gate 1: `spec.md`, `plan.md`, `tasks.md`, `quickstart.md`, and `agent-routing.md` are reconciled to the current Marcus contract.
- Gate 2: the feature can be replayed through the smallest professional slice using python3 .agents/scripts/validate_specs.py --feature .agents/specs/004-planning-deep-research-v30; python3 -m py_compile .agents/scripts/validate_planning_research.py.
- Gate 3: `execution-brief.md` is current and the docs-to-read list is still bounded to the active slice.
- Gate 4: residual risk is explicit; no hidden dependency is being smuggled past review.


## Local Preconditions

- Required services: none beyond the local tools already referenced by this feature's verification commands.
- Required environment variables: inherit the existing project-local environment only; do not introduce new secrets during replay.
- Required commands: `python3`, `python3`, `python3`.
- Planning remains a docs-first workflow; no code-generation runtime is required.
- Research validators must run locally without network dependencies.


## Validation Path

1. Rebuild the execution brief for the active task shape:
   ```bash
   python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/004-planning-deep-research-v30 --task-shape general
   ```
2. Run the primary validation commands:
   ```bash
   python3 .agents/scripts/validate_specs.py --feature .agents/specs/004-planning-deep-research-v30
   python3 -m py_compile .agents/scripts/validate_planning_research.py
   ```
3. Confirm the feature package is still execution-ready:
   ```bash
   python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/004-planning-deep-research-v30
   ```


## POC Rehearsal

- Smallest professional slice: execute the documented commands for `004-planning-deep-research-v30`, verify the evidence lands in `verification.md`, and confirm readiness still passes without widening context beyond the feature package.
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
- Required read: `.agents/specs/004-planning-deep-research-v30/execution-brief.md`
- Required read: `.agents/specs/004-planning-deep-research-v30/spec.md` only if the brief or failing evidence says deeper requirement context is needed.
- Required read: `.agents/specs/004-planning-deep-research-v30/plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, and `agent-routing.md` only when the current write scope or failing evidence requires the deeper artifact.
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
