# Tasks: Context Index and Architecture Graph

> Feature ID: `018-context-index-and-architecture-graph`

## Tasks

- [x] `T001` Index generator script
  - Owner: `marcus-ai-orchestrator`
  - Write Scope: `.agents/scripts/build_context_index.py`, `.agents/index/README.md`, `.agents/.gitignore`
  - Verification: build produces non-empty `docs_index.md`, `skills_index.md`, `code_index.md`, `architecture_graph.mmd`, `index_manifest.json`
  - Docs: `.agents/index/README.md`
  - Sync: none
- [x] `T002` Index validator script
  - Owner: `marcus-ai-orchestrator`
  - Write Scope: `.agents/scripts/validate_context_index.py`
  - Verification: passes after build; fails on missing outputs or staleness
  - Docs: none
  - Sync: none
- [x] `T003` Harness wiring
  - Owner: `marcus-ai-orchestrator`
  - Write Scope: `.agents/scripts/run_harness_preflight.py`
  - Verification: execution preflight runs index build + validate before repo-wide gates
  - Docs: workflows (via registry/contract)
  - Sync: rerun preflight replay
- [x] `T004` Workflow + registry wiring
  - Owner: `marcus-ai-orchestrator`
  - Write Scope: `.agents/workflows/develop.md`, `.agents/workflows/quick_fix.md`, `.agents/workflows/refactor-planning.md`, `.agents/SLASH_COMMAND_REGISTRY.md`
  - Verification: workflows mention index-first routing; registry lists index scripts as required invocations
  - Docs: workflows + registry
  - Sync: rerun command-surface validation
- [x] `T005` Command-surface enforcement + docs
  - Owner: `marcus-ai-orchestrator`
  - Write Scope: `.agents/scripts/validate_command_surface.py`, `.agents/README.md`, `.agents/USAGE_GUIDE.md`
  - Verification: `validate_command_surface.py --root .` passes and enforces index markers
  - Docs: README/USAGE
  - Sync: rerun command-surface validation
- [ ] `T006` Verification + brief rebuild
  - Owner: `marcus-ai-orchestrator`
  - Write Scope: `specs/018-context-index-and-architecture-graph/verification.md`, `execution-brief.md`
  - Verification: record evidence for build, validate, preflight replay, and command-surface replay
  - Docs: `verification.md`, `execution-brief.md`
  - Sync: rebuild brief after final evidence changes

## Parallel Groups

- Group A: `T001` + `T002`
- Group B: `T003` + `T004` + `T005`
- Group C: `T006`

## Execution Monitoring

- Stop if `validate_command_surface.py --root .` fails after wiring changes.
- Stop if index build becomes unbounded or slow; tune excludes and file limits instead.

## Review Loop Tasks

- Confirm the index outputs are small and deterministic.
- Confirm preflight always runs index build/validate before repo-wide gates.

