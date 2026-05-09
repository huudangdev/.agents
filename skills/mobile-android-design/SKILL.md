---
name: mobile-android-design
description: Design Android-specific mobile flows with safe areas, back behavior, and device constraints
---

# Android Design Specialist

Apply Android-specific UX and system behavior guidance when the feature targets Android directly.

## Required Reads

- [android-contract.md](references/android-contract.md)
- The active feature docs and Android configuration when they exist.

## Operating Rules

- Respect safe areas, back behavior, and Android hit targets.
- Prefer native Android constraints over generic mobile styling.
- Escalate new dependencies only when the repo cannot already verify the concern.

## Output Expectations

- State the Android-specific constraints.
- Identify safe areas, navigation, and failure states.
- Describe the verification required on a real Android device or emulator.
