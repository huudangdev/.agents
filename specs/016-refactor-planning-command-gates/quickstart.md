# Quickstart Validation: Refactor Planning Command Gates

> Feature ID: `016-refactor-planning-command-gates`

## Local Preconditions

- Required services: none beyond the local `.agents` workspace
- Required environment variables: none
- Required commands: `python3`

## Validation Path

1. Run:
   ```bash
   python3 scripts/validate_refactor_planning_readiness.py --root <project-root>
   python3 scripts/validate_refactor_planning_outputs.py --root <project-root>
   python3 scripts/validate_command_surface.py --root .
   ```
2. Confirm:
   ```text
   `/refactor-planning` fails before brownfield refactor planning on unreconciled
   docs, passes on a minimally valid docs package, and validates its closeout
   artifacts separately.
   ```

## Expected Artifacts

- `scripts/validate_refactor_planning_readiness.py`
- `scripts/validate_refactor_planning_outputs.py`
- Updated `workflows/refactor-planning.md`
- Updated `SLASH_COMMAND_REGISTRY.md`
- Refreshed `specs/016-refactor-planning-command-gates/execution-brief.md`

## POC Rehearsal

- Smallest end-to-end path to demonstrate: one valid readiness fixture, one
  valid output fixture, one missing-doc negative proof, and one passing
  command-surface replay.
- Evidence to capture during rehearsal: validator pass/fail output and public
  doc references to the new `/refactor-planning` chain.
- Criteria to stop and revise docs before broader execution: readiness hides the
  real blocker, output validation misses a required closeout artifact, or public
  command docs diverge from the workflow contract.

## Rollback Check

- Reverting the two validators and command-surface wiring should restore the
  previous mixed shell/workflow contract without changing the refactor engine.
