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
5. Add execution monitoring notes: blocking pre-code gates, mid-slice evidence
   checkpoints, and escalation conditions.
6. Define the professional POC slice in `## 9. POC Slice and Review Cadence`:
   smallest slice, evidence expected, stop conditions, and proceed conditions.
7. Populate review topology and quickstart rehearsal so the docs package tells
   reviewers exactly how to challenge and replay the slice.
8. Any failed constitution gate must be justified in `## 8. Complexity Tracking`.
9. Run:
   ```bash
   python3 .agents/scripts/validate_specs.py --feature .agents/specs/<feature-id>
   ```
10. Do not hand off to `/marcus.tasks` until the planning package is deep
    enough for task derivation. `validate_execution_readiness.py` is a later
    gate owned by `/marcus.tasks` and `/marcus.review`, after
    `execution-brief.md` exists.

## Output

- `plan.md`
- `contracts/`
- `data-model.md`
- `quickstart.md`
- `agent-routing.md`
