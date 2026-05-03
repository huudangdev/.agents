# Execution Brief: Feature Specification: Epic-First Development Ledger

> Feature ID: `009-epic-first-development-ledger`
> Task Shape: `architecture-refactor`
> Generated From: `spec.md`, `plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, `agent-routing.md`

## 1. Operator Intent Snapshot

## 1. Purpose

Upgrade Marcus Fleet development documentation from flat buckets into a
hierarchical PM-grade knowledge graph. The new ledger must make every epic the
parent container for its features, modules, pages, tasks, and sync notes while
keeping existing V30 flat ledgers readable.


## 2. Required Behavior

## 3. Functional Requirements

- `FR-001`: New development ledgers MUST default to `topology: epic_first`.
- `FR-002`: Canonical IDs MUST follow `E-001-*`, `F-001-001-*`,
  `M-001-001-*`, `P-001-001-*`, and `T-001-001-001-*`.
- `FR-003`: Child notes MUST include `parent_epic` matching their containing
  `E-###-*` directory.
- `FR-004`: Validators MUST reject V31 flat bucket docs, orphan root files,
  malformed filenames, placeholder IDs, and frontmatter IDs that do not match
  filenames.
- `FR-005`: Sync tooling MUST support epic-local sync notes while preserving
  root sync compatibility.
- `FR-006`: Workflows, rules, templates, docs, and skills MUST direct agents to
  the V31 structure.
- `FR-007`: `/develop` MUST update or confirm docs before material source edits.
- `FR-008`: Every epic/module/feature/page/task doc MUST include Jira-style
  Story, Priority, Relationship Map, and Work Log.
- `FR-009`: Every epic MUST include QA-reviewed Issues.
- `FR-010`: Relationship maps MUST use explicit labels such as `DEPENDS_ON`,
  `BLOCKS`, `ENABLES`, `IMPLEMENTS`, `USES`, `EXTENDS`, `CONFLICTS_WITH`,
  `SUPERSEDES`, `DUPLICATES`, and `RELATES_TO`.


## 5. Acceptance Criteria

- `AC-001`: A new scaffold creates an `E-###-*` tree with canonical child files.
- `AC-002`: Strict validation rejects a V31 ledger containing a root flat
  `features/` bucket.
- `AC-003`: Strict validation rejects a child file whose `parent_epic` does not
  match the containing epic.
- `AC-004`: Legacy-flat manifests remain supported by the validator.
- `AC-005`: `/develop`, `.clinerules`, README, USAGE, release notes, and a
  dedicated skill describe V31.
- `AC-006`: Strict validation rejects docs missing Story, Priority, Relationship
  Map labels, Work Log, or epic Issues.
- `AC-007`: Doc sync validation rejects source changes whose sync note lacks
  docs-before-code evidence.


## 3. Scope Boundaries

## 7. Constraints

- Existing V30.4 content gates must remain active.
- Downstream application code is out of scope.
- Project-specific migration of `finviet-nexus` is out of scope until the
  operator approves direct edits there.


## 4. Active Work Slice

## 1. Technical Summary

Upgrade Marcus Fleet development documentation from flat buckets into a
hierarchical PM-grade knowledge graph. The new ledger must make every epic the
parent container for its features, modules, pages, tasks, and sync notes while
keeping existing V30 flat ledgers readable.


## 6. Agent Routing

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| Planning and contract reconciliation | `marcus-ai-orchestrator` | current-contract feature package | spec/readiness validation |
| QA and release gate | `ada-qa-agent` | verification evidence and release recommendation | validator output |

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: python3 .agents/scripts/validate_specs.py --feature .agents/specs/009-epic-first-development-ledger; python3 .agents/scripts/validate_development_docs.py --strict-counts.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: python3 .agents/scripts/validate_specs.py --feature .agents/specs/009-epic-first-development-ledger; python3 .agents/scripts/validate_development_docs.py --strict-counts.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.


## Tasks

