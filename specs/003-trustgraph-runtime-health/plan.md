# Implementation Plan: TrustGraph Runtime Health

> Feature ID: `003-trustgraph-runtime-health`
> Spec: `spec.md`
> Constitution: `.agents/memory/constitution.md`

## 1. Technical Summary

Add a dedicated health endpoint and UI runtime status component:

- Extend viewer config with Chroma host/port.
- Add shared runtime health response types.
- Add `/api/health` to query Neo4j and ChromaDB in parallel.
- Replace hardcoded footer text with a `RuntimeStatus` client component.
- Verify with lint, build, and spec validation.

## 2. Constitution Gates

- [x] Specification has no unresolved `[NEEDS CLARIFICATION]` markers, or the
      operator accepted the residual risk.
- [x] Contracts are defined before implementation.
- [x] Verification method is named before implementation.
- [x] No shell `eval` or unbounded command execution is introduced.
- [x] No hardcoded production secret is introduced.
- [x] TypeScript changes avoid `any` unless justified in Complexity Tracking.
- [x] Rollback path is documented for user-facing or operational changes.

## 3. Architecture

### 3.1 Current State

- Existing modules: `lib/trustgraphConfig.ts`, `lib/graphTypes.ts`,
  `app/page.tsx`.
- Current coupling: footer status is a static UI label and not connected to
  service state.
- Known constraints: local Neo4j/Chroma may be offline during development.

### 3.2 Target State

- New or changed modules:
  - `app/api/health/route.ts`
  - `components/RuntimeStatus.tsx`
  - `lib/trustgraphConfig.ts`
  - `lib/graphTypes.ts`
  - `app/page.tsx`
- Data flow: `RuntimeStatus` fetches `/api/health`; endpoint checks Neo4j and
  Chroma; UI renders aggregate status and per-service tooltip.
- Operational flow: health is checked on load and every 30 seconds.

### 3.3 Mermaid Diagram

```mermaid
flowchart TD
    UI[RuntimeStatus] --> HealthAPI[/api/health]
    HealthAPI --> Neo4j[Neo4j RETURN 1]
    HealthAPI --> Chroma[Chroma heartbeat]
    Neo4j --> Aggregate[online/degraded/offline]
    Chroma --> Aggregate
    Aggregate --> UI
```

## 4. Contracts

| Contract | Purpose | Producer | Consumer |
| --- | --- | --- | --- |
| `runtime-health-api.md` | Feature-specific contract consumed by the current slash-command surface. | feature owner | `/develop`, `/quick_fix`, and reviewers |

## 5. Data Model

Entities are listed in `data-model.md`: `RuntimeServiceHealth` and
`RuntimeHealthResponse`.

## 6. Agent Routing

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| Health API | `alan-tech-lead` | `/api/health` | lint/build |
| Runtime UI | `benny-frontend-engineer` | `RuntimeStatus` footer | lint/build |
| Verification | `ada-qa-agent` | evidence | spec/lint/build |

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: npm run build; npm run lint.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: npm run build; npm run lint.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: npm run build; npm run lint.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.

## 7. Migration and Rollback

- Migration steps:
  1. Reconcile the feature package to the current contract.
  2. Rebuild `execution-brief.md` for the active task shape.
  3. Re-run spec and readiness validation before downstream execution.
- Rollback steps:
  1. Restore the previous `003-trustgraph-runtime-health` docs package if the contract upgrade proves misleading.
  2. Revert only the additive governance sections; do not silently discard verified implementation evidence.
- Compatibility notes: preserve the implemented behavior and existing contracts while making the feature package consumable by the current slash-command surface.

## 8. Complexity Tracking

| Decision | Reason | Alternative Rejected | Review Needed |
| --- | --- | --- | --- |
| Client polling every 30 seconds | Keeps UI accurate without adding sockets or Prometheus dependency | Manual refresh only | Low |

## 9. POC Slice and Review Cadence

- POC slice boundary: prove `003-trustgraph-runtime-health` end-to-end using the smallest professional slice that exercises the main contract and verification path.
- Success evidence for the slice: npm run build; npm run lint plus updated review-loop and release-recommendation artifacts.
- What remains intentionally unproven after the slice: broader product rollout, unrelated modules, and any live services the current feature explicitly left as residual risk.
- Review cadence:
  - Draft architecture review: after the package is reconciled to the current contract.
  - Challenge review: after tasks, routing, and quickstart replay are concrete.
  - Final readiness review: after verification evidence and release recommendation are updated.
- Stop conditions: readiness fails, review findings expose hidden scope growth, or the replay steps cannot be followed from docs alone.
- Proceed conditions: spec validation passes, execution-brief freshness passes, readiness passes, and the verification package names a clear release recommendation.
