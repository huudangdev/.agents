# Quickstart Validation: Harness Observability and Dynamic Context

> Feature ID: `012-harness-observability-and-dynamic-context`

## Local Preconditions

- Required services: none beyond the local `.agents` workspace.
- Required environment variables: none required for the feature itself; optional
  `FIGMA_ACCESS_TOKEN` may still warn during bootstrap health checks.
- Required commands: `python3`, `bash`.

## Validation Path

1. Run:
   ```bash
   python3 scripts/run_harness_preflight.py --root . --phase execution --feature specs/012-harness-observability-and-dynamic-context
   python3 scripts/build_execution_brief.py --feature specs/012-harness-observability-and-dynamic-context --task-shape architecture-refactor --changed-files "scripts/build_execution_brief.py,scripts/run_harness_preflight.py" --failing-evidence "validate_harness_contract.py failed on missing marker"
   python3 scripts/run_harness_postflight.py --root . --phase execution --feature specs/012-harness-observability-and-dynamic-context
   ```
2. Confirm:
   ```text
   Wrapper runs append structured JSONL entries under `.agents/logs/harness/`,
   and the rebuilt brief contains bounded changed-file and failing-evidence context.
   ```

## Expected Artifacts

- Files, logs, screenshots, or documents that should exist after validation:
- `.agents/logs/harness/*.jsonl`
- Updated `execution-brief.md` containing dynamic context input sections.
- Updated `verification.md` with replay evidence.

## POC Rehearsal

- Smallest end-to-end path to demonstrate: one execution wrapper run that logs
  a JSONL event and one brief rebuild with both optional dynamic inputs.
- Evidence to capture during rehearsal: JSONL log lines, brief section output,
  and readiness/freshness replay after the rebuild.
- Criteria to stop and revise docs before broader execution: logs hide the
  failing command, dynamic brief sections widen default reads, or validators
  stop passing.

## Rollback Check

- Remove wrapper logging calls and stop passing the optional brief flags. Core
  wrapper and brief behavior should remain intact.
