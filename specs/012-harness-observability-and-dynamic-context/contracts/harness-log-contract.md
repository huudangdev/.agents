# Harness Log Contract

> Feature ID: `012-harness-observability-and-dynamic-context`

## Purpose

Define the structured local event shape for harness wrapper runs.

## Event Shape

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `timestamp` | string | yes | ISO-8601 UTC timestamp |
| `phase` | string | yes | `bootstrap` or `execution` |
| `stage` | string | yes | `preflight` or `postflight` |
| `feature` | string | no | feature path when provided |
| `status` | string | yes | `pass` or `fail` |
| `failing_command` | string | no | first blocking command, if any |
| `commands` | array | yes | ordered command results |

## Command Result Shape

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `command` | string | yes | printable command string |
| `exit_code` | integer | yes | raw subprocess exit code |
| `status` | string | yes | `pass` or `fail` |

## Rules

- Logs are append-only JSONL files under `.agents/logs/harness/`.
- Logs must stay local to the `.agents` workspace.
- Logs must not include environment dumps or secret values.
