# Slash Command Contract

Owner: `marcus-ai-orchestrator`

## Purpose

Define what makes a published slash command valid inside `.agents`.

## Contract

- A published slash command must appear in `README.md` and `USAGE_GUIDE.md`.
- A workflow file must exist under `.agents/workflows/`.
- Script-backed commands must name their required script, gate, or shell
  invocations in the workflow.
- `.agents/SLASH_COMMAND_REGISTRY.md` must document the owning workflow and
  required invocation markers.
- `python3 scripts/validate_command_surface.py --root .` is the compatibility
  check for this contract.

## Compatibility Check

- Positive replay: validator passes on the current public surface.
- Negative replay: removing one required marker from a copied public doc or
  workflow causes validator failure for the specific command.
