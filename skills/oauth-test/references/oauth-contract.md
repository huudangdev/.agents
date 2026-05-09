# OAuth Test Contract

Use this skill when authentication or authorization flows need validation.

## Required Inputs

- The OAuth flow under test
- The provider, redirect, and scope constraints
- The expected success and failure paths

## Decision Rules

- Test both happy path and hostile path behavior.
- Verify redirect, token, and state handling explicitly.
- Treat auth regressions as blocking until proven safe.

## Output Contract

- State the exact OAuth behavior under test.
- Identify the failure modes and required evidence.
- Describe the verification steps and expected result.
