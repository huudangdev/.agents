# Implementation Plan: Brownfield Doc Reconcile Command

> Feature ID: `010-brownfield-doc-reconcile-command`
> Spec: `spec.md`
> Constitution: `.agents/memory/constitution.md`

## 1. Technical Summary

Add `/doc_reconcile`, a brownfield documentation recovery command for projects
whose implementation has moved faster than their docs. The command must review
the whole codebase, map code to product docs, migrate or enrich
`/docs/development` to V31.1, and update global planning docs.

## 2. Constitution Gates

- Context before construction: full code/docs inventory before doc mutation.
- Evidence before completion: audit artifact and validators.
- Human-visible handoff: PM receives reconciled epics, issues, relationships,
  updated global docs, and residual risks.

## 3. Architecture

### 3.1 Current State

- Existing feature scope: `010-brownfield-doc-reconcile-command` already captures the requirement intent, but the package still uses the older Marcus contract.
- Current coupling: downstream workflows can only consume this feature safely after review-loop, readiness, and execution-brief sections exist.
- Known constraints: preserve the already-implemented code and evidence while upgrading the docs package around it.

### 3.2 Target State

- Upgrade `010-brownfield-doc-reconcile-command` to the current Marcus contract without discarding the implemented behavior.
- Keep the feature-specific contracts, data model, and evidence, but add review cadence, execution monitoring, and replayable quickstart guidance.
- Ensure `/develop` and `/quick_fix` can consume the package through `execution-brief.md` rather than re-reading the whole repo.

### 3.3 Mermaid Diagram

```mermaid
flowchart TD
    Spec[spec.md] --> Plan[plan.md]
    Plan --> Tasks[tasks.md]
    Tasks --> Brief[execution-brief.md]
    Brief --> Work[/develop or /quick_fix]
    Work --> Verify[verification.md]
```

## 4. Contracts

| Contract | Purpose | Producer | Consumer |
| --- | --- | --- | --- |
| `doc-reconcile-contract.md` | Feature-specific contract consumed by the current slash-command surface. | feature owner | `/develop`, `/quick_fix`, and reviewers |

## 5. Data Model

# Data Model: Brownfield Doc Reconcile Command

## 6. Agent Routing

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| Planning and contract reconciliation | `marcus-ai-orchestrator` | current-contract feature package | spec/readiness validation |
| QA and release gate | `ada-qa-agent` | verification evidence and release recommendation | validator output |

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: python3 .agents/scripts/validate_specs.py --feature .agents/specs/010-brownfield-doc-reconcile-command; python3 .agents/scripts/audit_development_docs.py --root ..
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: python3 .agents/scripts/validate_specs.py --feature .agents/specs/010-brownfield-doc-reconcile-command; python3 .agents/scripts/audit_development_docs.py --root ..
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.

## 7. Migration and Rollback

1. Reconcile the feature package to the current contract.
  2. Rebuild `execution-brief.md` for the active task shape.
  3. Re-run spec and readiness validation before downstream execution.

  1. Restore the previous `010-brownfield-doc-reconcile-command` docs package if the contract upgrade proves misleading.
  2. Revert only the additive governance sections; do not silently discard verified implementation evidence.
 preserve the implemented behavior and existing contracts while making the feature package consumable by the current slash-command surface.

## 8. Complexity Tracking

| Decision | Reason | Alternative Rejected | Review Needed |
| --- | --- | --- | --- |
| Upgrade `010-brownfield-doc-reconcile-command` in place instead of replacing it wholesale | Preserves existing evidence and reduces migration risk | Rewriting the entire feature package from scratch | Medium |

## 9. POC Slice and Review Cadence

- POC slice boundary: prove `010-brownfield-doc-reconcile-command` end-to-end using the smallest professional slice that exercises the main contract and verification path.
- Success evidence for the slice: python3 .agents/scripts/validate_specs.py --feature .agents/specs/010-brownfield-doc-reconcile-command; python3 .agents/scripts/audit_development_docs.py --root . plus updated review-loop and release-recommendation artifacts.
- What remains intentionally unproven after the slice: broader product rollout, unrelated modules, and any live services the current feature explicitly left as residual risk.
- Review cadence:
  - Draft architecture review: after the package is reconciled to the current contract.
  - Challenge review: after tasks, routing, and quickstart replay are concrete.
  - Final readiness review: after verification evidence and release recommendation are updated.
- Stop conditions: readiness fails, review findings expose hidden scope growth, or the replay steps cannot be followed from docs alone.
- Proceed conditions: spec validation passes, execution-brief freshness passes, readiness passes, and the verification package names a clear release recommendation.
