# Contract: Substantive Development Documentation Quality

## Producer

Agents writing `/docs/development/**` or `/docs/development/sync/**`.

## Consumer

PM review, QA review, future agents, CI validation, and TrustGraph memory.

## Rejected Content

- `TBD`
- `pending`
- `<Name>` or other placeholders
- unchecked checklist items
- empty bullets
- generic template instructions
- docs with no concrete code paths
- docs with no rationale, evidence, impact, or risk

## Required Content

Every code-phase note must include:

- PM-visible impact
- exact code paths in backticks
- implementation rationale
- tradeoffs or rejected alternatives
- verification evidence
- residual risk
- change log entry

## Validation

```bash
python3 .agents/scripts/validate_development_docs.py --strict-counts
python3 .agents/scripts/validate_doc_sync.py --strict
```
