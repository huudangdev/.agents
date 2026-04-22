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

## Quality Gates

### 1. No Template Residue

Invalid content includes:

- `TBD`
- `pending`
- `<Name>` or other angle-bracket placeholders
- unchecked checklist items
- empty bullets such as `Reason:` with no value
- phrases like `Describe the`, `State the`, or `no change needed / updated because ...`

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
- [ ] Does it include rationale, tradeoff, evidence, and risk?
- [ ] Does it update or explicitly review relevant legacy planning docs?
- [ ] Does it update or explicitly review relevant development ledger docs?
- [ ] Would a new agent understand what changed without rereading the entire diff?
