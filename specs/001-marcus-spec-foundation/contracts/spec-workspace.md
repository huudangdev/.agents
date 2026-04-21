# Contract: Marcus Feature Workspace

## Required Directory Shape

```text
.agents/specs/<feature-id>/
  README.md
  spec.md
  plan.md
  tasks.md
  verification.md
  agent-routing.md
  research.md
  data-model.md
  quickstart.md
  contracts/
  implementation-details/
```

## Feature ID

The feature id must match:

```text
NNN-lowercase-kebab-slug
```

Examples:

- `001-marcus-spec-foundation`
- `002-viewer-type-safety`

## Validation Rules

- Required files must exist and contain text.
- `spec.md` must include Purpose, User Stories, Functional Requirements, and
  Acceptance Criteria sections.
- `[NEEDS CLARIFICATION: ...]` markers fail validation unless draft mode is
  explicitly allowed.
- `plan.md` must include Constitution Gates.
- `tasks.md` must include `Owner:` and `Verification:` markers.

## Backward Compatibility

This contract does not remove legacy `/docs` flows. During migration, legacy
global docs may coexist with feature-scoped specs.
