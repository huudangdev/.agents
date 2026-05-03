# Quickstart Validation: Substantive Development Docs Quality

> Feature ID: `007-substantive-development-docs-quality`

## Local Preconditions

- Required services: none beyond the local tools already referenced by this feature's verification commands.
- Required environment variables: inherit the existing project-local environment only; do not introduce new secrets during replay.
- Required commands: `python3`, `python3`, `python3`.
- Generated ledger docs are drafts until concrete project facts replace placeholders.
- Strict validators are expected to fail on template-only output by design.

## Validation Path

1. Rebuild the execution brief for the active task shape:
   ```bash
   python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/007-substantive-development-docs-quality --task-shape general
   ```
2. Run the primary validation commands:
   ```bash
   python3 .agents/scripts/validate_specs.py --feature .agents/specs/007-substantive-development-docs-quality
   python3 .agents/scripts/validate_development_docs.py --strict-counts
   ```
3. Confirm the feature package is still execution-ready:
   ```bash
   python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/007-substantive-development-docs-quality
   ```

## Expected Artifacts

- Stricter development-docs and doc-sync validators.
- Updated templates and shared quality rubric.
- Workflow and operator docs describing the substantive quality bar.
- A refreshed `.agents/specs/<feature-id>/execution-brief.md` aligned with the current docs package.

## POC Rehearsal

- Smallest professional slice: execute the documented commands for `007-substantive-development-docs-quality`, verify the evidence lands in `verification.md`, and confirm readiness still passes without widening context beyond the feature package.
- Capture evidence: command output, any manual confirmation steps, and the final release recommendation.
- Stop and revise if the replay requires reading unrelated repo areas, inventing missing docs, or skipping a failing validator.

## Rollback Check

- Revert the stricter quality checks and template/rubric changes together if the quality bar must be loosened.
- If the replay exposes a broader governance mismatch, roll back the docs package changes first and only then reconsider code-level rollback.
