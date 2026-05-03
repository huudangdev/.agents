# Marcus Init Command Contract

Owner: `marcus-ai-orchestrator`

## Purpose

Define the deterministic closeout gate for `/marcus_init`.

## Contract

- `/marcus_init` must seed a project root containing:
  - `docs/`
  - `.agents/`
  - `.clinerules`
  - `agents.md`
  - `.agents/agents.md`
  - `docs/prd_draft.md`
- `/marcus_init` must run
  `python3 .agents/scripts/validate_marcus_init_outputs.py --root projects/$PROJECT_NAME`
  before claiming success.
- README, `USAGE_GUIDE.md`, `SLASH_COMMAND_REGISTRY.md`, and
  `workflows/marcus_init.md` must all expose the same output-validation step.

## Compatibility Check

- Positive replay: validator passes on a valid scaffold fixture.
- Negative replay: validator fails when one required scaffold output is missing.
