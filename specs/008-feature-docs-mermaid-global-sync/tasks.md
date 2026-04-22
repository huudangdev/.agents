# Task Breakdown: Feature Docs Mermaid Global Sync

> Feature ID: `008-feature-docs-mermaid-global-sync`
> Plan: `plan.md`

## Task Rules

- `[P]` means parallel-safe with disjoint write scope.
- Every task needs one owner and one verification method.
- Do not mark a task complete until `verification.md` has evidence.

## Tasks

- [x] `T001` Owner: `ada-qa-agent` Scope: update
      `validate_development_docs.py` to require Mermaid. Verification: scaffold
      without valid completed docs fails.
- [x] `T002` Owner: `ada-qa-agent` Scope: update `validate_doc_sync.py` to
      require global `/docs` updates. Verification: source-only change fails.
- [x] `T003` Owner: `knowledge-work-architecture` Scope: update templates and
      rubric with Mermaid/global docs rules. Verification: templates contain
      `## Mermaid Diagram`.
- [x] `T004` Owner: `marcus-ai-orchestrator` Scope: update `/develop`, README,
      USAGE, and release notes. Verification: rules are visible to future agents.

## Parallel Groups

- Group A: validator and template updates are parallel-safe.
- Group B: docs/workflow updates after validator rules are defined.

## Completion Checklist

- [x] `spec.md` accepted
- [x] `plan.md` accepted
- [x] `contracts/` complete or explicitly not applicable
- [x] `tasks.md` complete
- [x] `verification.md` contains evidence
- [x] Root `agents.md` updated
- [x] TrustGraph write attempted
