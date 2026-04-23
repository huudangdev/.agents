# Quickstart: Brownfield Doc Reconcile Command

Run audit:

```bash
python3 .agents/scripts/audit_development_docs.py --root .
```

Then invoke `/doc_reconcile` and reconcile docs until:

```bash
python3 .agents/scripts/validate_development_docs.py --strict-counts
python3 .agents/scripts/validate_doc_sync.py --strict
```

pass or residual risks are explicitly accepted.
