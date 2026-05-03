# Execution Brief: Feature Specification: Marcus Init Output Contract Hardening

> Feature ID: `015-marcus-init-output-contract-hardening`
> Task Shape: `architecture-refactor`
> Generated From: `spec.md`, `plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, `agent-routing.md`

## 1. Operator Intent Snapshot

## 1. Purpose

Harden `/marcus_init` so project bootstrapping no longer ends with a purely
narrative claim that a workspace was scaffolded correctly. The workflow already
describes a deterministic shell scaffold, root-memory creation, and PRD draft
seeding, but nothing in `.agents` currently validates the resulting project
root before the command is considered complete.

This feature adds a local scaffold-output validator and wires it into the public
slash-command contract. The goal is narrow and practical: any model should be
able to inspect `/marcus_init`, know which outputs must exist, and validate that
the scaffolded project root contains them before claiming the bootstrap phase
worked.


## 2. Required Behavior

## 3. Functional Requirements

- `FR-001`: The system MUST provide a local validator for `/marcus_init` that
  checks the expected scaffold outputs for a generated project root.
- `FR-002`: The system MUST wire `/marcus_init` into the public slash-command
  contract so README, `USAGE_GUIDE.md`, registry, and workflow file all expose
  the output-validation step.
- `FR-003`: The system MUST fail validation when required scaffold outputs such
  as `agents.md`, `.agents/agents.md`, `.clinerules`, or `docs/prd_draft.md`
  are missing or empty.
- `FR-004`: The system MUST keep `/marcus_init` scoped to bootstrap verification
  and avoid expanding it into a general project-generator rewrite.

Requirement writing rules:

- Every requirement must be testable.
- Every requirement must describe observable behavior, not implementation taste.
- Every requirement must name the actor, trigger, and outcome when relevant.


## 5. Acceptance Criteria

- `AC-001`: Given a scaffold root with `docs/`, `.agents/`, `.clinerules`,
  `agents.md`, `.agents/agents.md`, and `docs/prd_draft.md`, when
  `python3 scripts/validate_marcus_init_outputs.py --root <project-root>` runs,
  then it passes.
- `AC-002`: Given a scaffold root missing one required output, when the same
  validator runs, then it fails and names the missing path.
- `AC-003`: Given `/marcus_init` is published in README and `USAGE_GUIDE.md`,
  when `python3 scripts/validate_command_surface.py --root .` runs, then it
  confirms `/marcus_init` points to the output validator chain.
- `AC-004`: Given `/marcus_init` hardening is added, when command-surface
  validation replays, then the broader public contract still passes.

Acceptance criteria rules:

- Every `FR-*` must map to at least one `AC-*`.
- If a requirement cannot be verified yet, mark it in Clarifications or Risks.
- Do not use generic criteria like "works correctly" or "looks good".


## 3. Scope Boundaries

## 7. Constraints

- Constitution articles that apply: Article I, Article IV, Article IX, and
  Article XI.
- Existing files or modules in scope: `workflows/marcus_init.md`, README,
  `USAGE_GUIDE.md`, `SLASH_COMMAND_REGISTRY.md`,
  `scripts/validate_command_surface.py`, and this feature package.
- Files or modules out of scope: rewriting the bootstrap shell chain, changing
  downstream scaffolded app code, or adding remote project templating.
- Compatibility requirements: `/marcus_init` must stay a bootstrap command and
  must not become a generic repo mutation engine.
- Documentation prerequisites already reviewed: current `/marcus_init`
  workflow, public command docs, and registry state after features `013` and
  `014`.
- Rollback or containment expectations: removing the validator and contract
  markers should restore the previous workflow-only `/marcus_init` behavior.

Out of scope:

- Replacing the shell scaffold with a new Python orchestrator.
- Automatically validating the quality of the seeded PRD content.
- Converting `/refactor-planning` in this slice.


## 4. Active Work Slice

## 1. Technical Summary

This feature converts `/marcus_init` from a workflow-only public command into a
command with deterministic closeout validation. The implementation is narrow:
add one output validator for scaffolded project roots, patch the workflow to run
it after PRD draft seeding, and wire the validator into the shared public
command contract.

The shell-based scaffold remains intact. This slice only hardens the proof that
the expected outputs exist before the command is considered complete.


## 6. Agent Routing

The ownership model from `agent-routing.md` is restated here for execution.

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| Requirement and scope hardening | `sophia-product-manager` | accepted `/marcus_init` output contract | spec validation |
| Validator and contract design | `david-systems-architect` | scaffold-output gate design | plan review |
| Implementation and public-surface wiring | `marcus-ai-orchestrator` | output validator and command-surface updates | validator replay |
| Verification and release gate | `ada-qa-agent` | evidence-backed recommendation | fixture replay |

Execution monitoring:

- Blocking gates before implementation: `validate_specs.py --feature specs/015-marcus-init-output-contract-hardening`
  and completion of the review loop.
- Evidence checkpoints during implementation: replay the output validator on a
  valid fixture, then replay command-surface validation after `/marcus_init`
  wiring.
- Escalation condition after repeated failure: if the work starts requiring a
  rewrite of the shell scaffold rather than a closeout validator, stop and
  rescope.


## Tasks

- [x] `T001` Owner: `sophia-product-manager` Write Scope: `spec.md`,
      `verification.md`. Verification: no unresolved clarification markers and
      review-loop status is complete. Docs: `spec.md`, `verification.md`. Sync:
      patch traceability and review evidence before code work.
- [x] `T002` Owner: `david-systems-architect` Write Scope: `plan.md`,
      `data-model.md`, `contracts/`, `quickstart.md`. Verification:
      `/marcus_init` output contract and rollback path are explicit. Docs:
      `plan.md`, `data-model.md`, contracts, `quickstart.md`. Sync: update
      traceability if scaffold expectations change.
- [x] `T003` Owner: `marcus-ai-orchestrator` Write Scope: `agent-routing.md`,
      `tasks.md`, `verification.md`. Verification: workstreams and write scopes
      cover output validation, workflow, and public-doc wiring. Docs:
      `agent-routing.md`, `tasks.md`, `verification.md`. Sync: refresh routing
      if the command chain changes.
- [x] `T004` Owner: `marcus-ai-orchestrator` Write Scope:
      `scripts/validate_marcus_init_outputs.py`, `workflows/marcus_init.md`,
      `SLASH_COMMAND_REGISTRY.md`, `scripts/validate_command_surface.py`,
      `README.md`, `USAGE_GUIDE.md`. Verification: output validator passes on a
      valid fixture and command-surface replay stays green. Docs:
      `verification.md`, README, USAGE, registry. Sync: patch docs in the same
      slice as validator changes.
- [x] `T005` Owner: `ada-qa-agent` Write Scope: `verification.md`,
      `execution-brief.md`. Verification: positive replay covers output
      validation and command-surface replay; one bounded negative proof catches
      a missing scaffold output. Docs: `verification.md`, `execution-brief.md`.
      Sync: rebuild the brief after final evidence changes.


## 4.1 Dynamic Execution Signals

### Changed Files

- `scripts/validate_marcus_init_outputs.py`
- `workflows/marcus_init.md`
- `SLASH_COMMAND_REGISTRY.md`
- `scripts/validate_command_surface.py`
- `README.md`
- `USAGE_GUIDE.md`
- `specs/015-marcus-init-output-contract-hardening/spec.md`
- `specs/015-marcus-init-output-contract-hardening/plan.md`
- `specs/015-marcus-init-output-contract-hardening/tasks.md`
- `specs/015-marcus-init-output-contract-hardening/verification.md`

### Failing Evidence

- bounded negative proof: marcus_init output validation fails when docs/prd_draft.md is missing

## Execution Monitoring

- Required pre-code gates: `python3 scripts/validate_specs.py --feature specs/015-marcus-init-output-contract-hardening`
  before implementation and again before closeout.
- Mid-slice checkpoints: replay output validation first, then replay
  command-surface validation after `/marcus_init` wiring.
- Circuit breaker after repeated failure: after three repeated failures on the
  same scaffold-output marker, stop and patch that exact output contract.
- Human escalation trigger: if hardening `/marcus_init` starts requiring a full
  scaffold-engine rewrite or remote bootstrap integration, stop and rescope.


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
| `FR-001` | Positive replay | run `python3 scripts/validate_marcus_init_outputs.py --root <fixture>` on a valid scaffold fixture | passes when required scaffold outputs exist |
| `FR-002` | Positive replay | run `python3 scripts/validate_command_surface.py --root .` after wiring `/marcus_init` into docs and registry | `/marcus_init` appears as script-backed and validator passes |
| `FR-003` | Negative replay | remove one required output from a bounded `/tmp` fixture and rerun `validate_marcus_init_outputs.py` | validator fails on the missing or empty path |
| `FR-004` | No-regression replay | rerun command-surface validation after `/marcus_init` hardening | public command contract stays green |


## Execution Gates

- Pre-implementation gates passed: feature `015` package must pass
  `validate_specs.py` before closeout.
- Plan/contract readiness confirmed: output contract, validator, and rollback
  path are written before implementation is claimed complete.
- Documentation targets created or reconciled: `workflows/marcus_init.md`,
  README, `USAGE_GUIDE.md`, `SLASH_COMMAND_REGISTRY.md`, and feature `015`
  package.
- Required human approvals: none beyond local `.agents` edits.


## Local Preconditions

- Required services: none beyond the local `.agents` workspace
- Required environment variables: none
- Required commands: `python3`


## Validation Path

1. Run:
   ```bash
   python3 scripts/validate_marcus_init_outputs.py --root <scaffolded-project-root>
   python3 scripts/validate_command_surface.py --root .
   ```
2. Confirm:
   ```text
   `/marcus_init` closeout fails when required scaffold outputs are missing and
   passes when the expected project root artifacts exist.
   ```


## POC Rehearsal

- Smallest end-to-end path to demonstrate: one valid scaffold fixture, one
  missing-output negative proof, and one passing command-surface replay.
- Evidence to capture during rehearsal: validator pass/fail output and public
  doc references to the new `/marcus_init` chain.
- Criteria to stop and revise docs before broader execution: validator errors
  are vague, `/marcus_init` is still workflow-only in the registry, or public
  docs drift from the workflow contract.


## 7. Review and Release Signals

## 10. Review Loop

Document the review rounds that must happen before implementation is allowed to
proceed.

| Round | Reviewer | Focus | Exit Criteria | Status |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Scope challenge | hardening stays limited to scaffold-output validation | Complete |
| `R2` | `sophia-product-manager` | Requirement quality | `/marcus_init` output contract is explicit and testable | Complete |
| `R3` | `marcus-ai-orchestrator` | Go/no-go to planning | script-backed `/marcus_init` closeout is specific enough for implementation | Complete |


## Review Loop Tasks

- `R1`: Challenge whether the new gate stays limited to scaffold outputs.
- `R2`: Confirm validator errors point to exact missing or empty artifacts.
- `R3`: Rebuild `execution-brief.md` and reconcile `verification.md` after final
  evidence so readiness remains fresh.


## Review Rounds

| Round | Reviewer | Finding Summary | Required Changes | Disposition |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Do not rewrite the shell scaffold in this slice. | Keep the hardening limited to closeout validation. | Accepted and applied |
| `R2` | `sophia-product-manager` | `/marcus_init` needs a deterministic notion of success, not just shell prose. | Add a validator for required scaffold outputs. | Accepted and applied |
| `R3` | `marcus-ai-orchestrator` | `/marcus_init` should join the same public command contract as the other hardened commands. | Wire it into registry, README, USAGE, and command-surface validation. | Accepted and applied |


## Release Recommendation

- Recommendation: `GO`
- Basis for recommendation: `/marcus_init` now has deterministic scaffold-output
  validation and shared command-surface coverage.
- Required follow-up before wider rollout: none required inside `.agents`
  beyond normal review of uncommitted diffs.


## 8. Context Expansion Rules

### Task Shape Decision

- Selected task shape: `architecture-refactor`
- Why this shape: Read decisions, diagrams, affected modules, and execution boundaries first.

### Required Reads

- Required read: `agents.md`
- Required read: `.agents/memory/constitution.md`
- Required read: `.agents/specs/015-marcus-init-output-contract-hardening/execution-brief.md`
- Required read: `.agents/specs/015-marcus-init-output-contract-hardening/spec.md` only if the brief or failing evidence says deeper requirement context is needed.
- Required read: `.agents/specs/015-marcus-init-output-contract-hardening/plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, and `agent-routing.md` only when the current write scope or failing evidence requires the deeper artifact.
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

- Escalate when `/marcus_init` hardening starts replacing the shell scaffold
  rather than validating its outputs.
- Escalate when public command docs drift away from the workflow contract.
- Escalate when validator coverage starts assuming framework-specific files not
  present in the workflow contract.
