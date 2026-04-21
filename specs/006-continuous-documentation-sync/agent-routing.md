# Agent Routing: Continuous Documentation Sync

> Feature ID: `006-continuous-documentation-sync`

## Routing Contract

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| Workflow gate | `marcus-ai-orchestrator` | `sophia-product-manager` | `.agents/workflows/develop.md` | Node 6.5 sync checkpoint |
| Knowledge policy | `knowledge-work-architecture` | `architecture-decision-records` | templates and docs | Append/patch policy |
| Script implementation | `alan-tech-lead` | `ada-qa-agent` | `.agents/scripts/create_doc_sync_note.py`, `.agents/scripts/validate_doc_sync.py` | CLI tools |
| PM docs | `sophia-product-manager` | `marcus-ai-orchestrator` | README, USAGE, release notes | Operator guidance |
| QA gate | `ada-qa-agent` | `eve-qa-approver` | CI template and verification | Repeatable checks |

## Handoff Rules

- Code owner creates the sync note.
- PM/product owner patches planning docs when behavior or scope changes.
- Technical owner patches module/feature/page/task docs when code behavior changes.
- QA owner runs strict validation before next major slice.
