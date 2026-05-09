# Dashboard Launch Contract

Use this reference when starting the knowledge graph dashboard.

## Required Inputs

- Project directory from `$ARGUMENTS` or the current working directory
- Knowledge graph at `<project-dir>/.understand-anything/knowledge-graph.json`
- Dashboard plugin root that contains `packages/dashboard`

## Launch Steps

1. Resolve the project directory.
2. Fail fast if the graph is missing.
3. Resolve the plugin root from `~/.understand-anything-plugin`, `${CLAUDE_PLUGIN_ROOT}`, or the self-relative fallback.
4. Install dependencies and build `@understand-anything/core`.
5. Start Vite with `GRAPH_DIR=<project-dir>` and `--open`.
6. Report the local dashboard URL and graph path.

## Output Contract

- Return a running dashboard URL.
- State the graph file being viewed.
- Keep the message short and operational.

## Failure Contract

- If the graph is missing, say to run `/understand` first.
- If the plugin root cannot be resolved, stop and report the installation issue.
