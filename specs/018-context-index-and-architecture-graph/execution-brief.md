# Execution Brief: Feature Specification: Context Index and Architecture Graph

> Feature ID: `018-context-index-and-architecture-graph`
> Task Shape: `architecture-refactor`
> Generated From: `spec.md`, `plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, `agent-routing.md`

## 1. Operator Intent Snapshot

## 1. Purpose

Models using `.agents` currently waste context window by repeatedly scanning
large documentation trees, re-reading skills, and opening broad code areas.
This increases token spend and causes context drift (reading unrelated files,
missing the actual relevant ones, and forming wrong conclusions).

This feature adds an index-first routing layer:

- A deterministic shallow index of `docs/`, code files, and available skills.
- A lightweight architecture graph to guide targeted reads.
- Workflow and harness wiring so index generation becomes the default
  pre-reading step.

The goal is not semantic summarization or a vector database. The goal is a
cheap, deterministic entrypoint that any model can follow before expanding
context.


## 2. Required Behavior

## 3. Functional Requirements

- `FR-001`: The system MUST provide a script that generates a context index under
  `.agents/index/` for a given `--root`.
- `FR-002`: The generated index MUST include:
  - `docs_index.md` (shallow headings index of `docs/`)
  - `code_index.md` (shallow code file index + counts)
  - `skills_index.md` (skill list and descriptions)
  - `architecture_graph.mmd` (Mermaid architecture map)
  - `index_manifest.json` (generation metadata)
- `FR-003`: The system MUST provide a validator that fails when the context
  index is missing, empty, or stale beyond a bounded age.
- `FR-004`: Harness execution preflight MUST build and validate the context
  index before repo-wide validation gates.
- `FR-005`: `/develop`, `/quick_fix`, and `/refactor-planning` workflows MUST
  instruct models to route reads through the generated index files first.
- `FR-006`: The public slash-command contract MUST list the index scripts as
  required invocations for `/develop`, `/quick_fix`, and `/refactor-planning`.


## 5. Acceptance Criteria

- `AC-001`: Running `python3 scripts/build_context_index.py --root <root>`
  produces all required files under `.agents/index/`.
- `AC-002`: Running `python3 scripts/validate_context_index.py --root <root>`
  passes after generation and fails when outputs are missing or stale.
- `AC-003`: `python3 scripts/run_harness_preflight.py --root . --phase execution`
  builds and validates the index before repo-wide gates.
- `AC-004`: `python3 scripts/validate_command_surface.py --root .` passes after
  wiring index markers into docs/registry/workflows.


## 3. Scope Boundaries

## 7. Constraints

- In scope: `.agents/scripts/build_context_index.py`,
  `.agents/scripts/validate_context_index.py`, `.agents/index/README.md`,
  `.agents/scripts/run_harness_preflight.py`, the workflows and registry updates,
  and this feature package.
- Out of scope: remote indexing services, embeddings, or any network-dependent
  indexing pipeline.


## 4. Active Work Slice

## 1. Technical Summary

Add a deterministic index-first routing layer to `.agents`:

- `build_context_index.py` generates shallow indices + a Mermaid architecture map.
- `validate_context_index.py` enforces presence and bounded freshness.
- Harness execution preflight builds + validates the index before repo-wide gates.
- Core workflows and the slash-command registry reference the index gate so any
  model uses the same entrypoints before reading docs/code/skills.


## 6. Agent Routing

- Owner: `marcus-ai-orchestrator`
- Write Scope: `.agents/scripts/*context_index*`, `.agents/index/README.md`,
  `.agents/scripts/run_harness_preflight.py`, `.agents/workflows/*`, README/USAGE,
  `.agents/SLASH_COMMAND_REGISTRY.md`, `.agents/scripts/validate_command_surface.py`,
  and this feature package.


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


## 4.1 Dynamic Execution Signals

### Changed Files

- `scripts/build_context_index.py`
- `scripts/validate_context_index.py`
- `scripts/run_harness_preflight.py`
- `workflows/develop.md`
- `workflows/quick_fix.md`
- `workflows/refactor-planning.md`
- `SLASH_COMMAND_REGISTRY.md`
- `scripts/validate_command_surface.py`
- `README.md`
- `USAGE_GUIDE.md`
- `release_manifest.json`
- `V32.0_RELEASE_NOTES.md`

### Failing Evidence

- Models were re-reading broad doc/code/skills trees causing token exhaustion and context drift; the fix adds index-first routing artifacts under .agents/index and wires them into preflight/workflows.

## Execution Monitoring

- Stop if `validate_command_surface.py --root .` fails after wiring changes.
- Stop if index build becomes unbounded or slow; tune excludes and file limits instead.


## 5. Development Ledger Context

Read these development-ledger notes before source edits for the active slice:

No `docs/development/` notes matched this feature workspace.
Before behavior-changing code work, create or reconcile the development ledger for this feature slice.
Preferred paths:
- If the feature is new: run `python3 .agents/scripts/create_development_docs.py --name "<epic-or-feature-name>" --feature-id "<feature-id>" --epic-number 001 --child-number 001 --task-number 001`.
- If the project is brownfield or docs are stale: route to `/doc_reconcile` and repair the ledger before source edits.

## 6. Verification Path

## Verification Plan

| Requirement | Method | Command or Procedure | Expected Result |
| --- | --- | --- | --- |
| `FR-001`/`FR-002` | Positive replay | run `python3 .agents/scripts/build_context_index.py --root .` | index artifacts exist and are non-empty |
| `FR-003` | Positive replay | run `python3 .agents/scripts/validate_context_index.py --root .` | passes within max-age window |
| `FR-004` | Positive replay | run `python3 .agents/scripts/run_harness_preflight.py --root . --phase execution` | index build/validate occurs before repo-wide gates |
| `FR-006` | No-regression replay | run `python3 .agents/scripts/validate_command_surface.py --root .` | public contract stays green |


## Execution Gates

- Rebuild `execution-brief.md` after updating evidence in this file.


## Local Preconditions

- Required commands: `python3`


## Validation Path

```bash
python3 .agents/scripts/build_context_index.py --root .
python3 .agents/scripts/validate_context_index.py --root .
python3 .agents/scripts/run_harness_preflight.py --root . --phase execution
python3 .agents/scripts/validate_command_surface.py --root .
```


## POC Rehearsal

- Confirm `.agents/index/architecture_graph.mmd` exists and renders as Mermaid.
- Confirm `.agents/index/docs_index.md` remains shallow and does not dump full docs.


## 7. Review and Release Signals

## 10. Review Loop

- `R1` Scope check: confirm the index remains shallow and local-only.
- `R2` Wiring check: confirm harness + workflows + registry agree.
- `R3` Verification check: confirm evidence is recorded and replayable.


## Review Loop Tasks

- Confirm the index outputs are small and deterministic.
- Confirm preflight always runs index build/validate before repo-wide gates.


## Review Rounds

| Round | Reviewer | Finding Summary | Required Changes | Disposition |
| --- | --- | --- | --- | --- |
| `R1` | `marcus-ai-orchestrator` | Keep the index shallow and deterministic; no embeddings/vector DB. | Enforce bounded scan limits and explicit excludes. | Accepted |
| `R2` | `ada-qa-agent` | Ensure wiring cannot be skipped and that preflight orders index steps first. | Put index build/validate at the top of execution preflight. | Accepted |
| `R3` | `marcus-ai-orchestrator` | Ensure public docs and registry remain aligned. | Enforce markers in validate_command_surface. | Accepted |


## Release Recommendation

- Recommendation: `GO`
- Basis: index artifacts are generated deterministically, validated, and wired into harness/workflows with command-surface enforcement.


## 8. Context Expansion Rules

### Task Shape Decision

- Selected task shape: `architecture-refactor`
- Why this shape: Read decisions, diagrams, affected modules, and execution boundaries first.

### Required Reads

- Required read: `agents.md`
- Required read: `.agents/memory/constitution.md`
- Required read: `.agents/specs/018-context-index-and-architecture-graph/execution-brief.md`
- Required read: `.agents/specs/018-context-index-and-architecture-graph/spec.md` only if the brief or failing evidence says deeper requirement context is needed.
- Required read: `.agents/specs/018-context-index-and-architecture-graph/plan.md`, `tasks.md`, `verification.md`, `quickstart.md`, and `agent-routing.md` only when the current write scope or failing evidence requires the deeper artifact.
- Required read: create or reconcile the missing `docs/development/` notes before behavior-changing source edits.
- Required read: start with the changed files listed under `## 4.1 Dynamic Execution Signals` before widening to adjacent artifacts.

### Forbidden Default Reads

- Forbidden by default: full repo scans without a bounded module list
- Forbidden by default: random DB exploration unrelated to the refactor boundary
- Forbidden by default: random UI exploration unrelated to the refactor boundary

### Expansion Triggers

- Read decisions, diagrams, affected modules, and execution boundaries first.
- Do not scan the full repo without a bounded module list.
- Load architecture/refactor skills first.
- Read the `docs/development/` notes listed in this brief before widening beyond the current work slice.
- If the required epic/feature/module/page/task note is missing, stop and reconcile the development ledger instead of improvising from code alone.

## Review Topology

- Review focuses on determinism and cost: index remains shallow, local-only, and fast.


## Escalation Rules

- Escalate if the index starts doing semantic summarization/embeddings.
- Escalate if preflight wiring diverges from workflows or registry markers.
