---
name: understand
description: Analyze a codebase and build a knowledge graph for architecture, components, and relationships
argument-hint: [options]
---

# /understand

Analyze the current codebase and produce `.understand-anything/knowledge-graph.json`.

## Required Reads

- `project-scanner-prompt.md`
- `file-analyzer-prompt.md`
- `architecture-analyzer-prompt.md`
- `tour-builder-prompt.md`
- `graph-reviewer-prompt.md`

## Operating Rules

- Prefer incremental updates when the graph is current.
- Read the smallest graph slice needed for the task.
- Treat layers, tours, and diff overlays as first-class outputs.
- Never invent node IDs or file paths.

## Output Expectations

- Scan, analyze, assemble, and review the graph in order.
- Write the graph to `.understand-anything/knowledge-graph.json`.
- Keep `.understand-anything/meta.json` in sync with the commit hash.
- Fail closed when graph integrity is broken.
