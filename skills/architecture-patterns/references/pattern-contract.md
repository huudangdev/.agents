# Architecture Pattern Contract

Use this skill to choose the smallest pattern that satisfies the requirement.

## Required Inputs

- Current feature spec or change request
- Existing constraints, platform limits, and operational requirements
- Verification cost and rollout risk
- Existing repo conventions before proposing new structure

## Decision Rules

- Prefer the simplest pattern that fits the documented constraints.
- Do not recommend a larger topology unless the smaller one fails a concrete requirement.
- Name the tradeoff, the blast radius, and the verification burden.
- Separate the pattern choice from the implementation details.

## Output Contract

- State the pattern chosen and why.
- List the anti-patterns to avoid.
- Describe the file/module boundaries that follow from the choice.
- State what evidence would invalidate the recommendation.
