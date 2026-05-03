# Execution Brief: Feature Specification: Refactor Planning Command Gates

> Feature ID: `016-refactor-planning-command-gates`
> Task Shape: `architecture-refactor`
> Generated From: `spec.md`, `plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, `agent-routing.md`

## 1. Operator Intent Snapshot

## 1. Purpose

Harden `/refactor-planning` so a model can no longer treat it as an open-ended
refactor ritual with only narrative guardrails. The existing workflow already
contains two strong contract ideas: it must stop on unreconciled brownfield
docs, and it must leave a durable refactor audit trail. What is missing is the
mechanical gate that proves those conditions before and after the workflow runs.

This feature adds deterministic local validators around `/refactor-planning`.
Before the workflow begins, a readiness gate must confirm that the brownfield
docs package is present and that the development ledger meets the current
quality gate. After the workflow completes, an output gate must confirm the
refactor closeout artifacts exist. The goal is to make this risky command more
enterprise-safe without rewriting its AST, lint, or QA runtime body.


## 2. Required Behavior

## 3. Functional Requirements

- `FR-001`: The system MUST provide a readiness validator for
  `/refactor-planning` that checks the required brownfield planning docs and
  development-ledger quality gate before the command proceeds.
- `FR-002`: The system MUST provide an output validator for
  `/refactor-planning` that checks for `agents.md` and `docs/ADR_REFACTOR_LOG.md`
  before the command is considered complete.
- `FR-003`: The system MUST wire `/refactor-planning` into the public
  slash-command contract so README, `USAGE_GUIDE.md`, registry, and workflow all
  point to the same validator-backed chain.
- `FR-004`: The system MUST preserve `/refactor-planning` as a brownfield
  governance and planning command rather than rewriting the refactor engine itself.

Requirement writing rules:

- Every requirement must be testable.
- Every requirement must describe observable behavior, not implementation taste.
- Every requirement must name the actor, trigger, and outcome when relevant.


## 5. Acceptance Criteria

- `AC-001`: Given a project root with the required brownfield planning docs and
  a minimally valid development ledger, when
  `python3 scripts/validate_refactor_planning_readiness.py --root <project-root>`
  runs, then it passes.
- `AC-002`: Given a project root missing a required planning doc or failing the
  development-doc quality gate, when the same validator runs, then it fails and
  names the exact blocking input or gate.
- `AC-003`: Given a project root with non-empty `agents.md` and
  `docs/ADR_REFACTOR_LOG.md`, when
  `python3 scripts/validate_refactor_planning_outputs.py --root <project-root>`
  runs, then it passes.
- `AC-004`: Given `/refactor-planning` is published in README and
  `USAGE_GUIDE.md`, when `python3 scripts/validate_command_surface.py --root .`
  runs, then it confirms the readiness and output validator chain.
- `AC-005`: Given `/refactor-planning` hardening is added, when command-surface
  validation replays, then the broader public command contract still passes.

Acceptance criteria rules:

- Every `FR-*` must map to at least one `AC-*`.
- If a requirement cannot be verified yet, mark it in Clarifications or Risks.
- Do not use generic criteria like "works correctly" or "looks good".


## 3. Scope Boundaries

## 7. Constraints

- Constitution articles that apply: Article I, Article IV, Article IX, and
  Article XI.
- Existing files or modules in scope: `workflows/refactor-planning.md`, README,
  `USAGE_GUIDE.md`, `SLASH_COMMAND_REGISTRY.md`,
  `scripts/validate_command_surface.py`, `scripts/validate_development_docs.py`,
  and this feature package.
- Files or modules out of scope: rewriting the AST/refactor engine, executing
  the full refactor toolchain in this feature, or changing downstream app code.
- Compatibility requirements: `/refactor-planning` must stay a brownfield
  planning and governance command.
- Documentation prerequisites already reviewed: current `/refactor-planning`
  workflow, `/doc_reconcile` brownfield requirements, and the hardened public
  command surface from features `013` to `015`.
- Rollback or containment expectations: removing the two validators should
  restore the previous mixed shell/workflow contract without altering the rest
  of the refactor flow.

Out of scope:

- Replacing `npx understand-anything`, lint, typecheck, or QA runtime steps.
- Validating the quality of the actual refactor plan content.
- Adding browser or AST-runtime integration tests for this slice.


## 4. Active Work Slice

## 1. Technical Summary

This feature adds two deterministic gates to `/refactor-planning`: one
readiness validator for brownfield docs and development-ledger quality, and one
output validator for the closeout artifacts. The workflow, README,
`USAGE_GUIDE.md`, registry, and command-surface validator are updated to expose
that chain explicitly.

The refactor engine itself remains unchanged. This slice only hardens whether
the command is allowed to start and whether it can legitimately claim completion.


## 6. Agent Routing

The ownership model from `agent-routing.md` is restated here for execution.

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| Requirement and scope hardening | `sophia-product-manager` | accepted `/refactor-planning` command contract | spec validation |
| Validator and contract design | `david-systems-architect` | readiness/output gate design | plan review |
| Implementation and public-surface wiring | `marcus-ai-orchestrator` | validator scripts and command-surface updates | validator replay |
| Verification and release gate | `ada-qa-agent` | evidence-backed recommendation | fixture replay |

Execution monitoring:

- Blocking gates before implementation: `validate_specs.py --feature specs/016-refactor-planning-command-gates`
  and completion of the review loop.
- Evidence checkpoints during implementation: first replay readiness and output
  validators on fixtures, then replay command-surface validation.
- Escalation condition after repeated failure: if hardening requires executing
  the full AST/refactor runtime rather than checking command gates, stop and rescope.


## Tasks

- [x] `T001` Owner: `sophia-product-manager` Write Scope: `spec.md`,
      `verification.md`. Verification: no unresolved clarification markers and
      review-loop status is complete. Docs: `spec.md`, `verification.md`. Sync:
      patch traceability and review evidence before code work.
- [x] `T002` Owner: `david-systems-architect` Write Scope: `plan.md`,
      `data-model.md`, `contracts/`, `quickstart.md`. Verification:
      `/refactor-planning` readiness/output contract and rollback path are explicit.
      Docs: `plan.md`, `data-model.md`, contracts, `quickstart.md`. Sync:
      update traceability if the command chain changes.
- [x] `T003` Owner: `marcus-ai-orchestrator` Write Scope: `agent-routing.md`,
      `tasks.md`, `verification.md`. Verification: workstreams and write scopes
      cover validators, workflow, and public-doc wiring. Docs:
      `agent-routing.md`, `tasks.md`, `verification.md`. Sync: refresh routing
      if the command chain changes.
- [x] `T004` Owner: `marcus-ai-orchestrator` Write Scope:
      `scripts/validate_refactor_planning_readiness.py`,
      `scripts/validate_refactor_planning_outputs.py`,
      `workflows/refactor-planning.md`, `SLASH_COMMAND_REGISTRY.md`,
      `scripts/validate_command_surface.py`, README, `USAGE_GUIDE.md`.
      Verification: readiness/output validators pass on valid fixtures and
      command-surface replay stays green. Docs: `verification.md`, README,
      USAGE, registry. Sync: patch docs in the same slice as validator changes.
- [x] `T005` Owner: `ada-qa-agent` Write Scope: `verification.md`,
      `execution-brief.md`. Verification: positive replay covers readiness,
      outputs, and command-surface validation; one bounded negative proof catches
      a missing brownfield planning doc. Docs: `verification.md`,
      `execution-brief.md`. Sync: rebuild the brief after final evidence changes.


## 4.1 Dynamic Execution Signals

### Changed Files

- `scripts/validate_refactor_planning_readiness.py`
- `scripts/validate_refactor_planning_outputs.py`
- `workflows/refactor-planning.md`
- `SLASH_COMMAND_REGISTRY.md`
- `README.md`
- `USAGE_GUIDE.md`
- `scripts/validate_command_surface.py`
- `specs/016-refactor-planning-command-gates/verification.md`

### Failing Evidence

- Initial positive fixture failed until the development ledger satisfied the current strict-counts gate and the fixture exposed workflows/refactor-planning.md under the resolved root mode.

## Execution Monitoring

- Required pre-code gates: `python3 scripts/validate_specs.py --feature specs/016-refactor-planning-command-gates`
  before implementation and again before closeout.
- Mid-slice checkpoints: replay readiness validator first, then output
  validator, then command-surface validation after `/refactor-planning` wiring.
- Circuit breaker after repeated failure: after three repeated failures on the
  same readiness or output gate, stop and patch that exact contract.
- Human escalation trigger: if the slice starts requiring live AST/runtime tool
  execution instead of command gates, stop and rescope.


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
| `FR-001` | Positive + negative replay | run `python3 scripts/validate_refactor_planning_readiness.py --root <fixture>` on valid and invalid brownfield fixtures | passes on a minimally valid docs package and fails on missing docs or ledger gate failure |
| `FR-002` | Positive replay | run `python3 scripts/validate_refactor_planning_outputs.py --root <fixture>` on a valid closeout fixture | passes when `agents.md` and `docs/ADR_REFACTOR_LOG.md` exist and are non-empty |
| `FR-003` | Positive replay | run `python3 scripts/validate_command_surface.py --root .` after wiring `/refactor-planning` into docs and registry | `/refactor-planning` appears as script-backed and validator passes |
| `FR-004` | No-regression replay | rerun command-surface validation after refactor-planning hardening | broader public command contract still passes |


## Execution Gates

- Pre-implementation gates passed: feature `016` package must pass
  `validate_specs.py` before closeout.
- Plan/contract readiness confirmed: readiness/output contracts and rollback
  path are written before implementation is claimed complete.
- Documentation targets created or reconciled: `workflows/refactor-planning.md`,
  README, `USAGE_GUIDE.md`, `SLASH_COMMAND_REGISTRY.md`, and feature `016`
  package.
- Required human approvals: none beyond local `.agents` edits.


## Local Preconditions

- Required services: none beyond the local `.agents` workspace
- Required environment variables: none
- Required commands: `python3`


## Validation Path

1. Run:
   ```bash
   python3 scripts/validate_refactor_planning_readiness.py --root <project-root>
   python3 scripts/validate_refactor_planning_outputs.py --root <project-root>
   python3 scripts/validate_command_surface.py --root .
   ```
2. Confirm:
   ```text
   `/refactor-planning` fails before brownfield refactor planning on unreconciled
   docs, passes on a minimally valid docs package, and validates its closeout
   artifacts separately.
   ```


## POC Rehearsal

- Smallest end-to-end path to demonstrate: one valid readiness fixture, one
  valid output fixture, one missing-doc negative proof, and one passing
  command-surface replay.
- Evidence to capture during rehearsal: validator pass/fail output and public
  doc references to the new `/refactor-planning` chain.
- Criteria to stop and revise docs before broader execution: readiness hides the
  real blocker, output validation misses a required closeout artifact, or public
  command docs diverge from the workflow contract.


## 7. Review and Release Signals

## 10. Review Loop

Document the review rounds that must happen before implementation is allowed to
proceed.

| Round | Reviewer | Focus | Exit Criteria | Status |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Scope challenge | hardening stays limited to command gates, not an engine rewrite | Complete |
| `R2` | `sophia-product-manager` | Requirement quality | `/refactor-planning` has explicit deterministic entry and exit rules | Complete |
| `R3` | `marcus-ai-orchestrator` | Go/no-go to planning | validator-backed contract is specific enough for implementation | Complete |


## Review Loop Tasks

- `R1`: Challenge whether the gates stay focused on brownfield governance and
  closeout artifacts.
- `R2`: Confirm failures point to exact docs or artifacts rather than vague
  “refactor failed” messaging.
- `R3`: Rebuild `execution-brief.md` and reconcile `verification.md` after final
  evidence so readiness remains fresh.


## Review Rounds

| Round | Reviewer | Finding Summary | Required Changes | Disposition |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Do not rewrite the refactor engine in this slice. | Keep the hardening limited to entry and exit gates. | Accepted and applied |
| `R2` | `sophia-product-manager` | Brownfield governance must fail before any AST or refactor planning proceeds. | Make readiness validator call the current development-doc quality gate. | Accepted and applied |
| `R3` | `marcus-ai-orchestrator` | `/refactor-planning` should join the same command-surface contract as the other hardened commands. | Wire it into registry, README, USAGE, and command-surface validation. | Accepted and applied |


## Release Recommendation

- Recommendation: `GO WITH RESIDUAL RISK`
- Basis for recommendation: `/refactor-planning` now has deterministic entry and
  exit validators plus public command-surface coverage.
- Required follow-up before wider rollout: no additional `.agents` changes are
  required beyond normal review of the uncommitted diff.


## 8. Context Expansion Rules

### Task Shape Decision

- Selected task shape: `architecture-refactor`
- Why this shape: Read decisions, diagrams, affected modules, and execution boundaries first.

### Required Reads

- Required read: `agents.md`
- Required read: `.agents/memory/constitution.md`
- Required read: `.agents/specs/016-refactor-planning-command-gates/execution-brief.md`
- Required read: `.agents/specs/016-refactor-planning-command-gates/spec.md` only if the brief or failing evidence says deeper requirement context is needed.
- Required read: `.agents/specs/016-refactor-planning-command-gates/plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, and `agent-routing.md` only when the current write scope or failing evidence requires the deeper artifact.
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

- Escalate when the slice starts rewriting the AST/refactor engine instead of
  adding command gates.
- Escalate when public command docs drift away from the workflow contract.
- Escalate when readiness assumptions extend beyond the current brownfield docs
  and development-ledger quality gate.
