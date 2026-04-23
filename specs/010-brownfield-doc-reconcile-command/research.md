# Research: Brownfield Doc Reconcile Command

## Findings

- In-progress projects often accumulate source behavior faster than docs.
- A code inventory gives minimum evidence that reconciliation is based on the
  implemented system, not stale prompt memory.
- Epic-local `issues.md` prevents QA/product risks from being buried inside
  narrative notes.

## Decision

Add `/doc_reconcile` as an explicit brownfield docs recovery command before
resuming `/develop`.
