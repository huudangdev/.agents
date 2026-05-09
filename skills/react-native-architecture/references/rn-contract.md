# React Native Architecture Contract

Use this skill when the mobile stack depends on React Native topology.

## Required Inputs

- The app's current React Native architecture
- State-management, navigation, and native-module constraints
- Performance and verification expectations

## Decision Rules

- Prefer the smallest architecture that fits the shipped behavior.
- Keep navigation, state, and native concerns explicit.
- Do not add architecture layers without a clear benefit.

## Output Contract

- State the React Native topology and the reason for it.
- Identify the boundary between JS and native concerns.
- Describe the verification required for shipped behavior.
