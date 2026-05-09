---
name: understand-dashboard
description: Launch the knowledge graph dashboard for the current project
argument-hint: [project-path]
---

# /understand-dashboard

Start the Understand Anything dashboard to visualize the knowledge graph for the current project.

## Required Reads

- [launch.md](references/launch.md)

## Operating Rules

- Resolve the project directory first.
- Fail fast if the graph does not exist.
- Use the plugin root resolver from the reference, not an ad hoc path.
- Run the dashboard in the background and report the local URL.

## Output Expectations

- Launch the dashboard with `GRAPH_DIR` pointed at the target project.
- Report the URL and the graph file being viewed.
- Keep the message short and operational.
