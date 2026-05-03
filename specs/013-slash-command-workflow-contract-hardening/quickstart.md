# Quickstart Validation: Slash Command Workflow Contract Hardening

> Feature ID: `013-slash-command-workflow-contract-hardening`

## Local Preconditions

- Required services: none beyond the local `.agents` workspace
- Required environment variables: none
- Required commands: `python3`

## Validation Path

1. Run:
   ```bash
   python3 scripts/validate_command_surface.py --root .
   python3 scripts/validate_harness_contract.py --root .
   python3 scripts/validate_routing_regression.py --root .
   ```
2. Confirm:
   ```text
   The command-surface validator passes, and harness/routing gates remain green
   after the public command registry and doc-surface hardening.
   ```

## Expected Artifacts

- `.agents/SLASH_COMMAND_REGISTRY.md`
- Updated `README.md` and `USAGE_GUIDE.md`
- Updated `scripts/validate_command_surface.py`
- Refreshed `specs/013-slash-command-workflow-contract-hardening/execution-brief.md`

## POC Rehearsal

- Smallest end-to-end path to demonstrate: one positive replay of
  `validate_command_surface.py` plus one bounded negative proof where a copied
  public-doc marker is removed and validation fails on the specific command.
- Evidence to capture during rehearsal: passing validator output, bounded
  negative failure output, and no-regression harness/routing results.
- Criteria to stop and revise docs before broader execution: registry and public
  docs disagree, validator errors are vague, or existing governance gates fail.

## Rollback Check

- Reverting the registry and validator patches should restore the prior looser
  command-surface behavior without changing runtime source-edit workflows.
