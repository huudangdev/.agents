# Refactor Planning Command Contract

Owner: `marcus-ai-orchestrator`

## Purpose

Define the deterministic entry and exit gates for `/refactor-planning`.

## Contract

- `/refactor-planning` must run
  `python3 .agents/scripts/validate_refactor_planning_readiness.py --root .`
  before AST parsing or brownfield refactor planning proceeds.
- `/refactor-planning` must run
  `python3 .agents/scripts/validate_refactor_planning_outputs.py --root .`
  before claiming closeout.
- The readiness validator must enforce the current brownfield planning-doc set
  and development-ledger quality gate.
- README, `USAGE_GUIDE.md`, `SLASH_COMMAND_REGISTRY.md`, and
  `workflows/refactor-planning.md` must all expose the same validator-backed chain.

## Compatibility Check

- Positive replay: readiness/output validators pass on valid fixtures and
  `validate_command_surface.py --root .` passes.
- Negative replay: removing a required planning doc causes readiness failure.
