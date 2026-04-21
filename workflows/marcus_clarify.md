---
description: Resolve ambiguity in a Marcus Fleet feature specification.
---

# Marcus Clarify Workflow

Use this workflow after `/marcus.specify` and before `/marcus.plan`.

## Required Actions

1. Read the target feature's `spec.md`.
2. Extract every `[NEEDS CLARIFICATION: ...]` marker.
3. Ask only the questions that materially change architecture, tests, user
   behavior, tenant isolation, security, data retention, or rollback.
4. Record answers in `spec.md` under `## 6. Clarifications`.
5. Remove resolved markers and keep accepted risks explicit.
6. Run:
   ```bash
   python3 .agents/scripts/validate_specs.py --feature .agents/specs/<feature-id>
   ```

## Output

- Clarified `spec.md`
- Validation result
