# Data Model: Slash Command Workflow Contract Hardening

> Feature ID: `013-slash-command-workflow-contract-hardening`

## Entities

### Command Entry

- `command`: published slash command name such as `/marcus.tasks`
- `workflow_relpath`: owning workflow file under `.agents/workflows/`
- `required_markers`: script, gate, or shell markers that must remain visible
- `publication_surfaces`: README, `USAGE_GUIDE.md`, and registry

### Script-Backed Command

- A command whose workflow must name specific local scripts or shell entrypoints
- Validated strictly by `validate_command_surface.py`
- Examples: `/marcus.tasks`, `/develop`, `/planning`, `/bootstrap`

### Workflow-Only Command

- A command that remains part of the public surface but does not yet have one
  narrow deterministic local script chain
- Documented explicitly so models do not over-assume automation
- Examples: `/design`, `/marcus_init`

## Validation Rules

- Every script-backed published command must exist in the registry.
- Every registry entry must correspond to a real workflow file.
- Every required marker must be present in the workflow and public docs where
  applicable.
- Validation failure must identify the command and missing marker, not just the
  repo generically.
