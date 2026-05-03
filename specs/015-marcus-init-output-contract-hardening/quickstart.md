# Quickstart Validation: Marcus Init Output Contract Hardening

> Feature ID: `015-marcus-init-output-contract-hardening`

## Local Preconditions

- Required services: none beyond the local `.agents` workspace
- Required environment variables: none
- Required commands: `python3`

## Validation Path

1. Run:
   ```bash
   python3 scripts/validate_marcus_init_outputs.py --root <scaffolded-project-root>
   python3 scripts/validate_command_surface.py --root .
   ```
2. Confirm:
   ```text
   `/marcus_init` closeout fails when required scaffold outputs are missing and
   passes when the expected project root artifacts exist.
   ```

## Expected Artifacts

- `scripts/validate_marcus_init_outputs.py`
- Updated `workflows/marcus_init.md`
- Updated `SLASH_COMMAND_REGISTRY.md`
- Refreshed `specs/015-marcus-init-output-contract-hardening/execution-brief.md`

## POC Rehearsal

- Smallest end-to-end path to demonstrate: one valid scaffold fixture, one
  missing-output negative proof, and one passing command-surface replay.
- Evidence to capture during rehearsal: validator pass/fail output and public
  doc references to the new `/marcus_init` chain.
- Criteria to stop and revise docs before broader execution: validator errors
  are vague, `/marcus_init` is still workflow-only in the registry, or public
  docs drift from the workflow contract.

## Rollback Check

- Reverting the validator and command-surface wiring should restore the
  previous workflow-only `/marcus_init` behavior without changing the shell
  scaffold itself.
