---
description: Brownfield command to reconcile in-progress project docs with actual code, migrate /docs/development to V31.1, and fill product-grade documentation.
---

# /doc_reconcile - Brownfield Development Docs Reconciliation

> **CORE MANDATE:**  
> Use this slash command for projects already in progress whose docs are stale,
> flat, shallow, duplicated, or not aligned with code. This command updates
> documentation based on the actual codebase. It must not change application
> source code unless the operator explicitly asks for implementation fixes.

// turbo-all

## Non-Negotiable Rules

1. **Review code before changing docs.** Create a whole-codebase inventory first.
2. **Docs before future code.** After this command, `/develop` must start from
   the reconciled docs, not stale planning assumptions.
3. **No empty templates.** Scaffold files are invalid until filled with real
   code-derived, PM-readable content.
4. **Epic-first topology.** Canonical source of truth is
   `docs/development/E-###-description/`.
5. **Issues file per epic.** Every epic must have `issues.md`, generated or
   reviewed with QA skill reasoning.
6. **Relationship labels are mandatory.** Use `DEPENDS_ON`, `BLOCKS`,
   `ENABLES`, `IMPLEMENTS`, `USES`, `EXTENDS`, `CONFLICTS_WITH`, `SUPERSEDES`,
   `DUPLICATES`, and `RELATES_TO`.
7. **Jira product model.** Every epic/module/feature/page/task/issues note must
   contain Story and Priority.
8. **Global docs are authoritative.** Update legacy `/docs` planning files when
   implementation behavior differs from them.
9. **This gate is inherited by all implementation skills.** Any workflow or
   skill that discovers missing, boilerplate, stale, or template-only docs in a
   brownfield project must route here before allowing material code edits.

## Required Skills

- `development-ledger-architect`
- `knowledge-work-architecture`
- `ada-qa-agent`
- `sophia-product-manager`
- `marcus-ai-orchestrator`

## Phase 0: Preflight Inventory

Run:

```bash
python3 .agents/scripts/audit_development_docs.py --root .
```

Then read the generated `docs/development/audits/*.md` file. This audit is the
minimum proof that the codebase was inventoried before docs reconciliation.

Also read:

```text
docs/prd.md
docs/tasks.md
docs/knowledge.md
docs/decisions.md
docs/memory.md
docs/planning/flows.md
docs/planning/screens.md
docs/planning/diagrams.md
docs/development/development_manifest.json
docs/development/index.md
```

If some files are missing, record that in the audit and create the missing docs
only when needed for a coherent PM handoff.

If the project has only bootstrap docs such as a default framework README, that
still counts as missing PM docs for routing purposes.

## Phase 1: Code-Derived Domain Model

Review all source clusters from the audit and classify them:

| Code Cluster | Canonical Doc | Required Evidence |
| --- | --- | --- |
| routes/pages/screens | `pages/P-###-###-*.md` | route, states, UI behavior, accessibility, screenshots/manual check |
| components/hooks | feature/page/module docs | props, state, user behavior, failure modes |
| APIs/server actions | feature/module/task docs | contracts, auth, validation, error behavior |
| services/lib | modules/M-###-###-*.md | ownership, public contract, dependencies |
| migrations/schema | module/task docs | data model, rollback, risk |
| tests | task/issues docs | coverage, failure evidence, gaps |

The agent must not rely only on filenames. Read representative implementation
files for every cluster and inspect relationships between clusters.

## Phase 2: Build The Epic Graph

Create or reconcile:

```text
docs/development/
  development_manifest.json
  index.md
  E-001-description/
    epic.md
    issues.md
    features/F-001-001-description.md
    modules/M-001-001-description.md
    pages/P-001-001-description.md
    tasks/T-001-001-001-description.md
    sync/
  _archive/
```

Canonical naming:

- Epic: `E-001-description`
- Feature: `F-001-001-description`
- Module: `M-001-001-description`
- Page: `P-001-001-description`
- Task: `T-001-001-001-description`
- Issues: `issues.md` with `id: ISSUES-E-001-description`

Migration rules:

- Preserve useful legacy content by targeted merge.
- Move duplicate/stale/template-only docs to `_archive/` only when the operator
  authorizes migration.
- Do not silently delete historical docs.
- Record every merge/archive decision in an epic-local sync note.

## Phase 3: Fill Product-Grade Docs

Every canonical note must include real, code-derived content:

- `## Jira Story`
- `## Priority`
- PM/user value or engineering responsibility
- concrete code paths in backticks
- `## Relationship Map`
- Mermaid diagram
- verification evidence
- risks/tradeoffs
- `## Work Log`
- `## Change Log`

Every epic must also have `issues.md` with:

- QA Issue Register
- detection method
- open issues
- relationship map
- Mermaid diagram
- Work Log

No file may remain only as a template. The agent must replace placeholder prose
with concrete details from code, docs, tests, or explicit assumptions.

## Phase 4: Relationship Labels

Every related feature/module/page/task/docs edge must use one label:

- `DEPENDS_ON`: source cannot work without target.
- `BLOCKS`: source must be resolved before target can proceed.
- `ENABLES`: source unlocks target capability.
- `IMPLEMENTS`: source realizes a requirement or epic outcome.
- `USES`: source consumes target behavior/data.
- `EXTENDS`: source adds behavior on top of target.
- `CONFLICTS_WITH`: source may break or overlap target.
- `SUPERSEDES`: source replaces an older behavior or decision.
- `DUPLICATES`: source repeats target and should be merged/archived.
- `RELATES_TO`: non-blocking contextual relationship.

## Phase 5: Global Docs Sync

Patch the legacy planning package based on code reality:

```text
docs/prd.md
docs/tasks.md
docs/knowledge.md
docs/decisions.md
docs/memory.md
docs/planning/flows.md
docs/planning/screens.md
docs/planning/diagrams.md
```

Use append or targeted patch. Do not replace whole PM docs unless explicitly
requested.

Create sync notes:

```bash
python3 .agents/scripts/create_doc_sync_note.py --name "Doc Reconcile <scope>" --epic-id "E-001-description" --changed-files "<changed-doc-files>"
```

## Phase 6: Gates

Run:

```bash
python3 .agents/scripts/validate_development_docs.py --strict-counts
python3 .agents/scripts/validate_doc_sync.py --strict
```

If validation fails, continue reconciling docs until the failures are either
fixed or explicitly documented as operator-accepted risk.

No downstream `/develop`, `/quick_fix`, frontend, backend, QA, refactor, or
architecture skill may treat this failure as non-blocking for behavior-changing
work unless the operator explicitly accepts the risk.

## Output

The final response must include:

- audit file path,
- epics reconciled,
- files migrated/archived,
- issues found by QA,
- global docs updated,
- validation commands and results,
- residual risks.
