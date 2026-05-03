# Verification Log: Harness Auto Enforcement and Freshness

> Feature ID: `011-harness-auto-enforcement-and-freshness`

## Verification Plan

| Requirement | Method | Command or Procedure | Expected Result |
| --- | --- | --- | --- |
| `FR-001` | Positive replay | `python3 scripts/run_harness_preflight.py --root . --phase bootstrap` and `python3 scripts/run_harness_preflight.py --root . --phase execution --feature specs/011-harness-auto-enforcement-and-freshness` | both pass and print deterministic phase summaries |
| `FR-002` | Positive replay | `python3 scripts/run_harness_postflight.py --root . --phase execution --feature specs/011-harness-auto-enforcement-and-freshness` | pass and replay postflight checks |
| `FR-003` | Positive + negative replay | `python3 scripts/validate_harness_contract.py --root .` plus one missing-marker mutation if needed | validator fails on contract drift and passes on aligned docs |
| `FR-004` | Document inspection + replay | README/USAGE/workflow marker checks and wrapper replay | public surface matches the real command chain |
| `FR-005` | Standalone `.agents` replay | all commands above from `/Users/lequynhanh/marcus-fleet/.agents` | no `.agents/.agents/...` regressions |

## Execution Gates

- Pre-implementation gates passed: `validate_specs.py --allow-clarifications`
  during drafting, then full `validate_specs.py` before implementation.
- Plan/contract readiness confirmed: wrapper phases, docs scope, rollback path,
  and feature verification path are written before code changes.
- Documentation targets created or reconciled: feature `011` package,
  affected workflows, README, USAGE, and script inventory.
- Required human approvals: none beyond normal local file edits in `.agents`.

## Evidence

| Date | Check | Result | Notes |
| --- | --- | --- | --- |
| 2026-05-03 | Spec + plan package | Passed | `python3 scripts/validate_specs.py --feature specs/011-harness-auto-enforcement-and-freshness` passed |
| 2026-05-03 | Python compile | Passed | `PYTHONPYCACHEPREFIX=/tmp/marcus-pycache python3 -m py_compile scripts/path_utils.py scripts/validate_harness_contract.py scripts/run_harness_preflight.py scripts/run_harness_postflight.py` passed |
| 2026-05-03 | Harness contract positive replay | Passed | `python3 scripts/validate_harness_contract.py --root .` passed |
| 2026-05-03 | Bootstrap preflight replay | Passed | `python3 scripts/run_harness_preflight.py --root . --phase bootstrap` passed |
| 2026-05-03 | Execution preflight replay | Passed | `python3 scripts/run_harness_preflight.py --root . --phase execution --feature specs/011-harness-auto-enforcement-and-freshness` passed |
| 2026-05-03 | Execution postflight replay | Passed | `python3 scripts/run_harness_postflight.py --root . --phase execution --feature specs/011-harness-auto-enforcement-and-freshness` passed |
| 2026-05-03 | Harness contract negative replay | Failed as expected | Minimal `/tmp` fixture missing the postflight marker in `workflows/marcus_verify.md` failed with `HARNESS CONTRACT VALIDATION FAILED` |

## Review Rounds

| Round | Reviewer | Finding Summary | Required Changes | Disposition |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Keep scope on orchestration and freshness; do not slide into full telemetry platform work. | Add explicit out-of-scope and POC boundary lines. | Accepted and applied |
| `R2` | `ada-qa-agent` | Wrappers are only useful if they expose the underlying failing command and preserve exit semantics. | Require deterministic summaries and direct command replay evidence. | Accepted and applied |
| `R3` | `marcus-ai-orchestrator` | The docs package must be ready before script edits begin. | Complete plan, tasks, quickstart, and contract artifacts first. | Accepted and applied |

## Release Recommendation

- Recommendation: `GO`, `GO WITH RESIDUAL RISK`, or `NO-GO`
- Recommendation: `GO WITH RESIDUAL RISK`
- Basis for recommendation: wrapper scripts, repo-wide freshness validation, and
  workflow/doc wiring all replay successfully in the standalone `.agents`
  repository. The negative fixture also proves the freshness validator fails on
  a real contract drift.
- Required follow-up before wider rollout: add harness observability metrics in
  a later feature if the team wants trend data rather than command-by-command replay.

## Residual Risk

- Until implementation finishes, the harness still depends on agents manually
  remembering some deeper task-specific validators beyond the wrapper boundary.
- `figma` still warns when `FIGMA_ACCESS_TOKEN` is absent, but bootstrap
  preflight correctly classifies that as optional instead of blocking.
- The blast radius remains limited to `.agents` workflows and operator
  documentation, not downstream application repositories.
