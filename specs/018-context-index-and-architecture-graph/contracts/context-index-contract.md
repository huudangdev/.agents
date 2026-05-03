# Context Index Contract

Owner: `marcus-ai-orchestrator`

## Purpose

Provide a deterministic, cheap routing layer so models do not read the entire
repo by default.

## Contract

- Agents MUST build and consult `.agents/index/*` before reading large doc/code
  trees.
- The index MUST be generated locally via:
  - `python3 .agents/scripts/build_context_index.py --root .`
  - `python3 .agents/scripts/validate_context_index.py --root .`
- Harness execution preflight MUST run index build + validate before repo-wide
  gates.
- `/develop`, `/quick_fix`, and `/refactor-planning` workflows MUST mention
  index-first routing and name the generated entrypoints.

