# Agent Routing: Feature Docs Mermaid Global Sync

> Feature ID: `008-feature-docs-mermaid-global-sync`

## Routing Contract

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| Mermaid validation | `ada-qa-agent` | `knowledge-work-architecture` | `validate_development_docs.py` | Diagram gate |
| Global docs validation | `ada-qa-agent` | `sophia-product-manager` | `validate_doc_sync.py` | Global docs gate |
| Templates and rubric | `knowledge-work-architecture` | `chartis-data-visualizer` | templates, rubric | Mermaid guidance |
| Workflow/docs | `marcus-ai-orchestrator` | `sophia-product-manager` | `/develop`, README, USAGE, release notes | Operator-visible rule |

## Handoff Rules

- Feature/page/module/task owners write Mermaid diagrams.
- PM/product owner patches at least one global doc when behavior changes.
- QA owner runs strict validators before closeout.
