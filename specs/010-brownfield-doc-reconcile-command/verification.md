# Verification Log: Brownfield Doc Reconcile Command

> Feature ID: `010-brownfield-doc-reconcile-command`

## Verification Plan

| Check | Command / Method | Expected Result | Evidence |
| --- | --- | --- | --- |
| Python compile | `PYTHONPYCACHEPREFIX=/tmp/marcus-pycache python3 -m py_compile ...` | Pass | Passed |
| Spec validation | `python3 .agents/scripts/validate_specs.py` | Pass | Passed: 10 specs validated |
| Audit smoke | `audit_development_docs.py --root /tmp/...` | Creates audit markdown | Passed |
| V31 scaffold smoke | `create_development_docs.py --root /tmp/...` | Includes `issues.md` | Passed |
| Missing issues negative smoke | Remove `issues.md` then validate | Fails | Failed as expected: `missing issues.md` |

Command or Procedure evidence must be captured for each requirement-linked check before release is claimed.

## Execution Gates

- Gate 1: `spec.md`, `plan.md`, `tasks.md`, `quickstart.md`, and `agent-routing.md` are reconciled to the current Marcus contract.
- Gate 2: the feature can be replayed through the smallest professional slice using python3 .agents/scripts/validate_specs.py --feature .agents/specs/010-brownfield-doc-reconcile-command; python3 .agents/scripts/audit_development_docs.py --root ..
- Gate 3: `execution-brief.md` is current and the docs-to-read list is still bounded to the active slice.
- Gate 4: residual risk is explicit; no hidden dependency is being smuggled past review.

## Evidence

- Python compile passed for updated validators, scaffold, sync, spec validator,
  and `audit_development_docs.py`.
- `validate_specs.py` passed with `SPEC VALIDATION PASSED: 10 feature(s)`.
- Standalone `.agents` repo-root replay now passes for the repaired validation
  and bootstrap surface after resolving root-path assumptions in
  `scripts/validate_command_surface.py`,
  `scripts/validate_execution_readiness.py`,
  `scripts/validate_routing_regression.py`,
  `scripts/audit_feature_contracts.py`,
  `scripts/sync_project_mcp.py`,
  `scripts/check_mcp_health.py`,
  `scripts/print_update_brief.py`, and
  `scripts/check_repo_setup.sh`.
- `python3 scripts/validate_command_surface.py` passed.
- `python3 scripts/validate_execution_readiness.py --root . --feature specs/010-brownfield-doc-reconcile-command`
  passed.
- `python3 scripts/validate_routing_regression.py` passed.
- `python3 scripts/audit_feature_contracts.py` passed with 10 current-contract
  features and 0 validation failures.
- `python3 scripts/sync_project_mcp.py --root .` passed and created `.mcp.json`
  in the `.agents` repo root with `drawio`, `figma`, `playwright`, and `stitch`
  server definitions.
- `bash scripts/check_repo_setup.sh .` passed after `.mcp.json` existed.
- `python3 scripts/check_mcp_health.py --root .` passed with one optional
  warning: missing `FIGMA_ACCESS_TOKEN` for optional `figma`.
- `python3 scripts/print_update_brief.py --root .` passed and printed release
  highlights instead of crashing on path resolution.
- Audit smoke created
  `docs/development/audits/20260423-184502-code-docs-audit.md`.
- V31 scaffold smoke created `docs/development/E-001-doc-reconcile-smoke/issues.md`.
- Negative smoke removed `issues.md`; strict validation failed with
  `docs/development/E-001-doc-reconcile-smoke: missing issues.md`.

## Review Rounds

| Round | Reviewer | Finding Summary | Required Changes | Disposition |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Challenge whether the slice stayed bounded and whether the quickstart is replayable. | Tighten scope or replay guidance if hidden widening appeared. | Accepted and applied |
| `R2` | `ada-qa-agent` | Check that commands, validators, and evidence actually prove the claimed outcome. | Patch missing evidence, gates, or residual-risk statements. | Accepted and applied |
| `R3` | `marcus-ai-orchestrator` | Decide whether the feature is ready for downstream execution or closeout. | Rebuild the brief/readiness chain if the package changed during review. | Accepted and applied |

## Release Recommendation

- Recommendation: `GO WITH RESIDUAL RISK`
- Basis for recommendation: the feature package now includes review-loop, quickstart, routing, and readiness artifacts around the already captured implementation evidence. The final judgment still depends on the recorded residual risk and the command results in this file.

## Residual Risk

- `/doc_reconcile` can identify and document gaps, but actual downstream app
  fixes still require operator-approved `/develop` or `/quick_fix`.
- Root `../agents.md` remains the declared source of truth for session memory,
  but this Codex run could not update it because the file sits outside the
  current writable root.
