# Research Notes: Design Command Readiness Hardening

> Feature ID: `014-design-command-readiness-hardening`

## Research Focus

- Which inputs `/design` explicitly depends on today.
- Which output artifacts `/design` promises today.
- Whether the repo already has local scripts that can enforce those boundaries.

## Findings

- `/design` explicitly depends on `agents.md`, `docs/prd.md`,
  `docs/planning/screens.md`, and `docs/planning/flows.md`.
- `/design` explicitly promises `docs/BRAND_GUIDELINES.md` and
  `docs/UI_COMPONENTS_STATE.md`.
- No local script previously checked either the required inputs or the required
  outputs, so the command was public but not deterministic.

## Decision

Add two small local validators and wire them into the workflow and public
command contract. Keep creative content generation out of scope.
