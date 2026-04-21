# Agent Routing: Develop Knowledge Ledger

> Feature ID: `005-develop-knowledge-ledger`

## Routing Table

| Workstream | Primary Skill | Supporting Skills | Write Scope | Verification |
| --- | --- | --- | --- | --- |
| Workflow contract | `marcus-ai-orchestrator` | `knowledge-work-architecture` | `.agents/workflows/develop.md` | Review output contract |
| Knowledge ontology | `knowledge-work-architecture` | `sophia-product-manager` | `.agents/templates/development-*` | Template coverage |
| Scripts | `alan-tech-lead` | `ada-qa-agent` | `.agents/scripts/create_development_docs.py`, `.agents/scripts/validate_development_docs.py` | Python compile and scaffold validation |
| Governance docs | `marcus-ai-orchestrator` | `architecture-decision-records` | README, usage guide, release notes, `.clinerules`, CI template | Docs mention gates |

## Parallelization Plan

- `[P]` Template creation and validator implementation are parallel-safe when
  file ownership is disjoint.
- Workflow and docs updates should happen after the contract terms are stable.

## Handoff Rules

- Each future `/develop` owner skill must update the relevant bucket note before
  reporting code completion.
- QA owner must run the development docs validator when `/docs/development/`
  exists.
