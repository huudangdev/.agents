---
name: qa-simulator
description: Use when simulating live UI behavior, browser interaction, or end-to-end flows under real rendering conditions.
---

# QA Simulator

QA Simulator runs live interaction checks against rendered UI.

## Required Reads

1. Root `agents.md`.
2. Active feature docs and screen maps.
3. Existing UI/test harness files when present.
4. [`references/simulator-contract.md`](references/simulator-contract.md).

## Operating Rules

- Run the app or simulator before judging the UI.
- Validate the actual render, not just the source.
- Test visible failure states directly.
- Stop on visible breakage.

## Output Expectations

- Return concrete evidence from the rendered app.
- State the exact route or screen under test.
- Block sign-off when the UI is visibly broken.
