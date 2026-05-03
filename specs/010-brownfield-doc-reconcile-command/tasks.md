# Task Breakdown: Brownfield Doc Reconcile Command

> Feature ID: `010-brownfield-doc-reconcile-command`
> Plan: `plan.md`

## Task Rules

- `[P]` means parallel-safe with disjoint write scope.
- Every task needs one owner and one verification method.
- Do not mark a task complete until `verification.md` has evidence.
- Every task must name its write scope, docs targets, and sync expectation explicitly.
- If a task changes the public slash-command surface or runtime behavior, it must update the matching docs and verification evidence in the same slice.

## Tasks

- [x] `T001` Owner: `marcus-ai-orchestrator` Write Scope: add `/doc_reconcile` workflow. Verification: workflow file exists. Docs: `tasks.md`, `agent-routing.md`, `verification.md`. Sync: If command sequencing or gates change, patch the command-surface docs and the agent-routing contract before closing the slice.
- [x] `T002` Owner: `development-ledger-architect` Write Scope: add code/docs audit script. Verification: audit smoke creates markdown report. Docs: `plan.md`, `tasks.md`, `verification.md`. Sync: If validator behavior or required artifacts change, update the quickstart, review loop, and verification evidence in the same slice.
- [x] `T003` Owner: `ada-qa-agent` Write Scope: add `issues.md` template and V31 validator requirement. Verification: scaffold includes issues and negative smoke rejects missing issues. Docs: `plan.md`, `tasks.md`, `verification.md`. Sync: If validator behavior or required artifacts change, update the quickstart, review loop, and verification evidence in the same slice.
- [x] `T004` Owner: `knowledge-work-architecture` Write Scope: update README, USAGE, `.clinerules`, release notes, and `/develop`. Verification: docs mention command and issue-file policy. Docs: `tasks.md`, `agent-routing.md`, `verification.md`. Sync: If command sequencing or gates change, patch the command-surface docs and the agent-routing contract before closing the slice.
- [x] `T005` Owner: `ada-qa-agent` Write Scope: final validation evidence. Verification: `verification.md` contains command results. Docs: `tasks.md`, `verification.md`. Sync: If scope, evidence, or release posture changes, patch the feature package and verification summary in the same slice.

## Parallel Groups

- Group B: `T001`, `T002`, `T003`, `T004`, `T005` close the loop after the implementation artifacts and validation evidence exist.

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
