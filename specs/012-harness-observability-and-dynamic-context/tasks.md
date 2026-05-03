# Task Breakdown: Harness Observability and Dynamic Context

> Feature ID: `012-harness-observability-and-dynamic-context`
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
      `data-model.md`, `contracts/`, `quickstart.md`. Verification: log schema,
      dynamic context inputs, and rollback path are explicit. Docs: `plan.md`,
      `data-model.md`, contracts, `quickstart.md`. Sync: update plan if the log
      shape or brief flags change.
- [x] `T003` Owner: `marcus-ai-orchestrator` Write Scope: `agent-routing.md`,
      `tasks.md`, `verification.md`. Verification: workstreams and write scopes
      cover wrappers, helper layer, and brief generator. Docs: `agent-routing.md`,
      `tasks.md`, `verification.md`. Sync: refresh routing if implementation scope changes.
- [x] `T004` Owner: `marcus-ai-orchestrator` Write Scope: shared helper layer,
      harness wrappers, `build_execution_brief.py`. Verification: py_compile
      passes, wrapper logs are written, and briefs rebuild with optional dynamic
      inputs. Docs: `verification.md`, README/USAGE if flags or log paths are exposed.
      Sync: patch docs in the same slice as code changes.
- [x] `T005` Owner: `knowledge-work-architecture` Write Scope: `README.md`,
      `USAGE_GUIDE.md`, and any workflow text that should mention dynamic brief
      inputs or log paths. Verification: docs mention the new log location and
      optional brief flags consistently. Docs: same files plus `verification.md`.
      Sync: update docs after code behavior stabilizes.
- [x] `T006` Owner: `ada-qa-agent` Write Scope: `verification.md`,
      `execution-brief.md`. Verification: positive replay covers logs and
      dynamic brief inputs; one bounded negative proof catches bad contract or
      malformed inputs. Docs: `verification.md`, `execution-brief.md`. Sync:
      rebuild the brief after evidence changes.

## Parallel Groups

- Group A: `T004` then `T005` because docs depend on code behavior.
- Group B: `T006` closes after scripts and docs stabilize.

## Execution Monitoring

- Required pre-code gates: `python3 scripts/validate_specs.py --feature specs/012-harness-observability-and-dynamic-context`
  before implementation and again before closeout.
- Mid-slice checkpoints: replay wrappers after logging changes, then replay
  brief generation with dynamic inputs after builder changes.
- Circuit breaker after repeated failure: after three repeated failures in the
  same helper or builder path, stop and patch that layer directly.
- Human escalation trigger: if the slice starts requiring external telemetry
  systems, git daemons, or unrelated repo integration, stop and rescope.

## Review Loop Tasks

- `R1`: Challenge whether the log payload stays minimal and whether dynamic
  context remains optional and bounded.
- `R2`: Confirm wrappers still expose the underlying failing command and that
  brief sections remain validator-compatible.
- `R3`: Rebuild `execution-brief.md` and reconcile `verification.md` after final
  evidence so readiness remains fresh.

## Completion Checklist

- [ ] `spec.md` accepted
- [ ] `plan.md` accepted
- [ ] `contracts/` complete or explicitly not applicable
- [x] `tasks.md` complete
- [x] `verification.md` contains evidence
- [x] Root `agents.md` update intentionally not required for this `.agents`-only feature
- [x] TrustGraph write attempted or explicitly deferred
