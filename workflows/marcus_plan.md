---
description: Translate an accepted Marcus Fleet specification into a technical plan.
---

# Marcus Plan Workflow

Use this workflow only after the target `spec.md` is clear enough to implement.

## Required Actions

1. Read `.agents/memory/constitution.md`.
2. Read the target feature's `spec.md`, `research.md`, and existing project docs.
3. Complete `plan.md` with architecture, contracts, data model, rollback, and
   constitution gates.
4. Fill `contracts/`, `data-model.md`, `quickstart.md`, and `agent-routing.md`.
5. Any failed constitution gate must be justified in `## 8. Complexity Tracking`.
6. Run:
   ```bash
   python3 .agents/scripts/validate_specs.py --feature .agents/specs/<feature-id>
   ```

## Output

- `plan.md`
- `contracts/`
- `data-model.md`
- `quickstart.md`
- `agent-routing.md`
