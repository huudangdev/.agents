# Task Breakdown: Epic-First Development Ledger

> Feature ID: `009-epic-first-development-ledger`
> Plan: `plan.md`

## Task Rules

- `[P]` means parallel-safe with disjoint write scope.
- Every task needs one owner and one verification method.

## Tasks

- [x] `T001` Owner: `marcus-ai-orchestrator` Scope: update
      `create_development_docs.py` for V31 scaffold. Verification: scaffold
      creates `E-001-*` tree.
- [x] `T002` Owner: `ada-qa-agent` Scope: update
      `validate_development_docs.py` for topology, ID, parent, orphan, and
      placeholder gates. Verification: negative smoke fails malformed ledger.
- [x] `T003` Owner: `knowledge-work-architecture` Scope: update templates,
      manifest, index, and rubric. Verification: templates describe V31.
- [x] `T004` Owner: `marcus-ai-orchestrator` Scope: update `/develop`,
      `.clinerules`, README, USAGE, release notes. Verification: future agents
      can discover V31 rules.
- [x] `T005` Owner: `development-ledger-architect` Scope: add dedicated skill.
      Verification: skill exists and states canonical topology.
- [x] `T006` Owner: `ada-qa-agent` Scope: final validation evidence.
      Verification: `verification.md` contains command results.
- [x] `T007` Owner: `sophia-product-manager` Scope: enforce product-grade
      Story/Priority/Issues/Relationship/Work Log/docs-before-code rules.
      Verification: validators and templates include required sections and
      sync notes require docs-before-code evidence.

## Completion Checklist

- [x] `spec.md` accepted
- [x] `plan.md` accepted
- [x] `contracts/` complete or explicitly not applicable
- [x] `tasks.md` complete
- [x] `verification.md` contains evidence
- [ ] Root `agents.md` updated
- [x] TrustGraph write attempted
