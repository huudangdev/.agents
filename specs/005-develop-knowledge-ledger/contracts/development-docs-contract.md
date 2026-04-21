# Contract: Development Docs Ledger

## Producer

`/develop` and the active implementation agents.

## Consumer

Future agents, reviewers, CI validation, and TrustGraph ingestion.

## Required Root

```text
docs/development/
```

## Required Files

- `development_manifest.json`
- `index.md`

## Required Buckets

- `epics/*.md`
- `modules/*.md`
- `features/*.md`
- `pages/*.md`
- `tasks/*.md`

## Required Markdown Frontmatter

```yaml
---
id: feature-000
type: feature
status: draft
owner_skill: marcus-ai-orchestrator
source_trace:
  - docs/prd.md
verification:
  - pending
---
```

## Validation

```bash
python3 .agents/scripts/validate_development_docs.py --strict-counts
```

## Compatibility

The ledger is additive. It must not rename, replace, or collapse approved
`/docs` planning artifacts.
