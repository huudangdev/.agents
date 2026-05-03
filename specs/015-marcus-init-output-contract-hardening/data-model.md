# Data Model: Marcus Init Output Contract Hardening

> Feature ID: `015-marcus-init-output-contract-hardening`

## Entities

### Scaffold Output

- `docs/`
- `.agents/`
- `.clinerules`
- `agents.md`
- `.agents/agents.md`
- `docs/prd_draft.md`

Each required output must exist. File outputs must also be non-empty.

## Validation Rules

- `validate_marcus_init_outputs.py` checks scaffold outputs for a provided
  project root.
- `validate_command_surface.py` checks that `/marcus_init` is part of the
  published script-backed command contract.
