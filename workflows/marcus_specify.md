---
description: Create or refine a feature-scoped Marcus Fleet specification.
---

# Marcus Specify Workflow

Use this workflow when a request is larger than a localized `/quick_fix`.

## Inputs

- Operator goal in plain language.
- Existing code or docs that constrain the goal.
- Any known deadline, compliance, tenant, rollback, or UX requirement.

## Required Actions

1. Read `.agents/memory/constitution.md`.
2. Create a feature workspace:
   ```bash
   python3 .agents/scripts/create_feature_spec.py "<Feature Title>" --prompt "<operator prompt>"
   ```
3. Fill `spec.md` with user stories, functional requirements, non-functional
   requirements, and acceptance criteria.
4. Mark unknowns with `[NEEDS CLARIFICATION: ...]`.
5. Stop before planning if unresolved clarification markers remain.

## Output

- `.agents/specs/<feature-id>/spec.md`
- A short list of unresolved clarifications, or a statement that the spec is
  ready for `/marcus.plan`.
