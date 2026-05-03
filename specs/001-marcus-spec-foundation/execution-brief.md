# Execution Brief: Feature Specification: Marcus Spec Foundation

> Feature ID: `001-marcus-spec-foundation`
> Task Shape: `general`
> Generated From: `spec.md`, `plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, `agent-routing.md`

## 1. Operator Intent Snapshot

## 1. Purpose

Marcus Fleet needs a spec-driven foundation inspired by GitHub Spec Kit without
replacing its existing strengths: skills, workflows, TrustGraph memory, sandbox
execution, and observability. The outcome is a durable planning layer that lets
agents work from feature-scoped contracts instead of loosely interpreted prompts.

This feature establishes the first version of that layer: a constitution,
templates, scripts, workflow documents, and a sample feature workspace that can
be validated locally.


## 2. Required Behavior

## 3. Functional Requirements

- `FR-001`: The system MUST provide a project-level constitution under
  `.agents/memory/constitution.md`.
- `FR-002`: The system MUST provide reusable templates for `spec.md`,
  `plan.md`, `tasks.md`, `verification.md`, `agent-routing.md`, `research.md`,
  `data-model.md`, and `quickstart.md`.
- `FR-003`: The system MUST provide a script that creates a numbered
  `.agents/specs/<feature-id>/` workspace from templates.
- `FR-004`: The system MUST provide a script that validates required feature
  artifacts and unresolved clarification markers.
- `FR-005`: The system MUST provide workflow documents for specify, clarify,
  plan, tasks, and verify phases.
- `FR-006`: The system MUST preserve the existing `.agents` ecosystem and avoid
  replacing current skills or TrustGraph adapters.


## 5. Acceptance Criteria

- `AC-001`: Given the repository root, when
  `python3 .agents/scripts/create_feature_spec.py "Example Feature"` runs, then
  a numbered feature folder is created under `.agents/specs/`.
- `AC-002`: Given a generated feature folder, when
  `python3 .agents/scripts/validate_specs.py --feature <folder>` runs after
  clarifications are resolved, then validation passes.
- `AC-003`: Given a generated draft with unresolved clarification markers, when
  validation runs without `--allow-clarifications`, then validation fails.
- `AC-004`: Given an agent planning a non-trivial change, when it reads the new
  workflow docs, then it can follow specify -> clarify -> plan -> tasks ->
  verify without using legacy global `/docs` artifacts as the only source of
  truth.


## 3. Scope Boundaries

## 7. Constraints

- Constitution articles that apply: all initial articles in
  `.agents/memory/constitution.md`.
- Existing files or modules in scope: `.agents/workflows/`, `.agents/templates/`,
  `.agents/scripts/`, `.agents/specs/`, root `agents.md`.
- Files or modules out of scope: `.agents/skills/*/SKILL.md` mass migration,
  TrustGraph schema migration, viewer lint cleanup.
- Compatibility requirements: no existing workflow file may be deleted; new
  scripts must run with `python3` and no third-party packages.
- Documentation prerequisites already reviewed: root `agents.md`,
  `.agents/README.md`, `.agents/USAGE_GUIDE.md`, and the workflow set under
  `.agents/workflows/`.
- Rollback or containment expectations: this foundation must remain additive so
  that legacy slash-command flows still operate even if feature-scoped specs are
  not yet adopted everywhere.

Out of scope:

- Rewriting every legacy skill to the new tool vocabulary in the same feature.
- Replacing the historical `/planning` package with `.agents/specs/` only.
- Introducing network-dependent spec tooling or a hosted policy service.


## 4. Active Work Slice

## 1. Technical Summary

Implement the first Marcus Fleet spec-driven foundation as an additive layer
inside `.agents`. This plan creates durable governance and feature-scoped
artifacts while preserving existing workflows and skills.

The implementation is intentionally small and local:

- Markdown constitution and templates.
- Python standard-library scripts for feature creation and validation.
- Workflow docs that map the new lifecycle to Marcus Fleet agents.
- A sample feature folder proving the process works.


## 6. Agent Routing

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| Specification | `sophia-product-manager` | `spec.md` | no unresolved clarifications |
| Architecture | `david-systems-architect` | `plan.md`, `contracts/` | constitution gates |
| Orchestration | `marcus-ai-orchestrator` | `agent-routing.md` | owners and write scopes |
| QA | `ada-qa-agent` | `verification.md` | evidence table |

Execution monitoring:

- Blocking gates before implementation: `spec.md` clarity, contracts present,
  verification plan named, and no placeholder-heavy artifacts in the workspace.
- Evidence checkpoints during implementation: feature creation, validator pass,
  workflow population, and `agents.md` memory update.
- Escalation condition after repeated failure: if validation fails repeatedly
  for the same unresolved artifact without new edits, stop and repair the spec
  package before continuing.


## Tasks

- [x] `T001` Owner: `sophia-product-manager` Write Scope:
      `.agents/memory/constitution.md`, `spec.md`. Verification: constitution
      exists and `spec.md` has no unresolved clarification markers. Docs:
      `spec.md`, `verification.md`. Sync: if scope boundaries change, update
      traceability and acceptance criteria before any downstream planning.
- [x] `T002` [P] Owner: `david-systems-architect` Write Scope:
      `.agents/templates/*.md`, `plan.md`, `data-model.md`,
      `contracts/spec-workspace.md`, `quickstart.md`. Verification: required
      templates exist and plan gates are concrete. Docs: `plan.md`,
      `data-model.md`, `quickstart.md`. Sync: update quickstart and contracts
      whenever validation or rollout assumptions change.
- [x] `T003` [P] Owner: `alan-tech-lead` Write Scope:
      `.agents/scripts/create_feature_spec.py`,
      `.agents/scripts/validate_specs.py`. Verification: scripts parse and
      `create_feature_spec.py` created this feature workspace. Docs:
      `tasks.md`, `verification.md`. Sync: append validator changes to
      verification evidence and note any new required artifact fields.
- [x] `T004` [P] Owner: `marcus-ai-orchestrator` Write Scope:
      `.agents/workflows/marcus_*.md`, `agent-routing.md`. Verification:
      workflows map specify, clarify, plan, tasks, verify and respect the new
      execution gate. Docs: `agent-routing.md`, `tasks.md`. Sync: when routing
      expectations change, patch workflow docs and ownership matrix together.
- [x] `T005` Owner: `ada-qa-agent` Write Scope: `verification.md`,
      `.agents/specs/001-marcus-spec-foundation/*`. Verification:
      `validate_specs.py --feature .agents/specs/001-marcus-spec-foundation`
      passes. Docs: `verification.md`, `tasks.md`. Sync: append evidence and
      residual risk whenever stricter gates expose shallow sample artifacts.


## Execution Monitoring

- Required pre-code gates: feature workspace exists, clarifications resolved,
  contracts named, and verification plan drafted before implementation changes.
- Mid-slice checkpoints: templates updated, validator rules updated, workflows
  updated, then sample feature reconciled against the same stricter rules.
- Circuit breaker after repeated failure: if the same spec validation error
  persists across three passes without new artifact edits, halt execution and
  repair the docs package before touching more workflow scope.
- Human escalation trigger: if stricter validation would break a large body of
  legacy features or workflows beyond this bounded feature, escalate for
  migration planning instead of silently weakening the validator.


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
| `FR-001` | File check | `test -f .agents/memory/constitution.md` | File exists |
| `FR-002` | File check | `find .agents/templates -type f` | Required templates exist |
| `FR-003` | Runtime check | `python3 .agents/scripts/create_feature_spec.py "Marcus Spec Foundation" ...` | Feature workspace created |
| `FR-004` | Runtime check | `python3 .agents/scripts/validate_specs.py --feature .agents/specs/001-marcus-spec-foundation` | Validation passes |
| `FR-005` | File check | `find .agents/workflows -name 'marcus_*.md'` | Five workflow docs exist |


## Execution Gates

- Pre-implementation gates passed: constitution created, spec clarified, and
  required artifacts scaffolded before deeper workflow changes.
- Plan/contract readiness confirmed: `plan.md`, `contracts/spec-workspace.md`,
  `agent-routing.md`, and `quickstart.md` were populated before the final
  validator pass.
- Documentation targets created or reconciled: the sample feature workspace was
  upgraded to match the stricter templates and validation rules instead of being
  left as a shallow exception.
- Required human approvals: none for the local additive foundation, but any
  future migration of legacy skill files remains an explicit follow-up decision.


## Local Preconditions

- Required services: none for local spec creation and validation.
- Required environment variables: none.
- Required commands: `python3`.


## Validation Path

1. Run:
   ```bash
   python3 .agents/scripts/create_feature_spec.py "Example Feature" --prompt "Example prompt"
   ```
2. Confirm:
   ```text
   .agents/specs/NNN-example-feature
   ```


## POC Rehearsal

- Smallest end-to-end path to demonstrate: create or reconcile the feature
  workspace, run strict validation, run execution readiness validation, and
  confirm the workflow docs point to the same gate language.
- Evidence to capture during rehearsal: validator pass output, readiness pass
  output, and verification-log updates naming what was reconciled.
- Criteria to stop and revise docs before broader execution: any mismatch
  between templates, validators, workflows, and the sample feature package.


## 7. Review and Release Signals

## 10. Review Loop

| Round | Reviewer | Focus | Exit Criteria | Status |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Scope challenge | additive-only scope confirmed, migration fantasy removed | Complete |
| `R2` | `sophia-product-manager` | Requirement quality | user stories, FRs, ACs, and evidence obligations aligned | Complete |
| `R3` | `marcus-ai-orchestrator` | Go/no-go to planning | spec package stable enough to create architecture artifacts | Complete |


## Review Loop Tasks

- `R1`: Challenge review task: challenge whether the spec package is additive,
  bounded, and not pretending to migrate the whole legacy corpus at once.
- `R2`: Verification readiness review task: confirm templates, validators, and
  workflows agree on the same required artifacts and gate language.
- `R3`: Post-evidence reconcile task: patch the sample feature workspace until
  the same stricter validators pass without exceptions.


## Review Rounds

| Round | Reviewer | Finding Summary | Required Changes | Disposition |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Scope risk: do not merge spec-foundation with mass legacy migration. | Keep this feature additive and bounded. | Accepted and applied |
| `R2` | `alan-tech-lead` | Template/validator drift risk: rules must be encoded, not merely described. | Add stricter validator sections and reconcile the sample feature. | Accepted and applied |
| `R3` | `ada-qa-agent` | Readiness gate must prove replayability, not just file presence. | Require review-loop and release markers in artifacts. | Accepted and applied |


## Release Recommendation

- Recommendation: `GO WITH RESIDUAL RISK`
- Basis for recommendation: the docs-first foundation, stricter validators, and
  readiness gate all pass locally for the sample feature and remain additive to
  the existing `.agents` ecosystem.
- Required follow-up before wider rollout: run the same process on a real
  feature touching source code and reconcile any brownfield doc gaps that
  surface there.


## 8. Context Expansion Rules

### Task Shape Decision

- Selected task shape: `general`
- Why this shape: Start from the active feature workspace and only expand context when the write scope demands it.

### Required Reads

- Required read: `agents.md`
- Required read: `.agents/memory/constitution.md`
- Required read: `.agents/specs/001-marcus-spec-foundation/execution-brief.md`
- Required read: `.agents/specs/001-marcus-spec-foundation/spec.md` only if the brief or failing evidence says deeper requirement context is needed.
- Required read: `.agents/specs/001-marcus-spec-foundation/plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, and `agent-routing.md` only when the current write scope or failing evidence requires the deeper artifact.
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

| Review Stage | Primary Reviewer | Input Artifact | Output Artifact |
| --- | --- | --- | --- |
| Spec challenge | `aurora-plan-challenger` | `spec.md` | challenged scope and accepted boundaries |
| Plan challenge | `alan-tech-lead` | `plan.md` | reconciled architecture and gate language |
| Verification sign-off | `ada-qa-agent` | `verification.md` | recommendation with residual risk |


## Escalation Rules

- Escalate when the sample feature fails the same validation gate repeatedly
  after template and workflow edits, because the docs package must be fixed
  before expanding scope further.
- Escalate when a proposed routing change would silently widen write scope for a
  skill without updating `tasks.md` and verification commitments.
- Escalate when legacy compatibility and strict governance are in direct
  conflict, so the migration can be planned explicitly instead of improvised.
