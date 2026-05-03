# Refactor Planning Toolchain Contract

Owner: `marcus-ai-orchestrator`

## Purpose

Define a deterministic prerequisite gate for `/refactor-planning` that fails
fast on missing toolchain requirements.

## Contract

- `/refactor-planning` MUST run
  `python3 .agents/scripts/validate_refactor_planning_toolchain.py --root .`
  before invoking `npx understand-anything`, `npx tsc --noEmit`, `eslint --fix`,
  or `npm run dev`.
- The toolchain validator MUST:
  - require `node`, `npm`, and `npx` in `PATH`
  - require ESLint either in `PATH` or at `<root>/node_modules/.bin/eslint*`
- README, `USAGE_GUIDE.md`, `SLASH_COMMAND_REGISTRY.md`, and
  `workflows/refactor-planning.md` MUST all expose the same toolchain gate.

