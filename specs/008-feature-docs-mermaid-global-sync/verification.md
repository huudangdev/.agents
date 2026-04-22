# Verification: Feature Docs Mermaid Global Sync

> Feature ID: `008-feature-docs-mermaid-global-sync`

## Verification Plan

| Check | Command / Method | Expected Result | Evidence |
| --- | --- | --- | --- |
| Spec validation | `python3 .agents/scripts/validate_specs.py` | Pass | Passed: 8 specs validated |
| Python compile | `PYTHONPYCACHEPREFIX=/tmp/marcus-pycache python3 -m py_compile .agents/scripts/validate_development_docs.py .agents/scripts/validate_doc_sync.py .agents/scripts/create_development_docs.py .agents/scripts/create_doc_sync_note.py .agents/scripts/validate_specs.py` | Pass | Passed |
| Missing Mermaid negative smoke | Scaffold docs, remove Mermaid fence from a feature note, run strict development validator | Fail on missing Mermaid and shallow placeholders | Failed as expected: `feature-mermaid-smoke.md: missing Mermaid diagram code fence` |
| Missing global docs negative smoke | Validate source change without global `/docs` change | Fail | Failed as expected: `Source files changed but no required global /docs planning file was updated` |

## Evidence

- `validate_specs.py` passed with `SPEC VALIDATION PASSED: 8 feature(s)`.
- Python compile passed for both updated validators and supporting scaffold
  scripts.
- Development docs negative smoke now rejects feature docs without a useful
  Mermaid code fence. This prevents code-phase feature/module/page/task notes
  from becoming text-only summaries.
- Doc sync negative smoke now rejects behavior-changing source updates that do
  not also update at least one legacy global planning doc under `/docs`.
- Sync-note strict mode also checks for explicit `updated because` reasoning so
  PM-facing docs show why a global document was changed.

## Residual Risk

- Agents may add superficial diagrams. Mitigation: rubric states diagrams must
  explain behavior, state, dependency, data flow, or handoff.
- Global docs may be over-updated if agents are careless. Mitigation: sync rules
  require targeted patches and reasoned `updated because` entries, not wholesale
  replacement.
