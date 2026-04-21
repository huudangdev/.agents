# Agent Routing: {{FEATURE_TITLE}}

> Feature ID: `{{FEATURE_ID}}`

## Routing Contract

Every workstream needs one primary owner. Supporting agents may review, but they
must not change files outside their assigned write scope without updating this
file.

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| Product specification | `sophia-product-manager` | `aurora-plan-challenger` | `spec.md` | Accepted requirements |
| Architecture plan | `david-systems-architect` | `alan-tech-lead` | `plan.md`, `contracts/`, `data-model.md` | Technical plan |
| Implementation | TBD | TBD | TBD | Code changes |
| Verification | `ada-qa-agent` | `qa-simulator`, `eve-qa-approver` | `verification.md`, tests | Evidence |

## Handoff Rules

- A producing agent writes evidence of what changed.
- A reviewing agent records findings without rewriting unrelated work.
- A task with failed verification returns to the owning agent once, then escalates
  after three repeated failures.
