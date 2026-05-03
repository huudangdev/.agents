# Agent Routing: Marcus Init Output Contract Hardening

> Feature ID: `015-marcus-init-output-contract-hardening`

## Routing Contract

Every workstream needs one primary owner. Supporting agents may review, but they
must not change files outside their assigned write scope without updating this
file.

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| Product specification | `sophia-product-manager` | `aurora-plan-challenger` | `spec.md`, `verification.md` | Accepted `/marcus_init` output contract |
| Validator and contract design | `david-systems-architect` | `alan-tech-lead` | `plan.md`, `contracts/`, `data-model.md`, `quickstart.md` | Scaffold-output gate design |
| Implementation | `marcus-ai-orchestrator` | `knowledge-work-architecture` | `scripts/validate_marcus_init_outputs.py`, `workflows/marcus_init.md`, README, `USAGE_GUIDE.md`, registry, command-surface validator | Script-backed `/marcus_init` closeout |
| Verification | `ada-qa-agent` | `eve-qa-approver` | `verification.md`, `execution-brief.md` | Evidence-backed recommendation |

## Handoff Rules

- A producing agent writes evidence of what changed.
- A reviewing agent records findings without rewriting unrelated work.
- A task with failed verification returns to the owning agent once, then
  escalates after three repeated failures on the same scaffold output gate.

## Review Topology

| Review Stage | Primary Reviewer | Input Artifact | Output Artifact |
| --- | --- | --- | --- |
| Spec challenge | `aurora-plan-challenger` | `spec.md` | updated `spec.md` or findings |
| Plan challenge | `alan-tech-lead` | `plan.md` | updated `plan.md` or findings |
| Verification sign-off | `ada-qa-agent` | `verification.md` | evidence-backed recommendation |

## Escalation Rules

- Escalate when `/marcus_init` hardening starts replacing the shell scaffold
  rather than validating its outputs.
- Escalate when public command docs drift away from the workflow contract.
- Escalate when validator coverage starts assuming framework-specific files not
  present in the workflow contract.
