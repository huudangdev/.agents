# Quickstart: Continuous Documentation Sync

> Feature ID: `006-continuous-documentation-sync`

## Local Preconditions

- `/develop` has initialized `/docs/development/`.
- A material code slice has changed one or more source files.

## Validation Path

1. Create a sync note:

```bash
python3 .agents/scripts/create_doc_sync_note.py --name "Checkout API slice" --changed-files "src/api/checkout.ts,docs/tasks.md"
```

2. Append or patch affected docs. Do not replace entire PM docs.

3. Validate:

```bash
python3 .agents/scripts/validate_doc_sync.py --strict
```

## Rollback Check

- If validation fails, pause code work and add the missing documentation trace.
