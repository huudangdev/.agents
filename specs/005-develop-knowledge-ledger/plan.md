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

List files under `contracts/` and summarize each contract.

| Contract | Purpose | Producer | Consumer |
| --- | --- | --- | --- |
| `contracts/development-docs-contract.md` | Defines manifest, bucket, metadata, and validation contract | `/develop` | validators and future agents |

## 5. Data Model

Entities are `DevelopmentManifest`, `DevelopmentBucket`, and
`DevelopmentArtifact`. See `data-model.md`.

## 6. Agent Routing

Summarize ownership from `agent-routing.md`.

| Workstream | Primary Agent | Output | Verification |
| --- | --- | --- | --- |
| Workflow contract | `marcus-ai-orchestrator` | `/develop` update | `validate_specs.py` |
| Knowledge ontology | `knowledge-work-architecture` | templates and bucket rules | development validator |
| QA gate | `ada-qa-agent` | validator and CI rule | positive/negative validation |

## 7. Migration and Rollback

- Migration steps: add docs contract and validator; future projects opt in when
  `/develop` runs and creates `/docs/development/`.
- Rollback steps: remove the V30.1 docs gate and templates if it blocks a
  workflow unexpectedly; source code generation remains unaffected.
- Compatibility notes: page notes can be optional for non-UI tasks through
  manifest minimum counts.

## 8. Complexity Tracking

Use this section only when a constitution gate fails or a new abstraction is
introduced.

| Decision | Reason | Alternative Rejected | Review Needed |
| --- | --- | --- | --- |
| TBD | TBD | TBD | TBD |
