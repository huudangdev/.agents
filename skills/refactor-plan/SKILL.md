---
name: refactor-plan
description: Use when planning incremental brownfield refactors with explicit risk, sequencing, and verification evidence.
---

# Refactor Plan

Use this skill when a brownfield change needs a surgical refactor plan rather than a rewrite.

## Required Reads

1. Root `agents.md`.
2. Active feature docs and affected files.
3. Relevant local tests or validators.
4. [`references/refactor-plan-contract.md`](references/refactor-plan-contract.md).

## Operating Rules

- Map imports, exports, side effects, and boundaries before suggesting change.
- Split the work into dependency-ordered phases.
- Attach a verification command to every phase.
- Stop if the package is too shallow to plan safely.

## Output Expectations

- Produce a sequence, risk map, and verification plan.
- Keep the plan incremental and reversible.
- Explain what must stay stable.
