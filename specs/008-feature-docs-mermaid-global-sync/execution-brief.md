# Execution Brief: Feature Specification: Feature Docs Mermaid Global Sync

> Feature ID: `008-feature-docs-mermaid-global-sync`
> Task Shape: `general`
> Generated From: `spec.md`, `plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, `agent-routing.md`

## 1. Operator Intent Snapshot

## 1. Purpose

Ensure feature-level development documentation is visual, detailed, and tied
back to the PM-facing global planning package. Every epic/module/feature/page/task
note must include Mermaid, and every behavior-changing code slice must update at
least one global `/docs` planning artifact.


## 2. Required Behavior

## 3. Functional Requirements

- `FR-001`: Development docs validation MUST require Mermaid code fences for
  epic/module/feature/page/task notes.
- `FR-002`: Mermaid diagrams MUST use diagram types appropriate to the artifact.
- `FR-003`: Doc sync validation MUST require at least one global `/docs`
  planning file update when source behavior changes.
- `FR-004`: Sync notes MUST include at least one `updated because` global doc
  decision.
- `FR-005`: Templates and workflow docs MUST explain diagram and global sync
  requirements.


## 5. Acceptance Criteria

- `AC-001`: Given a development note without Mermaid, when strict validation
  runs, then it fails.
- `AC-002`: Given source files changed but no global `/docs` file changed, when
  doc sync strict validation runs, then it fails.
- `AC-003`: Given a source change with feature docs and a global doc update, when
  strict validation runs, then it passes if all other quality gates pass.


## 3. Scope Boundaries

## 7. Constraints

- Constitution articles that apply: Human-Visible Handoff, Evidence Before
  Completion, Context Before Construction.
- Existing files or modules in scope: development validators, doc sync validator,
  development templates, `/develop`, README, USAGE, release notes, rubric.
- Files or modules out of scope: downstream project application code.
- Compatibility requirements: additive, but strict validation is intentionally
  harsher.


## 4. Active Work Slice

## 1. Technical Summary

Extend V30.3 docs quality gates with mandatory Mermaid diagrams and mandatory
global planning doc updates. Validators, templates, rubric, and `/develop` now
make diagrams and global docs synchronization non-optional.


## 6. Agent Routing

Every workstream needs one primary owner. Supporting agents may challenge, verify, or contribute evidence, but they must not rewrite unrelated scopes without updating this routing contract.

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| Mermaid validation | `ada-qa-agent` | `knowledge-work-architecture` | `validate_development_docs.py` | Diagram gate |
| Global docs validation | `ada-qa-agent` | `sophia-product-manager` | `validate_doc_sync.py` | Global docs gate |
| Templates and rubric | `knowledge-work-architecture` | `chartis-data-visualizer` | templates, rubric | Mermaid guidance |
| Workflow/docs | `marcus-ai-orchestrator` | `sophia-product-manager` | `/develop`, README, USAGE, release notes | Operator-visible rule |

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: python3 .agents/scripts/validate_specs.py --feature .agents/specs/008-feature-docs-mermaid-global-sync; python3 .agents/scripts/validate_doc_sync.py --strict.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.


## Tasks

- [x] `T001` Owner: `ada-qa-agent` Write Scope: update `validate_development_docs.py` to require Mermaid. Verification: scaffold without valid completed docs fails. Docs: `plan.md`, `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T002` Owner: `ada-qa-agent` Write Scope: update `validate_doc_sync.py` to require global `/docs` updates. Verification: source-only change fails. Docs: `plan.md`, `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T003` Owner: `knowledge-work-architecture` Write Scope: update templates and rubric with Mermaid/global docs rules. Verification: templates contain `## Mermaid Diagram`. Docs: `plan.md`, `data-model.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T004` Owner: `marcus-ai-orchestrator` Write Scope: update `/develop`, README, USAGE, and release notes. Verification: rules are visible to future agents. Docs: `tasks.md`, `agent-routing.md`, `verification.md`. Sync: If command sequencing or gates change, patch the command-surface docs and the agent-routing contract before closing the slice.


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
| Spec validation | `python3 .agents/scripts/validate_specs.py` | Pass | Passed: 8 specs validated |
| Python compile | `PYTHONPYCACHEPREFIX=/tmp/marcus-pycache python3 -m py_compile .agents/scripts/validate_development_docs.py .agents/scripts/validate_doc_sync.py .agents/scripts/create_development_docs.py .agents/scripts/create_doc_sync_note.py .agents/scripts/validate_specs.py` | Pass | Passed |
| Missing Mermaid negative smoke | Scaffold docs, remove Mermaid fence from a feature note, run strict development validator | Fail on missing Mermaid and shallow placeholders | Failed as expected: `feature-mermaid-smoke.md: missing Mermaid diagram code fence` |
| Missing global docs negative smoke | Validate source change without global `/docs` change | Fail | Failed as expected: `Source files changed but no required global /docs planning file was updated` |

Command or Procedure evidence must be captured for each requirement-linked check before release is claimed.


## Execution Gates

- Gate 1: `spec.md`, `plan.md`, `tasks.md`, `quickstart.md`, and `agent-routing.md` are reconciled to the current Marcus contract.
- Gate 2: the feature can be replayed through the smallest professional slice using python3 .agents/scripts/validate_specs.py --feature .agents/specs/008-feature-docs-mermaid-global-sync; python3 .agents/scripts/validate_doc_sync.py --strict.
- Gate 3: `execution-brief.md` is current and the docs-to-read list is still bounded to the active slice.
- Gate 4: residual risk is explicit; no hidden dependency is being smuggled past review.


## Local Preconditions

- Required services: none beyond the local tools already referenced by this feature's verification commands.
- Required environment variables: inherit the existing project-local environment only; do not introduce new secrets during replay.
- Required commands: `python3`, `python3`, `python3`.
- Behavior-changing work must have at least one matching global `/docs` artifact ready for targeted updates.
- Development notes should already exist so Mermaid and sync rules can be verified in context.


## Validation Path

1. Rebuild the execution brief for the active task shape:
   ```bash
   python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/008-feature-docs-mermaid-global-sync --task-shape general
   ```
2. Run the primary validation commands:
   ```bash
   python3 .agents/scripts/validate_specs.py --feature .agents/specs/008-feature-docs-mermaid-global-sync
   python3 .agents/scripts/validate_doc_sync.py --strict
   ```
3. Confirm the feature package is still execution-ready:
   ```bash
   python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/008-feature-docs-mermaid-global-sync
   ```


## POC Rehearsal

- Smallest professional slice: execute the documented commands for `008-feature-docs-mermaid-global-sync`, verify the evidence lands in `verification.md`, and confirm readiness still passes without widening context beyond the feature package.
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
- Required read: `.agents/specs/008-feature-docs-mermaid-global-sync/execution-brief.md`
- Required read: `.agents/specs/008-feature-docs-mermaid-global-sync/spec.md` only if the brief or failing evidence says deeper requirement context is needed.
- Required read: `.agents/specs/008-feature-docs-mermaid-global-sync/plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, and `agent-routing.md` only when the current write scope or failing evidence requires the deeper artifact.
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
