---
name: flutter-architecture
description: Define Flutter topology, state boundaries, and performance-safe implementation paths
---

# Flutter Architecture

Use this skill when Flutter architecture or performance decisions are needed.

## Required Reads

- [flutter-contract.md](references/flutter-contract.md)
- The active feature docs and Flutter config when they exist.

## Operating Rules

- Prefer the repo's current stack and state model.
- Keep presentation, domain, and data boundaries explicit.
- Verify widget trees and build health locally.

## Output Expectations

- State the Flutter topology and why it fits.
- Identify isolate, async, and offline/error boundaries.
- Describe the verification required before implementation.
