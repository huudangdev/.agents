---
name: oauth-test
description: Verify OAuth authentication and authorization flows with hostile evidence-based tests
---

# OAuth Test

Use this skill when authentication or authorization flows need validation.

## Required Reads

- [oauth-contract.md](references/oauth-contract.md)
- The OAuth flow under test when it exists.

## Operating Rules

- Test both happy path and hostile path behavior.
- Verify redirect, token, and state handling explicitly.
- Treat auth regressions as blocking until proven safe.

## Output Expectations

- State the exact OAuth behavior under test.
- Identify the failure modes and required evidence.
- Describe the verification steps and expected result.
