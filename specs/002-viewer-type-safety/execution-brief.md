# Execution Brief: Feature Specification: Viewer Type Safety

> Feature ID: `002-viewer-type-safety`
> Task Shape: `frontend-behavior`
> Generated From: `spec.md`, `plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, `agent-routing.md`

## 1. Operator Intent Snapshot

## 1. Purpose

The TrustGraph viewer should be safe to maintain and safe to expose locally. Its
API must not execute vector search through a shell command string, and its
frontend should satisfy the project's own TypeScript standards instead of
carrying `any` debt.


## 2. Required Behavior

## 3. Functional Requirements

- `FR-001`: The `/api/chroma` route MUST use argv-based process execution, not
  shell command string execution.
- `FR-002`: The viewer MUST define shared types for graph nodes, graph links,
  filter modes, and vector search results.
- `FR-003`: `page.tsx`, `Inspector.tsx`, and `GraphVisualizer.tsx` MUST avoid
  explicit `any`.
- `FR-004`: Highlight calculation MUST avoid synchronous setState inside effects.
- `FR-005`: The viewer MUST pass `npm run lint` and `npm run build`.


## 5. Acceptance Criteria

- `AC-001`: Given the viewer package, when `npm run lint` runs, then it exits 0.
- `AC-002`: Given the viewer package, when `npm run build` runs, then it exits 0.
- `AC-003`: Given a malicious-looking vector query string, when `/api/chroma`
  handles it, then the text is passed as an argv value to Python rather than
  interpreted by a shell.


## 3. Scope Boundaries

## 7. Constraints

- Constitution articles that apply: Article IV, Article V, Article VII,
  Article VIII.
- Existing files or modules in scope: `.agents/trustgraph-viewer/app`,
  `.agents/trustgraph-viewer/components`, `.agents/trustgraph-viewer/lib`.
- Files or modules out of scope: visual redesign, Neo4j/Chroma runtime startup,
  TrustGraph schema changes.
- Compatibility requirements: keep existing API routes and UI behavior.


## 4. Active Work Slice

## 1. Technical Summary

Harden the TrustGraph viewer in one focused increment:

- Replace `/api/chroma` shell string execution with `execFile`.
- Add shared graph/vector TypeScript types in `lib/graphTypes.ts`.
- Type page, inspector, and graph visualizer props/state.
- Move highlight derivation from effect-setState to memoized calculation.
- Verify with `npm run lint` and `npm run build`.


## 6. Agent Routing

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| API hardening | `alan-tech-lead` | Safe `app/api/chroma/route.ts` | lint/build |
| Type cleanup | `benny-frontend-engineer` | typed viewer components | lint/build |
| Verification | `ada-qa-agent` | evidence in `verification.md` | commands exit 0 |

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: npm run lint; npm run build.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: npm run lint; npm run build.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: npm run lint; npm run build.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.


## Tasks

- [x] `T001` Owner: `alan-tech-lead` Write Scope: `app/api/chroma/route.ts`. Verification: route uses `execFile` and lint passes. Docs: `quickstart.md`, `verification.md`, `agent-routing.md`. Sync: If the implementation scope widens, update the feature package, quickstart replay path, and verification notes before additional code edits.
- [x] `T002` Owner: `benny-frontend-engineer` Write Scope: `lib/graphTypes.ts`, `app/page.tsx`, `components/Inspector.tsx`. Verification: no explicit `any` in those files and build passes. Docs: `quickstart.md`, `verification.md`, `agent-routing.md`. Sync: If the implementation scope widens, update the feature package, quickstart replay path, and verification notes before additional code edits.
- [x] `T003` Owner: `benny-frontend-engineer` Write Scope: `components/GraphVisualizer.tsx`. Verification: no explicit `any`, no setState-in-effect lint error, build passes. Docs: `quickstart.md`, `verification.md`, `agent-routing.md`. Sync: If the implementation scope widens, update the feature package, quickstart replay path, and verification notes before additional code edits.
- [x] `T004` Owner: `ada-qa-agent` Write Scope: `verification.md`. Verification: `npm run lint` and `npm run build` evidence recorded. Docs: `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.


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
| `FR-001` | Static review | Inspect `app/api/chroma/route.ts` | Uses `execFile`, not shell string |
| `FR-002` | Static review | Inspect `lib/graphTypes.ts` | Shared graph/vector types exist |
| `FR-003` | Lint | `npm run lint` in viewer | Exit 0 |
| `FR-004` | Lint | `npm run lint` in viewer | Exit 0 |
| `FR-005` | Build | `npm run build` in viewer | Exit 0 |

Command or Procedure evidence must be captured for each requirement-linked check before release is claimed.

Command or Procedure evidence must be captured for each requirement-linked check before release is claimed.


## Execution Gates

- Gate 1: `spec.md`, `plan.md`, `tasks.md`, `quickstart.md`, and `agent-routing.md` are reconciled to the current Marcus contract.
- Gate 2: the feature can be replayed through the smallest professional slice using npm run lint; npm run build.
- Gate 3: `execution-brief.md` is current and the docs-to-read list is still bounded to the active slice.
- Gate 4: residual risk is explicit; no hidden dependency is being smuggled past review.


## Local Preconditions

- Required services: none beyond the local tools already referenced by this feature's verification commands.
- Required environment variables: inherit the existing project-local environment only; do not introduce new secrets during replay.
- Required commands: `npm`, `npm`, `python3`.
- Change into `.agents/trustgraph-viewer` before running frontend commands.
- Use the local Node/npm toolchain already configured for the viewer package.


## Validation Path

1. Rebuild the execution brief for the active task shape:
   ```bash
   python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/002-viewer-type-safety --task-shape frontend-behavior
   ```
2. Run the primary validation commands:
   ```bash
   npm run lint
   npm run build
   ```
3. Confirm the feature package is still execution-ready:
   ```bash
   python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/002-viewer-type-safety
   ```


## POC Rehearsal

- Smallest professional slice: execute the documented commands for `002-viewer-type-safety`, verify the evidence lands in `verification.md`, and confirm readiness still passes without widening context beyond the feature package.
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

- Selected task shape: `frontend-behavior`
- Why this shape: Read page, feature, hook, and browser-interaction artifacts first.

### Required Reads

- Required read: `agents.md`
- Required read: `.agents/memory/constitution.md`
- Required read: `.agents/specs/002-viewer-type-safety/execution-brief.md`
- Required read: `.agents/specs/002-viewer-type-safety/spec.md` only if the brief or failing evidence says deeper requirement context is needed.
- Required read: `.agents/specs/002-viewer-type-safety/plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, and `agent-routing.md` only when the current write scope or failing evidence requires the deeper artifact.
- Required read: create or reconcile the missing `docs/development/` notes before behavior-changing source edits.

### Forbidden Default Reads

- Forbidden by default: schema and migration files
- Forbidden by default: analytics stacks
- Forbidden by default: cloud orchestration
- Forbidden by default: unrelated persistence layers

### Expansion Triggers

- Read page, feature, hook, and browser-interaction artifacts first.
- Do not widen into data-contract or infrastructure context without failing evidence.
- Load frontend, technical lead, and QA skills unless the spec explicitly says otherwise.
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
