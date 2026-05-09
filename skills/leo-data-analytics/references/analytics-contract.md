# Analytics Contract

Use this skill when metrics or instrumentation must support a real decision.

## Required Inputs

- The decision the metric should inform
- The schema or event context already in the repo
- Collection cost and privacy constraints

## Decision Rules

- Ask only for metrics that change a decision.
- Prefer explicit event names and dimensions.
- Avoid broad or vanity instrumentation.

## Output Contract

- State the KPI or analysis goal.
- Identify the exact event or query shape.
- Describe where instrumentation should be added and why.
