# Task Breakdown: {{FEATURE_TITLE}}

> Feature ID: `{{FEATURE_ID}}`
> Plan: `plan.md`

## Task Rules

- `[P]` means parallel-safe with disjoint write scope.
- Every task needs one owner and one verification method.
- Do not mark a task complete until `verification.md` has evidence.

## Tasks

- [ ] `T001` Owner: `sophia-product-manager` Scope: refine `spec.md`.
      Verification: no unresolved clarification markers unless accepted.
- [ ] `T002` Owner: `david-systems-architect` Scope: complete `plan.md`,
      `data-model.md`, and `contracts/`. Verification: constitution gates pass.
- [ ] `T003` Owner: `marcus-ai-orchestrator` Scope: complete
      `agent-routing.md`. Verification: every task has one owner and write scope.
- [ ] `T004` Owner: `ada-qa-agent` Scope: complete `verification.md` plan.
      Verification: commands or manual checks are repeatable.

## Parallel Groups

- Group A: TBD
- Group B: TBD

## Completion Checklist

- [ ] `spec.md` accepted
- [ ] `plan.md` accepted
- [ ] `contracts/` complete or explicitly not applicable
- [ ] `tasks.md` complete
- [ ] `verification.md` contains evidence
- [ ] Root `agents.md` updated
- [ ] TrustGraph write attempted
