# Flutter Architecture Contract

Use this skill when Flutter architecture or performance decisions are needed.

## Required Inputs

- The active feature docs and Flutter config
- State-management, async, and device constraints
- Verification or build expectations

## Decision Rules

- Prefer the repo's current stack and state model.
- Keep presentation, domain, and data boundaries explicit.
- Verify widget trees and build health locally.

## Output Contract

- State the Flutter topology and why it fits.
- Identify isolate, async, and offline/error boundaries.
- Describe the verification required before implementation.
