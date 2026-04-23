---
id: development-index
type: development-index
status: draft
owner_skill: marcus-ai-orchestrator
source_trace:
  - docs/prd.md
  - docs/tasks.md
---

# Development Knowledge Index

> QUALITY BAR: this index must help a PM and a future agent understand current
> POC implementation state in under five minutes. It must link to real notes,
> summarize progress, and call out stale or risky areas.

## Execution Scope

- Feature/spec id:
- Implementation branch:
- Approved planning package:
- Active owner skills:

## Artifact Map

| Artifact | Path | Purpose |
| --- | --- | --- |
| Manifest | `docs/development/development_manifest.json` | Canonical registry for topology, IDs, quality gates, and epic children |
| Epic Root | `docs/development/E-001-<description>/` | Parent folder for one delivery outcome |
| Epic Note | `docs/development/E-001-<description>/epic.md` | Major delivery outcome and acceptance boundary |
| Issues | `docs/development/E-001-<description>/issues.md` | QA/product risk register for the epic |
| Features | `docs/development/E-001-<description>/features/F-001-001-<description>.md` | User-visible behavior and implementation slices |
| Modules | `docs/development/E-001-<description>/modules/M-001-001-<description>.md` | Code ownership, APIs, data contracts, dependencies |
| Pages | `docs/development/E-001-<description>/pages/P-001-001-<description>.md` | UI route/screen/page behavior, states, accessibility |
| Tasks | `docs/development/E-001-<description>/tasks/T-001-001-001-<description>.md` | Execution notes, tests, commits, residual risks |
| Sync | `docs/development/E-001-<description>/sync/` | Epic-local code/docs sync notes |

## Canonical ID Registry

| ID | Type | Parent | Status | File |
| --- | --- | --- | --- | --- |
| `E-001-example` | epic | root | draft | `docs/development/E-001-example/epic.md` |
| `ISSUES-E-001-example` | epic-issues | `E-001-example` | draft | `docs/development/E-001-example/issues.md` |
| `F-001-001-example` | feature | `E-001-example` | draft | `docs/development/E-001-example/features/F-001-001-example.md` |
| `M-001-001-example` | module | `E-001-example` | draft | `docs/development/E-001-example/modules/M-001-001-example.md` |
| `P-001-001-example` | page | `E-001-example` | draft | `docs/development/E-001-example/pages/P-001-001-example.md` |
| `T-001-001-001-example` | task | `E-001-example` | draft | `docs/development/E-001-example/tasks/T-001-001-001-example.md` |

## Relationship Label Taxonomy

| Label | Meaning | Use When |
| --- | --- | --- |
| `DEPENDS_ON` | Source artifact cannot work without target | Feature needs module, page needs data contract |
| `BLOCKS` | Source must finish before target can proceed | Task sequencing or unresolved issue blocks release |
| `ENABLES` | Source unlocks target capability | Module/epic enables feature or demo |
| `IMPLEMENTS` | Source realizes target requirement | Feature implements epic, task implements story |
| `USES` | Source consumes target behavior/data | Page uses module, task edits module |
| `EXTENDS` | Source adds behavior on top of target | Feature extends an existing feature |
| `CONFLICTS_WITH` | Source may overlap or break target | Competing UX/state/data choices |
| `SUPERSEDES` | Source replaces an older behavior/doc decision | Updated design or implementation decision |
| `DUPLICATES` | Source appears to repeat target | Migration/audit duplicate detection |
| `RELATES_TO` | Source has non-blocking contextual relation | Shared user journey, shared data, adjacent feature |

## Jira / Product Governance

- Story format:
- Priority model: `P0`, `P1`, `P2`, `P3`, `P4`
- Issue source: QA auto-detect, user report, research finding, regression test
- Docs-before-code status:
- Last deep research source reviewed:

## Migration / Archive Notes

- Legacy flat buckets:
- Duplicate files archived:
- Files intentionally retained:
- Files requiring manual PM review:

## Verification Summary

- Unit tests:
- Integration tests:
- UI/E2E tests:
- Build/lint/typecheck:
- Manual checks:

## Open Risks

- Risk:
  - Owner:
  - Mitigation:

## Documentation Freshness

- Last code slice synced:
- Last sync note:
- Docs intentionally stale:
- Next documentation action:
