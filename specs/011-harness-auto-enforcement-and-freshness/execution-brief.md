# Execution Brief: Feature Specification: Harness Auto Enforcement and Freshness

> Feature ID: `011-harness-auto-enforcement-and-freshness`
> Task Shape: `architecture-refactor`
> Generated From: `spec.md`, `plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, `agent-routing.md`

## 1. Operator Intent Snapshot

## 1. Purpose

Upgrade `.agents` from a mostly documented governance layer into a stronger
mechanical harness. Operators already have spec validation, routing validation,
and bootstrap checks, but those protections still depend too much on an agent
remembering which commands to run and in what order. This feature adds a
one-command preflight and postflight path for the most critical execution
moments, plus a repo-wide freshness validator that catches stale workflow/docs/
script wiring before an agent starts or closes work.

The outcome is narrower than "make the whole system autonomous." It is to make
the current harness harder to forget, easier to replay, and more resistant to
doc drift. An operator should be able to run a bootstrap preflight, an
execution preflight, and an execution postflight and get a deterministic answer
about whether `.agents` is in a safe state for the next step.


## 2. Required Behavior

## 3. Functional Requirements

- `FR-001`: The system MUST provide a runnable harness preflight command for
  bootstrap and execution phases, with deterministic exit status and clear
  reporting.
- `FR-002`: The system MUST provide a runnable harness postflight command for
  execution closeout so operators can replay core validation after edits.
- `FR-003`: The system MUST provide a repo-wide harness contract validator that
  fails when core `.agents` docs, workflows, and scripts disagree about the
  required enforcement chain.
- `FR-004`: The system MUST wire the new commands into the public `.agents`
  operating surface, including bootstrap, `/develop`, `/quick_fix`, README, and
  USAGE guidance.
- `FR-005`: The system MUST remain compatible with both supported root layouts:
  project root containing `.agents`, and the standalone `.agents` repository.

Requirement writing rules:

- Every requirement must be testable.
- Every requirement must state observable behavior, not implementation taste.
- Every requirement must name the actor, trigger, and outcome when relevant.


## 5. Acceptance Criteria

- `AC-001`: Given the standalone `.agents` repository, when an operator runs
  the bootstrap preflight, then MCP sync, health classification, update brief,
  and harness freshness checks run in one deterministic chain.
- `AC-002`: Given a feature-scoped execution path, when an operator runs the
  execution preflight and postflight, then readiness and harness checks run in
  the documented order and fail non-zero on blocking problems.
- `AC-003`: Given stale or missing workflow/doc/script wiring, when the harness
  contract validator runs, then it reports the mismatched file and missing
  marker instead of silently passing.
- `AC-004`: Given updated harness scripts, when README, USAGE, `/init_brain`,
  `/develop`, and `/quick_fix` are read, then they present the same preflight
  and postflight command chain.
- `AC-005`: Given either supported root layout, when the new scripts run, then
  they resolve paths correctly without `.agents/.agents/...` regressions.

Acceptance criteria rules:

- Every `FR-*` must map to at least one `AC-*`.
- If a requirement cannot be verified yet, mark it in Clarifications or Risks.
- Do not use generic criteria like "works correctly" or "looks good".


## 3. Scope Boundaries

## 7. Constraints

- Constitution articles that apply: Article I (spec as source of truth),
  Article IV (verification evidence), Article IX (execution readiness),
  Article X (review loop), and Article XI (POC rehearsal).
- Existing files or modules in scope: `.agents/scripts/`, `README.md`,
  `USAGE_GUIDE.md`, `workflows/init_brain.md`, `workflows/develop.md`,
  `workflows/quick_fix.md`, `workflows/marcus_verify.md`, `mcp/mcp.json`, and
  the feature spec package.
- Files or modules out of scope: downstream application repositories, TrustGraph
  adapters, and unrelated skills or workflow content that do not participate in
  harness enforcement.
- Compatibility requirements: preserve the current slash-command surface and the
  two supported root layouts; avoid forcing networked services or external
  dependencies.
- Documentation prerequisites already reviewed: `memory/constitution.md`,
  `workflows/marcus_specify.md`, `workflows/develop.md`, `workflows/quick_fix.md`,
  `workflows/init_brain.md`, and `specs/010-brownfield-doc-reconcile-command/`.
- Rollback or containment expectations: the new orchestration layer must be
  removable without corrupting existing validators or feature packages.

Out of scope:

- Full observability dashboards, historical metrics storage, or automatic
  background daemons.
- Rewriting every `.agents` document for style consistency.
- Replacing existing validators that already prove useful localized behavior.


## 4. Active Work Slice

## 1. Technical Summary

This feature adds a thin orchestration layer on top of the existing `.agents`
validators and bootstrap scripts. The goal is not to invent new policy; it is
to make current policy mechanically replayable. The implementation will add
three new scripts:

- `run_harness_preflight.py`
- `run_harness_postflight.py`
- `validate_harness_contract.py`

The first two wrap existing checks into deterministic phase-oriented entry
points. The third proves that docs, workflows, and scripts still describe the
same chain. The surrounding documentation and workflow files will then be
updated so the public operating surface points to those orchestration commands
instead of expecting agents to remember several individual script invocations.


## 6. Agent Routing

The ownership model from `agent-routing.md` is restated here for implementation planning.

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| Spec and command-surface requirements | `sophia-product-manager` | accepted operator-facing contract | spec validation |
| Script architecture and contract design | `david-systems-architect` | wrapper and freshness design | review + replay |
| Harness implementation | `marcus-ai-orchestrator` | scripts and workflow/doc updates | py_compile + command replay |
| Verification and release gate | `ada-qa-agent` | evidence-backed recommendation | `verification.md` |

Execution monitoring:

- Blocking gates before implementation: `validate_specs.py --allow-clarifications`
  during spec fill, then full `validate_specs.py` before implementation.
- Evidence checkpoints during implementation: run positive replay in standalone
  `.agents` root after each major script/doc batch.
- Escalation condition after repeated failure: if the same harness script fails
  three times without new evidence, stop widening scope and patch the failing
  contract directly.


## Tasks

- [x] `T001` Owner: `sophia-product-manager` Write Scope: `spec.md`,
      `verification.md`. Verification: no unresolved clarification markers and
      review-loop status is complete. Docs: `spec.md`, `verification.md`. Sync:
      patch traceability and review evidence before code work.
- [x] `T002` Owner: `david-systems-architect` Write Scope: `plan.md`,
      `data-model.md`, `contracts/`, `quickstart.md`. Verification: wrapper
      phases, command ordering, and rollback path are explicit. Docs: `plan.md`,
      `data-model.md`, `contracts/harness-phase-contract.md`, `quickstart.md`.
      Sync: update plan and quickstart if command ordering changes.
- [x] `T003` Owner: `marcus-ai-orchestrator` Write Scope: `agent-routing.md`,
      `tasks.md`, affected workflow/docs inventory. Verification: every changed
      public surface names the same preflight/postflight chain. Docs:
      `agent-routing.md`, `tasks.md`, `verification.md`. Sync: refresh task and
      routing artifacts if script or workflow scope changes.
- [x] `T004` Owner: `marcus-ai-orchestrator` Write Scope: `scripts/path_utils.py`,
      `scripts/run_harness_preflight.py`, `scripts/run_harness_postflight.py`,
      `scripts/validate_harness_contract.py`, `scripts/check_repo_setup.sh`.
      Verification: py_compile passes and the wrappers return deterministic
      results in standalone `.agents`. Docs: `verification.md`, `README.md`,
      `USAGE_GUIDE.md`. Sync: patch docs in the same slice as script changes.
- [x] `T005` Owner: `knowledge-work-architecture` Write Scope: `README.md`,
      `USAGE_GUIDE.md`, `workflows/init_brain.md`, `workflows/develop.md`,
      `workflows/quick_fix.md`, `workflows/marcus_verify.md`. Verification:
      harness contract validator passes. Docs: same files plus `verification.md`.
      Sync: update command-surface docs and workflow instructions together.
- [x] `T006` Owner: `ada-qa-agent` Write Scope: `verification.md`,
      `execution-brief.md`. Verification: positive replay covers bootstrap,
      execution preflight, execution postflight, and freshness validation. Docs:
      `verification.md`, `execution-brief.md`. Sync: rebuild the brief after
      evidence changes.


## Execution Monitoring

- Required pre-code gates: `python3 scripts/validate_specs.py --feature specs/011-harness-auto-enforcement-and-freshness`
  before implementation and again before closeout.
- Mid-slice checkpoints: rerun standalone `.agents` replay after each major
  batch: scripts, docs/workflows, then verification evidence.
- Circuit breaker after repeated failure: after three failures of the same
  harness wrapper without new evidence, stop adding docs and patch the failing
  script or validator directly.
- Human escalation trigger: if additive wrappers require changing unrelated
  repos or introducing unsupported runtime dependencies, stop and rescope.


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
| `FR-001` | Positive replay | `python3 scripts/run_harness_preflight.py --root . --phase bootstrap` and `python3 scripts/run_harness_preflight.py --root . --phase execution --feature specs/011-harness-auto-enforcement-and-freshness` | both pass and print deterministic phase summaries |
| `FR-002` | Positive replay | `python3 scripts/run_harness_postflight.py --root . --phase execution --feature specs/011-harness-auto-enforcement-and-freshness` | pass and replay postflight checks |
| `FR-003` | Positive + negative replay | `python3 scripts/validate_harness_contract.py --root .` plus one missing-marker mutation if needed | validator fails on contract drift and passes on aligned docs |
| `FR-004` | Document inspection + replay | README/USAGE/workflow marker checks and wrapper replay | public surface matches the real command chain |
| `FR-005` | Standalone `.agents` replay | all commands above from `/Users/lequynhanh/marcus-fleet/.agents` | no `.agents/.agents/...` regressions |


## Execution Gates

- Pre-implementation gates passed: `validate_specs.py --allow-clarifications`
  during drafting, then full `validate_specs.py` before implementation.
- Plan/contract readiness confirmed: wrapper phases, docs scope, rollback path,
  and feature verification path are written before code changes.
- Documentation targets created or reconciled: feature `011` package,
  affected workflows, README, USAGE, and script inventory.
- Required human approvals: none beyond normal local file edits in `.agents`.


## Local Preconditions

- Required services: none beyond the local `.agents` workspace.
- Required environment variables: optional `FIGMA_ACCESS_TOKEN` may still be
  absent; it should remain a warning, not a blocker.
- Required commands: `python3`, `bash`.


## Validation Path

1. Run:
   ```bash
   python3 scripts/run_harness_preflight.py --root . --phase bootstrap
   python3 scripts/run_harness_preflight.py --root . --phase execution --feature specs/011-harness-auto-enforcement-and-freshness
   python3 scripts/run_harness_postflight.py --root . --phase execution --feature specs/011-harness-auto-enforcement-and-freshness
   python3 scripts/validate_harness_contract.py --root .
   ```
2. Confirm:
   ```text
   Each command exits zero, reports the underlying checks it ran, and does not
   regress into `.agents/.agents/...` path resolution.
   ```


## POC Rehearsal

- Smallest end-to-end path to demonstrate: run bootstrap preflight once, then
  run execution preflight and postflight against feature `011`, and finally run
  the harness contract validator.
- Evidence to capture during rehearsal: command outputs, py_compile success, and
  any warning-only classification such as optional `figma`.
- Criteria to stop and revise docs before broader execution: a wrapper obscures
  the failing child command, docs mention a chain different from the replayed
  one, or path resolution differs between standalone and vendored layouts.


## 7. Review and Release Signals

## 10. Review Loop

Document the review rounds that must happen before implementation is allowed to
proceed.

| Round | Reviewer | Focus | Exit Criteria | Status |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Scope challenge | orchestration stays bounded to harness enforcement, not full telemetry | Complete |
| `R2` | `sophia-product-manager` | Requirement quality | requirements and acceptance criteria name concrete commands and surfaces | Complete |
| `R3` | `marcus-ai-orchestrator` | Go/no-go to planning | spec package is stable enough for `plan.md` and code work | Complete |


## Review Loop Tasks

- `R1`: Challenge whether wrapper scripts are genuinely additive and whether
  freshness validation stays bounded to real contract files.
- `R2`: Confirm bootstrap and execution phases use deterministic command order
  and expose the underlying failure cleanly.
- `R3`: Rebuild `execution-brief.md` and reconcile `verification.md` after final
  evidence so readiness remains fresh.


## Review Rounds

| Round | Reviewer | Finding Summary | Required Changes | Disposition |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Keep scope on orchestration and freshness; do not slide into full telemetry platform work. | Add explicit out-of-scope and POC boundary lines. | Accepted and applied |
| `R2` | `ada-qa-agent` | Wrappers are only useful if they expose the underlying failing command and preserve exit semantics. | Require deterministic summaries and direct command replay evidence. | Accepted and applied |
| `R3` | `marcus-ai-orchestrator` | The docs package must be ready before script edits begin. | Complete plan, tasks, quickstart, and contract artifacts first. | Accepted and applied |


## Release Recommendation

- Recommendation: `GO`, `GO WITH RESIDUAL RISK`, or `NO-GO`
- Recommendation: `GO WITH RESIDUAL RISK`
- Basis for recommendation: wrapper scripts, repo-wide freshness validation, and
  workflow/doc wiring all replay successfully in the standalone `.agents`
  repository. The negative fixture also proves the freshness validator fails on
  a real contract drift.
- Required follow-up before wider rollout: add harness observability metrics in
  a later feature if the team wants trend data rather than command-by-command replay.


## 8. Context Expansion Rules

### Task Shape Decision

- Selected task shape: `architecture-refactor`
- Why this shape: Read decisions, diagrams, affected modules, and execution boundaries first.

### Required Reads

- Required read: `agents.md`
- Required read: `.agents/memory/constitution.md`
- Required read: `.agents/specs/011-harness-auto-enforcement-and-freshness/execution-brief.md`
- Required read: `.agents/specs/011-harness-auto-enforcement-and-freshness/spec.md` only if the brief or failing evidence says deeper requirement context is needed.
- Required read: `.agents/specs/011-harness-auto-enforcement-and-freshness/plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, and `agent-routing.md` only when the current write scope or failing evidence requires the deeper artifact.
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

| Review Stage | Primary Reviewer | Input Artifact | Output Artifact |
| --- | --- | --- | --- |
| Spec challenge | `aurora-plan-challenger` | `spec.md` | updated `spec.md` or findings |
| Plan challenge | `alan-tech-lead` | `plan.md` | updated `plan.md` or findings |
| Verification sign-off | `ada-qa-agent` | `verification.md` | evidence-backed recommendation |


## Escalation Rules

- Escalate when documentation prerequisites are missing or misleading.
- Escalate when verification fails repeatedly without new evidence.
- Escalate when write scope conflicts with another agent's ownership.
