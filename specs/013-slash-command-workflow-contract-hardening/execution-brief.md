# Execution Brief: Feature Specification: Slash Command Workflow Contract Hardening

> Feature ID: `013-slash-command-workflow-contract-hardening`
> Task Shape: `architecture-refactor`
> Generated From: `spec.md`, `plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, `agent-routing.md`

## 1. Operator Intent Snapshot

## 1. Purpose

Harden the `.agents` operating surface so published slash commands are no longer
described only by prose spread across README, `USAGE_GUIDE.md`, and workflow
files. The immediate problem is ambiguity: some commands are visible in one
public doc but not another, some workflow files call important scripts without a
single source of truth, and validators only cover a narrow subset of the
surface. That leaves too much room for model guesswork, especially when a new
model or a shallow context window tries to infer which script should run next.

This feature establishes a deterministic slash-command contract for the
published `.agents` surface. The outcome must be concrete: if a command is
presented as supported, the repo must show which workflow file owns it, which
script or gate chain it must invoke, and which validator proves the public docs
and workflow still agree. The business value is governance quality. Any model
should be able to read the contract, follow the same execution chain, and fail
closed when the contract drifts instead of improvising enterprise-critical
workflow behavior.


## 2. Required Behavior

## 3. Functional Requirements

- `FR-001`: The system MUST define a public slash-command registry for the
  published `.agents` commands, including the owning workflow file and required
  script or gate chain for each script-backed command.
- `FR-002`: The system MUST fail validation when README, `USAGE_GUIDE.md`, the
  registry, and workflow files disagree about a published slash command or its
  required script chain.
- `FR-003`: The system MUST normalize command-surface coverage for commands that
  were previously under-specified, including `/bootstrap` and
  `/marcus.routecheck`.
- `FR-004`: The system MUST preserve existing bounded-context and harness
  behavior while adding this stricter public contract.

Requirement writing rules:

- Every requirement must be testable.
- Every requirement must describe observable behavior, not implementation taste.
- Every requirement must name the actor, trigger, and outcome when relevant.


## 5. Acceptance Criteria

- `AC-001`: Given a published script-backed slash command, when a maintainer
  reads `.agents/SLASH_COMMAND_REGISTRY.md`, then the owning workflow file and
  required script or gate chain are explicit.
- `AC-002`: Given a drift between a workflow file and the public command
  contract, when `python3 scripts/validate_command_surface.py --root .` runs,
  then it fails with the offending command and missing marker.
- `AC-003`: Given the public docs are aligned, when
  `python3 scripts/validate_command_surface.py --root .` runs, then it passes
  and confirms README, `USAGE_GUIDE.md`, registry, and workflow files agree.
- `AC-004`: Given `/bootstrap` and `/marcus.routecheck` are part of the public
  surface, when operators read README and `USAGE_GUIDE.md`, then those commands
  are no longer hidden or inconsistently documented.
- `AC-005`: Given command-surface hardening is added, when routing and harness
  validators replay, then they still pass without changing bounded-context or
  harness semantics.

Acceptance criteria rules:

- Every `FR-*` must map to at least one `AC-*`.
- If a requirement cannot be verified yet, mark it in Clarifications or Risks.
- Do not use generic criteria like "works correctly" or "looks good".


## 3. Scope Boundaries

## 7. Constraints

- Constitution articles that apply: Article I, Article IV, Article IX, and
  Article XI.
- Existing files or modules in scope: `README.md`, `USAGE_GUIDE.md`,
  `workflows/*.md`, `scripts/validate_command_surface.py`, and this feature
  package.
- Files or modules out of scope: downstream repos, external model adapters,
  TrustGraph runtime, and application source code outside `.agents`.
- Compatibility requirements: existing harness and routing validators must keep
  working; command-surface hardening must be additive and file-local.
- Documentation prerequisites already reviewed: current README execution command
  sections, `USAGE_GUIDE.md` slash-command wiring rules, and the workflow files
  for published commands.
- Rollback or containment expectations: reverting the registry and validator
  changes should restore the prior looser command-surface checks without
  affecting source-edit workflows.

Out of scope:

- Rewriting every legacy workflow into a fully automated script chain.
- Introducing external registries, remote metadata, or runtime command brokers.
- Changing command semantics beyond making the published contract explicit and
  validator-enforced.


## 4. Active Work Slice

## 1. Technical Summary

This feature turns the published slash-command surface into an explicit,
validator-backed contract instead of a loose collection of README prose and
workflow notes. The implementation has three parts:

- add a public command registry that any model can read quickly
- strengthen `validate_command_surface.py` to validate command-by-command
  workflow ownership and script-chain markers
- reconcile README and `USAGE_GUIDE.md` so the published surface matches the
  actual workflow and validator chain

The change stays inside `.agents` and does not alter application code. It is a
governance hardening slice designed to reduce command ambiguity for any model
that enters the repo with partial context.


## 6. Agent Routing

The ownership model from `agent-routing.md` is restated here for execution.

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| Requirement and scope hardening | `sophia-product-manager` | accepted command-governance spec | spec validation |
| Contract and validator design | `david-systems-architect` | registry shape and validator strategy | plan review |
| Implementation and doc reconciliation | `marcus-ai-orchestrator` | validator rewrite and public-doc patches | validator replay |
| Verification and release gate | `ada-qa-agent` | evidence-backed recommendation | verification replay |

Execution monitoring:

- Blocking gates before implementation: `validate_specs.py --feature specs/013-slash-command-workflow-contract-hardening`
  and completion of the review loop.
- Evidence checkpoints during implementation: first after validator rewrite,
  then after README and `USAGE_GUIDE.md` reconciliation.
- Escalation condition after repeated failure: if command-surface replay fails
  three times on the same command without new evidence, stop and patch the
  specific command contract directly.


## Tasks

- [x] `T001` Owner: `sophia-product-manager` Write Scope: `spec.md`,
      `verification.md`. Verification: no unresolved clarification markers and
      review-loop status is complete. Docs: `spec.md`, `verification.md`. Sync:
      patch traceability and review evidence before code work.
- [x] `T002` Owner: `david-systems-architect` Write Scope: `plan.md`,
      `data-model.md`, `contracts/`, `quickstart.md`. Verification: command
      registry boundaries, validation rule, and rollback path are explicit.
      Docs: `plan.md`, `data-model.md`, contracts, `quickstart.md`. Sync:
      update traceability if command coverage changes.
- [x] `T003` Owner: `marcus-ai-orchestrator` Write Scope: `agent-routing.md`,
      `tasks.md`, `verification.md`. Verification: workstreams and write scopes
      cover registry, validator, and public-doc reconciliation. Docs:
      `agent-routing.md`, `tasks.md`, `verification.md`. Sync: refresh routing
      if command ownership or sequencing changes.
- [x] `T004` Owner: `marcus-ai-orchestrator` Write Scope:
      `SLASH_COMMAND_REGISTRY.md`, `scripts/validate_command_surface.py`,
      `README.md`, `USAGE_GUIDE.md`. Verification: command-surface validator
      passes and catches bounded drift. Docs: `verification.md`, README, USAGE,
      registry. Sync: patch docs in the same slice as validator changes.
- [x] `T005` Owner: `ada-qa-agent` Write Scope: `verification.md`,
      `execution-brief.md`. Verification: positive replay covers command,
      harness, and routing gates; one bounded negative proof shows command drift
      fails validation. Docs: `verification.md`, `execution-brief.md`. Sync:
      rebuild the brief after final evidence changes.


## 4.1 Dynamic Execution Signals

### Changed Files

- `SLASH_COMMAND_REGISTRY.md`
- `scripts/validate_command_surface.py`
- `README.md`
- `USAGE_GUIDE.md`
- `specs/013-slash-command-workflow-contract-hardening/spec.md`
- `specs/013-slash-command-workflow-contract-hardening/plan.md`
- `specs/013-slash-command-workflow-contract-hardening/tasks.md`
- `specs/013-slash-command-workflow-contract-hardening/verification.md`

### Failing Evidence

- bounded drift proof: command-surface validation fails when a published command marker is removed from a copied public doc

## Execution Monitoring

- Required pre-code gates: `python3 scripts/validate_specs.py --feature specs/013-slash-command-workflow-contract-hardening`
  before implementation and again before closeout.
- Mid-slice checkpoints: replay `validate_command_surface.py` after validator
  rewrite, then replay after README and `USAGE_GUIDE.md` reconciliation.
- Circuit breaker after repeated failure: after three repeated failures on the
  same command marker, stop and patch that exact contract entry instead of
  widening changes across unrelated commands.
- Human escalation trigger: if the work starts requiring remote metadata,
  external registries, or non-`.agents` runtime changes, stop and rescope.


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
| `FR-001` | Positive replay | inspect `.agents/SLASH_COMMAND_REGISTRY.md` and run `python3 scripts/validate_command_surface.py --root .` | published commands show owning workflow and required script chain |
| `FR-002` | Positive + negative replay | pass the validator on current docs, then remove one required command marker in a bounded `/tmp` fixture and rerun | validator passes on current surface and fails on drift |
| `FR-003` | Positive replay | inspect README and `USAGE_GUIDE.md` after patching `/bootstrap` and `/marcus.routecheck` coverage | both commands are visible in the public surface |
| `FR-004` | No-regression replay | rerun command, harness, and routing validators after command-surface hardening | existing governance gates still pass |


## Execution Gates

- Pre-implementation gates passed: feature `013` package must pass
  `validate_specs.py` before closeout.
- Plan/contract readiness confirmed: registry, validator strategy, and rollback
  path are written before implementation is claimed complete.
- Documentation targets created or reconciled: README, `USAGE_GUIDE.md`,
  `SLASH_COMMAND_REGISTRY.md`, and affected workflow references.
- Required human approvals: none beyond local `.agents` edits.


## Local Preconditions

- Required services: none beyond the local `.agents` workspace
- Required environment variables: none
- Required commands: `python3`


## Validation Path

1. Run:
   ```bash
   python3 scripts/validate_command_surface.py --root .
   python3 scripts/validate_harness_contract.py --root .
   python3 scripts/validate_routing_regression.py --root .
   ```
2. Confirm:
   ```text
   The command-surface validator passes, and harness/routing gates remain green
   after the public command registry and doc-surface hardening.
   ```


## POC Rehearsal

- Smallest end-to-end path to demonstrate: one positive replay of
  `validate_command_surface.py` plus one bounded negative proof where a copied
  public-doc marker is removed and validation fails on the specific command.
- Evidence to capture during rehearsal: passing validator output, bounded
  negative failure output, and no-regression harness/routing results.
- Criteria to stop and revise docs before broader execution: registry and public
  docs disagree, validator errors are vague, or existing governance gates fail.


## 7. Review and Release Signals

## 10. Review Loop

Document the review rounds that must happen before implementation is allowed to
proceed.

| Round | Reviewer | Focus | Exit Criteria | Status |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Scope challenge | hardening stays inside `.agents` and does not widen into unrelated automation | Complete |
| `R2` | `sophia-product-manager` | Requirement quality | public command contract is specific enough for any model to follow | Complete |
| `R3` | `marcus-ai-orchestrator` | Go/no-go to planning | validator, registry, and doc-surface strategy are stable enough for implementation | Complete |


## Review Loop Tasks

- `R1`: Challenge whether the registry stays limited to published commands and
  does not over-promise full automation.
- `R2`: Confirm the validator reports exact command/file drift instead of vague
  repo-level failures.
- `R3`: Rebuild `execution-brief.md` and reconcile `verification.md` after final
  evidence so readiness remains fresh.


## Review Rounds

| Round | Reviewer | Finding Summary | Required Changes | Disposition |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Do not claim full automation for legacy commands that still rely on workflow narrative. | Distinguish script-backed commands from workflow-only commands in the registry. | Accepted and applied |
| `R2` | `sophia-product-manager` | Public docs must show missing commands, not just the validator internals. | Reconcile `/bootstrap` and `/marcus.routecheck` in README and USAGE. | Accepted and applied |
| `R3` | `marcus-ai-orchestrator` | The validator must fail on command-specific drift with explicit file markers. | Rewrite `validate_command_surface.py` around command contracts instead of generic repo checks. | Accepted and applied |


## Release Recommendation

- Recommendation: `GO`
- Basis for recommendation: command-surface validation now covers the published
  slash-command contract, registry/doc/workflow drift is replayable, and
  harness/routing validators still pass after the hardening slice.
- Required follow-up before wider rollout: none required inside `.agents`
  beyond normal review of uncommitted diffs.


## 8. Context Expansion Rules

### Task Shape Decision

- Selected task shape: `architecture-refactor`
- Why this shape: Read decisions, diagrams, affected modules, and execution boundaries first.

### Required Reads

- Required read: `agents.md`
- Required read: `.agents/memory/constitution.md`
- Required read: `.agents/specs/013-slash-command-workflow-contract-hardening/execution-brief.md`
- Required read: `.agents/specs/013-slash-command-workflow-contract-hardening/spec.md` only if the brief or failing evidence says deeper requirement context is needed.
- Required read: `.agents/specs/013-slash-command-workflow-contract-hardening/plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, and `agent-routing.md` only when the current write scope or failing evidence requires the deeper artifact.
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

- Escalate when a published command still lacks an owning workflow file.
- Escalate when a command is described as script-backed but only has narrative
  workflow text.
- Escalate when command-surface replay fails repeatedly without new evidence
  about the specific command that drifted.
