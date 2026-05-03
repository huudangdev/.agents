# Task Breakdown: Harness Auto Enforcement and Freshness

> Feature ID: `011-harness-auto-enforcement-and-freshness`
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
      `data-model.md`, `contracts/`, `quickstart.md`. Verification: wrapper
      phases, command ordering, and rollback path are explicit. Docs: `plan.md`,
      `data-model.md`, `contracts/harness-phase-contract.md`, `quickstart.md`.
      Sync: update plan and quickstart if command ordering changes.
- [x] `T003` Owner: `marcus-ai-orchestrator` Write Scope: `agent-routing.md`,
      `tasks.md`, affected workflow/docs inventory. Verification: every changed
      public surface names the same preflight/postflight chain. Docs:
      `agent-routing.md`, `tasks.md`, `verification.md`. Sync: refresh task and
      routing artifacts if script or workflow scope changes.
- [x] `T004` Owner: `marcus-ai-orchestrator` Write Scope: `scripts/path_utils.py`,
      `scripts/run_harness_preflight.py`, `scripts/run_harness_postflight.py`,
      `scripts/validate_harness_contract.py`, `scripts/check_repo_setup.sh`.
      Verification: py_compile passes and the wrappers return deterministic
      results in standalone `.agents`. Docs: `verification.md`, `README.md`,
      `USAGE_GUIDE.md`. Sync: patch docs in the same slice as script changes.
- [x] `T005` Owner: `knowledge-work-architecture` Write Scope: `README.md`,
      `USAGE_GUIDE.md`, `workflows/init_brain.md`, `workflows/develop.md`,
      `workflows/quick_fix.md`, `workflows/marcus_verify.md`. Verification:
      harness contract validator passes. Docs: same files plus `verification.md`.
      Sync: update command-surface docs and workflow instructions together.
- [x] `T006` Owner: `ada-qa-agent` Write Scope: `verification.md`,
      `execution-brief.md`. Verification: positive replay covers bootstrap,
      execution preflight, execution postflight, and freshness validation. Docs:
      `verification.md`, `execution-brief.md`. Sync: rebuild the brief after
      evidence changes.

## Parallel Groups

- Group A: `T004` then `T005` because workflow/docs depend on the new scripts.
- Group B: `T006` closes after scripts and docs stabilize.

## Execution Monitoring

- Required pre-code gates: `python3 scripts/validate_specs.py --feature specs/011-harness-auto-enforcement-and-freshness`
  before implementation and again before closeout.
- Mid-slice checkpoints: rerun standalone `.agents` replay after each major
  batch: scripts, docs/workflows, then verification evidence.
- Circuit breaker after repeated failure: after three failures of the same
  harness wrapper without new evidence, stop adding docs and patch the failing
  script or validator directly.
- Human escalation trigger: if additive wrappers require changing unrelated
  repos or introducing unsupported runtime dependencies, stop and rescope.

## Review Loop Tasks

- `R1`: Challenge whether wrapper scripts are genuinely additive and whether
  freshness validation stays bounded to real contract files.
- `R2`: Confirm bootstrap and execution phases use deterministic command order
  and expose the underlying failure cleanly.
- `R3`: Rebuild `execution-brief.md` and reconcile `verification.md` after final
  evidence so readiness remains fresh.

## Completion Checklist

- [x] `spec.md` accepted
- [x] `plan.md` accepted
- [x] `contracts/` complete or explicitly not applicable
- [x] `tasks.md` complete
- [x] `verification.md` contains evidence
- [x] Root `agents.md` update intentionally not required for this `.agents`-only feature
- [x] TrustGraph write explicitly deferred for this `.agents`-only local harness slice
