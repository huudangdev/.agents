# Quickstart Validation: Refactor Planning Toolchain Gate

> Feature ID: `017-refactor-planning-toolchain-gate`

## Local Preconditions

- Required commands: `python3`, `node`, `npm`, `npx`

## Validation Path

```bash
python3 scripts/validate_refactor_planning_toolchain.py --root <project-root>
python3 scripts/validate_command_surface.py --root .
```

## Expected Artifacts

- `scripts/validate_refactor_planning_toolchain.py`
- Updated `workflows/refactor-planning.md`
- Updated `SLASH_COMMAND_REGISTRY.md`
- Updated README and `USAGE_GUIDE.md`

## POC Rehearsal

- Positive: create `<root>/node_modules/.bin/eslint` in a temp fixture root and
  replay the validator.
- Negative: remove the local ESLint marker and replay again.

## Rollback Check

- Remove `scripts/validate_refactor_planning_toolchain.py` and delete the
  toolchain stage from `workflows/refactor-planning.md`, then remove references
  from README, `USAGE_GUIDE.md`, `SLASH_COMMAND_REGISTRY.md`, and
  `scripts/validate_command_surface.py`.
