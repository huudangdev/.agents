# Agent Routing: Substantive Development Docs Quality

> Feature ID: `007-substantive-development-docs-quality`

## Routing Contract

Every workstream needs one primary owner. Supporting agents may challenge, verify, or contribute evidence, but they must not rewrite unrelated scopes without updating this routing contract.

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| Quality rubric | `knowledge-work-architecture` | `sophia-product-manager` | `.agents/DEVELOPMENT_DOCS_QUALITY_RUBRIC.md` | PM-grade documentation bar |
| Development validator | `ada-qa-agent` | `alan-tech-lead` | `.agents/scripts/validate_development_docs.py` | Strict content validation |
| Sync validator | `ada-qa-agent` | `knowledge-work-architecture` | `.agents/scripts/validate_doc_sync.py` | Strict sync note validation |
| Templates | `knowledge-work-architecture` | `marcus-ai-orchestrator` | `.agents/templates/development-*` | Quality-bar prompts |
| Workflow/docs | `marcus-ai-orchestrator` | `sophia-product-manager` | `/develop`, README, USAGE, `.clinerules` | Visible enforcement |

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
