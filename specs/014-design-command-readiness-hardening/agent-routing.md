# Agent Routing: Design Command Readiness Hardening

> Feature ID: `014-design-command-readiness-hardening`

## Routing Contract

Every workstream needs one primary owner. Supporting agents may review, but they
must not change files outside their assigned write scope without updating this
file.

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| Product specification | `sophia-product-manager` | `aurora-plan-challenger` | `spec.md`, `verification.md` | Accepted `/design` command requirements |
| Validator and contract design | `david-systems-architect` | `alan-tech-lead` | `plan.md`, `contracts/`, `data-model.md`, `quickstart.md` | Input/output gate contract |
| Implementation | `marcus-ai-orchestrator` | `knowledge-work-architecture` | `scripts/validate_design_readiness.py`, `scripts/validate_design_outputs.py`, `workflows/design.md`, README, `USAGE_GUIDE.md`, registry, command-surface validator | Script-backed `/design` |
| Verification | `ada-qa-agent` | `eve-qa-approver` | `verification.md`, `execution-brief.md` | Evidence-backed recommendation |

## Handoff Rules

- A producing agent writes evidence of what changed.
- A reviewing agent records findings without rewriting unrelated work.
- A task with failed verification returns to the owning agent once, then
  escalates after three repeated failures on the same `/design` gate.

## Review Topology

| Review Stage | Primary Reviewer | Input Artifact | Output Artifact |
| --- | --- | --- | --- |
| Spec challenge | `aurora-plan-challenger` | `spec.md` | updated `spec.md` or findings |
| Plan challenge | `alan-tech-lead` | `plan.md` | updated `plan.md` or findings |
| Verification sign-off | `ada-qa-agent` | `verification.md` | evidence-backed recommendation |

## Escalation Rules

- Escalate when `/design` starts requiring source-code or browser-runtime
  execution.
- Escalate when a validator tries to judge creative quality instead of file
  readiness or artifact existence.
- Escalate when public command docs drift away from the `/design` workflow.
