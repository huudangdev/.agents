# Quickstart: Develop Knowledge Ledger

> Feature ID: `005-develop-knowledge-ledger`

## Prerequisites

- Approved `/docs` planning package.
- Optional accepted `.agents/specs/<feature-id>/` workspace.

## Steps

1. Initialize the code-phase ledger:

```bash
python3 .agents/scripts/create_development_docs.py --name "Checkout Flow" --feature-id "005-checkout-flow"
```

2. Fill the generated notes under:

```text
docs/development/epics/
docs/development/modules/
docs/development/features/
docs/development/pages/
docs/development/tasks/
```

3. Run validation before final `/develop` completion:

```bash
python3 .agents/scripts/validate_development_docs.py --strict-counts
```

## Validation

```bash
python3 .agents/scripts/validate_specs.py --feature .agents/specs/005-develop-knowledge-ledger
```
