# Agent Routing: Brownfield Doc Reconcile Command

> Feature ID: `010-brownfield-doc-reconcile-command`

## Routing Contract

Every workstream needs one primary owner. Supporting agents may challenge, verify, or contribute evidence, but they must not rewrite unrelated scopes without updating this routing contract.

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| T001 | `marcus-ai-orchestrator` | feature-specific support only | add `/doc_reconcile` workflow | workflow file exists |
| T002 | `development-ledger-architect` | feature-specific support only | add code/docs audit script | audit smoke creates markdown report |
| T003 | `ada-qa-agent` | feature-specific support only | add `issues.md` template and V31 validator requirement | scaffold includes issues and negative smoke rejects missing issues |
| T004 | `knowledge-work-architecture` | feature-specific support only | update README, USAGE, `.clinerules`, release notes, and `/develop` | docs mention command and issue-file policy |
| T005 | `ada-qa-agent` | feature-specific support only | final validation evidence | `verification.md` contains command results |

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
