---
name: understand-diff
description: Analyze git diffs against the knowledge graph to map change impact and risk
---

# /understand-diff

Analyze the current code changes against `.understand-anything/knowledge-graph.json`.

## Required Reads

- [knowledge-graph-contract.md](references/knowledge-graph-contract.md)

## Operating Rules

- Get the changed files list before reading the graph.
- Read only the project metadata you need.
- Find graph nodes for each changed file path.
- Identify affected layers and 1-hop dependencies.

## Output Expectations

- Describe what changed, what is likely impacted, and why.
- Keep the analysis tied to real node IDs, files, and layers.
- Write `.understand-anything/diff-overlay.json` for the dashboard.
