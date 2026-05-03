# Agent Routing: Refactor Planning Toolchain Gate

> Feature ID: `017-refactor-planning-toolchain-gate`

## Routing Contract

Single-owner feature slice. This package exists to keep the `/refactor-planning`
toolchain gate spec-driven and replayable.

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| Toolchain gate + wiring | `marcus-ai-orchestrator` | `ada-qa-agent` | `.agents/scripts/validate_refactor_planning_toolchain.py`, `.agents/workflows/refactor-planning.md`, README, `USAGE_GUIDE.md`, `SLASH_COMMAND_REGISTRY.md`, `.agents/scripts/validate_command_surface.py`, and this feature package | Deterministic toolchain prerequisite gate and evidence-backed release |

## Handoff Rules

- The producing agent records fixture paths and command output in `verification.md`.
- The reviewing agent only adds findings; it must not rewrite unrelated workflow content.
- If the gate expands into runtime execution, stop and rescope back to prerequisites only.

## Review Topology

- Reviewer focus: gate must remain non-invasive and wiring must be validated by
  `validate_command_surface.py`.

## Escalation Rules

- Escalate if the toolchain gate starts executing refactor runtime commands.
- Escalate if wiring changes drift across README/USAGE/registry/workflow.
