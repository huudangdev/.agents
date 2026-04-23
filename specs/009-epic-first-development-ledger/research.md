# Research: Epic-First Development Ledger

## Findings

- Flat type buckets are easy to validate but weak at preserving parent-child
  knowledge. They let agents create orphan docs and duplicate slugs.
- Epic-first folders make PM review and agent handoff easier because one
  delivery outcome owns its features, modules, pages, tasks, and sync notes.
- Backward compatibility requires topology detection; otherwise older V30
  ledgers would fail for structural reasons unrelated to their content.

## Decision

Use epic-first as the default for new ledgers and keep legacy-flat as a
validator path for existing manifests.
