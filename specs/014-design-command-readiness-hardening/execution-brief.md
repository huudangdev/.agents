# Execution Brief: Feature Specification: Design Command Readiness Hardening

> Feature ID: `014-design-command-readiness-hardening`
> Task Shape: `ui-only`
> Generated From: `spec.md`, `plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, `agent-routing.md`

## 1. Operator Intent Snapshot

## 1. Purpose

Harden `/design` so Phase 2 no longer depends on a model informally reading a
workflow and inferring whether planning inputs are ready or whether the design
artifacts were actually produced. Today `/design` is public, but its contract is
mostly narrative: it mentions planning docs, TrustGraph query, and the expected
outputs, yet it lacks local validator scripts that can fail early and fail
closed when required inputs or artifacts are missing.

This feature adds a deterministic command contract for `/design`. Any model
entering `.agents` should be able to run a local readiness gate before Phase 2,
produce the design artifacts, and then run a local output gate before claiming
the command is complete. The business outcome is governance clarity: design work
becomes as replayable and auditable as the stronger slash-command flows already
present in `.agents`.


## 2. Required Behavior

## 3. Functional Requirements

- `FR-001`: The system MUST provide a local readiness validator for `/design`
  that checks the required Phase 2 planning inputs before design work begins.
- `FR-002`: The system MUST provide a local output validator for `/design` that
  checks whether `docs/BRAND_GUIDELINES.md` and `docs/UI_COMPONENTS_STATE.md`
  exist and are non-empty before `/design` is considered complete.
- `FR-003`: The system MUST wire `/design` into the public slash-command
  contract so README, `USAGE_GUIDE.md`, the registry, and the workflow file all
  name the same script chain.
- `FR-004`: The system MUST preserve `/design` as a non-codegen design phase
  while adding these deterministic validator gates.

Requirement writing rules:

- Every requirement must be testable.
- Every requirement must describe observable behavior, not implementation taste.
- Every requirement must name the actor, trigger, and outcome when relevant.


## 5. Acceptance Criteria

- `AC-001`: Given a project with `agents.md`, `docs/prd.md`,
  `docs/planning/screens.md`, and `docs/planning/flows.md`, when
  `python3 scripts/validate_design_readiness.py --root <project>` runs, then it
  passes.
- `AC-002`: Given a project missing one of the required planning inputs, when
  `python3 scripts/validate_design_readiness.py --root <project>` runs, then it
  fails and names the missing file.
- `AC-003`: Given a project with non-empty `docs/BRAND_GUIDELINES.md` and
  `docs/UI_COMPONENTS_STATE.md`, when
  `python3 scripts/validate_design_outputs.py --root <project>` runs, then it
  passes.
- `AC-004`: Given `/design` is published in README and `USAGE_GUIDE.md`, when
  `python3 scripts/validate_command_surface.py --root .` runs, then it confirms
  `/design` points to the readiness and output validator chain.
- `AC-005`: Given `/design` hardening is added, when command-surface validation
  replays, then the broader public command contract still passes.

Acceptance criteria rules:

- Every `FR-*` must map to at least one `AC-*`.
- If a requirement cannot be verified yet, mark it in Clarifications or Risks.
- Do not use generic criteria like "works correctly" or "looks good".


## 3. Scope Boundaries

## 7. Constraints

- Constitution articles that apply: Article I, Article IV, Article IX, and
  Article XI.
- Existing files or modules in scope: `workflows/design.md`,
  `scripts/validate_command_surface.py`, README, `USAGE_GUIDE.md`,
  `SLASH_COMMAND_REGISTRY.md`, and this feature package.
- Files or modules out of scope: frontend application code, remote design
  tooling, and automated Figma generation.
- Compatibility requirements: `/design` must remain Phase 2 only and must not
  become a source-code workflow.
- Documentation prerequisites already reviewed: current `/design` workflow,
  README execution-command section, and `USAGE_GUIDE.md` command table plus
  script invocation rules.
- Rollback or containment expectations: removing the new validators should
  restore the old prose-only `/design` behavior without affecting other command
  chains.

Out of scope:

- Generating the actual content of `BRAND_GUIDELINES.md` or
  `UI_COMPONENTS_STATE.md` automatically.
- Converting `/marcus_init` or `/refactor-planning` in this slice.
- Adding remote design approval, screenshots, or browser-based rendering checks.


## 4. Active Work Slice

## 1. Technical Summary

This feature converts `/design` from a workflow-only public command into a
script-backed command with explicit preflight and postflight validation. The
design remains intentionally narrow: add a readiness validator for planning
inputs, add an output validator for the two Phase 2 design docs, patch the
workflow to call both scripts, and wire the new chain into the registry and the
shared command-surface validator.

The implementation stays inside `.agents` and keeps `/design` as a docs-first,
non-codegen design phase. It does not attempt to automate the content of the
design artifacts themselves.


## 6. Agent Routing

The ownership model from `agent-routing.md` is restated here for execution.

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| Requirement and scope hardening | `sophia-product-manager` | accepted `/design` command contract | spec validation |
| Validator and contract design | `david-systems-architect` | readiness/output gate design | plan review |
| Implementation and public-surface wiring | `marcus-ai-orchestrator` | validator scripts and command-surface updates | validator replay |
| Verification and release gate | `ada-qa-agent` | evidence-backed recommendation | fixture replay |

Execution monitoring:

- Blocking gates before implementation: `validate_specs.py --feature specs/014-design-command-readiness-hardening`
  and completion of the review loop.
- Evidence checkpoints during implementation: replay readiness and output
  validators on `/tmp` fixtures, then replay command-surface validation.
- Escalation condition after repeated failure: if `/design` hardening starts
  requiring nonlocal services or source-edit semantics, stop and rescope.


## Tasks

- [x] `T001` Owner: `sophia-product-manager` Write Scope: `spec.md`,
      `verification.md`. Verification: no unresolved clarification markers and
      review-loop status is complete. Docs: `spec.md`, `verification.md`. Sync:
      patch traceability and review evidence before code work.
- [x] `T002` Owner: `david-systems-architect` Write Scope: `plan.md`,
      `data-model.md`, `contracts/`, `quickstart.md`. Verification: `/design`
      input/output contract and rollback path are explicit. Docs: `plan.md`,
      `data-model.md`, contracts, `quickstart.md`. Sync: update traceability if
      command coverage changes.
- [x] `T003` Owner: `marcus-ai-orchestrator` Write Scope: `agent-routing.md`,
      `tasks.md`, `verification.md`. Verification: workstreams and write scopes
      cover validators, workflow, and public-doc wiring. Docs:
      `agent-routing.md`, `tasks.md`, `verification.md`. Sync: refresh routing
      if the command chain changes.
- [x] `T004` Owner: `marcus-ai-orchestrator` Write Scope:
      `scripts/validate_design_readiness.py`,
      `scripts/validate_design_outputs.py`, `workflows/design.md`,
      `SLASH_COMMAND_REGISTRY.md`, `scripts/validate_command_surface.py`,
      `README.md`, `USAGE_GUIDE.md`. Verification: both design validators pass
      on valid fixtures and command-surface replay stays green. Docs:
      `verification.md`, README, USAGE, registry. Sync: patch docs in the same
      slice as validator changes.
- [x] `T005` Owner: `ada-qa-agent` Write Scope: `verification.md`,
      `execution-brief.md`. Verification: positive replay covers readiness,
      outputs, and command-surface validation; one bounded negative proof catches
      a missing design input. Docs: `verification.md`, `execution-brief.md`.
      Sync: rebuild the brief after final evidence changes.


## 4.1 Dynamic Execution Signals

### Changed Files

- `scripts/validate_design_readiness.py`
- `scripts/validate_design_outputs.py`
- `workflows/design.md`
- `SLASH_COMMAND_REGISTRY.md`
- `scripts/validate_command_surface.py`
- `README.md`
- `USAGE_GUIDE.md`
- `specs/014-design-command-readiness-hardening/spec.md`
- `specs/014-design-command-readiness-hardening/plan.md`
- `specs/014-design-command-readiness-hardening/tasks.md`
- `specs/014-design-command-readiness-hardening/verification.md`

### Failing Evidence

- bounded negative proof: design readiness fails when docs/planning/flows.md is missing

## Execution Monitoring

- Required pre-code gates: `python3 scripts/validate_specs.py --feature specs/014-design-command-readiness-hardening`
  before implementation and again before closeout.
- Mid-slice checkpoints: replay readiness validator first, then output
  validator, then command-surface validation after `/design` wiring.
- Circuit breaker after repeated failure: after three repeated failures on the
  same design gate, stop and patch that exact input or output contract.
- Human escalation trigger: if `/design` hardening starts requiring browser,
  Figma, or application source-code changes, stop and rescope.


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
| `FR-001` | Positive + negative replay | run `python3 scripts/validate_design_readiness.py --root <fixture>` on valid and invalid `/tmp` fixtures | passes when required planning inputs exist, fails when one is missing |
| `FR-002` | Positive replay | run `python3 scripts/validate_design_outputs.py --root <fixture>` on a valid output fixture | passes when both design artifacts exist and are non-empty |
| `FR-003` | Positive replay | run `python3 scripts/validate_command_surface.py --root .` after wiring `/design` into docs and registry | `/design` appears as script-backed and validator passes |
| `FR-004` | No-regression replay | rerun command-surface validation after `/design` hardening and keep the workflow phase semantics intact | public command surface stays green without turning `/design` into codegen |


## Execution Gates

- Pre-implementation gates passed: feature `014` package must pass
  `validate_specs.py` before closeout.
- Plan/contract readiness confirmed: readiness/output contracts and rollback path
  are written before implementation is claimed complete.
- Documentation targets created or reconciled: `workflows/design.md`, README,
  `USAGE_GUIDE.md`, `SLASH_COMMAND_REGISTRY.md`, and feature `014` package.
- Required human approvals: none beyond local `.agents` edits.


## Local Preconditions

- Required services: none beyond the local `.agents` workspace
- Required environment variables: none
- Required commands: `python3`


## Validation Path

1. Run:
   ```bash
   python3 scripts/validate_design_readiness.py --root <project-root>
   python3 scripts/validate_design_outputs.py --root <project-root>
   python3 scripts/validate_command_surface.py --root .
   ```
2. Confirm:
   ```text
   `/design` fails early when planning inputs are missing, passes when design
   artifacts exist, and remains part of the validated public command surface.
   ```


## POC Rehearsal

- Smallest end-to-end path to demonstrate: one valid readiness fixture, one
  valid output fixture, one invalid readiness fixture, and one passing
  command-surface replay.
- Evidence to capture during rehearsal: validator pass/fail output and public
  doc references to the new `/design` chain.
- Criteria to stop and revise docs before broader execution: validators hide
  the missing file, `/design` is still missing from the registry, or the public
  command surface diverges.


## 7. Review and Release Signals

## 10. Review Loop

Document the review rounds that must happen before implementation is allowed to
proceed.

| Round | Reviewer | Focus | Exit Criteria | Status |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Scope challenge | hardening stays limited to `/design` command readiness and output gating | Complete |
| `R2` | `sophia-product-manager` | Requirement quality | the gate explains exactly what `/design` needs before and after Phase 2 | Complete |
| `R3` | `marcus-ai-orchestrator` | Go/no-go to planning | script-backed `/design` contract is specific enough for implementation | Complete |


## Review Loop Tasks

- `R1`: Challenge whether the `/design` gate remains Phase 2-only and does not
  overstep into judging design taste.
- `R2`: Confirm validator errors point to exact missing inputs or outputs.
- `R3`: Rebuild `execution-brief.md` and reconcile `verification.md` after final
  evidence so readiness remains fresh.


## Review Rounds

| Round | Reviewer | Finding Summary | Required Changes | Disposition |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Keep `/design` bounded to readiness and artifact existence, not subjective taste review. | Use file presence checks only. | Accepted and applied |
| `R2` | `sophia-product-manager` | `/design` should fail before and after the phase, not only during command-surface review. | Add both readiness and output validators. | Accepted and applied |
| `R3` | `marcus-ai-orchestrator` | `/design` must become part of the same published command contract as other slash commands. | Wire it into registry, workflow, README, USAGE, and command-surface validation. | Accepted and applied |


## Release Recommendation

- Recommendation: `GO`
- Basis for recommendation: `/design` now has deterministic local entry and exit
  gates, and the shared command surface recognizes it as a script-backed
  command.
- Required follow-up before wider rollout: none required inside `.agents`
  beyond normal review of uncommitted diffs.


## 8. Context Expansion Rules

### Task Shape Decision

- Selected task shape: `ui-only`
- Why this shape: Read UI-specific docs, target components, and QA expectations first.

### Required Reads

- Required read: `agents.md`
- Required read: `.agents/memory/constitution.md`
- Required read: `.agents/specs/014-design-command-readiness-hardening/execution-brief.md`
- Required read: `.agents/specs/014-design-command-readiness-hardening/spec.md` only if the brief or failing evidence says deeper requirement context is needed.
- Required read: `.agents/specs/014-design-command-readiness-hardening/plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, and `agent-routing.md` only when the current write scope or failing evidence requires the deeper artifact.
- Required read: create or reconcile the missing `docs/development/` notes before behavior-changing source edits.
- Required read: start with the changed files listed under `## 4.1 Dynamic Execution Signals` before widening to adjacent artifacts.

