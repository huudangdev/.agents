# Knowledge Graph Contract

Use this reference for all `/understand-*` skills.

## Graph Shape

The knowledge graph at `.understand-anything/knowledge-graph.json` contains:
- `project`: `{name, description, languages, frameworks, analyzedAt, gitCommitHash}`
- `nodes[]`: file, function, class, module, concept nodes
- `edges[]`: imports, contains, calls, depends_on, and related edge types
- `layers[]`: architectural layers with `nodeIds[]`
- `tour[]`: guided onboarding steps with `nodeIds[]`

## Reading Rules

- Prefer `grep` over full-file reads.
- Read only the smallest relevant slice of the graph.
- Use node summaries and tags first; use source files only when a deep dive is needed.
- For diffs, read the changed-file set first, then resolve affected nodes and edges.

## Output Discipline

- Always tie claims back to node IDs, file paths, layers, or tour steps.
- Never invent file paths or node IDs.
- Prefer concise, evidence-led answers over broad architectural narration.
