# Quickstart: Substantive Development Docs Quality

> Feature ID: `007-substantive-development-docs-quality`

## Local Preconditions

- `/docs/development/` exists.
- Agent has filled docs with real implementation content.

## Validation Path

```bash
python3 .agents/scripts/validate_development_docs.py --strict-counts
python3 .agents/scripts/validate_doc_sync.py --strict
```

## Expected Result

- Template-only docs fail.
- Filled docs with code paths, rationale, evidence, PM impact, and risk pass.
