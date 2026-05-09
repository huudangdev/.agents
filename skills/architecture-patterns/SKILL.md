---
name: architecture-patterns
description: Choose architecture patterns based on constraints, risk, and verification cost
---

# Architecture Patterns Specialist

Choose the smallest architecture pattern that satisfies the documented requirement.

## Required Reads

- [pattern-contract.md](references/pattern-contract.md)
- The active feature spec, plan, and verification notes when they exist.
- Local repo conventions before proposing new structure.

## Operating Rules

- Prefer the simplest pattern that fits the constraints.
- Do not recommend a larger topology unless the smaller one fails a concrete requirement.
- Name the tradeoff, blast radius, and verification burden.
- Separate pattern choice from implementation details.

## Output Expectations

- State the pattern chosen and why.
- List the anti-patterns to avoid.
- Describe the file/module boundaries that follow from the choice.
- State what evidence would invalidate the recommendation.
