# Task Breakdown: Design Command Readiness Hardening

> Feature ID: `014-design-command-readiness-hardening`
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

## Parallel Groups

- Group A: `T001` to `T003` define the contract before code edits.
- Group B: `T004` then `T005` because verification depends on the final
  validators and public-doc wiring.

## Execution Monitoring

- Required pre-code gates: `python3 scripts/validate_specs.py --feature specs/014-design-command-readiness-hardening`
  before implementation and again before closeout.
- Mid-slice checkpoints: replay readiness validator first, then output
  validator, then command-surface validation after `/design` wiring.
- Circuit breaker after repeated failure: after three repeated failures on the
  same design gate, stop and patch that exact input or output contract.
- Human escalation trigger: if `/design` hardening starts requiring browser,
  Figma, or application source-code changes, stop and rescope.

## Review Loop Tasks

- `R1`: Challenge whether the `/design` gate remains Phase 2-only and does not
  overstep into judging design taste.
- `R2`: Confirm validator errors point to exact missing inputs or outputs.
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
