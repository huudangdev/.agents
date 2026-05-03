# Design Command Contract

Owner: `marcus-ai-orchestrator`

## Purpose

Define the deterministic local gate chain for `/design`.

## Contract

- `/design` must run `python3 .agents/scripts/validate_design_readiness.py --root .`
  before Phase 2 design work starts.
- `/design` must still run
  `python3 .agents/adapters/trustgraph_query.py --task "Design Phase Boot"` as
  part of the existing workflow narrative.
- `/design` must run `python3 .agents/scripts/validate_design_outputs.py --root .`
  before presenting final design artifacts for human review.
- README, `USAGE_GUIDE.md`, `SLASH_COMMAND_REGISTRY.md`, and
  `workflows/design.md` must all describe the same local script chain.

## Compatibility Check

- Positive replay: both design validators pass on valid fixtures and
  `validate_command_surface.py --root .` passes.
- Negative replay: removing one required planning input causes
  `validate_design_readiness.py` to fail.
