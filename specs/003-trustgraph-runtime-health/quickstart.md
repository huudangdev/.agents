# Quickstart Validation: TrustGraph Runtime Health

> Feature ID: `003-trustgraph-runtime-health`

## Local Preconditions

- Required services: none beyond the local tools already referenced by this feature's verification commands.
- Required environment variables: inherit the existing project-local environment only; do not introduce new secrets during replay.
- Required commands: `npm`, `npm`, `python3`.
- Change into `.agents/trustgraph-viewer` before running viewer checks.
- Neo4j/Chroma may be offline; the feature must still report truthful health states.

## Validation Path

1. Rebuild the execution brief for the active task shape:
   ```bash
   python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/003-trustgraph-runtime-health --task-shape frontend-behavior
   ```
2. Run the primary validation commands:
   ```bash
   npm run build
   npm run lint
   ```
3. Confirm the feature package is still execution-ready:
   ```bash
   python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/003-trustgraph-runtime-health
   ```

## Expected Artifacts

- `app/api/health/route.ts` and `components/RuntimeStatus.tsx`.
- Shared runtime health types and config updates in `lib/`.
- Footer status updated to consume live health instead of a hardcoded label.
- A refreshed `.agents/specs/<feature-id>/execution-brief.md` aligned with the current docs package.

## POC Rehearsal

- Smallest professional slice: execute the documented commands for `003-trustgraph-runtime-health`, verify the evidence lands in `verification.md`, and confirm readiness still passes without widening context beyond the feature package.
- Capture evidence: command output, any manual confirmation steps, and the final release recommendation.
- Stop and revise if the replay requires reading unrelated repo areas, inventing missing docs, or skipping a failing validator.

## Rollback Check

- Remove `/api/health` and `RuntimeStatus`, then restore the previous footer status wiring and config values.
- If the replay exposes a broader governance mismatch, roll back the docs package changes first and only then reconsider code-level rollback.
