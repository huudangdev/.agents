# Data Model: Refactor Planning Toolchain Gate

> Feature ID: `017-refactor-planning-toolchain-gate`

## Entities

- `ToolchainPrereqs`
  - `node`: required
  - `npm`: required
  - `npx`: required
  - `eslint`: required (global PATH or local `node_modules/.bin`)

## Validation Rules

- Missing executable in `PATH` fails the gate with an explicit error.
- Missing ESLint fails the gate with an explicit error.

