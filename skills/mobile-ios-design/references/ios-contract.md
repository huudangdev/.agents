# iOS Design Contract

Use this skill when the target experience must respect iPhone or iPad behavior.

## Required Inputs

- Active feature docs and iOS configuration
- Safe area, permission, and navigation constraints
- Motion expectations and device class assumptions

## Decision Rules

- Respect Dynamic Island, home indicator, and navigation stack behavior.
- Prefer native iOS materials and spacing over generic styling.
- Escalate dependencies only when the need is documented and real.

## Output Contract

- State the iOS-specific constraints.
- Identify the safe areas, hierarchy, and motion rules.
- Describe the verification required on a real iOS device or simulator.