### Forbidden Default Reads

- Forbidden by default: Supabase
- Forbidden by default: SQL
- Forbidden by default: migrations
- Forbidden by default: analytics
- Forbidden by default: cloud configs
- Forbidden by default: unrelated backend services

### Expansion Triggers

- Read UI-specific docs, target components, and QA expectations first.
- Do not inspect Supabase, SQL, migrations, analytics, or infrastructure by default.
- Load frontend/design/QA skills only unless failing evidence proves wider scope.
- Read the `docs/development/` notes listed in this brief before widening beyond the current work slice.
- If the required epic/feature/module/page/task note is missing, stop and reconcile the development ledger instead of improvising from code alone.

## Review Topology

| Review Stage | Primary Reviewer | Input Artifact | Output Artifact |
| --- | --- | --- | --- |
| Spec challenge | `aurora-plan-challenger` | `spec.md` | updated `spec.md` or findings |
| Plan challenge | `alan-tech-lead` | `plan.md` | updated `plan.md` or findings |
| Verification sign-off | `ada-qa-agent` | `verification.md` | evidence-backed recommendation |


## Escalation Rules

- Escalate when `/design` starts requiring source-code or browser-runtime
  execution.
- Escalate when a validator tries to judge creative quality instead of file
  readiness or artifact existence.
- Escalate when public command docs drift away from the `/design` workflow.
