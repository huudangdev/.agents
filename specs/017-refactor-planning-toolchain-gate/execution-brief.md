# Execution Brief: Feature Specification: Refactor Planning Toolchain Gate

> Feature ID: `017-refactor-planning-toolchain-gate`
> Task Shape: `architecture-refactor`
> Generated From: `spec.md`, `plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, `agent-routing.md`

## 1. Operator Intent Snapshot

## 1. Purpose

`/refactor-planning` is intentionally runtime-heavy: it calls `npx`, TypeScript,
ESLint, and a dev server. In practice, a large fraction of failures are
avoidable prerequisite issues (missing Node toolchain, missing ESLint). When
these fail late, the model tends to improvise or widen scope.

This feature adds a deterministic local toolchain gate that fails fast and
names the exact missing prerequisite. The gate is designed to be safe: it does
not execute the refactor runtime, it only verifies that the required
executables exist and that ESLint is available either globally or via local
`node_modules/.bin`.


## 2. Required Behavior

## 3. Functional Requirements

- `FR-001`: The system MUST provide a local toolchain validator for
  `/refactor-planning` that checks `node`, `npm`, and `npx` are available in
  `PATH` for the target project root.
- `FR-002`: The toolchain validator MUST fail when ESLint is unavailable, where
  "available" means either `eslint` is in `PATH` or
  `<root>/node_modules/.bin/eslint*` exists.
- `FR-003`: `/refactor-planning` workflow MUST run the toolchain validator
  before calling `npx understand-anything`, `tsc`, `eslint`, or `npm run dev`.
- `FR-004`: The public command surface MUST be updated so README,
  `USAGE_GUIDE.md`, the registry, and `validate_command_surface.py` all include
  the toolchain gate for `/refactor-planning`.


## 5. Acceptance Criteria

- `AC-001`: Given a root where `node`, `npm`, and `npx` are present in `PATH` and
  ESLint is available (global or local), when
  `python3 scripts/validate_refactor_planning_toolchain.py --root <root>` runs,
  then it passes.
- `AC-002`: Given a root where ESLint is unavailable, when the same validator
  runs, then it fails and names the missing ESLint requirement.
- `AC-003`: Given README, `USAGE_GUIDE.md`, the registry, and the workflow are
  wired to the toolchain gate, when
  `python3 scripts/validate_command_surface.py --root .` runs, then it passes.


## 3. Scope Boundaries

## 7. Constraints

- In scope: `.agents/scripts/validate_refactor_planning_toolchain.py`,
  `.agents/workflows/refactor-planning.md`, `.agents/SLASH_COMMAND_REGISTRY.md`,
  `.agents/scripts/validate_command_surface.py`, README, `USAGE_GUIDE.md`, and
  this feature package.
- Out of scope: rewriting the refactor engine, running the full refactor runtime
  inside validators, or changing target project dependencies.


## 4. Active Work Slice

## 1. Technical Summary

Add a new validator script `validate_refactor_planning_toolchain.py` and wire it
into `/refactor-planning` workflow and the public command surface contract.

The validator checks:

- `node`, `npm`, `npx` in `PATH`
- ESLint availability via either global `eslint` or local `node_modules/.bin`


## 6. Agent Routing

- Owner: `marcus-ai-orchestrator`
- Support: optional QA review for bounded fixtures and error messaging
- Write scope: only `/refactor-planning` surfaces and this feature package (no
  app code, no refactor engine changes)
- Handoff: record evidence in `verification.md`, then rebuild the brief so
  `validate_execution_brief_freshness.py` stays green


## Tasks

- [x] `T001` Toolchain validator
  - Owner: `marcus-ai-orchestrator`
  - Write Scope: `.agents/scripts/validate_refactor_planning_toolchain.py`
  - Verification: `python3 -m py_compile` passes; validator fails closed with explicit messages
  - Docs: none
  - Sync: none
- [x] `T002` Workflow wiring
  - Owner: `marcus-ai-orchestrator`
  - Write Scope: `.agents/workflows/refactor-planning.md`
  - Verification: workflow contains the exact script invocation under a dedicated stage
  - Docs: `.agents/workflows/refactor-planning.md`
  - Sync: none
- [x] `T003` Public contract wiring
  - Owner: `marcus-ai-orchestrator`
  - Write Scope: `.agents/SLASH_COMMAND_REGISTRY.md`, `.agents/README.md`, `.agents/USAGE_GUIDE.md`
  - Verification: the toolchain gate is named explicitly in all public docs
  - Docs: README, `USAGE_GUIDE.md`, registry
  - Sync: rerun command-surface validation
- [x] `T004` Command-surface enforcement
  - Owner: `marcus-ai-orchestrator`
  - Write Scope: `.agents/scripts/validate_command_surface.py`
  - Verification: `python3 .agents/scripts/validate_command_surface.py --root .` passes
  - Docs: none
  - Sync: none
- [x] `T005` Evidence + brief rebuild
  - Owner: `marcus-ai-orchestrator`
  - Write Scope: `specs/017-refactor-planning-toolchain-gate/verification.md`, `execution-brief.md`
  - Verification: bounded positive/negative fixtures are recorded; freshness passes after brief rebuild
  - Docs: `verification.md`, `execution-brief.md`
  - Sync: rebuild the brief after final evidence changes


## 4.1 Dynamic Execution Signals

### Changed Files

- `specs/017-refactor-planning-toolchain-gate/plan.md`

### Failing Evidence

- Spec validator requires exact numbered plan headings (## 7/8/9) for migration/complexity/POC; adjusted without changing behavior.

## Execution Monitoring

- Stop if `validate_command_surface.py --root .` fails after wiring changes.
- Treat any change that starts executing the runtime toolchain inside the
  validator as out of scope.


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
| `FR-001` | Positive replay | run toolchain validator on a fixture root with Node tooling in PATH | passes |
| `FR-002` | Negative replay | run toolchain validator on a fixture missing ESLint | fails with explicit ESLint error |
| `FR-003` | Public contract replay | rerun `validate_command_surface.py --root .` | passes |


## Execution Gates

- Rebuild `execution-brief.md` after updating evidence in this file.


## Local Preconditions

- Required commands: `python3`, `node`, `npm`, `npx`


## Validation Path

```bash
python3 scripts/validate_refactor_planning_toolchain.py --root <project-root>
python3 scripts/validate_command_surface.py --root .
```


## POC Rehearsal

- Positive: create `<root>/node_modules/.bin/eslint` in a temp fixture root and
  replay the validator.
- Negative: remove the local ESLint marker and replay again.


## 7. Review and Release Signals

## 10. Review Loop

- `R1` Contract review: confirm the gate is non-invasive and only checks
  deterministic prerequisites.
- `R2` Wiring review: confirm workflow + registry + README + USAGE + command
  surface validation agree on the same invocation and phase.
- `R3` Verification review: confirm bounded positive/negative fixture replays are
  recorded in `verification.md` and the brief is rebuilt after evidence changes.


## Review Loop Tasks

- Ensure validator output is actionable (names missing binary/ESLint).
- Ensure docs and workflow mention the validator in the correct phase.


## Review Rounds

| Round | Reviewer | Finding Summary | Required Changes | Disposition |
| --- | --- | --- | --- | --- |
| `R1` | `marcus-ai-orchestrator` | Gate must remain non-invasive and deterministic. | Validate binaries and ESLint without executing runtime commands. | Accepted |


## Release Recommendation

- Recommendation: `GO`
- Basis: toolchain gate is wired into `/refactor-planning` workflow + public contract, and bounded positive/negative fixture replays pass.


## 8. Context Expansion Rules

### Task Shape Decision

- Selected task shape: `architecture-refactor`
- Why this shape: Read decisions, diagrams, affected modules, and execution boundaries first.

### Required Reads

- Required read: `agents.md`
- Required read: `.agents/memory/constitution.md`
- Required read: `.agents/specs/017-refactor-planning-toolchain-gate/execution-brief.md`
- Required read: `.agents/specs/017-refactor-planning-toolchain-gate/spec.md` only if the brief or failing evidence says deeper requirement context is needed.
- Required read: `.agents/specs/017-refactor-planning-toolchain-gate/plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, and `agent-routing.md` only when the current write scope or failing evidence requires the deeper artifact.
- Required read: create or reconcile the missing `docs/development/` notes before behavior-changing source edits.
- Required read: start with the changed files listed under `## 4.1 Dynamic Execution Signals` before widening to adjacent artifacts.

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

- Reviewer focus: gate must remain non-invasive and wiring must be validated by
  `validate_command_surface.py`.


## Escalation Rules

- Escalate if the toolchain gate starts executing refactor runtime commands.
- Escalate if wiring changes drift across README/USAGE/registry/workflow.
