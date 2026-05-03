# Task Breakdown: Epic-First Development Ledger

> Feature ID: `009-epic-first-development-ledger`
> Plan: `plan.md`

## Task Rules

- `[P]` means parallel-safe with disjoint write scope.
- Every task needs one owner and one verification method.
- Do not mark a task complete until `verification.md` has evidence.
- Every task must name its write scope, docs targets, and sync expectation explicitly.
- If a task changes the public slash-command surface or runtime behavior, it must update the matching docs and verification evidence in the same slice.

## Tasks

- [x] `T001` Owner: `marcus-ai-orchestrator` Write Scope: update `create_development_docs.py` for V31 scaffold. Verification: scaffold creates `E-001-*` tree. Docs: `plan.md`, `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T002` Owner: `ada-qa-agent` Write Scope: update `validate_development_docs.py` for topology, ID, parent, orphan, and placeholder gates. Verification: negative smoke fails malformed ledger. Docs: `plan.md`, `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T003` Owner: `knowledge-work-architecture` Write Scope: update templates, manifest, index, and rubric. Verification: templates describe V31. Docs: `plan.md`, `data-model.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T004` Owner: `marcus-ai-orchestrator` Write Scope: update `/develop`, `.clinerules`, README, USAGE, release notes. Verification: future agents can discover V31 rules. Docs: `tasks.md`, `agent-routing.md`, `verification.md`. Sync: If command sequencing or gates change, patch the command-surface docs and the agent-routing contract before closing the slice.
- [x] `T005` Owner: `development-ledger-architect` Write Scope: add dedicated skill. Verification: skill exists and states canonical topology. Docs: `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T006` Owner: `ada-qa-agent` Write Scope: final validation evidence. Verification: `verification.md` contains command results. Docs: `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T007` Owner: `sophia-product-manager` Write Scope: enforce product-grade Story/Priority/Issues/Relationship/Work Log/docs-before-code rules. Verification: validators and templates include required sections and sync notes require docs-before-code evidence. Docs: `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.

## Parallel Groups

- Group B: `T001`, `T002`, `T003`, `T004`, `T005`, `T006`, `T007` close the loop after the implementation artifacts and validation evidence exist.

## Execution Monitoring

- Required pre-code gates: `validate_specs.py`, `build_execution_brief.py`, `validate_execution_brief_freshness.py`, and `validate_execution_readiness.py` for the active feature.
- Mid-slice checkpoints: keep `verification.md`, `quickstart.md`, and `agent-routing.md` synchronized with any scope or replay-path change.
- Circuit breaker after repeated failure: after three repeated failures of the same command or validator without new evidence, stop coding and repair the contract, routing, or implementation assumption that is actually failing.
- Human escalation trigger: if review findings show the feature now depends on an unrelated repo area or undocumented product behavior, route back to planning/reconciliation before more edits.

## Review Loop Tasks

- `R1`: Challenge the slice boundary, hidden dependencies, and whether the current quickstart is replayable without improvisation.
- `R2`: Confirm the execution brief names the right docs-to-read set for the active task shape and does not widen context without evidence.
- `R3`: Verify the final evidence and release recommendation match the real commands and residual risk.

## Completion Checklist

- [x] `spec.md` accepted
- [x] `plan.md` accepted
- [x] `contracts/` complete or explicitly not applicable
- [x] `tasks.md` complete
- [x] `verification.md` contains evidence
- [x] Root `agents.md` updated or explicitly scheduled for update in verification notes
- [x] TrustGraph write attempted or intentionally deferred with reason
