# Agent Routing: Slash Command Workflow Contract Hardening

> Feature ID: `013-slash-command-workflow-contract-hardening`

## Routing Contract

Every workstream needs one primary owner. Supporting agents may review, but they
must not change files outside their assigned write scope without updating this
file.

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| Product specification | `sophia-product-manager` | `aurora-plan-challenger` | `spec.md`, `verification.md` | Accepted command-governance requirements |
| Contract and plan | `david-systems-architect` | `alan-tech-lead` | `plan.md`, `contracts/`, `data-model.md`, `quickstart.md` | Registry and validator design |
| Implementation | `marcus-ai-orchestrator` | `knowledge-work-architecture` | `SLASH_COMMAND_REGISTRY.md`, `scripts/validate_command_surface.py`, `README.md`, `USAGE_GUIDE.md` | Hardened command surface |
| Verification | `ada-qa-agent` | `eve-qa-approver` | `verification.md`, `execution-brief.md` | Evidence-backed release recommendation |

## Handoff Rules

- A producing agent writes evidence of what changed.
- A reviewing agent records findings without rewriting unrelated work.
- A task with failed verification returns to the owning agent once, then
  escalates after three repeated failures on the same command contract.

## Review Topology

| Review Stage | Primary Reviewer | Input Artifact | Output Artifact |
| --- | --- | --- | --- |
| Spec challenge | `aurora-plan-challenger` | `spec.md` | updated `spec.md` or findings |
| Plan challenge | `alan-tech-lead` | `plan.md` | updated `plan.md` or findings |
| Verification sign-off | `ada-qa-agent` | `verification.md` | evidence-backed recommendation |

## Escalation Rules

- Escalate when a published command still lacks an owning workflow file.
- Escalate when a command is described as script-backed but only has narrative
  workflow text.
- Escalate when command-surface replay fails repeatedly without new evidence
  about the specific command that drifted.
