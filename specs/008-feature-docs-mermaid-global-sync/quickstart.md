# Quickstart: Feature Docs Mermaid Global Sync

> Feature ID: `008-feature-docs-mermaid-global-sync`

## Local Preconditions

- `/docs/development/` exists.
- A behavior-changing code slice exists.

## Validation Path

```bash
python3 .agents/scripts/validate_development_docs.py --strict-counts
python3 .agents/scripts/validate_doc_sync.py --changed-files "src/example.ts,docs/tasks.md,docs/development/features/feature-example.md" --strict
```

## Expected Result

- Missing Mermaid fails development docs validation.
- Missing global `/docs` updates fail doc sync validation.
