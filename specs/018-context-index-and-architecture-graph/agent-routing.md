# Agent Routing: Context Index and Architecture Graph

> Feature ID: `018-context-index-and-architecture-graph`

## Routing Contract

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| Index-first hotfix | `marcus-ai-orchestrator` | `ada-qa-agent` | scripts + workflows + registry + docs + this feature package | Deterministic context index gate and replayable evidence |

## Handoff Rules

- Record evidence in `verification.md` as concrete command replays with paths.
- Rebuild `execution-brief.md` after evidence changes.

## Review Topology

- Review focuses on determinism and cost: index remains shallow, local-only, and fast.

## Escalation Rules

- Escalate if the index starts doing semantic summarization/embeddings.
- Escalate if preflight wiring diverges from workflows or registry markers.

