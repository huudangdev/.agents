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

List files under `contracts/` and summarize each contract.

| Contract | Purpose | Producer | Consumer |
| --- | --- | --- | --- |
| `contracts/runtime-health-api.md` | Defines `/api/health` response. | `alan-tech-lead` | Viewer footer, future checks |

## 5. Data Model

Entities are listed in `data-model.md`: `RuntimeServiceHealth` and
`RuntimeHealthResponse`.

## 6. Agent Routing

Summarize ownership from `agent-routing.md`.

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| Health API | `alan-tech-lead` | `/api/health` | lint/build |
| Runtime UI | `benny-frontend-engineer` | `RuntimeStatus` footer | lint/build |
| Verification | `ada-qa-agent` | evidence | spec/lint/build |

## 7. Migration and Rollback

- Migration steps:
  1. Extend config/types.
  2. Add health API.
  3. Add footer status component.
  4. Run lint/build/spec validation.
- Rollback steps:
  1. Remove `/api/health` and `RuntimeStatus`.
  2. Restore static footer text.
- Compatibility notes: no change to graph or vector search payloads.

## 8. Complexity Tracking

Use this section only when a constitution gate fails or a new abstraction is
introduced.

| Decision | Reason | Alternative Rejected | Review Needed |
| --- | --- | --- | --- |
| Client polling every 30 seconds | Keeps UI accurate without adding sockets or Prometheus dependency | Manual refresh only | Low |
