# Task Breakdown: Marcus Spec Foundation

> Feature ID: `001-marcus-spec-foundation`
> Plan: `plan.md`

## Task Rules

- `[P]` means parallel-safe with disjoint write scope.
- Every task needs one owner and one verification method.
- Do not mark a task complete until `verification.md` has evidence.

## Tasks

- [x] `T001` Owner: `sophia-product-manager` Scope:
      `.agents/memory/constitution.md`, `spec.md`. Verification: constitution
      exists and `spec.md` has no unresolved clarification markers.
- [x] `T002` [P] Owner: `david-systems-architect` Scope:
      `.agents/templates/*.md`, `plan.md`, `data-model.md`,
      `contracts/spec-workspace.md`. Verification: required templates exist.
- [x] `T003` [P] Owner: `alan-tech-lead` Scope:
      `.agents/scripts/create_feature_spec.py`,
      `.agents/scripts/validate_specs.py`. Verification: scripts parse and
      `create_feature_spec.py` created this feature workspace.
- [x] `T004` [P] Owner: `marcus-ai-orchestrator` Scope:
      `.agents/workflows/marcus_*.md`, `agent-routing.md`. Verification:
      workflows map specify, clarify, plan, tasks, verify.
- [x] `T005` Owner: `ada-qa-agent` Scope: `verification.md`. Verification:
      `validate_specs.py --feature .agents/specs/001-marcus-spec-foundation`
      passes.

## Parallel Groups

- Group A: `T002`, `T003`, `T004` are parallel-safe after `T001` because their
  write scopes are disjoint.
- Group B: `T005` runs after generated artifacts are populated.

## Completion Checklist

- [x] `spec.md` accepted
- [x] `plan.md` accepted
- [x] `contracts/` complete or explicitly not applicable
- [x] `tasks.md` complete
- [x] `verification.md` contains evidence
- [x] Root `agents.md` updated
- [x] TrustGraph write attempted
