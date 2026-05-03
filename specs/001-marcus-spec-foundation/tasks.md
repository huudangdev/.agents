# Task Breakdown: Marcus Spec Foundation

> Feature ID: `001-marcus-spec-foundation`
> Plan: `plan.md`

## Task Rules

- `[P]` means parallel-safe with disjoint write scope.
- Every task needs one owner and one verification method.
- Do not mark a task complete until `verification.md` has evidence.
- Every task must name its write scope explicitly and point to the docs package
  it updates.
- Every task must record how source-of-truth docs stay synchronized if behavior
  or validation rules change.

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

## Parallel Groups

- Group A: `T002`, `T003`, `T004` are parallel-safe after `T001` because their
  write scopes are disjoint.
- Group B: `T005` runs after generated artifacts are populated.

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

## Review Loop Tasks

- `R1`: Challenge review task: challenge whether the spec package is additive,
  bounded, and not pretending to migrate the whole legacy corpus at once.
- `R2`: Verification readiness review task: confirm templates, validators, and
  workflows agree on the same required artifacts and gate language.
- `R3`: Post-evidence reconcile task: patch the sample feature workspace until
  the same stricter validators pass without exceptions.

## Completion Checklist

- [x] `spec.md` accepted
- [x] `plan.md` accepted
- [x] `contracts/` complete or explicitly not applicable
- [x] `tasks.md` complete
- [x] `verification.md` contains evidence
- [x] Root `agents.md` updated
- [x] TrustGraph write attempted