- [x] `T001` Owner: `marcus-ai-orchestrator` Write Scope: update `create_development_docs.py` for V31 scaffold. Verification: scaffold creates `E-001-*` tree. Docs: `plan.md`, `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T002` Owner: `ada-qa-agent` Write Scope: update `validate_development_docs.py` for topology, ID, parent, orphan, and placeholder gates. Verification: negative smoke fails malformed ledger. Docs: `plan.md`, `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T003` Owner: `knowledge-work-architecture` Write Scope: update templates, manifest, index, and rubric. Verification: templates describe V31. Docs: `plan.md`, `data-model.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T004` Owner: `marcus-ai-orchestrator` Write Scope: update `/develop`, `.clinerules`, README, USAGE, release notes. Verification: future agents can discover V31 rules. Docs: `tasks.md`, `agent-routing.md`, `verification.md`. Sync: If command sequencing or gates change, patch the command-surface docs and the agent-routing contract before closing the slice.
- [x] `T005` Owner: `development-ledger-architect` Write Scope: add dedicated skill. Verification: skill exists and states canonical topology. Docs: `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T006` Owner: `ada-qa-agent` Write Scope: final validation evidence. Verification: `verification.md` contains command results. Docs: `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T007` Owner: `sophia-product-manager` Write Scope: enforce product-grade Story/Priority/Issues/Relationship/Work Log/docs-before-code rules. Verification: validators and templates include required sections and sync notes require docs-before-code evidence. Docs: `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.


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
| Spec validation | `python3 .agents/scripts/validate_specs.py` | Pass | Passed: 9 specs validated |
| Manifest JSON validation | `python3 -m json.tool` on manifest templates | Pass | Passed |
| V31 scaffold smoke | `create_development_docs.py --root /tmp/marcus-v31-smoke-final --name "Ledger V31 Smoke"` | Creates `E-001-ledger-v31-smoke` tree | Passed |
| V31 flat bucket negative smoke | Add root `docs/development/features/` to V31 ledger | Fail | Failed as expected: legacy flat bucket rejected |
| V31 parent mismatch negative smoke | Change child `parent_epic` to wrong epic | Fail | Failed as expected: parent mismatch rejected |
| Epic-local sync smoke | `create_doc_sync_note.py --epic-id E-001-ledger-v31-smoke` | Writes to `E-001-*/sync/` | Passed |
| Legacy compatibility smoke | `create_development_docs.py --topology legacy-flat` | Legacy mode remains reachable | Passed: no V31 topology rejection; scaffold still fails only content gates until filled |
| Product governance gate compile | Validator includes Story/Priority/relationship/work-log/epic-issues gates | Pass | Passed |
| Product governance scaffold smoke | Scaffold V31.1 and grep required sections | Required sections exist | Passed |
| Docs-before-code sync smoke | Create epic-local sync note and grep `## Docs Before Code` | Required section exists | Passed |

Command or Procedure evidence must be captured for each requirement-linked check before release is claimed.


## Execution Gates

- Gate 1: `spec.md`, `plan.md`, `tasks.md`, `quickstart.md`, and `agent-routing.md` are reconciled to the current Marcus contract.
- Gate 2: the feature can be replayed through the smallest professional slice using python3 .agents/scripts/validate_specs.py --feature .agents/specs/009-epic-first-development-ledger; python3 .agents/scripts/validate_development_docs.py --strict-counts.
- Gate 3: `execution-brief.md` is current and the docs-to-read list is still bounded to the active slice.
- Gate 4: residual risk is explicit; no hidden dependency is being smuggled past review.


## Local Preconditions

- Required services: none beyond the local tools already referenced by this feature's verification commands.
- Required environment variables: inherit the existing project-local environment only; do not introduce new secrets during replay.
- Required commands: `python3`, `python3`, `python3`.
- Use V31 epic-first topology for new ledgers unless legacy mode is explicitly requested.
- Legacy flat ledgers remain readable during migration but must not be treated as the new default.


## Validation Path

1. Rebuild the execution brief for the active task shape:
   ```bash
   python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/009-epic-first-development-ledger --task-shape architecture-refactor
   ```
2. Run the primary validation commands:
   ```bash
   python3 .agents/scripts/validate_specs.py --feature .agents/specs/009-epic-first-development-ledger
   python3 .agents/scripts/validate_development_docs.py --strict-counts
   ```
3. Confirm the feature package is still execution-ready:
   ```bash
   python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/009-epic-first-development-ledger
   ```


## POC Rehearsal

- Smallest professional slice: execute the documented commands for `009-epic-first-development-ledger`, verify the evidence lands in `verification.md`, and confirm readiness still passes without widening context beyond the feature package.
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
- Required read: `.agents/specs/009-epic-first-development-ledger/execution-brief.md`
- Required read: `.agents/specs/009-epic-first-development-ledger/spec.md` only if the brief or failing evidence says deeper requirement context is needed.
- Required read: `.agents/specs/009-epic-first-development-ledger/plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, and `agent-routing.md` only when the current write scope or failing evidence requires the deeper artifact.
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
