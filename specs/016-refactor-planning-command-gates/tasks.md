# Task Breakdown: Refactor Planning Command Gates

> Feature ID: `016-refactor-planning-command-gates`
> Plan: `plan.md`

## Task Rules

- `[P]` means parallel-safe with disjoint write scope.
- Every task needs one owner and one verification method.
- Do not mark a task complete until `verification.md` has evidence.
- Every task must name the documentation artifact it updates before or alongside
  code.
- Every implementation task must declare what would block or fail it.

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

## Parallel Groups

- Group A: `T001` to `T003` define the contract before code edits.
- Group B: `T004` then `T005` because verification depends on the final
  validators and public-doc wiring.

## Execution Monitoring

- Required pre-code gates: `python3 scripts/validate_specs.py --feature specs/016-refactor-planning-command-gates`
  before implementation and again before closeout.
- Mid-slice checkpoints: replay readiness validator first, then output
  validator, then command-surface validation after `/refactor-planning` wiring.
- Circuit breaker after repeated failure: after three repeated failures on the
  same readiness or output gate, stop and patch that exact contract.
- Human escalation trigger: if the slice starts requiring live AST/runtime tool
  execution instead of command gates, stop and rescope.

## Review Loop Tasks

- `R1`: Challenge whether the gates stay focused on brownfield governance and
  closeout artifacts.
- `R2`: Confirm failures point to exact docs or artifacts rather than vague
  “refactor failed” messaging.
- `R3`: Rebuild `execution-brief.md` and reconcile `verification.md` after final
  evidence so readiness remains fresh.

## Completion Checklist

- [x] `spec.md` accepted
- [x] `plan.md` accepted
- [x] `contracts/` complete or explicitly not applicable
- [x] `tasks.md` complete
- [x] `verification.md` contains evidence
- [x] Root `agents.md` update intentionally not required for this `.agents`-only feature
- [x] TrustGraph write attempted or explicitly deferred
