# Tailwind Mobile-First Contract

Use this skill when mobile layout or responsive behavior is driven by Tailwind.

## Required Inputs

- The current responsive layout problem
- Breakpoint and spacing constraints
- The target device assumptions

## Decision Rules

- Design mobile first and expand outward.
- Avoid desktop-first overrides that hide mobile defects.
- Prefer explicit, readable utility composition over cleverness.

## Output Contract

- State the responsive strategy.
- Identify the mobile layout boundaries.
- Describe the verification expected on small screens.
