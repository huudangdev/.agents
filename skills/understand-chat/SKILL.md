---
name: understand-chat
description: Answer codebase questions using the knowledge graph with minimal reads
argument-hint: [query]
---

# /understand-chat

Answer questions about this codebase using `.understand-anything/knowledge-graph.json`.

## Required Reads

- [knowledge-graph-contract.md](references/knowledge-graph-contract.md)

## Operating Rules

- Grep the graph before reading it in full.
- Use node summaries, tags, and edges before touching source files.
- Keep the answer grounded in actual file paths, node IDs, and layer names.
- If the graph does not exist, tell the user to run `/understand` first.

## Instructions

1. Check that the graph exists.
2. Read only the project metadata you need.
3. Search for matching nodes using the query keywords.
4. Follow 1-hop edges from the matched nodes.
5. Read the layer context for the matched nodes.
6. Answer using only the relevant subgraph.

## Output Expectations

- Reference specific nodes, files, and relationships.
- Explain which layer or layers are relevant and why.
- Stay concise, evidence-led, and scoped to the query.
