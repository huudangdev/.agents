# Research Notes: Refactor Planning Command Gates

> Feature ID: `016-refactor-planning-command-gates`

## Research Focus

- Which inputs `/refactor-planning` explicitly requires before it should run.
- Which closeout artifacts the workflow already implies.
- Whether the repo already has a quality gate appropriate for brownfield doc readiness.

## Findings

- The workflow explicitly requires the legacy planning docs plus a substantive
  `docs/development/` ledger before proceeding.
- `validate_development_docs.py --strict-counts` already encodes the repo’s
  current quality expectation for the development ledger.
- The workflow already names `agents.md` and `docs/ADR_REFACTOR_LOG.md` as
  affected closeout artifacts.

## Decision

Use the existing development-doc quality gate inside a new readiness validator,
and add a small output validator for the closeout artifacts.
