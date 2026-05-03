# Data Model: Refactor Planning Command Gates

> Feature ID: `016-refactor-planning-command-gates`

## Entities

### Readiness Inputs

- `agents.md`
- `docs/prd.md`
- `docs/tasks.md`
- `docs/knowledge.md`
- `docs/decisions.md`
- `docs/memory.md`
- `docs/planning/flows.md`
- `docs/planning/screens.md`
- `docs/planning/diagrams.md`
- `docs/development/development_manifest.json`
- `docs/development/index.md`
- development-ledger bucket content as enforced by `validate_development_docs.py --strict-counts`

### Closeout Outputs

- `agents.md`
- `docs/ADR_REFACTOR_LOG.md`

## Validation Rules

- `validate_refactor_planning_readiness.py` checks readiness inputs and runs the
  development-doc quality gate.
- `validate_refactor_planning_outputs.py` checks closeout outputs.
- `validate_command_surface.py` checks public wiring for `/refactor-planning`.
