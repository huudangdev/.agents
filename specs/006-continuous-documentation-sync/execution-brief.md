# Execution Brief: Feature Specification: Continuous Documentation Sync

> Feature ID: `006-continuous-documentation-sync`
> Task Shape: `general`
> Generated From: `spec.md`, `plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, `agent-routing.md`

## 1. Operator Intent Snapshot

## 1. Purpose

Keep PM-facing planning documents and code-phase development ledgers current
throughout repeated `/develop` cycles. Agents must update documentation in
parallel with code by apunfinished draft marker missing facts and targeted-patching changed facts
instead of replacing documents wholesale.


## 2. Required Behavior

## 3. Functional Requirements

- `FR-001`: `/develop` MUST include a documentation sync checkpoint after each
  material code slice.
- `FR-002`: The system MUST create `/docs/development/sync/*.md` notes that
  reference changed source files.
- `FR-003`: Sync notes MUST record decisions for legacy planning docs and
  development ledger docs.
- `FR-004`: Validation MUST fail in strict mode when source files changed but no
  sync note or documentation review exists.
- `FR-005`: The policy MUST forbid wholesale replacement of PM docs unless the
  operator explicitly asks for a rewrite.


## 5. Acceptance Criteria

- `AC-001`: Given source files changed, when `validate_doc_sync.py --strict`
  runs, then validation fails unless a sync note references those files.
- `AC-002`: Given a sync note exists, when strict validation runs, then unchecked
  targeted-patch policy items fail validation.
- `AC-003`: Given docs were reviewed, when source and doc files are supplied to
  strict validation, then validation passes.


## 3. Scope Boundaries

## 7. Constraints

- Constitution articles that apply: Context Before Construction, Evidence Before
  Completion, Human-Visible Handoff.
- Existing files or modules in scope: `/develop`, `.clinerules`, README,
  `USAGE_GUIDE.md`, release notes, CI template, development templates/scripts.
- Files or modules out of scope: generated project application docs themselves.
- Compatibility requirements: additive only; docs must be append/patched.


## 4. Active Work Slice

## 1. Technical Summary

Add a continuous documentation sync gate to `/develop` so code changes and PM
docs evolve together. The implementation adds sync templates, a sync note
creator, strict validation, workflow gates, and documentation policy updates.


## 6. Agent Routing

Every workstream needs one primary owner. Supporting agents may challenge, verify, or contribute evidence, but they must not rewrite unrelated scopes without updating this routing contract.

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| Workflow gate | `marcus-ai-orchestrator` | `sophia-product-manager` | `.agents/workflows/develop.md` | Node 6.5 sync checkpoint |
| Knowledge policy | `knowledge-work-architecture` | `architecture-decision-records` | templates and docs | Append/patch policy |
| Script implementation | `alan-tech-lead` | `ada-qa-agent` | `.agents/scripts/create_doc_sync_note.py`, `.agents/scripts/validate_doc_sync.py` | CLI tools |
| PM docs | `sophia-product-manager` | `marcus-ai-orchestrator` | README, USAGE, release notes | Operator guidance |
| QA gate | `ada-qa-agent` | `eve-qa-approver` | CI template and verification | Repeatable checks |

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: python3 .agents/scripts/validate_specs.py --feature .agents/specs/006-continuous-documentation-sync; python3 .agents/scripts/validate_doc_sync.py --strict.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.


## Tasks

- [x] `T001` Owner: `marcus-ai-orchestrator` Write Scope: update `.agents/workflows/develop.md` with continuous doc sync loop. Verification: Node 6.5 and strict gate are present. Docs: `tasks.md`, `agent-routing.md`, `verification.md`. Sync: If command sequencing or gates change, patch the command-surface docs and the agent-routing contract before closing the slice.
- [x] `T002` Owner: `knowledge-work-architecture` Write Scope: add sync manifest and sync note templates. Verification: templates exist. Docs: `plan.md`, `data-model.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T003` Owner: `alan-tech-lead` Write Scope: add `create_doc_sync_note.py` and `validate_doc_sync.py`. Verification: Python compile and strict smoke. Docs: `plan.md`, `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T004` Owner: `ada-qa-agent` Write Scope: update CI and verification docs. Verification: validation commands are repeatable. Docs: `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T005` Owner: `sophia-product-manager` Write Scope: update PM-facing README and usage guide. Verification: docs describe append/targeted patch policy. Docs: `tasks.md`, `agent-routing.md`, `verification.md`. Sync: If command sequencing or gates change, patch the command-surface docs and the agent-routing contract before closing the slice.


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
| Spec validation | `python3 .agents/scripts/validate_specs.py` | Pass | `SPEC VALIDATION PASSED: 6 feature(s)` |
| Python compile | `PYTHONPYCACHEPREFIX=/tmp/marcus-pycache python3 -m py_compile .agents/scripts/create_doc_sync_note.py .agents/scripts/validate_doc_sync.py .agents/scripts/create_development_docs.py .agents/scripts/validate_development_docs.py .agents/scripts/validate_specs.py` | Pass | Exit 0 |
| Scaffold sync files | `python3 .agents/scripts/create_development_docs.py --root /tmp/marcus-doc-sync-smoke --name "Doc Sync" --feature-id "006-continuous-documentation-sync" --force` | Creates sync manifest | Created `docs/development/sync/sync_manifest.json` |
| Create sync note | `python3 .agents/scripts/create_doc_sync_note.py --root /tmp/marcus-doc-sync-smoke --name "API Slice" --changed-files "src/api/foo.ts,docs/tasks.md,docs/development/tasks/task-doc-sync.md" --mark-reviewed` | Creates note | Created timestamped API slice sync note |
| Strict sync validation | `python3 .agents/scripts/validate_doc_sync.py --root /tmp/marcus-doc-sync-smoke --changed-files "src/api/foo.ts,docs/tasks.md,docs/development/tasks/task-doc-sync.md" --strict` | Pass | `DOC SYNC VALIDATION PASSED` |

Command or Procedure evidence must be captured for each requirement-linked check before release is claimed.


## Execution Gates

- Gate 1: `spec.md`, `plan.md`, `tasks.md`, `quickstart.md`, and `agent-routing.md` are reconciled to the current Marcus contract.
- Gate 2: the feature can be replayed through the smallest professional slice using python3 .agents/scripts/validate_specs.py --feature .agents/specs/006-continuous-documentation-sync; python3 .agents/scripts/validate_doc_sync.py --strict.
- Gate 3: `execution-brief.md` is current and the docs-to-read list is still bounded to the active slice.
- Gate 4: residual risk is explicit; no hidden dependency is being smuggled past review.


## Local Preconditions

- Required services: none beyond the local tools already referenced by this feature's verification commands.
- Required environment variables: inherit the existing project-local environment only; do not introduce new secrets during replay.
- Required commands: `python3`, `python3`, `python3`.
- Development ledger docs already exist or are being created as part of the same governed code slice.
- Changed source files can be enumerated explicitly when generating sync notes.


## Validation Path

1. Rebuild the execution brief for the active task shape:
   ```bash
   python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/006-continuous-documentation-sync --task-shape general
   ```
2. Run the primary validation commands:
   ```bash
   python3 .agents/scripts/validate_specs.py --feature .agents/specs/006-continuous-documentation-sync
   python3 .agents/scripts/validate_doc_sync.py --strict
   ```
3. Confirm the feature package is still execution-ready:
   ```bash
   python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/006-continuous-documentation-sync
   ```


## POC Rehearsal

- Smallest professional slice: execute the documented commands for `006-continuous-documentation-sync`, verify the evidence lands in `verification.md`, and confirm readiness still passes without widening context beyond the feature package.
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
- Required read: `.agents/specs/006-continuous-documentation-sync/execution-brief.md`
- Required read: `.agents/specs/006-continuous-documentation-sync/spec.md` only if the brief or failing evidence says deeper requirement context is needed.
- Required read: `.agents/specs/006-continuous-documentation-sync/plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, and `agent-routing.md` only when the current write scope or failing evidence requires the deeper artifact.
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
