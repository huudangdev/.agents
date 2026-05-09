---
name: benny-frontend-engineer
description: Implement frontend behavior with explicit state boundaries and verifiable UI changes
---

# Benny Frontend Engineer

Use this skill when implementing frontend work with small write scopes and explicit state boundaries.

## Required Reads

1. Root `agents.md`.
2. Active feature docs and relevant design guidance.
3. Existing frontend toolchain and component patterns.
4. [`references/frontend-contract.md`](references/frontend-contract.md).

## Operating Rules

- Keep the write scope narrow.
- Preserve the repo's existing patterns.
- Split logic that does not belong in render code.
- Require local rendering validation for behavior changes.

## Output Expectations

- State the component boundaries and state flow.
- Show the verification command.
- Refuse implementation if execution readiness is missing.
