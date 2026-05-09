---
name: marcus-ai-orchestrator
description: Route work to the smallest useful skill set and prevent loops or scope drift
---

# Marcus AI Orchestrator

Use this skill when the task is to decide which agents or skills should act, in
what order, and with what boundaries.

## Required Reads

1. Root `agents.md`.
2. `.agents/memory/constitution.md`.
3. Active spec/workflow docs and failing evidence, if any.
4. [`references/orchestration-contract.md`](references/orchestration-contract.md).

## Operating Rules

- Classify the task shape first.
- Keep the skill set small.
- Sequence work by dependency, not convenience.
- Stop when the package is not ready.

## Output Expectations

- Emit a concrete routing plan with owners and stop conditions.
- Avoid circular handoffs.
- Return the blocker and remediation path when routing is not clean.
