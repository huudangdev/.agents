# Agent Routing: TrustGraph Runtime Health

> Feature ID: `003-trustgraph-runtime-health`

## Routing Contract

Every workstream needs one primary owner. Supporting agents may review, but they
must not change files outside their assigned write scope without updating this
file.

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| Product specification | `sophia-product-manager` | `aurora-plan-challenger` | `spec.md` | Accepted requirements |
| Health API | `alan-tech-lead` | `devops-system-architect` | `app/api/health/route.ts`, `lib/*` | Runtime health JSON |
| Runtime UI | `benny-frontend-engineer` | `maya-ui-ux-designer` | `components/RuntimeStatus.tsx`, `app/page.tsx` | Live footer state |
| Verification | `ada-qa-agent` | `qa-simulator`, `eve-qa-approver` | `verification.md` | lint/build evidence |

## Handoff Rules

- A producing agent writes evidence of what changed.
- A reviewing agent records findings without rewriting unrelated work.
- A task with failed verification returns to the owning agent once, then escalates
  after three repeated failures.
