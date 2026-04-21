# Agent Routing: Planning Deep Research V30

> Feature ID: `004-planning-deep-research-v30`

## Routing Contract

Every workstream needs one primary owner. Supporting agents may review, but they
must not change files outside their assigned write scope without updating this
file.

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| Product specification | `sophia-product-manager` | `aurora-plan-challenger` | `spec.md` | Accepted requirements |
| Planning workflow | `marcus-ai-orchestrator` | `david-systems-architect` | `.agents/workflows/planning.md` | V30 workflow |
| Research templates | `sage-research-synthesis` | `arthur-search-agent`, `elite6-research` | `.agents/templates/planning-*` | Ledger templates |
| Validator | `ada-qa-agent` | `feynman-skeptic-reviewer` | `.agents/scripts/validate_planning_research.py` | Validation script |
| Verification | `ada-qa-agent` | `eve-qa-approver` | `verification.md` | Evidence |

## Handoff Rules

- A producing agent writes evidence of what changed.
- A reviewing agent records findings without rewriting unrelated work.
- A task with failed verification returns to the owning agent once, then escalates
  after three repeated failures.
