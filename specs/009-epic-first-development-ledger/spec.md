# Feature Specification: Epic-First Development Ledger

> Feature ID: `009-epic-first-development-ledger`
> Created: `2026-04-23`
> Status: Draft
> Source Prompt: Standardize `/docs/development` around canonical epic-first parent-child docs, strict IDs, non-empty content, Mermaid, mandatory global docs sync, docs-before-code, Jira Story/Priority, QA issues, and labeled feature relationships without breaking legacy flat ledgers.

## 1. Purpose

Upgrade Marcus Fleet development documentation from flat buckets into a
hierarchical PM-grade knowledge graph. The new ledger must make every epic the
parent container for its features, modules, pages, tasks, and sync notes while
keeping existing V30 flat ledgers readable.

## 2. User Stories

- [x] As a PM, I need development docs grouped by epic so I can inspect a POC
      slice without searching across unrelated folders.
- [x] As an agent, I need canonical IDs that encode type, order, and parent
      context so I do not create duplicates like `epic-epic-*`.
- [x] As an operator, I need legacy flat docs to remain readable until an
      explicit migration archives or merges them.
- [x] As a product team, I need Story, Priority, Issues, Work Log, and labeled
      feature relationships so the docs behave like an international product
      research and delivery system.

## 3. Functional Requirements

- `FR-001`: New development ledgers MUST default to `topology: epic_first`.
- `FR-002`: Canonical IDs MUST follow `E-001-*`, `F-001-001-*`,
  `M-001-001-*`, `P-001-001-*`, and `T-001-001-001-*`.
- `FR-003`: Child notes MUST include `parent_epic` matching their containing
  `E-###-*` directory.
- `FR-004`: Validators MUST reject V31 flat bucket docs, orphan root files,
  malformed filenames, placeholder IDs, and frontmatter IDs that do not match
  filenames.
- `FR-005`: Sync tooling MUST support epic-local sync notes while preserving
  root sync compatibility.
- `FR-006`: Workflows, rules, templates, docs, and skills MUST direct agents to
  the V31 structure.
- `FR-007`: `/develop` MUST update or confirm docs before material source edits.
- `FR-008`: Every epic/module/feature/page/task doc MUST include Jira-style
  Story, Priority, Relationship Map, and Work Log.
- `FR-009`: Every epic MUST include QA-reviewed Issues.
- `FR-010`: Relationship maps MUST use explicit labels such as `DEPENDS_ON`,
  `BLOCKS`, `ENABLES`, `IMPLEMENTS`, `USES`, `EXTENDS`, `CONFLICTS_WITH`,
  `SUPERSEDES`, `DUPLICATES`, and `RELATES_TO`.

## 4. Non-Functional Requirements

- `NFR-001`: Backward compatibility: legacy flat manifests still validate using
  the old bucket model.
- `NFR-002`: PM readability: hierarchy must be visible from `index.md` and
  `development_manifest.json`.
- `NFR-003`: Migration safety: duplicate/stale docs must be archived or merged
  intentionally, not silently deleted.
- `NFR-004`: Product rigor: docs must resemble a deep research product delivery
  ledger, not a template checklist.

## 5. Acceptance Criteria

- `AC-001`: A new scaffold creates an `E-###-*` tree with canonical child files.
- `AC-002`: Strict validation rejects a V31 ledger containing a root flat
  `features/` bucket.
- `AC-003`: Strict validation rejects a child file whose `parent_epic` does not
  match the containing epic.
- `AC-004`: Legacy-flat manifests remain supported by the validator.
- `AC-005`: `/develop`, `.clinerules`, README, USAGE, release notes, and a
  dedicated skill describe V31.
- `AC-006`: Strict validation rejects docs missing Story, Priority, Relationship
  Map labels, Work Log, or epic Issues.
- `AC-007`: Doc sync validation rejects source changes whose sync note lacks
  docs-before-code evidence.

## 6. Clarifications

- No unresolved clarifications. The operator explicitly requested planning
  first, strict structure, and no breakage of currently correct logic.

## 7. Constraints

- Existing V30.4 content gates must remain active.
- Downstream application code is out of scope.
- Project-specific migration of `finviet-nexus` is out of scope until the
  operator approves direct edits there.

## 8. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| V31 breaks older projects | Existing docs fail unexpectedly | Use topology detection; legacy manifests remain flat |
| Agents create pretty hierarchy but empty docs | PM still lacks value | Keep V30.3/V30.4 substantive and Mermaid gates |
| Migration loses history | Prior decisions disappear | Archive/merge policy and sync notes are mandatory |

## 9. Traceability

| Requirement | Plan Section | Tasks | Verification |
| --- | --- | --- | --- |
| `FR-001` | `plan.md#3-implementation-plan` | `T001`, `T003` | scaffold smoke |
| `FR-004` | `plan.md#3-implementation-plan` | `T002` | negative validator smoke |
| `FR-006` | `plan.md#3-implementation-plan` | `T004`, `T005` | spec validation |
| `FR-007` | `plan.md#3-implementation-plan` | `T007` | doc sync negative smoke |
| `FR-008` | `plan.md#3-implementation-plan` | `T007` | development docs negative smoke |
