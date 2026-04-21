---
description: Derive agent-owned implementation tasks from a Marcus Fleet plan.
---

# Marcus Tasks Workflow

Use this workflow after `/marcus.plan`.

## Required Actions

1. Read `plan.md`, `contracts/`, `data-model.md`, `quickstart.md`, and
   `agent-routing.md`.
2. Rewrite `tasks.md` into concrete work items.
3. Each task must include:
   - Stable task id
   - Owner skill
   - Write scope
   - Verification method
   - Documentation targets under `/docs/development/`
   - Doc sync expectation when source files change
4. Mark `[P]` only when write scopes are disjoint.
5. For implementation tasks, include the expected epic/module/feature/page/task
   note and the legacy docs likely to need append/targeted patch updates.
6. Run `validate_specs.py`.

## Output

- Executable `tasks.md`
- Parallel groups and sequencing
- Documentation target matrix
