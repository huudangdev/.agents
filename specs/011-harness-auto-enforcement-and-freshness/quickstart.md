# Quickstart Validation: Harness Auto Enforcement and Freshness

> Feature ID: `011-harness-auto-enforcement-and-freshness`

## Local Preconditions

- Required services: none beyond the local `.agents` workspace.
- Required environment variables: optional `FIGMA_ACCESS_TOKEN` may still be
  absent; it should remain a warning, not a blocker.
- Required commands: `python3`, `bash`.

## Validation Path

1. Run:
   ```bash
   python3 scripts/run_harness_preflight.py --root . --phase bootstrap
   python3 scripts/run_harness_preflight.py --root . --phase execution --feature specs/011-harness-auto-enforcement-and-freshness
   python3 scripts/run_harness_postflight.py --root . --phase execution --feature specs/011-harness-auto-enforcement-and-freshness
   python3 scripts/validate_harness_contract.py --root .
   ```
2. Confirm:
   ```text
   Each command exits zero, reports the underlying checks it ran, and does not
   regress into `.agents/.agents/...` path resolution.
   ```

## Expected Artifacts

- Files, logs, screenshots, or documents that should exist after validation:
- `scripts/run_harness_preflight.py`
- `scripts/run_harness_postflight.py`
- `scripts/validate_harness_contract.py`
- Updated README, USAGE, and affected workflow files.
- Updated `verification.md` and refreshed `execution-brief.md`.

## POC Rehearsal

- Smallest end-to-end path to demonstrate: run bootstrap preflight once, then
  run execution preflight and postflight against feature `011`, and finally run
  the harness contract validator.
- Evidence to capture during rehearsal: command outputs, py_compile success, and
  any warning-only classification such as optional `figma`.
- Criteria to stop and revise docs before broader execution: a wrapper obscures
  the failing child command, docs mention a chain different from the replayed
  one, or path resolution differs between standalone and vendored layouts.

## Rollback Check

- Remove the wrapper references from docs/workflows and delete the additive
  scripts. Existing validators and setup scripts should still function directly.
