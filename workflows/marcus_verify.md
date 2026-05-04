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
6. Fail verification when `verification.md` still contains placeholders,
   shallow evidence, or vague claims not tied to requirements.
7. If the project is brownfield and source code changed, fail verification when
   the planning package is missing, only boilerplate docs exist, or the
   development ledger is stale/template-only. The required remediation is
   `/doc_reconcile`, not manual waiver by omission.
8. If source files changed during `/develop` or `/quick_fix`, confirm
   `/docs/development/sync/*.md` records the code slice and the append/targeted
   patch decisions for PM docs.
9. Fill `## Review Rounds` with at least one independent evaluator pass and a
   disposition for each non-trivial finding.
10. Fill `## Release Recommendation` with `GO`, `GO WITH RESIDUAL RISK`, or
    `NO-GO`. A blank recommendation is a failed verification state.
11. Attempt a TrustGraph write.
12. Run:
   ```bash
   python3 .agents/scripts/run_harness_postflight.py --root . --phase execution --feature .agents/specs/<feature-id>
   python3 .agents/scripts/validate_specs.py --feature .agents/specs/<feature-id>
   python3 .agents/scripts/validate_development_docs.py --strict-counts
   python3 .agents/scripts/validate_doc_sync.py --strict
   python3 .agents/scripts/validate_docs_substance.py --root . --include-development
   ```
   Run the development/doc-sync validators only when `docs/development/` exists.
   Inspect `.agents/logs/harness/postflight.jsonl` when you need structured
   closeout evidence for the executed gate chain.

## Output

- Updated `verification.md`
- Closeout summary
- Residual risk list
- Documentation sync summary
