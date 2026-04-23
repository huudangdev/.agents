# Contract: Brownfield Doc Reconcile Command

## Command Contract

- `/doc_reconcile` does not edit application source code by default.
- It must audit code/docs before changing development docs.
- It must create or update V31.1 epic-first docs and one `issues.md` per epic.
- It must update global docs when code reality differs from planning docs.

## Validation Contract

- Missing `issues.md` in V31 epic directories is invalid.
- Empty templates are invalid.
- Relationship labels, Story, Priority, Work Log, Mermaid, and verification are
  mandatory.
