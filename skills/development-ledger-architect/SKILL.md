---
name: development-ledger-architect
description: Use when creating, validating, auditing, or migrating /docs/development ledgers; enforces V31 epic-first topology, canonical IDs, parent-child documentation, Mermaid diagrams, and global docs synchronization.
---

# Development Ledger Architect

## Mission

Enforce Marcus Fleet V31 development documentation as a durable PM and agent
memory graph. Code-phase docs must be specific, visual, traceable, and organized
under the owning epic.

This skill is also the hard routing authority for brownfield doc readiness. If
the project has missing planning docs, stale or template-only `docs/development`
artifacts, or code reality that is not captured in `/docs`, this skill must
route to `/doc_reconcile` and must not allow material implementation to proceed
until reconciliation passes validation or the operator explicitly accepts risk.

## V31 Source Of Truth

New development ledgers must use this topology:

```text
docs/development/
  development_manifest.json
  index.md
  E-001-short-description/
    epic.md
    issues.md
    features/F-001-001-short-description.md
    modules/M-001-001-short-description.md
    pages/P-001-001-short-description.md
    tasks/T-001-001-001-short-description.md
    sync/
  sync/
  _archive/
```

Flat buckets (`epics/`, `modules/`, `features/`, `pages/`, `tasks/`) are legacy
compatibility only. Do not create new flat bucket docs unless the operator
explicitly requests legacy mode or the existing manifest is legacy-flat.

## Canonical IDs

- Epic: `E-001-description`
- Feature: `F-001-001-description`
- Module: `M-001-001-description`
- Page: `P-001-001-description`
- Task: `T-001-001-001-description`

Rules:

- Filename stem must equal frontmatter `id`.
- `epic.md` frontmatter `id` must equal the containing epic directory name.
- Child files must include `parent_epic` matching the containing epic directory.
- Every epic must include `issues.md` with `id: ISSUES-<epic-id>`.
- Never emit `*-000`, `<Name>`, `pending`, `TBD`, `epic-epic-*`,
  `feature-epic-*`, or duplicate variants such as `E05` and `E-05`.

## Required Workflow

1. Read `docs/development/development_manifest.json` and `docs/development/index.md`
   before changing docs.
2. If no ledger exists, scaffold V31:

```bash
python3 .agents/scripts/create_development_docs.py --name "<name>" --epic-number 001 --child-number 001 --task-number 001
```

3. Before source code edits, update or confirm the affected docs first:
   - owning epic,
   - related feature/module/page/task notes,
   - relationship maps,
   - work log,
   - QA issue table.
4. Put new notes under the correct `E-###-*` parent.
5. Update the affected epic's `epic.md`, feature/module/page/task note, and
   sync note. Update global `/docs` files when source behavior changes.
6. Reconcile `development_manifest.json` and `index.md` whenever a doc is added,
   renamed, moved, archived, or marked complete.
7. Run:

```bash
python3 .agents/scripts/validate_development_docs.py --strict-counts
python3 .agents/scripts/validate_doc_sync.py --strict
```

## Brownfield Reconciliation

Use `/doc_reconcile` when an in-progress project already has code and stale or
noncompliant docs. Before restructuring docs, run:

```bash
python3 .agents/scripts/audit_development_docs.py --root .
```

Then reconcile from code reality:

- map source clusters to epics/features/modules/pages/tasks;
- create or update `issues.md` in every epic;
- label cross-feature relationships;
- migrate flat/duplicate docs only with archive-safe decisions;
- update global planning docs;
- validate before resuming `/develop`.

Treat the following as mandatory brownfield reconcile triggers:

- required planning docs missing;
- boilerplate `README.md` is the only product documentation;
- `docs/development/` missing;
- `docs/development/` exists but is shallow, stale, flat, duplicate-heavy, or
  validator-noncompliant;
- behavior-changing work is requested on code that lacks an epic-first PM
  narrative.

When any trigger is present, this skill must explicitly stop implementation and
send the workflow through `/doc_reconcile` first.

## Documentation Quality

Every epic, feature, module, page, and task note must include:

- Jira Story and Priority.
- Labeled relationship map to related features, modules, pages, tasks, and docs.
- PM-visible purpose and impact.
- Concrete code paths in backticks.
- Rationale, tradeoff, evidence, and risk.
- Verification commands and observed result.
- Mermaid diagram explaining behavior, state, dependency, data flow, or handoff.
- Work Log proving docs were reviewed or updated before code.
- Change log with what changed in code and docs.

Relationship labels:

- `DEPENDS_ON`
- `BLOCKS`
- `ENABLES`
- `IMPLEMENTS`
- `USES`
- `EXTENDS`
- `CONFLICTS_WITH`
- `SUPERSEDES`
- `DUPLICATES`
- `RELATES_TO`

Every epic must include an `Issues` table. Use QA skill reasoning to detect
missing validation, blockers, regressions, stale docs, UX defects, and research
contradictions. Each issue needs source, priority, status, owner, evidence, and
resolution.

## Migration Policy

When migrating legacy flat docs:

- Do not delete historical docs silently.
- Move duplicate, stale, or template-only docs to `_archive/` only when the
  operator approves migration.
- Preserve useful content by targeted merge into canonical epic-first files.
- Record every archive or merge decision in an epic-local sync note.
