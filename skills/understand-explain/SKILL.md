---
name: understand-explain
description: Explain a specific file, function, or module using the knowledge graph and source
argument-hint: [file-path]
---

# /understand-explain

Provide a deep explanation of a specific code component.

## Required Reads

- [knowledge-graph-contract.md](references/knowledge-graph-contract.md)

## Operating Rules

- Find the target node first.
- Read connected edges and the owning layer.
- Read the source file when you need line-level detail.
- Keep the explanation grounded in actual code locations.

## Output Expectations

- Explain the role, structure, connections, and data flow.
- Highlight patterns and complexity that matter.
- Assume the reader may not know the language.
