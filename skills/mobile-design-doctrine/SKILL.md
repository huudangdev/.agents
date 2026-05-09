---
name: mobile-design-doctrine
description: Use when designing mobile interactions, gestures, motion, and recovery flows under real device constraints.
---

# Mobile Design Doctrine

Use this skill to shape mobile interactions that feel stable under real device constraints.

## Required Reads

1. Root `agents.md`.
2. Active feature docs and mobile screen maps.
3. Existing mobile design rules or constraints.
4. [`references/mobile-doctrine-contract.md`](references/mobile-doctrine-contract.md).

## Operating Rules

- Read the mobile flow and state transitions first.
- Respect gesture support, safe areas, and motion costs.
- Prefer platform-native behavior where possible.
- Keep the flow practical on real devices.

## Output Expectations

- State the mobile flow, failure states, and recovery path.
- Identify the platform-specific constraints.
- Describe how frontend and QA can verify the result.
