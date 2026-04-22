# Research: Feature Docs Mermaid Global Sync

> Feature ID: `008-feature-docs-mermaid-global-sync`

## Questions

- How do we make feature docs inspectable quickly for PM review?
- How do we keep feature-level docs from drifting away from global docs?
- What validator rules make diagrams and global docs mandatory?

## Findings

| Finding | Source | Decision Impact |
| --- | --- | --- |
| PMs need visual inspection of flows/states/dependencies. | User feedback | Require Mermaid per development note |
| Feature docs alone are insufficient for POC governance. | User feedback | Require global `/docs` update for behavior changes |
| Existing sync notes already list global docs decisions. | `development-sync-note-template.md` | Add validator gate for at least one global update |

## Rejected Alternatives

- Optional Mermaid: rejected because agents skipped diagrams.
- Updating only feature docs: rejected because PM-facing global docs remain stale.
