# Mobile Motion Contract

Use this skill when motion clarifies state or interaction on mobile.

## Required Inputs

- Target interaction and current motion stack
- Interruptibility, reduced-motion, and hit-target constraints
- Device assumptions and performance budget

## Decision Rules

- Use spring-like motion when it communicates state better than linear easing.
- Preserve touchability during scale and transition states.
- Do not add animation tooling unless the repo cannot support the need.

## Output Contract

- State the motion goal and the interaction it clarifies.
- Identify accessibility and performance constraints.
- Describe how the motion should be verified visually.
