# Implementation Plan: Epic-First Development Ledger

> Feature ID: `009-epic-first-development-ledger`
> Spec: `spec.md`
> Constitution: `.agents/memory/constitution.md`

## 1. Technical Summary

Upgrade Marcus Fleet development documentation from flat buckets into a
hierarchical PM-grade knowledge graph. The new ledger must make every epic the
parent container for its features, modules, pages, tasks, and sync notes while
keeping existing V30 flat ledgers readable.

## 2. Constitution Gates

- Human-visible handoff: PM can inspect one epic directory and see all children.
- Evidence before completion: validation and smoke tests must prove V31 gates.
- Context before construction: workflow requires reading planning docs, manifest,
  index, and relevant epic docs before code edits.
- Backward compatibility: existing V30 flat manifests cannot be forced into V31
  unless the operator requests migration.

## 3. Architecture

### 3.1 Current State

- Existing feature scope: `009-epic-first-development-ledger` already captures the requirement intent, but the package still uses the older Marcus contract.
- Current coupling: downstream workflows can only consume this feature safely after review-loop, readiness, and execution-brief sections exist.
- Known constraints: preserve the already-implemented code and evidence while upgrading the docs package around it.

### 3.2 Target State

- Upgrade `009-epic-first-development-ledger` to the current Marcus contract without discarding the implemented behavior.
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
| `epic-first-ledger-contract.md` | Feature-specific contract consumed by the current slash-command surface. | feature owner | `/develop`, `/quick_fix`, and reviewers |

## 5. Data Model

# Data Model: Epic-First Development Ledger

## 6. Agent Routing

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| Planning and contract reconciliation | `marcus-ai-orchestrator` | current-contract feature package | spec/readiness validation |
| QA and release gate | `ada-qa-agent` | verification evidence and release recommendation | validator output |

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: python3 .agents/scripts/validate_specs.py --feature .agents/specs/009-epic-first-development-ledger; python3 .agents/scripts/validate_development_docs.py --strict-counts.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: python3 .agents/scripts/validate_specs.py --feature .agents/specs/009-epic-first-development-ledger; python3 .agents/scripts/validate_development_docs.py --strict-counts.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.

## 7. Migration and Rollback

1. Reconcile the feature package to the current contract.
  2. Rebuild `execution-brief.md` for the active task shape.
  3. Re-run spec and readiness validation before downstream execution.

  1. Restore the previous `009-epic-first-development-ledger` docs package if the contract upgrade proves misleading.
  2. Revert only the additive governance sections; do not silently discard verified implementation evidence.
 preserve the implemented behavior and existing contracts while making the feature package consumable by the current slash-command surface.

## 8. Complexity Tracking

| Decision | Reason | Alternative Rejected | Review Needed |
| --- | --- | --- | --- |
| Upgrade `009-epic-first-development-ledger` in place instead of replacing it wholesale | Preserves existing evidence and reduces migration risk | Rewriting the entire feature package from scratch | Medium |

## 9. POC Slice and Review Cadence

- POC slice boundary: prove `009-epic-first-development-ledger` end-to-end using the smallest professional slice that exercises the main contract and verification path.
- Success evidence for the slice: python3 .agents/scripts/validate_specs.py --feature .agents/specs/009-epic-first-development-ledger; python3 .agents/scripts/validate_development_docs.py --strict-counts plus updated review-loop and release-recommendation artifacts.
- What remains intentionally unproven after the slice: broader product rollout, unrelated modules, and any live services the current feature explicitly left as residual risk.
- Review cadence:
  - Draft architecture review: after the package is reconciled to the current contract.
  - Challenge review: after tasks, routing, and quickstart replay are concrete.
  - Final readiness review: after verification evidence and release recommendation are updated.
- Stop conditions: readiness fails, review findings expose hidden scope growth, or the replay steps cannot be followed from docs alone.
- Proceed conditions: spec validation passes, execution-brief freshness passes, readiness passes, and the verification package names a clear release recommendation.
