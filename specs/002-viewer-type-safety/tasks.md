# Task Breakdown: Viewer Type Safety

> Feature ID: `002-viewer-type-safety`
> Plan: `plan.md`

## Task Rules

- `[P]` means parallel-safe with disjoint write scope.
- Every task needs one owner and one verification method.
- Do not mark a task complete until `verification.md` has evidence.
- Every task must name its write scope, docs targets, and sync expectation explicitly.
- If a task changes the public slash-command surface or runtime behavior, it must update the matching docs and verification evidence in the same slice.

## Tasks

- [x] `T001` Owner: `alan-tech-lead` Write Scope: `app/api/chroma/route.ts`. Verification: route uses `execFile` and lint passes. Docs: `quickstart.md`, `verification.md`, `agent-routing.md`. Sync: If the implementation scope widens, update the feature package, quickstart replay path, and verification notes before additional code edits.
- [x] `T002` Owner: `benny-frontend-engineer` Write Scope: `lib/graphTypes.ts`, `app/page.tsx`, `components/Inspector.tsx`. Verification: no explicit `any` in those files and build passes. Docs: `quickstart.md`, `verification.md`, `agent-routing.md`. Sync: If the implementation scope widens, update the feature package, quickstart replay path, and verification notes before additional code edits.
- [x] `T003` Owner: `benny-frontend-engineer` Write Scope: `components/GraphVisualizer.tsx`. Verification: no explicit `any`, no setState-in-effect lint error, build passes. Docs: `quickstart.md`, `verification.md`, `agent-routing.md`. Sync: If the implementation scope widens, update the feature package, quickstart replay path, and verification notes before additional code edits.
- [x] `T004` Owner: `ada-qa-agent` Write Scope: `verification.md`. Verification: `npm run lint` and `npm run build` evidence recorded. Docs: `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.

## Parallel Groups

- Group B: `T001`, `T002`, `T003`, `T004` close the loop after the implementation artifacts and validation evidence exist.

## Execution Monitoring

- Required pre-code gates: `validate_specs.py`, `build_execution_brief.py`, `validate_execution_brief_freshness.py`, and `validate_execution_readiness.py` for the active feature.
- Mid-slice checkpoints: keep `verification.md`, `quickstart.md`, and `agent-routing.md` synchronized with any scope or replay-path change.
- Circuit breaker after repeated failure: after three repeated failures of the same command or validator without new evidence, stop coding and repair the contract, routing, or implementation assumption that is actually failing.
- Human escalation trigger: if review findings show the feature now depends on an unrelated repo area or undocumented product behavior, route back to planning/reconciliation before more edits.

## Review Loop Tasks

- `R1`: Challenge the slice boundary, hidden dependencies, and whether the current quickstart is replayable without improvisation.
- `R2`: Confirm the execution brief names the right docs-to-read set for the active task shape and does not widen context without evidence.
- `R3`: Verify the final evidence and release recommendation match the real commands and residual risk.

## Completion Checklist

- [x] `spec.md` accepted
- [x] `plan.md` accepted
- [x] `contracts/` complete or explicitly not applicable
- [x] `tasks.md` complete
- [x] `verification.md` contains evidence
- [x] Root `agents.md` updated or explicitly scheduled for update in verification notes
- [x] TrustGraph write attempted or intentionally deferred with reason
