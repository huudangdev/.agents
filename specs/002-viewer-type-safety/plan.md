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

List files under `contracts/` and summarize each contract.

| Contract | Purpose | Producer | Consumer |
| --- | --- | --- | --- |
| `contracts/vector-search-api.md` | Defines `/api/chroma` request/response and execution safety. | `alan-tech-lead` | Viewer UI |

## 5. Data Model

Entities are listed in `data-model.md`: `GraphNode`, `GraphLink`, `GraphData`,
`VectorSearchResult`, and `VectorSearchResponse`.

## 6. Agent Routing

Summarize ownership from `agent-routing.md`.

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| API hardening | `alan-tech-lead` | Safe `app/api/chroma/route.ts` | lint/build |
| Type cleanup | `benny-frontend-engineer` | typed viewer components | lint/build |
| Verification | `ada-qa-agent` | evidence in `verification.md` | commands exit 0 |

## 7. Migration and Rollback

- Migration steps:
  1. Add shared types.
  2. Harden `/api/chroma`.
  3. Type page and components.
  4. Run lint and build.
- Rollback steps:
  1. Restore changed viewer files from git.
  2. Remove `lib/graphTypes.ts` if no longer referenced.
- Compatibility notes: API paths and UI layout remain unchanged.

## 8. Complexity Tracking

Use this section only when a constitution gate fails or a new abstraction is
introduced.

| Decision | Reason | Alternative Rejected | Review Needed |
| --- | --- | --- | --- |
| Local typed wrapper for `react-force-graph-3d` | Upstream type defaults do not know the Neo4j graph shape | Keep callbacks as unknown and cast repeatedly | Low |
