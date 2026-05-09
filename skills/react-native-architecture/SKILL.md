---
name: react-native-architecture
description: Define React Native topology, state boundaries, and native integration risks
---

# React Native Architecture Standard

Use this skill when the mobile stack depends on React Native topology.

## Required Reads

- [rn-contract.md](references/rn-contract.md)
- The app's current React Native architecture when it exists.

## Operating Rules

- Prefer the smallest architecture that fits the shipped behavior.
- Keep navigation, state, and native concerns explicit.
- Do not add architecture layers without a clear benefit.

## Output Expectations

- State the React Native topology and the reason for it.
- Identify the boundary between JS and native concerns.
- Describe the verification required for shipped behavior.
