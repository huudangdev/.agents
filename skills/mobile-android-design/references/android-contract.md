# Android Design Contract

Use this skill when the target experience must respect Android system behavior.

## Required Inputs

- Active feature docs and Android configuration
- Navigation, permission, and SDK constraints
- Verification or device assumptions that affect the flow

## Decision Rules

- Respect safe areas, back behavior, and Android hit targets.
- Prefer native Android constraints over generic mobile styling.
- Escalate new dependencies only when the repo cannot already verify the concern.

## Output Contract

- State the Android-specific constraints.
- Identify safe areas, navigation, and failure states.
- Describe the verification required on a real Android device or emulator.
