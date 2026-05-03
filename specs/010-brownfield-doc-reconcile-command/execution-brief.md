# Execution Brief: Feature Specification: Brownfield Doc Reconcile Command

> Feature ID: `010-brownfield-doc-reconcile-command`
> Task Shape: `architecture-refactor`
> Generated From: `spec.md`, `plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, `agent-routing.md`

## 1. Operator Intent Snapshot

## 1. Purpose

Add `/doc_reconcile`, a brownfield documentation recovery command for projects
whose implementation has moved faster than their docs. The command must review
the whole codebase, map code to product docs, migrate or enrich
`/docs/development` to V31.1, and update global planning docs.


## 2. Required Behavior

## 3. Functional Requirements

- `FR-001`: Add `/doc_reconcile` workflow.
- `FR-002`: Add a code/docs audit script that emits an audit artifact.
- `FR-003`: V31 epic-first scaffold and validation MUST require `issues.md` per
  epic.
- `FR-004`: `/doc_reconcile` MUST require full code inventory, relationship
  labels, Jira Story/Priority, Mermaid, Work Log, QA issues, and global docs
  sync.
- `FR-005`: The command MUST preserve history and archive/merge duplicates only
  intentionally.


## 5. Acceptance Criteria

- `AC-001`: Workflow file exists and describes `/doc_reconcile`.
- `AC-002`: Audit script creates `docs/development/audits/*-code-docs-audit.md`.
- `AC-003`: New V31 scaffold includes `issues.md`.
- `AC-004`: Validator rejects V31 epic directories without `issues.md`.
- `AC-005`: README, USAGE, `.clinerules`, release notes, and workflow docs
  mention `/doc_reconcile`.


## 3. Scope Boundaries

## 7. Constraints

- Do not edit downstream app code as part of command creation.
- Do not delete legacy docs silently.

Out of scope:

- Broad repo-wide migrations unrelated to `010-brownfield-doc-reconcile-command`.
- New hosted services, credentials, or runtime dependencies not already named by the feature.
- Silent rewrites of adjacent workflows or docs packages without explicit review evidence.


## 4. Active Work Slice

## 1. Technical Summary

Add `/doc_reconcile`, a brownfield documentation recovery command for projects
whose implementation has moved faster than their docs. The command must review
the whole codebase, map code to product docs, migrate or enrich
`/docs/development` to V31.1, and update global planning docs.


## 6. Agent Routing

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| Planning and contract reconciliation | `marcus-ai-orchestrator` | current-contract feature package | spec/readiness validation |
| QA and release gate | `ada-qa-agent` | verification evidence and release recommendation | validator output |

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: python3 .agents/scripts/validate_specs.py --feature .agents/specs/010-brownfield-doc-reconcile-command; python3 .agents/scripts/audit_development_docs.py --root ..
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: python3 .agents/scripts/validate_specs.py --feature .agents/specs/010-brownfield-doc-reconcile-command; python3 .agents/scripts/audit_development_docs.py --root ..
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.


## Tasks

- [x] `T001` Owner: `marcus-ai-orchestrator` Write Scope: add `/doc_reconcile` workflow. Verification: workflow file exists. Docs: `tasks.md`, `agent-routing.md`, `verification.md`. Sync: If command sequencing or gates change, patch the command-surface docs and the agent-routing contract before closing the slice.
- [x] `T002` Owner: `development-ledger-architect` Write Scope: add code/docs audit script. Verification: audit smoke creates markdown report. Docs: `plan.md`, `tasks.md`, `verification.md`. Sync: If validator behavior or required artifacts change, update the quickstart, review loop, and verification evidence in the same slice.
- [x] `T003` Owner: `ada-qa-agent` Write Scope: add `issues.md` template and V31 validator requirement. Verification: scaffold includes issues and negative smoke rejects missing issues. Docs: `plan.md`, `tasks.md`, `verification.md`. Sync: If validator behavior or required artifacts change, update the quickstart, review loop, and verification evidence in the same slice.
- [x] `T004` Owner: `knowledge-work-architecture` Write Scope: update README, USAGE, `.clinerules`, release notes, and `/develop`. Verification: docs mention command and issue-file policy. Docs: `tasks.md`, `agent-routing.md`, `verification.md`. Sync: If command sequencing or gates change, patch the command-surface docs and the agent-routing contract before closing the slice.
- [x] `T005` Owner: `ada-qa-agent` Write Scope: final validation evidence. Verification: `verification.md` contains command results. Docs: `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.


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
| Python compile | `PYTHONPYCACHEPREFIX=/tmp/marcus-pycache python3 -m py_compile ...` | Pass | Passed |
| Spec validation | `python3 .agents/scripts/validate_specs.py` | Pass | Passed: 10 specs validated |
| Audit smoke | `audit_development_docs.py --root /tmp/...` | Creates audit markdown | Passed |
| V31 scaffold smoke | `create_development_docs.py --root /tmp/...` | Includes `issues.md` | Passed |
| Missing issues negative smoke | Remove `issues.md` then validate | Fails | Failed as expected: `missing issues.md` |

Command or Procedure evidence must be captured for each requirement-linked check before release is claimed.


## Execution Gates

- Gate 1: `spec.md`, `plan.md`, `tasks.md`, `quickstart.md`, and `agent-routing.md` are reconciled to the current Marcus contract.
- Gate 2: the feature can be replayed through the smallest professional slice using python3 .agents/scripts/validate_specs.py --feature .agents/specs/010-brownfield-doc-reconcile-command; python3 .agents/scripts/audit_development_docs.py --root ..
- Gate 3: `execution-brief.md` is current and the docs-to-read list is still bounded to the active slice.
- Gate 4: residual risk is explicit; no hidden dependency is being smuggled past review.


## Local Preconditions

- Required services: none beyond the local tools already referenced by this feature's verification commands.
- Required environment variables: inherit the existing project-local environment only; do not introduce new secrets during replay.
- Required commands: `python3`, `python3`, `python3`.
- Use the command on in-progress projects whose docs lag behind code reality.
- Downstream application code remains out of scope unless the operator approves follow-up implementation work.


## Validation Path

1. Rebuild the execution brief for the active task shape:
   ```bash
   python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/010-brownfield-doc-reconcile-command --task-shape architecture-refactor
   ```
2. Run the primary validation commands:
   ```bash
   python3 .agents/scripts/validate_specs.py --feature .agents/specs/010-brownfield-doc-reconcile-command
   python3 .agents/scripts/audit_development_docs.py --root .
   ```
3. Confirm the feature package is still execution-ready:
   ```bash
   python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/010-brownfield-doc-reconcile-command
   ```


## POC Rehearsal

- Smallest professional slice: execute the documented commands for `010-brownfield-doc-reconcile-command`, verify the evidence lands in `verification.md`, and confirm readiness still passes without widening context beyond the feature package.
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

- Selected task shape: `architecture-refactor`
- Why this shape: Read decisions, diagrams, affected modules, and execution boundaries first.

### Required Reads

- Required read: `agents.md`
- Required read: `.agents/memory/constitution.md`
- Required read: `.agents/specs/010-brownfield-doc-reconcile-command/execution-brief.md`
- Required read: `.agents/specs/010-brownfield-doc-reconcile-command/spec.md` only if the brief or failing evidence says deeper requirement context is needed.
- Required read: `.agents/specs/010-brownfield-doc-reconcile-command/plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, and `agent-routing.md` only when the current write scope or failing evidence requires the deeper artifact.
- Required read: create or reconcile the missing `docs/development/` notes before behavior-changing source edits.

### Forbidden Default Reads

- Forbidden by default: full repo scans without a bounded module list
- Forbidden by default: random DB exploration unrelated to the refactor boundary
- Forbidden by default: random UI exploration unrelated to the refactor boundary

### Expansion Triggers

- Read decisions, diagrams, affected modules, and execution boundaries first.
- Do not scan the full repo without a bounded module list.
- Load architecture/refactor skills first.
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
