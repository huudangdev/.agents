---
description: Verify implementation evidence against a Marcus Fleet feature spec.
---

# Marcus Verify Workflow

Use this workflow before closing a feature.

## Required Actions

1. Read `spec.md`, `plan.md`, `tasks.md`, and `verification.md`.
2. Confirm every acceptance criterion has evidence.
3. Confirm every completed task has command output or manual evidence.
4. Confirm `agents.md` was updated.
5. If implementation touched source code, confirm `/docs/development/` exists
   and the changed code paths are represented in epic/module/feature/page/task
   notes.
6. If source files changed during `/develop` or `/quick_fix`, confirm
   `/docs/development/sync/*.md` records the code slice and the append/targeted
   patch decisions for PM docs.
7. Attempt a TrustGraph write.
8. Run:
   ```bash
   python3 .agents/scripts/validate_specs.py --feature .agents/specs/<feature-id>
   python3 .agents/scripts/validate_development_docs.py --strict-counts
   python3 .agents/scripts/validate_doc_sync.py --strict
   ```
   Run the development/doc-sync validators only when `docs/development/` exists.

## Output

- Updated `verification.md`
- Closeout summary
- Residual risk list
- Documentation sync summary
