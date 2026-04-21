# Task Breakdown: Planning Deep Research V30

> Feature ID: `004-planning-deep-research-v30`
> Plan: `plan.md`

## Task Rules

- `[P]` means parallel-safe with disjoint write scope.
- Every task needs one owner and one verification method.
- Do not mark a task complete until `verification.md` has evidence.

## Tasks

- [x] `T001` Owner: `marcus-ai-orchestrator` Scope:
      `.agents/workflows/planning.md`. Verification: workflow preserves all 8
      legacy outputs and adds V30 gates.
- [x] `T002` [P] Owner: `sage-research-synthesis` Scope:
      `.agents/templates/planning-*-template.*`. Verification: source/evidence/
      claim/contradiction/manifest templates exist.
- [x] `T003` [P] Owner: `ada-qa-agent` Scope:
      `.agents/scripts/validate_planning_research.py`. Verification: Python AST
      parse passes.
- [x] `T004` Owner: `david-systems-architect` Scope:
      `contracts/planning-output-contract.md`, `data-model.md`. Verification:
      output contract documents legacy and extra files.

## Parallel Groups

- Group A: `T002` and `T003` are parallel-safe after `T001` direction is known.
- Group B: `T004` follows the final output contract.

## Completion Checklist

- [x] `spec.md` accepted
- [x] `plan.md` accepted
- [x] `contracts/` complete or explicitly not applicable
- [x] `tasks.md` complete
- [x] `verification.md` contains evidence
- [x] Root `agents.md` updated
- [x] TrustGraph write attempted
