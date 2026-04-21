---
description: Verify implementation evidence against a Marcus Fleet feature spec.
---

# Marcus Verify Workflow

Use this workflow before closing a feature.

## Required Actions

1. Read `spec.md`, `plan.md`, `tasks.md`, and `verification.md`.
2. Confirm every acceptance criterion has evidence.
3. Confirm every completed task has command output or manual evidence.
4. Confirm `agents.md` was updated.
5. Attempt a TrustGraph write.
6. Run:
   ```bash
   python3 .agents/scripts/validate_specs.py --feature .agents/specs/<feature-id>
   ```

## Output

- Updated `verification.md`
- Closeout summary
- Residual risk list
