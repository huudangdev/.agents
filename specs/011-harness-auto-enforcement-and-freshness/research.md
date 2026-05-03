# Research Notes: Harness Auto Enforcement and Freshness

> Feature ID: `011-harness-auto-enforcement-and-freshness`

## Research Questions

- Which current `.agents` scripts already prove parts of bootstrap and execution
  readiness?
- Where does the public command surface still rely on humans remembering a
  sequence instead of invoking one command?
- Which parts of the harness need true runtime enforcement versus documentation
  cleanup only?

## Findings

| Topic | Finding | Source | Decision Impact |
| --- | --- | --- | --- |
| Existing bootstrap checks | `sync_project_mcp.py`, `check_mcp_health.py`, `print_update_brief.py`, and `check_repo_setup.sh` already cover most bootstrap needs but are not orchestrated behind one command. | local scripts and `workflows/init_brain.md` | add bootstrap preflight wrapper instead of replacing the scripts |
| Existing execution checks | `validate_command_surface.py`, `validate_routing_regression.py`, `validate_execution_readiness.py`, and `audit_feature_contracts.py` already exist and pass in standalone `.agents`. | current `.agents` verification replay | build execution pre/postflight wrappers around these validators |
| Harness doctrine | Public harness-engineering writing emphasizes mechanisms, bounded context, and structural enforcement beyond prompts. | external synthesis used in prior review | add wrappers and a freshness validator instead of more prose-only guidance |

## Decisions Ready for Plan

- Use additive orchestration wrappers rather than rewriting validated checks.
- Add one repo-wide freshness validator for docs/workflow/script agreement.
- Keep the feature scoped to `.agents` only; no downstream repo migration is
  included.
