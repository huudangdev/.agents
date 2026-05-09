---
name: leo-data-analytics
description: Define metrics and instrumentation that support real decisions
---

# Data Analytics

Use this skill when metrics or instrumentation must support a real decision.

## Required Reads

- [analytics-contract.md](references/analytics-contract.md)
- The schema or event context already in the repo when it exists.

## Operating Rules

- Ask only for metrics that change a decision.
- Prefer explicit event names and dimensions.
- Avoid broad or vanity instrumentation.

## Output Expectations

- State the KPI or analysis goal.
- Identify the exact event or query shape.
- Describe where instrumentation should be added and why.
