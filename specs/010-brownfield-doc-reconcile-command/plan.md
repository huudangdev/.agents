# Implementation Plan: Brownfield Doc Reconcile Command

> Feature ID: `010-brownfield-doc-reconcile-command`

## 1. Scope

Add a slash workflow and supporting audit/validation assets for code-derived
documentation reconciliation.

## 2. Constitution Gates

- Context before construction: full code/docs inventory before doc mutation.
- Evidence before completion: audit artifact and validators.
- Human-visible handoff: PM receives reconciled epics, issues, relationships,
  updated global docs, and residual risks.

## 3. Implementation Plan

1. Add `/doc_reconcile` workflow.
2. Add `audit_development_docs.py`.
3. Add `development-issues-template.md`.
4. Update V31 scaffold/validator to require `issues.md`.
5. Update README, USAGE, release notes, `.clinerules`, and `/develop`.
6. Validate scripts/specs and smoke audit/scaffold behavior.

## 4. Compatibility

The command is additive. It does not replace `/develop`; it prepares stale
brownfield docs so `/develop` can safely continue.
