# Task Breakdown: Substantive Development Docs Quality

> Feature ID: `007-substantive-development-docs-quality`
> Plan: `plan.md`

## Task Rules

- `[P]` means parallel-safe with disjoint write scope.
- Every task needs one owner and one verification method.
- Do not mark a task complete until `verification.md` has evidence.

## Tasks

- [x] `T001` Owner: `ada-qa-agent` Scope: strengthen
      `validate_development_docs.py`. Verification: rejects placeholders,
      shallow notes, missing rationale, and missing code paths.
- [x] `T002` Owner: `ada-qa-agent` Scope: strengthen
      `validate_doc_sync.py`. Verification: rejects shallow unfinished sync notes.
- [x] `T003` Owner: `knowledge-work-architecture` Scope: add quality rubric and
      improve templates. Verification: templates include PM notes, commentary,
      change logs, evidence, and risk prompts.
- [x] `T004` Owner: `marcus-ai-orchestrator` Scope: update `/develop`,
      `.clinerules`, README, USAGE, and release notes. Verification: quality
      gate is visible to future agents.

## Parallel Groups

- Group A: validator changes and template changes are parallel-safe.
- Group B: workflow/docs updates after quality rules are defined.

## Completion Checklist

- [x] `spec.md` accepted
- [x] `plan.md` accepted
- [x] `contracts/` complete or explicitly not applicable
- [x] `tasks.md` complete
- [x] `verification.md` contains evidence
- [x] Root `agents.md` updated
- [x] TrustGraph write attempted
