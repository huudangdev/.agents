# Contract: Mermaid Feature Docs and Global Docs Sync

## Producer

Agents writing `/docs/development/**` and `/docs/development/sync/**`.

## Consumer

PM review, future agents, QA gates, CI, and TrustGraph memory.

## Mermaid Requirements

Every development note for these buckets requires a Mermaid code fence:

- `epics`
- `modules`
- `features`
- `pages`
- `tasks`

The diagram must explain behavior, state, dependency, data flow, or handoff.

## Global Docs Requirements

When source behavior changes, the changed file set must include at least one:

- `docs/prd.md`
- `docs/tasks.md`
- `docs/knowledge.md`
- `docs/decisions.md`
- `docs/memory.md`
- `docs/planning/flows.md`
- `docs/planning/screens.md`
- `docs/planning/diagrams.md`

The sync note must include at least one `updated because` decision for a global
doc.

## Validation

```bash
python3 .agents/scripts/validate_development_docs.py --strict-counts
python3 .agents/scripts/validate_doc_sync.py --strict
```
