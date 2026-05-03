# Research Notes: Refactor Planning Toolchain Gate

> Feature ID: `017-refactor-planning-toolchain-gate`

## Findings

- `/refactor-planning` invokes Node-based tooling and should fail fast when the
  Node toolchain is missing.
- ESLint may be installed globally or as a local dev dependency; both are valid
  but must be explicit.

## Decision

Use a non-invasive validator that checks for required binaries and ESLint
availability without executing any runtime commands.

