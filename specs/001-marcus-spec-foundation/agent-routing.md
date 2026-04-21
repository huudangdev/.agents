# Agent Routing: Marcus Spec Foundation

> Feature ID: `001-marcus-spec-foundation`

## Routing Contract

Every workstream needs one primary owner. Supporting agents may review, but they
must not change files outside their assigned write scope without updating this
file.

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| Product specification | `sophia-product-manager` | `aurora-plan-challenger` | `spec.md`, `.agents/memory/constitution.md` | Accepted requirements |
| Architecture plan | `david-systems-architect` | `alan-tech-lead` | `plan.md`, `contracts/`, `data-model.md` | Technical plan |
| Script implementation | `alan-tech-lead` | `devops-system-architect` | `.agents/scripts/*.py` | Local CLI helpers |
| Workflow implementation | `marcus-ai-orchestrator` | `architecture-patterns` | `.agents/workflows/marcus_*.md` | Phase workflows |
| Verification | `ada-qa-agent` | `qa-simulator`, `eve-qa-approver` | `verification.md` | Evidence |

## Handoff Rules

- A producing agent writes evidence of what changed.
- A reviewing agent records findings without rewriting unrelated work.
- A task with failed verification returns to the owning agent once, then escalates
  after three repeated failures.
