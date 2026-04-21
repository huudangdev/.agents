# Research: Develop Knowledge Ledger

> Feature ID: `005-develop-knowledge-ledger`

## Questions

- How should implementation memory be structured so future agents can retrieve
  work by epic, module, feature, page, and task?
- How can the code phase enforce documentation without replacing planning docs?
- What metadata is minimal but useful for agent handoff?

## Findings

| Finding | Source | Decision Impact |
| --- | --- | --- |
| Bucketed Markdown with stable frontmatter fits the existing Marcus docs style. | `knowledge-work-architecture` skill | Use `docs/development/<bucket>/*.md` |
| Existing V30 scripts already validate specs and planning research. | `.agents/scripts/validate_specs.py`, `.agents/scripts/validate_planning_research.py` | Add a dedicated development validator with similar CLI ergonomics |
| `/develop` is the right enforcement point because it owns implementation and QA loops. | `.agents/workflows/develop.md` | Add a mandatory code-phase knowledge contract |

## Rejected Alternatives

- Single monolithic `implementation.md`: rejected because it does not give
  agents precise retrieval targets for modules, pages, or tasks.
- Replacing `/docs/tasks.md`: rejected because the user explicitly wants to keep
  old output structures and add richer code-phase docs.
