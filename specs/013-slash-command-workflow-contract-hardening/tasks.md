# Task Breakdown: Slash Command Workflow Contract Hardening

> Feature ID: `013-slash-command-workflow-contract-hardening`
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

## Parallel Groups

- Group A: `T001` to `T003` define the contract before code edits.
- Group B: `T004` then `T005` because verification depends on the final
  validator and public-doc surface.

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

## Review Loop Tasks

- `R1`: Challenge whether the registry stays limited to published commands and
  does not over-promise full automation.
- `R2`: Confirm the validator reports exact command/file drift instead of vague
  repo-level failures.
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
