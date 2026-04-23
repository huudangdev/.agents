# Implementation Plan: Epic-First Development Ledger

> Feature ID: `009-epic-first-development-ledger`

## 1. Scope

Upgrade `.agents` so future `/develop` runs create and validate epic-first
development docs while preserving legacy flat ledgers.

## 2. Constitution Gates

- Human-visible handoff: PM can inspect one epic directory and see all children.
- Evidence before completion: validation and smoke tests must prove V31 gates.
- Context before construction: workflow requires reading planning docs, manifest,
  index, and relevant epic docs before code edits.
- Backward compatibility: existing V30 flat manifests cannot be forced into V31
  unless the operator requests migration.

## 3. Implementation Plan

1. Extend `create_development_docs.py` with topology detection and V31 scaffold.
2. Extend `validate_development_docs.py` with V31 topology, ID, parent, orphan,
   and legacy-flat rejection rules.
3. Extend sync tooling to read/write epic-local sync notes without removing root
   sync compatibility.
4. Update templates, `/develop`, `.clinerules`, README, USAGE, release notes,
   and quality rubric.
5. Add `development-ledger-architect` skill for future routing.
6. Verify with compile, spec validation, scaffold smoke, and negative smoke.

## 4. Compatibility Strategy

- `topology: epic_first` activates V31 strict topology gates.
- Missing or legacy manifests continue through the legacy-flat validator path.
- Legacy bucket config remains present in the manifest template for migration
  reference, but V31 source of truth is `E-###-*`.

## 5. Rollout

V31 is additive. New projects use epic-first by default. Existing projects can
run legacy mode explicitly or migrate in a separate operator-approved pass.
