# Implementation Plan: Develop Knowledge Ledger

> Feature ID: `005-develop-knowledge-ledger`
> Spec: `spec.md`
> Constitution: `.agents/memory/constitution.md`

## 1. Technical Summary

Add an implementation-memory layer to `/develop`. The workflow will require a
`/docs/development/` ledger with bucketed Markdown notes, a manifest, scaffold
templates, and a validator. This uses the existing Marcus spec/template/script
style introduced in V30 and extends it into code phase.

## 2. Constitution Gates

- [x] Specification has no unresolved `[NEEDS CLARIFICATION]` markers, or the
      operator accepted the residual risk.
- [x] Contracts are defined before implementation.
- [x] Verification method is named before implementation.
- [x] No shell `eval` or unbounded command execution is introduced.
- [x] No hardcoded production secret is introduced.
- [x] TypeScript changes avoid `any` unless justified in Complexity Tracking.
- [x] Rollback path is documented for user-facing or operational changes.

## 3. Architecture

### 3.1 Current State

- Existing modules: `/develop` workflow, templates, scripts, usage guide,
  README, CI template, `.clinerules`.
- Current coupling: `/develop` depends on approved `/docs` and optional specs,
  but has no required fine-grained output artifacts for implementation memory.
- Known constraints: legacy planning outputs must remain unchanged.

### 3.2 Target State

- New or changed modules: development templates, scaffold script, validator,
  `/develop` workflow, documentation and CI references.
- Data flow: planning/spec artifacts -> development scaffold -> bucketed notes
  -> code/test execution -> validator -> final report and TrustGraph write.
- Operational flow: initialize docs before code edits, update notes during
  implementation, validate before completion.

### 3.3 Mermaid Diagram

```mermaid
flowchart TD
    Planning[Approved /docs + optional spec] --> Scaffold[create_development_docs.py]
    Scaffold --> Ledger[/docs/development]
    Ledger --> Code[Code edits by owner skills]
    Code --> Evidence[Tests + execution logs]
    Evidence --> Notes[Update bucket notes]
    Notes --> Validate[validate_development_docs.py]
    Validate --> Handoff[Final report + TrustGraph]
```

## 4. Contracts

| Contract | Purpose | Producer | Consumer |
| --- | --- | --- | --- |
| `development-docs-contract.md` | Feature-specific contract consumed by the current slash-command surface. | feature owner | `/develop`, `/quick_fix`, and reviewers |

## 5. Data Model

Entities are `DevelopmentManifest`, `DevelopmentBucket`, and
`DevelopmentArtifact`. See `data-model.md`.

## 6. Agent Routing

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| Workflow contract | `marcus-ai-orchestrator` | `/develop` update | `validate_specs.py` |
| Knowledge ontology | `knowledge-work-architecture` | templates and bucket rules | development validator |
| QA gate | `ada-qa-agent` | validator and CI rule | positive/negative validation |

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: python3 .agents/scripts/validate_specs.py --feature .agents/specs/005-develop-knowledge-ledger; python3 .agents/scripts/validate_development_docs.py --strict-counts.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.

Execution monitoring:

- Blocking gates before implementation: spec validation, execution-brief rebuild, and readiness validation must all pass.
- Evidence checkpoints during implementation: python3 .agents/scripts/validate_specs.py --feature .agents/specs/005-develop-knowledge-ledger; python3 .agents/scripts/validate_development_docs.py --strict-counts.
- Escalation condition after repeated failure: if the same validator or verification command fails three times without new evidence, stop widening scope and repair the package or code path that actually failed.

## 7. Migration and Rollback

add docs contract and validator; future projects opt in when
  `/develop` runs and creates `/docs/development/`.
 remove the V30.2 docs gate and templates if it blocks a
  workflow unexpectedly; source code generation remains unaffected.
 page notes can be optional for non-UI tasks through
  manifest minimum counts.

## 8. Complexity Tracking

| Decision | Reason | Alternative Rejected | Review Needed |
| --- | --- | --- | --- |
| Upgrade `005-develop-knowledge-ledger` in place instead of replacing it wholesale | Preserves existing evidence and reduces migration risk | Rewriting the entire feature package from scratch | Medium |

## 9. POC Slice and Review Cadence

- POC slice boundary: prove `005-develop-knowledge-ledger` end-to-end using the smallest professional slice that exercises the main contract and verification path.
- Success evidence for the slice: python3 .agents/scripts/validate_specs.py --feature .agents/specs/005-develop-knowledge-ledger; python3 .agents/scripts/validate_development_docs.py --strict-counts plus updated review-loop and release-recommendation artifacts.
- What remains intentionally unproven after the slice: broader product rollout, unrelated modules, and any live services the current feature explicitly left as residual risk.
- Review cadence:
  - Draft architecture review: after the package is reconciled to the current contract.
  - Challenge review: after tasks, routing, and quickstart replay are concrete.
  - Final readiness review: after verification evidence and release recommendation are updated.
- Stop conditions: readiness fails, review findings expose hidden scope growth, or the replay steps cannot be followed from docs alone.
- Proceed conditions: spec validation passes, execution-brief freshness passes, readiness passes, and the verification package names a clear release recommendation.
