# Feature Specification: TrustGraph Runtime Health

> Feature ID: `003-trustgraph-runtime-health`
> Created: `2026-04-20`
> Status: Accepted
> Source Prompt: Add real Neo4j and Chroma runtime health checks and replace hardcoded viewer connection status with live health state.

## 1. Purpose

The TrustGraph viewer must report real runtime health for Neo4j and ChromaDB
instead of showing a hardcoded connected state. Operators should be able to see
whether the graph stack is online, degraded, or offline before trusting graph or
vector search results.

## 2. User Stories

- [x] As an operator, I need the footer status to reflect live TrustGraph health
      so that I can distinguish offline services from working data.
- [x] As a maintainer, I need a JSON health endpoint so that UI, scripts, and
      future CI checks can reuse the same service status.

## 3. Functional Requirements

- `FR-001`: The viewer MUST expose `/api/health`.
- `FR-002`: The health endpoint MUST check Neo4j with a real query.
- `FR-003`: The health endpoint MUST check ChromaDB with a heartbeat request.
- `FR-004`: The health endpoint MUST return `online`, `degraded`, or `offline`.
- `FR-005`: The viewer footer MUST consume `/api/health` and remove the
  hardcoded `NEO4J CONNECTED` label.

## 4. Non-Functional Requirements

- `NFR-001`: Performance: health checks should use short timeouts and run in
  parallel.
- `NFR-002`: Security: health responses should expose status and error text only,
  never credentials.
- `NFR-003`: Observability: each service result should include latency when
  available.
- `NFR-004`: Maintainability: health response types should live in shared viewer
  type definitions.

## 5. Acceptance Criteria

- `AC-001`: Given the viewer package, when `npm run build` runs, then `/api/health`
  appears as a dynamic route and build exits 0.
- `AC-002`: Given TrustGraph services are offline, when the UI loads, then the
  footer can show an offline/degraded status rather than a false connected label.
- `AC-003`: Given the health endpoint runs, when one service fails, then the
  aggregate status is not `online`.

## 6. Clarifications

- Clarification resolved: do not start Docker as part of this feature; the endpoint
  must truthfully report offline services when they are down.
- Clarification resolved: this step targets health visibility, not automatic
  remediation or service startup.

## 7. Constraints

- Constitution articles that apply: Article IV, Article V, Article VIII.
- Existing files or modules in scope: viewer app API, viewer components, viewer
  shared config/types.
- Files or modules out of scope: Docker startup automation, Prometheus/Grafana
  dashboards, visual graph rendering behavior.
- Compatibility requirements: existing `/api/graph` and `/api/chroma` behavior
  must remain unchanged.

## 8. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Chroma heartbeat path differs by version | Medium | Use the current local container HTTP path and treat non-OK as offline. |
| Build cannot prove live runtime health without services running | Low | Record build/route evidence and leave runtime container test as residual risk. |

## 9. Traceability

| Requirement | Plan Section | Tasks | Verification |
| --- | --- | --- | --- |
| `FR-001` | `plan.md#3` | `T001` | `verification.md#evidence` |
| `FR-002` | `plan.md#3` | `T001` | `verification.md#evidence` |
| `FR-003` | `plan.md#3` | `T001` | `verification.md#evidence` |
| `FR-004` | `plan.md#3` | `T002` | `verification.md#evidence` |
| `FR-005` | `plan.md#3` | `T003` | `verification.md#evidence` |
