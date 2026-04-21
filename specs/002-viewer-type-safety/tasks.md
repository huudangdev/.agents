# Task Breakdown: Viewer Type Safety

> Feature ID: `002-viewer-type-safety`
> Plan: `plan.md`

## Task Rules

- `[P]` means parallel-safe with disjoint write scope.
- Every task needs one owner and one verification method.
- Do not mark a task complete until `verification.md` has evidence.

## Tasks

- [x] `T001` Owner: `alan-tech-lead` Scope:
      `app/api/chroma/route.ts`. Verification: route uses `execFile` and lint
      passes.
- [x] `T002` Owner: `benny-frontend-engineer` Scope:
      `lib/graphTypes.ts`, `app/page.tsx`, `components/Inspector.tsx`.
      Verification: no explicit `any` in those files and build passes.
- [x] `T003` Owner: `benny-frontend-engineer` Scope:
      `components/GraphVisualizer.tsx`. Verification: no explicit `any`, no
      setState-in-effect lint error, build passes.
- [x] `T004` Owner: `ada-qa-agent` Scope: `verification.md`. Verification:
      `npm run lint` and `npm run build` evidence recorded.

## Parallel Groups

- Group A: `T001` and `T002` were parallel-safe by file scope.
- Group B: `T003` followed shared type creation.

## Completion Checklist

- [x] `spec.md` accepted
- [x] `plan.md` accepted
- [x] `contracts/` complete or explicitly not applicable
- [x] `tasks.md` complete
- [x] `verification.md` contains evidence
- [x] Root `agents.md` updated
- [x] TrustGraph write attempted
