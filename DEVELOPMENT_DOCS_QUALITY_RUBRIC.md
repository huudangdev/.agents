# Development Docs Quality Rubric

This rubric applies to `/docs/development/**` and `/docs/development/sync/**`.
It exists to prevent template-only output during `/develop`.

## Core Rule

Development documentation is accepted only when it explains:

- what changed,
- why it changed,
- where it changed,
- how it was verified,
- what PM-visible impact exists,
- what risk or tradeoff remains.
- how the feature/module/page/task behaves using a Mermaid diagram.

Files that only restate headings, copy templates, or contain generic bullets are
not valid development documentation.

## V31 Topology Rule

New development ledgers are epic-first. The source of truth is:

```text
docs/development/E-001-short-description/
  epic.md
  issues.md
  features/F-001-001-short-description.md
  modules/M-001-001-short-description.md
  pages/P-001-001-short-description.md
  tasks/T-001-001-001-short-description.md
  sync/
```

Flat buckets are legacy compatibility only. When `development_manifest.json`
sets `topology: epic_first`, files under root `epics/`, `modules/`,
`features/`, `pages/`, or `tasks/` are invalid unless moved into `_archive/`.

Every child note must include `parent_epic` and the frontmatter `id` must match
the filename stem exactly. `epic.md` must use the containing directory name as
its `id`; `issues.md` must use `ISSUES-<epic-id>`. Placeholder IDs such as
`feature-000` are invalid.

## Docs Before Code

Before any material source edit, the active agent must update or confirm the
relevant development docs first:

- read the owning epic, related features, related modules/pages/tasks, and
  current sync notes;
- update the affected note's `Work Log` with the planned action and expected
  trace;
- review `Relationship Map` entries so dependent, blocking, duplicate, or
  superseded features are visible before code changes;
- record the pre-code docs evidence in the next sync note under
  `## Docs Before Code`.

## Quality Gates

### 1. No Template Residue

Invalid content includes:

- `TBD`
- `pending`
- `<Name>` or other angle-bracket placeholders
- unchecked checklist items
- empty bullets such as `Reason:` with no value
- phrases like `Describe the`, `State the`, or `no change needed / updated because ...`
- placeholder IDs such as `epic-000`, `feature-000`, `module-000`, `page-000`, or `task-000`
- duplicate or malformed names such as `epic-epic-*`, `feature-epic-*`, `E05-*`, or `E-05-*`

### 2. Concrete Source Trace

Every module, feature, page, task, and sync note must name concrete source files
in backticks, for example:

```text
`src/features/checkout/CheckoutForm.tsx`
```

### 3. PM-Readable Commentary

Each note must include narrative commentary that a PM can use for POC tracking.
At minimum, it must include rationale and impact language such as:

- because
- decision
- tradeoff
- impact
- evidence
- risk

### 4. Evidence Before Closure

Verification sections must include actual commands, observed results, screenshots
or manual checks, and residual risk. A note with `pending` verification is draft
state and cannot close a `/develop` slice.

### 5. Mermaid Before Closure

Every epic, module, feature, page, and task note must include a `mermaid` code
fence. Diagrams are not decoration; they must explain behavior, state,
sequence, dependency, data flow, or handoff.

Recommended diagrams:

- Epic: `flowchart` from PM outcome to feature/module/evidence.
- Feature: `sequenceDiagram` or `flowchart` showing user-triggered behavior.
- Module: `flowchart`, `classDiagram`, `erDiagram`, or `sequenceDiagram`.
- Page: `stateDiagram-v2` showing loading/empty/error/success/permission states.
- Task: `flowchart` or `sequenceDiagram` showing edit/test/docs/handoff.

### 6. Global Docs Are Mandatory

When source behavior changes, at least one legacy planning document must be
updated in the same code slice:

- `docs/prd.md`
- `docs/tasks.md`
- `docs/knowledge.md`
- `docs/decisions.md`
- `docs/memory.md`
- `docs/planning/flows.md`
- `docs/planning/screens.md`
- `docs/planning/diagrams.md`

The sync note must include at least one `updated because` decision for a global
doc. This prevents feature docs from drifting away from the PM-facing package.

### 7. Append or Targeted Patch

When code changes require doc updates:

- append new facts,
- target-patch changed facts,
- preserve older decisions by adding superseding notes,
- document intentionally unchanged docs with a reason.

Do not replace whole PM documents unless the operator explicitly requests a
rewrite.

### 8. Manifest Reconciliation

The manifest and index must agree with the filesystem. When an agent creates,
renames, archives, or moves a development note, it must update:

- `docs/development/development_manifest.json`
- `docs/development/index.md`
- the affected epic-local `sync/*.md` note

The manifest must not claim `complete` while any canonical child note is still
draft, missing Mermaid, missing verification, or carrying placeholder text.

### 9. Jira Product Governance

Every epic, module, feature, page, and task note must include:

- `## Jira Story`
- `## Priority`
- a Story/User Story statement in Jira style;
- a product priority such as `P0`, `P1`, `P2`, `P3`, `P4`, or
  Critical/High/Medium/Low.

Story and Priority are not labels for decoration. They must explain the user,
business, research, or delivery reason for the work and the consequence of not
shipping it.

### 10. Relationship Labels

Every note must include `## Relationship Map` with explicit relationship labels:

- `DEPENDS_ON`
- `BLOCKS`
- `ENABLES`
- `IMPLEMENTS`
- `USES`
- `EXTENDS`
- `CONFLICTS_WITH`
- `SUPERSEDES`
- `DUPLICATES`
- `RELATES_TO`

The map must be used before code begins so the agent understands how this
feature interacts with sibling features, modules, pages, tasks, and docs.

### 11. Epic Issues

Every epic must have `## Issues`. Issues should be detected from QA review,
validation failures, user feedback, risk review, or research contradictions.
Each issue needs source, priority, status, owner, evidence, and resolution.
Do not close an epic while P0/P1 issues remain unresolved or explicitly accepted
by the operator.

## Minimum Depth

Strict validation enforces approximate minimum body depth:

| Artifact | Minimum Words |
| --- | ---: |
| Epic | 180 |
| Module | 220 |
| Feature | 220 |
| Page | 180 |
| Task | 160 |
| Sync note | 180 |

## Reviewer Checklist

- [ ] Does the note explain PM-visible value or impact?
- [ ] Does it name exact code paths?
- [ ] Does it include a useful Mermaid diagram?
- [ ] Does the file path obey the V31 canonical ID and parent-child topology?
- [ ] Does the frontmatter `id` match the filename or epic directory exactly?
- [ ] Does it include rationale, tradeoff, evidence, and risk?
- [ ] Does it update or explicitly review relevant legacy planning docs?
- [ ] Does it update or explicitly review relevant development ledger docs?
- [ ] Does it include Jira Story and Priority?
- [ ] Does it include labeled relationships to related features/modules/pages/tasks?
- [ ] Does the epic include an Issues table generated or reviewed by QA?
- [ ] Does the Work Log prove docs were updated or reviewed before code?
- [ ] Would a new agent understand what changed without rereading the entire diff?
