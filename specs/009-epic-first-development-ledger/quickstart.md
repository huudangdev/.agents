# Quickstart: Epic-First Development Ledger

Create a new V31 ledger:

```bash
python3 .agents/scripts/create_development_docs.py --name "Checkout Flow" --feature-id "009-checkout-flow" --epic-number 001 --child-number 001 --task-number 001
```

Create an epic-local sync note:

```bash
python3 .agents/scripts/create_doc_sync_note.py --name "Checkout API Slice" --epic-id "E-001-checkout-flow" --changed-files "src/api/checkout.ts,docs/tasks.md"
```

Validate:

```bash
python3 .agents/scripts/validate_development_docs.py --strict-counts
python3 .agents/scripts/validate_doc_sync.py --strict
```
