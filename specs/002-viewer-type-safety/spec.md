# Feature Specification: Viewer Type Safety

> Feature ID: `002-viewer-type-safety`
> Created: `2026-04-20`
> Status: Accepted
> Source Prompt: Use the new Marcus spec lifecycle to fix TrustGraph viewer lint/type debt, starting with API command execution safety and TypeScript any removal.

## 1. Purpose

The TrustGraph viewer should be safe to maintain and safe to expose locally. Its
API must not execute vector search through a shell command string, and its
frontend should satisfy the project's own TypeScript standards instead of
carrying `any` debt.

## 2. User Stories

- [x] As an operator, I need vector search to pass arguments directly to Python
      so that search text cannot be interpreted as shell syntax.
- [x] As a maintainer, I need graph and vector data types so that viewer changes
      fail at build time instead of drifting silently.
- [x] As a QA agent, I need `npm run lint` and `npm run build` to pass so that
      future viewer changes have a clean baseline.

## 3. Functional Requirements

- `FR-001`: The `/api/chroma` route MUST use argv-based process execution, not
  shell command string execution.
- `FR-002`: The viewer MUST define shared types for graph nodes, graph links,
  filter modes, and vector search results.
- `FR-003`: `page.tsx`, `Inspector.tsx`, and `GraphVisualizer.tsx` MUST avoid
  explicit `any`.
- `FR-004`: Highlight calculation MUST avoid synchronous setState inside effects.
- `FR-005`: The viewer MUST pass `npm run lint` and `npm run build`.

## 4. Non-Functional Requirements

- `NFR-001`: Performance: graph filtering and highlighting should remain memoized.
- `NFR-002`: Security: vector search query must be passed as a subprocess
  argument, not interpolated into a shell string.
- `NFR-003`: Observability: completion evidence must be recorded in
  `verification.md` and root `agents.md`.
- `NFR-004`: Maintainability: shared viewer types should live in `lib/`.

## 5. Acceptance Criteria

- `AC-001`: Given the viewer package, when `npm run lint` runs, then it exits 0.
- `AC-002`: Given the viewer package, when `npm run build` runs, then it exits 0.
- `AC-003`: Given a malicious-looking vector query string, when `/api/chroma`
  handles it, then the text is passed as an argv value to Python rather than
  interpreted by a shell.

## 6. Clarifications

- Clarification resolved: this step targets type and command-execution safety in
  the existing viewer, not a visual redesign.
- Clarification resolved: runtime testing with a live Neo4j/Chroma cluster is out
  of scope because local containers are currently offline; build/lint are the
  required baseline checks.

## 7. Constraints

- Constitution articles that apply: Article IV, Article V, Article VII,
  Article VIII.
- Existing files or modules in scope: `.agents/trustgraph-viewer/app`,
  `.agents/trustgraph-viewer/components`, `.agents/trustgraph-viewer/lib`.
- Files or modules out of scope: visual redesign, Neo4j/Chroma runtime startup,
  TrustGraph schema changes.
- Compatibility requirements: keep existing API routes and UI behavior.

## 8. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Third-party force graph types do not match internal graph shape | Medium | Add a local typed wrapper around the dynamic component. |
| Build catches stricter type issues after lint passes | Low | Run both lint and build. |

## 9. Traceability

| Requirement | Plan Section | Tasks | Verification |
| --- | --- | --- | --- |
| `FR-001` | `plan.md#3` | `T001` | `verification.md#evidence` |
| `FR-002` | `plan.md#3` | `T002` | `verification.md#evidence` |
| `FR-003` | `plan.md#3` | `T003` | `verification.md#evidence` |
| `FR-004` | `plan.md#3` | `T004` | `verification.md#evidence` |
| `FR-005` | `plan.md#7` | `T005` | `verification.md#evidence` |

## 10. Review Loop

| Round | Reviewer | Focus | Exit Criteria | Status |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Scope challenge | the feature stays bounded and out-of-scope lines are explicit | Complete |
| `R2` | `sophia-product-manager` | Requirement quality | user stories, FRs, ACs, and constraints still align | Complete |
| `R3` | `marcus-ai-orchestrator` | Go/no-go to execution planning | the package is deep enough for tasks, quickstart, and readiness gates | Complete |
