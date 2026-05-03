# Agent Routing: Develop Knowledge Ledger

> Feature ID: `005-develop-knowledge-ledger`

## Routing Contract

Every workstream needs one primary owner. Supporting agents may challenge, verify, or contribute evidence, but they must not rewrite unrelated scopes without updating this routing contract.

| Workstream | Primary Skill | Supporting Skills | Write Scope | Verification |
| --- | --- | --- | --- | --- |
| Workflow contract | `marcus-ai-orchestrator` | `knowledge-work-architecture` | `.agents/workflows/develop.md` | Review output contract |
| Knowledge ontology | `knowledge-work-architecture` | `sophia-product-manager` | `.agents/templates/development-*` | Template coverage |
| Scripts | `alan-tech-lead` | `ada-qa-agent` | `.agents/scripts/create_development_docs.py`, `.agents/scripts/validate_development_docs.py` | Python compile and scaffold validation |
| Governance docs | `marcus-ai-orchestrator` | `architecture-decision-records` | README, usage guide, release notes, `.clinerules`, CI template | Docs mention gates |

## Handoff Rules

- Producers record what changed, why it changed, and which verification evidence proves the slice is safe to hand off.
- Reviewers record findings in `verification.md` and may request a brief rebuild when the docs-to-read set or slice boundary changes.
- If a task fails verification repeatedly, return it once to the owning agent, then escalate through the review topology instead of widening context by instinct.

## Review Topology

| Review Stage | Reviewer | Focus | Output |
| --- | --- | --- | --- |
| Planning challenge | `aurora-plan-challenger` | hidden scope, replay realism, contract drift | review findings in spec/tasks/verification |
| QA evidence review | `ada-qa-agent` | command evidence, residual risk, bounded context | verification findings and disposition |
| Final orchestration review | `marcus-ai-orchestrator` | brief freshness, readiness, and slash-command fit | proceed / revise / stop |

## Escalation Rules

- Escalate when a narrow feature unexpectedly requires unrelated backend, data, or infrastructure context not already justified in the package.
- Escalate when `execution-brief.md` becomes stale and a reviewer cannot determine the right docs-to-read set safely.
- Escalate after three repeated failures of the same validator or verification command without new evidence.
