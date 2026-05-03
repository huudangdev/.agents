# Task Breakdown: Substantive Development Docs Quality

> Feature ID: `007-substantive-development-docs-quality`
> Plan: `plan.md`

## Task Rules

- `[P]` means parallel-safe with disjoint write scope.
- Every task needs one owner and one verification method.
- Do not mark a task complete until `verification.md` has evidence.
- Every task must name its write scope, docs targets, and sync expectation explicitly.
- If a task changes the public slash-command surface or runtime behavior, it must update the matching docs and verification evidence in the same slice.

## Tasks

- [x] `T001` Owner: `ada-qa-agent` Write Scope: strengthen `validate_development_docs.py`. Verification: rejects placeholders, shallow notes, missing rationale, and missing code paths. Docs: `plan.md`, `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T002` Owner: `ada-qa-agent` Write Scope: strengthen `validate_doc_sync.py`. Verification: rejects shallow unfinished sync notes. Docs: `plan.md`, `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T003` Owner: `knowledge-work-architecture` Write Scope: add quality rubric and improve templates. Verification: templates include PM notes, commentary, change logs, evidence, and risk prompts. Docs: `plan.md`, `data-model.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.
- [x] `T004` Owner: `marcus-ai-orchestrator` Write Scope: update `/develop`, `.clinerules`, README, USAGE, and release notes. Verification: quality gate is visible to future agents. Docs: `tasks.md`, `agent-routing.md`, `verification.md`. Sync: If command sequencing or gates change, patch the command-surface docs and the agent-routing contract before closing the slice.

## Parallel Groups

- Group B: `T001`, `T002`, `T003`, `T004` close the loop after the implementation artifacts and validation evidence exist.

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
