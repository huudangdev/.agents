---
id: module-000
type: module
status: draft
owner_skill: alan-tech-lead
source_trace:
  - docs/planning/diagrams.md
verification:
  - pending
---

# Module: <Name>

> QUALITY BAR: explain the real module boundary, why the chosen structure is
> correct, what contracts it exposes, how failures are detected, and include
> Mermaid. Do not leave placeholders, pending verification, or generic bullets.

## Responsibility

Write 2-4 paragraphs defining module ownership, why this boundary exists, how it
relates to upstream/downstream modules, and what future agents must not violate.

## Implementation Commentary

- Decision:
- Rationale:
- Tradeoff:
- Impact:
- Risk:

## Code Scope

- Owns: `src/example.ts`
- Reads:
- Writes:
- Must not touch:

## Public Contracts

- API:
- Events:
- Data model:

## Dependencies

- Internal:
- External:

## Failure Modes

- Failure:
  - Detection:
  - Recovery:

## Mermaid Diagram

```mermaid
flowchart LR
    Caller[Caller module] --> Boundary[This module boundary]
    Boundary --> Contract[Public contract]
    Contract --> Dependency[Internal/external dependency]
    Dependency --> Failure{Failure mode}
    Failure --> Recovery[Detection and recovery path]
```

## Verification

- Unit:
- Integration:
- Runtime:

## Change Log

- Date:
  - Code change:
  - Documentation update:
  - Evidence:
