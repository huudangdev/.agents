---
description: Validate that Marcus Fleet routing still keeps narrow tasks narrow after workflow or skill-index changes.
---

# Marcus Routecheck Workflow

Use this workflow after changing `/develop`, `SKILLS_INDEX.md`, or routing-heavy
skills.

## Required Actions

1. Read `.agents/ROUTING_REGRESSION_CHECKLIST.md`.
2. Run:
   ```bash
   python3 .agents/scripts/validate_routing_regression.py --root .
   ```
3. Replay the five task shapes in the checklist when a release changes routing
   behavior materially:
   - `UI-only`
   - `Frontend behavior`
   - `Backend/API`
   - `Data/contract`
   - `Architecture/refactor`
4. Fail the routecheck if any narrow task widens into unrelated database,
   analytics, infrastructure, or full-repo context without explicit evidence.
5. Record any routing regression in the active feature's `verification.md` or
   in the release note before trusting the new release.

## Output

- Routing regression validator result
- Checklist replay notes
- `pass` or `fail` decision for the new routing behavior
