# Task Breakdown: Marcus Init Output Contract Hardening

> Feature ID: `015-marcus-init-output-contract-hardening`
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

## Parallel Groups

- Group A: `T001` to `T003` define the contract before code edits.
- Group B: `T004` then `T005` because verification depends on the final
  validator and public-doc wiring.

## Execution Monitoring

- Required pre-code gates: `python3 scripts/validate_specs.py --feature specs/015-marcus-init-output-contract-hardening`
  before implementation and again before closeout.
- Mid-slice checkpoints: replay output validation first, then replay
  command-surface validation after `/marcus_init` wiring.
- Circuit breaker after repeated failure: after three repeated failures on the
  same scaffold-output marker, stop and patch that exact output contract.
- Human escalation trigger: if hardening `/marcus_init` starts requiring a full
  scaffold-engine rewrite or remote bootstrap integration, stop and rescope.

## Review Loop Tasks

- `R1`: Challenge whether the new gate stays limited to scaffold outputs.
- `R2`: Confirm validator errors point to exact missing or empty artifacts.
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
