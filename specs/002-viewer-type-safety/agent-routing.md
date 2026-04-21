# Agent Routing: Viewer Type Safety

> Feature ID: `002-viewer-type-safety`

## Routing Contract

Every workstream needs one primary owner. Supporting agents may review, but they
must not change files outside their assigned write scope without updating this
file.

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| Product specification | `sophia-product-manager` | `aurora-plan-challenger` | `spec.md` | Accepted requirements |
| API hardening | `alan-tech-lead` | `cipher-security-approver` | `app/api/chroma/route.ts` | argv-based execution |
| Viewer typing | `benny-frontend-engineer` | `refactor-review` | `lib/graphTypes.ts`, `app/page.tsx`, `components/*.tsx` | typed components |
| Verification | `ada-qa-agent` | `qa-simulator`, `eve-qa-approver` | `verification.md` | lint/build evidence |

## Handoff Rules

- A producing agent writes evidence of what changed.
- A reviewing agent records findings without rewriting unrelated work.
- A task with failed verification returns to the owning agent once, then escalates
  after three repeated failures.
