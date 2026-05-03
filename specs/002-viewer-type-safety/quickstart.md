# Quickstart Validation: Viewer Type Safety

> Feature ID: `002-viewer-type-safety`

## Local Preconditions

- Required services: none beyond the local tools already referenced by this feature's verification commands.
- Required environment variables: inherit the existing project-local environment only; do not introduce new secrets during replay.
- Required commands: `npm`, `npm`, `python3`.
- Change into `.agents/trustgraph-viewer` before running frontend commands.
- Use the local Node/npm toolchain already configured for the viewer package.

## Validation Path

1. Rebuild the execution brief for the active task shape:
   ```bash
   python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/002-viewer-type-safety --task-shape frontend-behavior
   ```
2. Run the primary validation commands:
   ```bash
   npm run lint
   npm run build
   ```
3. Confirm the feature package is still execution-ready:
   ```bash
   python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/002-viewer-type-safety
   ```

## Expected Artifacts

- `lib/graphTypes.ts` with shared viewer types.
- `app/api/chroma/route.ts` using argv-based subprocess execution.
- Updated typed viewer files under `app/` and `components/`.
- A refreshed `.agents/specs/<feature-id>/execution-brief.md` aligned with the current docs package.

## POC Rehearsal

- Smallest professional slice: execute the documented commands for `002-viewer-type-safety`, verify the evidence lands in `verification.md`, and confirm readiness still passes without widening context beyond the feature package.
- Capture evidence: command output, any manual confirmation steps, and the final release recommendation.
- Stop and revise if the replay requires reading unrelated repo areas, inventing missing docs, or skipping a failing validator.

## Rollback Check

- Restore the touched viewer files and remove `lib/graphTypes.ts` only if no remaining imports depend on it.
- If the replay exposes a broader governance mismatch, roll back the docs package changes first and only then reconsider code-level rollback.
