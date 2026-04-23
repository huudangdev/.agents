# Feature Specification: Brownfield Doc Reconcile Command

> Feature ID: `010-brownfield-doc-reconcile-command`
> Created: `2026-04-23`
> Status: Draft
> Source Prompt: Create a slash command so in-progress projects can review code, reconcile docs to V31.1, fill concrete content, standardize structure/naming, create epic issues, and update global docs from code reality.

## 1. Purpose

Add `/doc_reconcile`, a brownfield documentation recovery command for projects
whose implementation has moved faster than their docs. The command must review
the whole codebase, map code to product docs, migrate or enrich
`/docs/development` to V31.1, and update global planning docs.

## 2. User Stories

- [x] As a PM, I need stale development docs reconciled from actual code so the
      POC package is trustworthy.
- [x] As an agent, I need a deterministic code/docs audit before restructuring
      docs so I do not invent epics or features from stale templates.
- [x] As QA, I need one `issues.md` per epic so blockers, regressions, and risks
      are visible before work continues.

## 3. Functional Requirements

- `FR-001`: Add `/doc_reconcile` workflow.
- `FR-002`: Add a code/docs audit script that emits an audit artifact.
- `FR-003`: V31 epic-first scaffold and validation MUST require `issues.md` per
  epic.
- `FR-004`: `/doc_reconcile` MUST require full code inventory, relationship
  labels, Jira Story/Priority, Mermaid, Work Log, QA issues, and global docs
  sync.
- `FR-005`: The command MUST preserve history and archive/merge duplicates only
  intentionally.

## 4. Non-Functional Requirements

- Backward compatible with existing V31.1 `/develop`.
- No application source code edits unless the operator explicitly asks.
- Useful for brownfield and in-progress projects.

## 5. Acceptance Criteria

- `AC-001`: Workflow file exists and describes `/doc_reconcile`.
- `AC-002`: Audit script creates `docs/development/audits/*-code-docs-audit.md`.
- `AC-003`: New V31 scaffold includes `issues.md`.
- `AC-004`: Validator rejects V31 epic directories without `issues.md`.
- `AC-005`: README, USAGE, `.clinerules`, release notes, and workflow docs
  mention `/doc_reconcile`.

## 6. Clarifications

- No unresolved clarifications.

## 7. Constraints

- Do not edit downstream app code as part of command creation.
- Do not delete legacy docs silently.

## 8. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Agent claims code review without evidence | Docs remain shallow | Audit script creates inventory evidence |
| Migration loses useful history | PM loses prior decisions | Archive/merge decisions must be sync-noted |
| Issues become generic | QA value is low | `issues.md` requires detection method and evidence |

## 9. Traceability

| Requirement | Plan Section | Tasks | Verification |
| --- | --- | --- | --- |
| `FR-001` | `plan.md#3-implementation-plan` | `T001` | workflow file exists |
| `FR-002` | `plan.md#3-implementation-plan` | `T002` | audit smoke |
| `FR-003` | `plan.md#3-implementation-plan` | `T003` | scaffold and negative smoke |
