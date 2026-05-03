# Implementation Plan: Viewer Type Safety

> Feature ID: `002-viewer-type-safety`
> Spec: `spec.md`
> Constitution: `.agents/memory/constitution.md`

## 1. Technical Summary

Harden the TrustGraph viewer in one focused increment:

- Replace `/api/chroma` shell string execution with `execFile`.
- Add shared graph/vector TypeScript types in `lib/graphTypes.ts`.
- Type page, inspector, and graph visualizer props/state.
- Move highlight derivation from effect-setState to memoized calculation.
- Verify with `npm run lint` and `npm run build`.

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

- Existing modules: `app/api/chroma/route.ts`, `app/page.tsx`,
  `components/GraphVisualizer.tsx`, `components/Inspector.tsx`.
- Current coupling: graph API returns flexible Neo4j-derived data that viewer
  components previously treated as `any`.
- Known constraints: `react-force-graph-3d` has broad generic types, so a local
  wrapper is needed to connect internal graph types to callback props.

### 3.2 Target State

- New or changed modules:
  - `lib/graphTypes.ts`
  - `app/api/chroma/route.ts`
  - `app/page.tsx`
  - `components/GraphVisualizer.tsx`
  - `components/Inspector.tsx`
- Data flow: `/api/graph` -> `GraphData` -> `GraphVisualizer` and `Inspector`;
  `/api/chroma` -> `VectorSearchResponse` -> vector result panel.
- Operational flow: query text is parsed from JSON, validated as a string, and
  passed to Python through `execFile("python3", [scriptPath, "--query", query])`.

### 3.3 Mermaid Diagram

```mermaid
flowchart TD
    Query[Vector Query] --> Route[/api/chroma]
    Route --> ExecFile[execFile argv]
    ExecFile --> Python[trustgraph_vector_search.py]
    GraphAPI[/api/graph] --> Types[graphTypes.ts]
    Types --> Visualizer[GraphVisualizer]
    Types --> Inspector[Inspector]
```

## 4. Contracts

| Contract | Purpose | Producer | Consumer |
| --- | --- | --- | --- |
| `vector-search-api.md` | Feature-specific contract consumed by the current slash-command surface. | feature owner | `/develop`, `/quick_fix`, and reviewers |

## 5. Data Model

Entities are listed in `data-model.md`: `GraphNode`, `GraphLink`, `GraphData`,
`VectorSearchResult`, and `VectorSearchResponse`.

## 6. Agent Routing

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| API hardening | `alan-tech-lead` | Safe `app/api/chroma/route.ts` | lint/build |
| Type cleanup | `benny-frontend-engineer` | typed viewer components | lint/build |
| Verification | `ada-qa-agent` | evidence in `verification.md` | commands exit 0 |

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: npm run lint; npm run build.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: npm run lint; npm run build.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: npm run lint; npm run build.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.

## 7. Migration and Rollback

- Migration steps:
  1. Reconcile the feature package to the current contract.
  2. Rebuild `execution-brief.md` for the active task shape.
  3. Re-run spec and readiness validation before downstream execution.
- Rollback steps:
  1. Restore the previous `002-viewer-type-safety` docs package if the contract upgrade proves misleading.
  2. Revert only the additive governance sections; do not silently discard verified implementation evidence.
- Compatibility notes: preserve the implemented behavior and existing contracts while making the feature package consumable by the current slash-command surface.

## 8. Complexity Tracking

| Decision | Reason | Alternative Rejected | Review Needed |
| --- | --- | --- | --- |
| Local typed wrapper for `react-force-graph-3d` | Upstream type defaults do not know the Neo4j graph shape | Keep callbacks as unknown and cast repeatedly | Low |

## 9. POC Slice and Review Cadence

- POC slice boundary: prove `002-viewer-type-safety` end-to-end using the smallest professional slice that exercises the main contract and verification path.
- Success evidence for the slice: npm run lint; npm run build plus updated review-loop and release-recommendation artifacts.
- What remains intentionally unproven after the slice: broader product rollout, unrelated modules, and any live services the current feature explicitly left as residual risk.
- Review cadence:
  - Draft architecture review: after the package is reconciled to the current contract.
  - Challenge review: after tasks, routing, and quickstart replay are concrete.
  - Final readiness review: after verification evidence and release recommendation are updated.
- Stop conditions: readiness fails, review findings expose hidden scope growth, or the replay steps cannot be followed from docs alone.
- Proceed conditions: spec validation passes, execution-brief freshness passes, readiness passes, and the verification package names a clear release recommendation.
