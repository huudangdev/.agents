# Feature Specification: Context Index and Architecture Graph

> Feature ID: `018-context-index-and-architecture-graph`
> Created: `2026-05-03`
> Status: Draft
> Source Prompt: Hotfix `.agents` so models stop re-reading entire docs/code/skills trees; add deterministic index + architecture graph and wire it into workflows/harness.

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

## 2. User Stories

- [x] As an operator, I want models to read an index first so they stop wasting
      tokens and drifting into unrelated context.
- [x] As an implementation model, I want a small set of generated entrypoints
      that I can use to pick the smallest credible read set.
- [x] As a governance maintainer, I want the index gate wired into workflows and
      enforced by harness preflight so it cannot be skipped silently.

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

## 4. Non-Functional Requirements

- `NFR-001`: The index generator MUST be deterministic and local-only.
- `NFR-002`: The index generator MUST avoid scanning large dependency folders
  by default (e.g., `node_modules/`, `.git/`, build outputs).
- `NFR-003`: The index MUST be shallow and cheap to produce; it must not attempt
  semantic summarization.

## 5. Acceptance Criteria

- `AC-001`: Running `python3 scripts/build_context_index.py --root <root>`
  produces all required files under `.agents/index/`.
- `AC-002`: Running `python3 scripts/validate_context_index.py --root <root>`
  passes after generation and fails when outputs are missing or stale.
- `AC-003`: `python3 scripts/run_harness_preflight.py --root . --phase execution`
  builds and validates the index before repo-wide gates.
- `AC-004`: `python3 scripts/validate_command_surface.py --root .` passes after
  wiring index markers into docs/registry/workflows.

## 6. Clarifications

- This is not a vector index / embedding system. It is a deterministic routing
  index that prevents broad reads by default.

## 7. Constraints

- In scope: `.agents/scripts/build_context_index.py`,
  `.agents/scripts/validate_context_index.py`, `.agents/index/README.md`,
  `.agents/scripts/run_harness_preflight.py`, the workflows and registry updates,
  and this feature package.
- Out of scope: remote indexing services, embeddings, or any network-dependent
  indexing pipeline.

## 8. Risks

- Some projects have unusual layouts; the index is heuristic and may not list
  the ideal entrypoints without tuning. The fix is to adjust excludes and
  directory heuristics, not to revert to "read everything".

## 9. Traceability

- Gate implementation: `.agents/scripts/build_context_index.py`,
  `.agents/scripts/validate_context_index.py`
- Harness wiring: `.agents/scripts/run_harness_preflight.py`
- Workflow wiring: `.agents/workflows/develop.md`, `.agents/workflows/quick_fix.md`,
  `.agents/workflows/refactor-planning.md`
- Public contract: `.agents/SLASH_COMMAND_REGISTRY.md`,
  `.agents/scripts/validate_command_surface.py`

## 10. Review Loop

- `R1` Scope check: confirm the index remains shallow and local-only.
- `R2` Wiring check: confirm harness + workflows + registry agree.
- `R3` Verification check: confirm evidence is recorded and replayable.

