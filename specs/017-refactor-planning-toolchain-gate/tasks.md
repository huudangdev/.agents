# Tasks: Refactor Planning Toolchain Gate

> Feature ID: `017-refactor-planning-toolchain-gate`

## Tasks

- [x] `T001` Toolchain validator
  - Owner: `marcus-ai-orchestrator`
  - Write Scope: `.agents/scripts/validate_refactor_planning_toolchain.py`
  - Verification: `python3 -m py_compile` passes; validator fails closed with explicit messages
  - Docs: none
  - Sync: none
- [x] `T002` Workflow wiring
  - Owner: `marcus-ai-orchestrator`
  - Write Scope: `.agents/workflows/refactor-planning.md`
  - Verification: workflow contains the exact script invocation under a dedicated stage
  - Docs: `.agents/workflows/refactor-planning.md`
  - Sync: none
- [x] `T003` Public contract wiring
  - Owner: `marcus-ai-orchestrator`
  - Write Scope: `.agents/SLASH_COMMAND_REGISTRY.md`, `.agents/README.md`, `.agents/USAGE_GUIDE.md`
  - Verification: the toolchain gate is named explicitly in all public docs
  - Docs: README, `USAGE_GUIDE.md`, registry
  - Sync: rerun command-surface validation
- [x] `T004` Command-surface enforcement
  - Owner: `marcus-ai-orchestrator`
  - Write Scope: `.agents/scripts/validate_command_surface.py`
  - Verification: `python3 .agents/scripts/validate_command_surface.py --root .` passes
  - Docs: none
  - Sync: none
- [x] `T005` Evidence + brief rebuild
  - Owner: `marcus-ai-orchestrator`
  - Write Scope: `specs/017-refactor-planning-toolchain-gate/verification.md`, `execution-brief.md`
  - Verification: bounded positive/negative fixtures are recorded; freshness passes after brief rebuild
  - Docs: `verification.md`, `execution-brief.md`
  - Sync: rebuild the brief after final evidence changes

## Parallel Groups

- Group A: `T001` + `T002` (implementation + workflow wiring)
- Group B: `T003` + `T004` (public contract + enforcement)
- Group C: `T005` (verification after wiring is stable)

## Execution Monitoring

- Stop if `validate_command_surface.py --root .` fails after wiring changes.
- Treat any change that starts executing the runtime toolchain inside the
  validator as out of scope.

## Review Loop Tasks

- Ensure validator output is actionable (names missing binary/ESLint).
- Ensure docs and workflow mention the validator in the correct phase.
