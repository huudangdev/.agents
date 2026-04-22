# Agent Routing: Substantive Development Docs Quality

> Feature ID: `007-substantive-development-docs-quality`

## Routing Contract

| Workstream | Primary Skill | Supporting Skills | Write Scope | Output |
| --- | --- | --- | --- | --- |
| Quality rubric | `knowledge-work-architecture` | `sophia-product-manager` | `.agents/DEVELOPMENT_DOCS_QUALITY_RUBRIC.md` | PM-grade documentation bar |
| Development validator | `ada-qa-agent` | `alan-tech-lead` | `.agents/scripts/validate_development_docs.py` | Strict content validation |
| Sync validator | `ada-qa-agent` | `knowledge-work-architecture` | `.agents/scripts/validate_doc_sync.py` | Strict sync note validation |
| Templates | `knowledge-work-architecture` | `marcus-ai-orchestrator` | `.agents/templates/development-*` | Quality-bar prompts |
| Workflow/docs | `marcus-ai-orchestrator` | `sophia-product-manager` | `/develop`, README, USAGE, `.clinerules` | Visible enforcement |

## Handoff Rules

- Template files may contain prompts, but generated project docs must not retain
  those prompts when closing `/develop`.
- QA owns strict validation before closeout.
