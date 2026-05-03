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
5. Explicitly define in-scope, out-of-scope, rollback expectations, and the
   evidence required before the feature can be considered done.
6. Populate `## 10. Review Loop` with at least:
   - a scope challenge round
   - a product-quality round
   - a go/no-go to planning round
7. Run:
   ```bash
   python3 .agents/scripts/validate_specs.py --feature .agents/specs/<feature-id> --allow-clarifications
   ```
8. Revise `spec.md` after each review round until the challenge findings are
   either resolved or explicitly accepted as residual risk.
9. Stop before planning if unresolved clarification markers remain or the
   review loop is incomplete.

## Output

- `.agents/specs/<feature-id>/spec.md`
- A short list of unresolved clarifications, or a statement that the spec is
  ready for `/marcus.plan`.
