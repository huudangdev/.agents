# Verification: Brownfield Doc Reconcile Command

> Feature ID: `010-brownfield-doc-reconcile-command`

## Verification Plan

| Check | Command / Method | Expected Result | Evidence |
| --- | --- | --- | --- |
| Python compile | `PYTHONPYCACHEPREFIX=/tmp/marcus-pycache python3 -m py_compile ...` | Pass | Passed |
| Spec validation | `python3 .agents/scripts/validate_specs.py` | Pass | Passed: 10 specs validated |
| Audit smoke | `audit_development_docs.py --root /tmp/...` | Creates audit markdown | Passed |
| V31 scaffold smoke | `create_development_docs.py --root /tmp/...` | Includes `issues.md` | Passed |
| Missing issues negative smoke | Remove `issues.md` then validate | Fails | Failed as expected: `missing issues.md` |

## Evidence

- Python compile passed for updated validators, scaffold, sync, spec validator,
  and `audit_development_docs.py`.
- `validate_specs.py` passed with `SPEC VALIDATION PASSED: 10 feature(s)`.
- Audit smoke created
  `docs/development/audits/20260423-184502-code-docs-audit.md`.
- V31 scaffold smoke created `docs/development/E-001-doc-reconcile-smoke/issues.md`.
- Negative smoke removed `issues.md`; strict validation failed with
  `docs/development/E-001-doc-reconcile-smoke: missing issues.md`.

## Residual Risk

- `/doc_reconcile` can identify and document gaps, but actual downstream app
  fixes still require operator-approved `/develop` or `/quick_fix`.
