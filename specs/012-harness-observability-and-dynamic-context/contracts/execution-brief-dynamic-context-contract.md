# Execution Brief Dynamic Context Contract

> Feature ID: `012-harness-observability-and-dynamic-context`

## Purpose

Define the additive dynamic inputs supported by `build_execution_brief.py`.

## Inputs

| Input | Type | Required | Notes |
| --- | --- | --- | --- |
| `--changed-files` | comma-separated string | no | current diff or active slice file list |
| `--failing-evidence` | string | no | concise failure signal or validator summary |

## Rules

- Both inputs are optional; no existing caller should be forced to provide them.
- The brief must place them in a dedicated bounded section rather than merging
  them into default required reads.
- Changed files may influence prioritization, but they must not automatically
  widen default reads to unrelated areas.
- Failing evidence must be treated as operator-provided context, not as a
  trigger to read arbitrary repo areas by default.
