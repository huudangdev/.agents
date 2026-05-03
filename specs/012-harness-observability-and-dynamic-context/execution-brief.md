# Execution Brief: Feature Specification: Harness Observability and Dynamic Context

> Feature ID: `012-harness-observability-and-dynamic-context`
> Task Shape: `architecture-refactor`
> Generated From: `spec.md`, `plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, `agent-routing.md`

## 1. Operator Intent Snapshot

## 1. Purpose

Extend the `.agents` harness so it not only enforces checks, but also leaves a
small, structured trail of what happened and why. Feature `011` added replayable
preflight/postflight wrappers and a freshness validator. This next slice adds
lightweight structured observability for those wrapper runs and improves
`execution-brief.md` so it can carry dynamic execution signals such as changed
files and failing evidence.

The goal is practical, not grandiose: when a harness phase runs, operators
should be able to inspect a structured log without re-reading raw console text,
and when a feature brief is rebuilt, it should optionally foreground the exact
files and failure signals driving the current slice. This reduces both harness
blind spots and unnecessary context loading.


## 2. Required Behavior

## 3. Functional Requirements

- `FR-001`: The system MUST emit a structured local log entry for every harness
  preflight and postflight run, including phase, feature, command list, and
  outcome.
- `FR-002`: The system MUST record per-command status within a harness run so a
  reviewer can tell which command passed, warned, or failed first.
- `FR-003`: The execution-brief builder MUST accept optional changed-file input
  and include it in the generated brief as dynamic context.
- `FR-004`: The execution-brief builder MUST accept optional failing-evidence
  input and include it in the generated brief as dynamic context.
- `FR-005`: The updated dynamic context and structured logging MUST preserve the
  current bounded-context philosophy rather than widening default reads.

Requirement writing rules:

- Every requirement must be testable.
- Every requirement must describe observable behavior, not implementation taste.
- Every requirement must name the actor, trigger, and outcome when relevant.


## 5. Acceptance Criteria

- `AC-001`: Given a harness preflight or postflight run in standalone `.agents`,
  when the command completes, then a structured log file is appended with run
  metadata and per-command results.
- `AC-002`: Given a failing harness command, when the wrapper exits non-zero,
  then the log still records the failing command and its exit code.
- `AC-003`: Given `build_execution_brief.py --changed-files ...`, when the brief
  is generated, then it includes those files in a dynamic context section and
  prioritizes them as current execution signals.
- `AC-004`: Given `build_execution_brief.py --failing-evidence ...`, when the
  brief is generated, then it includes a bounded summary of that evidence in the
  brief.
- `AC-005`: Given no dynamic inputs, when the brief is generated, then current
  behavior remains valid and no required sections disappear.

Acceptance criteria rules:

- Every `FR-*` must map to at least one `AC-*`.
- If a requirement cannot be verified yet, mark it in Clarifications or Risks.
- Do not use generic criteria like "works correctly" or "looks good".


## 3. Scope Boundaries

## 7. Constraints

- Constitution articles that apply: Article I, Article IV, Article IX, and
  Article XI.
- Existing files or modules in scope: `scripts/run_harness_preflight.py`,
  `scripts/run_harness_postflight.py`, `scripts/build_execution_brief.py`,
  shared script helpers, README/USAGE/workflows, and this feature package.
- Files or modules out of scope: downstream repos, long-term metrics backends,
  TrustGraph, and non-harness agent memory systems.
- Compatibility requirements: preserve wrapper compatibility from feature `011`
  and keep `build_execution_brief.py` working when no new flags are passed.
- Documentation prerequisites already reviewed: feature `011` package and
  current `build_execution_brief.py` contract.
- Rollback or containment expectations: logs can be ignored or deleted without
  breaking wrappers; optional brief flags must remain additive.

Out of scope:

- Full dashboards, alerting, or background telemetry pipelines.
- Semantic ranking of changed files beyond straightforward listing and grouping.
- Automatic retrieval from GitHub, CI, or external observability systems.


## 4. Active Work Slice

## 1. Technical Summary

This feature adds two bounded capabilities on top of the harness introduced in
feature `011`:

- structured JSONL logging for harness wrapper runs
- optional dynamic context inputs for `build_execution_brief.py`

The implementation will reuse local helpers, write append-only logs under
`.agents/logs/harness/`, and extend the execution brief generator with additive
flags such as `--changed-files` and `--failing-evidence`. The generated brief
will gain a small dynamic-signal section without changing the required core
sections already enforced by validators.


## 6. Agent Routing

The ownership model from `agent-routing.md` is restated here for execution.

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| Requirements and bounded scope | `sophia-product-manager` | accepted feature contract | spec validation |
| Logging and brief design | `david-systems-architect` | helper design and contracts | plan review |
| Script implementation | `marcus-ai-orchestrator` | JSONL logging and dynamic brief inputs | replay + py_compile |
| Verification and release gate | `ada-qa-agent` | evidence-backed recommendation | verification replay |

Execution monitoring:

- Blocking gates before implementation: `validate_specs.py --feature specs/012-harness-observability-and-dynamic-context`
  and review-loop completion.
- Evidence checkpoints during implementation: wrapper replay after logging
  changes, then brief rebuild replay with dynamic inputs.
- Escalation condition after repeated failure: if logging or brief generation
  breaks required sections three times without new evidence, stop and patch the
  last changed helper or builder layer directly.


## Tasks

- [x] `T001` Owner: `sophia-product-manager` Write Scope: `spec.md`,
      `verification.md`. Verification: no unresolved clarification markers and
      review-loop status is complete. Docs: `spec.md`, `verification.md`. Sync:
      patch traceability and review evidence before code work.
- [x] `T002` Owner: `david-systems-architect` Write Scope: `plan.md`,
      `data-model.md`, `contracts/`, `quickstart.md`. Verification: log schema,
      dynamic context inputs, and rollback path are explicit. Docs: `plan.md`,
      `data-model.md`, contracts, `quickstart.md`. Sync: update plan if the log
      shape or brief flags change.
- [x] `T003` Owner: `marcus-ai-orchestrator` Write Scope: `agent-routing.md`,
      `tasks.md`, `verification.md`. Verification: workstreams and write scopes
      cover wrappers, helper layer, and brief generator. Docs: `agent-routing.md`,
      `tasks.md`, `verification.md`. Sync: refresh routing if implementation scope changes.
- [x] `T004` Owner: `marcus-ai-orchestrator` Write Scope: shared helper layer,
      harness wrappers, `build_execution_brief.py`. Verification: py_compile
      passes, wrapper logs are written, and briefs rebuild with optional dynamic
      inputs. Docs: `verification.md`, README/USAGE if flags or log paths are exposed.
      Sync: patch docs in the same slice as code changes.
- [x] `T005` Owner: `knowledge-work-architecture` Write Scope: `README.md`,
      `USAGE_GUIDE.md`, and any workflow text that should mention dynamic brief
      inputs or log paths. Verification: docs mention the new log location and
      optional brief flags consistently. Docs: same files plus `verification.md`.
      Sync: update docs after code behavior stabilizes.
- [x] `T006` Owner: `ada-qa-agent` Write Scope: `verification.md`,
      `execution-brief.md`. Verification: positive replay covers logs and
      dynamic brief inputs; one bounded negative proof catches bad contract or
      malformed inputs. Docs: `verification.md`, `execution-brief.md`. Sync:
      rebuild the brief after evidence changes.


## 4.1 Dynamic Execution Signals

### Changed Files

- `scripts/build_execution_brief.py`
- `scripts/run_harness_preflight.py`
- `scripts/run_harness_postflight.py`
- `scripts/path_utils.py`
- `scripts/validate_harness_contract.py`
- `README.md`
- `USAGE_GUIDE.md`
- `workflows/init_brain.md`
- `workflows/develop.md`
- `workflows/quick_fix.md`
- `workflows/marcus_tasks.md`
- `workflows/marcus_review.md`
- `workflows/marcus_rehearse.md`
- `workflows/marcus_verify.md`
- `specs/012-harness-observability-and-dynamic-context/verification.md`
- `specs/012-harness-observability-and-dynamic-context/tasks.md`

### Failing Evidence

- bounded negative proof: validate_harness_contract.py fails when bootstrap workflow drops the harness log marker

## Execution Monitoring

- Required pre-code gates: `python3 scripts/validate_specs.py --feature specs/012-harness-observability-and-dynamic-context`
  before implementation and again before closeout.
- Mid-slice checkpoints: replay wrappers after logging changes, then replay
  brief generation with dynamic inputs after builder changes.
- Circuit breaker after repeated failure: after three repeated failures in the
  same helper or builder path, stop and patch that layer directly.
- Human escalation trigger: if the slice starts requiring external telemetry
  systems, git daemons, or unrelated repo integration, stop and rescope.


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
| `FR-001` | Positive replay | run preflight and postflight, then inspect `.agents/logs/harness/*.jsonl` | log entry exists for each wrapper run |
| `FR-002` | Positive + negative replay | inspect JSONL event after a pass and after a bounded negative case | per-command status and first failing command are recorded |
| `FR-003` | Positive replay | `python3 scripts/build_execution_brief.py --feature specs/012-harness-observability-and-dynamic-context --task-shape architecture-refactor --changed-files "scripts/build_execution_brief.py,scripts/run_harness_preflight.py"` | brief includes changed files section |
| `FR-004` | Positive replay | `python3 scripts/build_execution_brief.py ... --failing-evidence "validate_harness_contract.py failed on missing marker"` | brief includes failing-evidence section |
| `FR-005` | No-regression replay | rerun readiness and freshness after dynamic brief generation | required sections remain and validators still pass |


## Execution Gates

- Pre-implementation gates passed: spec package must pass `validate_specs.py`
  before code work.
- Plan/contract readiness confirmed: log schema and dynamic brief contracts are
  written before scripts change.
- Documentation targets created or reconciled: feature `012` package and any
  exposed docs/workflow references.
- Required human approvals: none beyond local `.agents` edits.


## Local Preconditions

- Required services: none beyond the local `.agents` workspace.
- Required environment variables: none required for the feature itself; optional
  `FIGMA_ACCESS_TOKEN` may still warn during bootstrap health checks.
- Required commands: `python3`, `bash`.


## Validation Path

1. Run:
   ```bash
   python3 scripts/run_harness_preflight.py --root . --phase execution --feature specs/012-harness-observability-and-dynamic-context
   python3 scripts/build_execution_brief.py --feature specs/012-harness-observability-and-dynamic-context --task-shape architecture-refactor --changed-files "scripts/build_execution_brief.py,scripts/run_harness_preflight.py" --failing-evidence "validate_harness_contract.py failed on missing marker"
   python3 scripts/run_harness_postflight.py --root . --phase execution --feature specs/012-harness-observability-and-dynamic-context
   ```
2. Confirm:
   ```text
   Wrapper runs append structured JSONL entries under `.agents/logs/harness/`,
   and the rebuilt brief contains bounded changed-file and failing-evidence context.
   ```


## POC Rehearsal

- Smallest end-to-end path to demonstrate: one execution wrapper run that logs
  a JSONL event and one brief rebuild with both optional dynamic inputs.
- Evidence to capture during rehearsal: JSONL log lines, brief section output,
  and readiness/freshness replay after the rebuild.
- Criteria to stop and revise docs before broader execution: logs hide the
  failing command, dynamic brief sections widen default reads, or validators
  stop passing.


## 7. Review and Release Signals

## 10. Review Loop

Document the review rounds that must happen before implementation is allowed to
proceed.

| Round | Reviewer | Focus | Exit Criteria | Status |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Scope challenge | logging stays lightweight and local; dynamic context stays bounded | Complete |
| `R2` | `sophia-product-manager` | Requirement quality | flags, logs, and acceptance criteria are concrete and replayable | Complete |
| `R3` | `marcus-ai-orchestrator` | Go/no-go to planning | spec package is stable enough for `plan.md` and script work | Complete |


## Review Loop Tasks

- `R1`: Challenge whether the log payload stays minimal and whether dynamic
  context remains optional and bounded.
- `R2`: Confirm wrappers still expose the underlying failing command and that
  brief sections remain validator-compatible.
- `R3`: Rebuild `execution-brief.md` and reconcile `verification.md` after final
  evidence so readiness remains fresh.


## Review Rounds

| Round | Reviewer | Finding Summary | Required Changes | Disposition |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Keep logging local and additive; do not expand into a telemetry platform. | Add explicit out-of-scope and bounded log wording. | Accepted and applied |
| `R2` | `ada-qa-agent` | Dynamic brief inputs are useful only if validators still pass and default bounded reads do not widen. | Require no-regression replay after dynamic brief generation. | Accepted and applied |
| `R3` | `marcus-ai-orchestrator` | The spec package must be ready before helper and builder edits. | Complete plan, tasks, quickstart, and contracts first. | Accepted and applied |


## Release Recommendation

- Recommendation: `GO`
- Basis for recommendation: wrapper logs are emitted on both execution phases,
  dynamic brief inputs rebuild cleanly, public docs/workflows mention the new
  behavior, and readiness/freshness/contract gates all pass after the update.
- Required follow-up before wider rollout: none required inside `.agents`
  beyond normal review of uncommitted diffs.


## 8. Context Expansion Rules

### Task Shape Decision

- Selected task shape: `architecture-refactor`
- Why this shape: Read decisions, diagrams, affected modules, and execution boundaries first.

### Required Reads

- Required read: `agents.md`
- Required read: `.agents/memory/constitution.md`
- Required read: `.agents/specs/012-harness-observability-and-dynamic-context/execution-brief.md`
- Required read: `.agents/specs/012-harness-observability-and-dynamic-context/spec.md` only if the brief or failing evidence says deeper requirement context is needed.
- Required read: `.agents/specs/012-harness-observability-and-dynamic-context/plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, and `agent-routing.md` only when the current write scope or failing evidence requires the deeper artifact.
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

| Review Stage | Primary Reviewer | Input Artifact | Output Artifact |
| --- | --- | --- | --- |
| Spec challenge | `aurora-plan-challenger` | `spec.md` | updated `spec.md` or findings |
| Plan challenge | `alan-tech-lead` | `plan.md` | updated `plan.md` or findings |
| Verification sign-off | `ada-qa-agent` | `verification.md` | evidence-backed recommendation |


## Escalation Rules

- Escalate when documentation prerequisites are missing or misleading.
- Escalate when verification fails repeatedly without new evidence.
- Escalate when write scope conflicts with another agent's ownership.
