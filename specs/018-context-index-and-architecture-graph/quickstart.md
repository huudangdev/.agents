# Quickstart Validation: Context Index and Architecture Graph

> Feature ID: `018-context-index-and-architecture-graph`

## Local Preconditions

- Required commands: `python3`

## Validation Path

```bash
python3 .agents/scripts/build_context_index.py --root .
python3 .agents/scripts/validate_context_index.py --root .
python3 .agents/scripts/run_harness_preflight.py --root . --phase execution
python3 .agents/scripts/validate_command_surface.py --root .
```

## Expected Artifacts

- `.agents/scripts/build_context_index.py`
- `.agents/scripts/validate_context_index.py`
- `.agents/index/README.md`
- Updates to workflows and the slash-command registry for index-first routing

## POC Rehearsal

- Confirm `.agents/index/architecture_graph.mmd` exists and renders as Mermaid.
- Confirm `.agents/index/docs_index.md` remains shallow and does not dump full docs.

## Rollback Check

- Remove the two scripts and their wiring from harness/workflows/registry, then
  rerun `python3 .agents/scripts/validate_command_surface.py --root .`.

