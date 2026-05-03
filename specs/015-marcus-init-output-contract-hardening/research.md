# Research Notes: Marcus Init Output Contract Hardening

> Feature ID: `015-marcus-init-output-contract-hardening`

## Research Focus

- Which scaffold outputs `/marcus_init` explicitly creates today.
- Whether a narrow output validator can prove success without rewriting the
  shell workflow.

## Findings

- The workflow explicitly creates `projects/$PROJECT_NAME/docs`,
  `projects/$PROJECT_NAME/.agents`, `.clinerules`, `agents.md`,
  `.agents/agents.md`, and seeds `docs/prd_draft.md`.
- The workflow is shell-heavy, so the most pragmatic hardening is a closeout
  validator rather than an orchestration rewrite.

## Decision

Add one local output validator and wire it into the public command contract.
