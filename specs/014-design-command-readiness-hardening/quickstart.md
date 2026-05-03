# Quickstart Validation: Design Command Readiness Hardening

> Feature ID: `014-design-command-readiness-hardening`

## Local Preconditions

- Required services: none beyond the local `.agents` workspace
- Required environment variables: none
- Required commands: `python3`

## Validation Path

1. Run:
   ```bash
   python3 scripts/validate_design_readiness.py --root <project-root>
   python3 scripts/validate_design_outputs.py --root <project-root>
   python3 scripts/validate_command_surface.py --root .
   ```
2. Confirm:
   ```text
   `/design` fails early when planning inputs are missing, passes when design
   artifacts exist, and remains part of the validated public command surface.
   ```

## Expected Artifacts

- `scripts/validate_design_readiness.py`
- `scripts/validate_design_outputs.py`
- Updated `workflows/design.md`
- Updated `SLASH_COMMAND_REGISTRY.md`
- Refreshed `specs/014-design-command-readiness-hardening/execution-brief.md`

## POC Rehearsal

- Smallest end-to-end path to demonstrate: one valid readiness fixture, one
  valid output fixture, one invalid readiness fixture, and one passing
  command-surface replay.
- Evidence to capture during rehearsal: validator pass/fail output and public
  doc references to the new `/design` chain.
- Criteria to stop and revise docs before broader execution: validators hide
  the missing file, `/design` is still missing from the registry, or the public
  command surface diverges.

## Rollback Check

- Reverting the new validators and `/design` wiring should restore the previous
  prose-only Phase 2 behavior without affecting unrelated commands.
