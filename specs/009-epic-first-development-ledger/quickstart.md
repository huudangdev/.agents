# Quickstart Validation: Epic-First Development Ledger

> Feature ID: `009-epic-first-development-ledger`

## Local Preconditions

- Required services: none beyond the local tools already referenced by this feature's verification commands.
- Required environment variables: inherit the existing project-local environment only; do not introduce new secrets during replay.
- Required commands: `python3`, `python3`, `python3`.
- Use V31 epic-first topology for new ledgers unless legacy mode is explicitly requested.
- Legacy flat ledgers remain readable during migration but must not be treated as the new default.

## Validation Path

1. Rebuild the execution brief for the active task shape:
   ```bash
   python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/009-epic-first-development-ledger --task-shape architecture-refactor
   ```
2. Run the primary validation commands:
   ```bash
   python3 .agents/scripts/validate_specs.py --feature .agents/specs/009-epic-first-development-ledger
   python3 .agents/scripts/validate_development_docs.py --strict-counts
   ```
3. Confirm the feature package is still execution-ready:
   ```bash
   python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/009-epic-first-development-ledger
   ```

## Expected Artifacts

- Epic-first scaffold, validator, sync tooling, and templates.
- Workflow/docs/skills updated to route future agents to the epic-first structure.
- Verification evidence for V31 scaffold smoke and negative topology checks.
- A refreshed `.agents/specs/<feature-id>/execution-brief.md` aligned with the current docs package.

## POC Rehearsal

- Smallest professional slice: execute the documented commands for `009-epic-first-development-ledger`, verify the evidence lands in `verification.md`, and confirm readiness still passes without widening context beyond the feature package.
- Capture evidence: command output, any manual confirmation steps, and the final release recommendation.
- Stop and revise if the replay requires reading unrelated repo areas, inventing missing docs, or skipping a failing validator.

## Rollback Check

- Preserve legacy-flat compatibility and remove only the new epic-first enforcement if the migration must be paused.
- If the replay exposes a broader governance mismatch, roll back the docs package changes first and only then reconsider code-level rollback.
