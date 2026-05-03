# Research Notes: Context Index and Architecture Graph

> Feature ID: `018-context-index-and-architecture-graph`

## Problem Pattern

- Models re-open broad doc/code/skills trees repeatedly.
- Token budgets are exhausted before the real root cause is understood.
- Context drift occurs: unrelated files are read and the relevant ones are missed.

## References (Informative)

- GitHub "skills" ecosystem patterns for keeping Markdown indexes current.
- Vector index tuning skills are useful for RAG systems, but this feature
  intentionally implements a cheap deterministic index without embeddings.

## Decision

Ship an index-first routing layer inside `.agents`:
- shallow markdown/code/skills indexing
- architecture map
- harness + workflow wiring so it cannot be skipped silently

