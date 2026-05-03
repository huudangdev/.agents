# Feature Specification: {{FEATURE_TITLE}}

> Feature ID: `{{FEATURE_ID}}`
> Created: `{{CREATED_DATE}}`
> Status: Draft
> Source Prompt: {{SOURCE_PROMPT}}

## 1. Purpose

Describe the user or operator outcome. Focus on what must be true and why it
matters. Do not specify implementation technology here unless it is a constraint
given by the operator. Include the exact failure or missed opportunity this
feature resolves, and name the observable business or user-facing outcome that
must improve.

## 2. User Stories

- [ ] As a `<role>`, I need `<capability>` so that `<outcome>`.
- [ ] As a `<role>`, I need `<capability>` so that `<outcome>`.
- [ ] As an internal operator, I need `<constraint or auditability>` so that
      execution remains observable and governable.

## 3. Functional Requirements

- `FR-001`: The system MUST ...
- `FR-002`: The system MUST ...
- `FR-003`: The system MUST ...

Requirement writing rules:

- Every requirement must be testable.
- Every requirement must describe observable behavior, not implementation taste.
- Every requirement must name the actor, trigger, and outcome when relevant.

## 4. Non-Functional Requirements

- `NFR-001`: Performance:
- `NFR-002`: Security:
- `NFR-003`: Observability:
- `NFR-004`: Maintainability:
- `NFR-005`: Documentation and traceability:

For any item that is intentionally deferred, say so explicitly and record the
accepted risk instead of leaving the field vague.

## 5. Acceptance Criteria

- `AC-001`: Given ..., when ..., then ...
- `AC-002`: Given ..., when ..., then ...
- `AC-003`: Given ..., when ..., then ...

Acceptance criteria rules:

- Every `FR-*` must map to at least one `AC-*`.
- If a requirement cannot be verified yet, mark it in Clarifications or Risks.
- Do not use generic criteria like "works correctly" or "looks good".

## 6. Clarifications

Record unresolved questions as explicit markers. Planning is blocked while any
marker remains unless the operator accepts the risk.

- [NEEDS CLARIFICATION: What is the exact user-visible success condition?]
- [NEEDS CLARIFICATION: What evidence is mandatory before this feature can be
  considered done?]

## 7. Constraints

- Constitution articles that apply:
- Existing files or modules in scope:
- Files or modules out of scope:
- Compatibility requirements:
- Documentation prerequisites already reviewed:
- Rollback or containment expectations:

Out of scope:

- Explicitly list adjacent requests or tempting follow-up work that this feature
  must not silently absorb.

## 8. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| TBD | TBD | TBD |

## 9. Traceability

| Requirement | Plan Section | Tasks | Verification |
| --- | --- | --- | --- |
| `FR-001` | TBD | TBD | TBD |

## 10. Review Loop

Document the review rounds that must happen before implementation is allowed to
proceed.

| Round | Reviewer | Focus | Exit Criteria | Status |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Scope challenge | unclear scope removed, risks surfaced | Pending |
| `R2` | `sophia-product-manager` | Requirement quality | acceptance criteria complete | Pending |
| `R3` | `marcus-ai-orchestrator` | Go/no-go to planning | spec package is stable enough for `plan.md` | Pending |
