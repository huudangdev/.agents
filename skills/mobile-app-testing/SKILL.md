---
name: mobile-app-testing
description: Verify mobile behavior with hostile, device-aware tests and release-blocking evidence
---

# Mobile App Testing

Use this skill to verify mobile behavior under device and emulator constraints.

## Required Reads

1. Root `agents.md`.
2. Active feature spec, tasks, and verification docs.
3. Existing mobile test harness or CI commands.
4. [`references/mobile-qa-contract.md`](references/mobile-qa-contract.md).

## Operating Rules

- Focus on device-specific risk.
- Write deterministic tests with explicit selectors or IDs.
- Capture executed evidence, not just assertions.
- Block sign-off when the evidence is vague.

## Output Expectations

- State the mobile behavior under test.
- Identify the device assumption and failure mode.
- Describe the reproduced evidence and remaining risk.
