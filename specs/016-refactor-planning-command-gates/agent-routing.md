# Agent Routing: Refactor Planning Command Gates

> Feature ID: `016-refactor-planning-command-gates`

## Routing Contract

Every workstream needs one primary owner. Supporting agents may review, but they
must not change files outside their assigned write scope without updating this
file.

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| Product specification | `sophia-product-manager` | `aurora-plan-challenger` | `spec.md`, `verification.md` | Accepted `/refactor-planning` gate contract |
| Validator and contract design | `david-systems-architect` | `alan-tech-lead` | `plan.md`, `contracts/`, `data-model.md`, `quickstart.md` | Readiness/output gate design |
| Implementation | `marcus-ai-orchestrator` | `knowledge-work-architecture` | refactor-planning validators, workflow, registry, README, USAGE, command-surface validator | Script-backed `/refactor-planning` command gates |
| Verification | `ada-qa-agent` | `eve-qa-approver` | `verification.md`, `execution-brief.md` | Evidence-backed recommendation |

## Handoff Rules

- A producing agent writes evidence of what changed.
- A reviewing agent records findings without rewriting unrelated work.
- A task with failed verification returns to the owning agent once, then
  escalates after three repeated failures on the same readiness or output gate.

## Review Topology

| Review Stage | Primary Reviewer | Input Artifact | Output Artifact |
| --- | --- | --- | --- |
| Spec challenge | `aurora-plan-challenger` | `spec.md` | updated `spec.md` or findings |
| Plan challenge | `alan-tech-lead` | `plan.md` | updated `plan.md` or findings |
| Verification sign-off | `ada-qa-agent` | `verification.md` | evidence-backed recommendation |

## Escalation Rules

- Escalate when the slice starts rewriting the AST/refactor engine instead of
  adding command gates.
- Escalate when public command docs drift away from the workflow contract.
- Escalate when readiness assumptions extend beyond the current brownfield docs
  and development-ledger quality gate.
