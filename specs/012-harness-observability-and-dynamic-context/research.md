# Research Notes: Harness Observability and Dynamic Context

> Feature ID: `012-harness-observability-and-dynamic-context`

## Research Questions

- How can wrappers emit useful local observability without adding heavy
  dependencies?
- Where can dynamic execution signals fit into `execution-brief.md` without
  breaking existing validators?
- Which current helper or workflow surfaces should expose the new behavior?

## Findings

| Topic | Finding | Source | Decision Impact |
| --- | --- | --- | --- |
| Wrapper replay exists | Feature `011` already provides preflight/postflight wrappers with deterministic command ordering. | local feature `011` package | add logging to existing wrappers instead of creating new ones |
| Brief contract is stable | `validate_execution_readiness.py` cares about section markers, not exact body text. | local validators and builder | add a bounded dynamic section without changing required headings |
| Observability requirement | The next harness gap after wrappers is visibility into what ran and what failed. | prior review and feature `011` residual follow-up | keep logs append-only and local |

## Decisions Ready for Plan

- Use JSONL files under `.agents/logs/harness/` for structured wrapper logs.
- Extend `build_execution_brief.py` with additive optional flags.
- Keep dynamic context human-supplied and bounded instead of auto-ingesting the
  full git or CI state.
