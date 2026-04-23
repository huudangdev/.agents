# Task Breakdown: Brownfield Doc Reconcile Command

> Feature ID: `010-brownfield-doc-reconcile-command`
> Plan: `plan.md`

## Task Rules

- Every task needs one owner and one verification method.

## Tasks

- [x] `T001` Owner: `marcus-ai-orchestrator` Scope: add
      `/doc_reconcile` workflow. Verification: workflow file exists.
- [x] `T002` Owner: `development-ledger-architect` Scope: add code/docs audit
      script. Verification: audit smoke creates markdown report.
- [x] `T003` Owner: `ada-qa-agent` Scope: add `issues.md` template and V31
      validator requirement. Verification: scaffold includes issues and negative
      smoke rejects missing issues.
- [x] `T004` Owner: `knowledge-work-architecture` Scope: update README, USAGE,
      `.clinerules`, release notes, and `/develop`. Verification: docs mention
      command and issue-file policy.
- [x] `T005` Owner: `ada-qa-agent` Scope: final validation evidence.
      Verification: `verification.md` contains command results.

## Completion Checklist

- [x] `spec.md` accepted
- [x] `plan.md` accepted
- [x] `contracts/` complete or explicitly not applicable
- [x] `tasks.md` complete
- [x] `verification.md` contains evidence
- [ ] Root `agents.md` updated
- [x] TrustGraph write attempted
