# Context Index and Architecture Graph

Feature ID: `018-context-index-and-architecture-graph`

This feature introduces an index-first routing layer for `.agents`:

- Build a shallow docs/code/skills index under `.agents/index/`.
- Generate a repo-agnostic architecture graph (Mermaid) to guide targeted reads.
- Wire the index gate into harness preflight and core workflows to prevent
  token waste and context drift from "read everything" behavior.

