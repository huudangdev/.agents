# Quickstart Validation: Planning Deep Research V30

> Feature ID: `004-planning-deep-research-v30`

## Local Preconditions

- Required services: none beyond the local tools already referenced by this feature's verification commands.
- Required environment variables: inherit the existing project-local environment only; do not introduce new secrets during replay.
- Required commands: `python3`, `python3`, `python3`.
- Planning remains a docs-first workflow; no code-generation runtime is required.
- Research validators must run locally without network dependencies.

## Validation Path

1. Rebuild the execution brief for the active task shape:
   ```bash
   python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/004-planning-deep-research-v30 --task-shape general
   ```
2. Run the primary validation commands:
   ```bash
   python3 .agents/scripts/validate_specs.py --feature .agents/specs/004-planning-deep-research-v30
   python3 -m py_compile .agents/scripts/validate_planning_research.py
   ```
3. Confirm the feature package is still execution-ready:
   ```bash
   python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/004-planning-deep-research-v30
   ```

## Expected Artifacts

- Updated `.agents/workflows/planning.md` preserving the legacy `/docs` outputs.
- Research ledger templates under `.agents/templates/`.
- `validate_planning_research.py` plus reconciled spec artifacts.
- A refreshed `.agents/specs/<feature-id>/execution-brief.md` aligned with the current docs package.

## POC Rehearsal

- Smallest professional slice: execute the documented commands for `004-planning-deep-research-v30`, verify the evidence lands in `verification.md`, and confirm readiness still passes without widening context beyond the feature package.
- Capture evidence: command output, any manual confirmation steps, and the final release recommendation.
- Stop and revise if the replay requires reading unrelated repo areas, inventing missing docs, or skipping a failing validator.

## Rollback Check

- Restore the previous planning workflow and remove only the additive research ledger templates and validator if the rollout is rejected.
- If the replay exposes a broader governance mismatch, roll back the docs package changes first and only then reconsider code-level rollback.
