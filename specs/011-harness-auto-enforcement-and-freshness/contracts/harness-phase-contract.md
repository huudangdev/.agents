# Harness Phase Contract

> Feature ID: `011-harness-auto-enforcement-and-freshness`

## Purpose

Define the supported harness phases and the minimum command chain each phase
must execute.

## Phases

| Phase | Stage | Required Checks | Blocking Semantics |
| --- | --- | --- | --- |
| `bootstrap` | `preflight` | `sync_project_mcp.py`, `check_mcp_health.py`, `print_update_brief.py`, `validate_harness_contract.py`, `check_repo_setup.sh` | fail on missing core setup; optional MCP warnings remain non-blocking |
| `execution` | `preflight` | `validate_command_surface.py`, `validate_routing_regression.py`, `validate_harness_contract.py`, and `validate_execution_readiness.py` when `--feature` is provided | fail if any command-surface, routing, freshness, or readiness gate fails |
| `execution` | `postflight` | `validate_command_surface.py`, `validate_routing_regression.py`, `validate_harness_contract.py`, `audit_feature_contracts.py`, and `validate_execution_readiness.py` when `--feature` is provided | fail if closeout checks fail; warning-only output must be labeled explicitly |

## Contract Rules

- Wrappers must print each invoked command before or while running it.
- Wrappers must preserve the first blocking non-zero exit code.
- Wrappers may summarize warning-only output, but they must not recast a
  blocking failure as a warning.
- The contract validator must ensure docs and workflows point to these phase
  commands, not a different hidden sequence.
