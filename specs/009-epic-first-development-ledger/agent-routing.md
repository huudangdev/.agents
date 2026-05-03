# Agent Routing: Epic-First Development Ledger

> Feature ID: `009-epic-first-development-ledger`

## Routing Contract

Every workstream needs one primary owner. Supporting agents may challenge, verify, or contribute evidence, but they must not rewrite unrelated scopes without updating this routing contract.

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| T001 | `marcus-ai-orchestrator` | feature-specific support only | update `create_development_docs.py` for V31 scaffold | scaffold creates `E-001-*` tree |
| T002 | `ada-qa-agent` | feature-specific support only | update `validate_development_docs.py` for topology, ID, parent, orphan, and placeholder gates | negative smoke fails malformed ledger |
| T003 | `knowledge-work-architecture` | feature-specific support only | update templates, manifest, index, and rubric | templates describe V31 |
| T004 | `marcus-ai-orchestrator` | feature-specific support only | update `/develop`, `.clinerules`, README, USAGE, release notes | future agents can discover V31 rules |
| T005 | `development-ledger-architect` | feature-specific support only | add dedicated skill | skill exists and states canonical topology |
| T006 | `ada-qa-agent` | feature-specific support only | final validation evidence | `verification.md` contains command results |
| T007 | `sophia-product-manager` | feature-specific support only | enforce product-grade Story/Priority/Issues/Relationship/Work Log/docs-before-code rules | validators and templates include required sections and sync notes require docs-before-code evidence |

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
