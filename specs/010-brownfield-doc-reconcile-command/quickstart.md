# Quickstart Validation: Brownfield Doc Reconcile Command

> Feature ID: `010-brownfield-doc-reconcile-command`

## Local Preconditions

- Required services: none beyond the local tools already referenced by this feature's verification commands.
- Required environment variables: inherit the existing project-local environment only; do not introduce new secrets during replay.
- Required commands: `python3`, `python3`, `python3`.
- Use the command on in-progress projects whose docs lag behind code reality.
- Downstream application code remains out of scope unless the operator approves follow-up implementation work.

## Validation Path

1. Rebuild the execution brief for the active task shape:
   ```bash
   python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/010-brownfield-doc-reconcile-command --task-shape architecture-refactor
   ```
2. Run the primary validation commands:
   ```bash
   python3 .agents/scripts/validate_specs.py --feature .agents/specs/010-brownfield-doc-reconcile-command
   python3 .agents/scripts/audit_development_docs.py --root .
   ```
3. Confirm the feature package is still execution-ready:
   ```bash
   python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/010-brownfield-doc-reconcile-command
   ```

## Expected Artifacts

- `/doc_reconcile` workflow plus code/docs audit script.
- Epic `issues.md` enforcement in V31 scaffolds and validators.
- Operator docs describing when reconciliation is mandatory before `/develop` or `/quick_fix`.
- A refreshed `.agents/specs/<feature-id>/execution-brief.md` aligned with the current docs package.

## POC Rehearsal

- Smallest professional slice: execute the documented commands for `010-brownfield-doc-reconcile-command`, verify the evidence lands in `verification.md`, and confirm readiness still passes without widening context beyond the feature package.
- Capture evidence: command output, any manual confirmation steps, and the final release recommendation.
- Stop and revise if the replay requires reading unrelated repo areas, inventing missing docs, or skipping a failing validator.

## Rollback Check

- Remove the command and additive audit/issue-file enforcement together if brownfield reconciliation needs to be reconsidered.
- If the replay exposes a broader governance mismatch, roll back the docs package changes first and only then reconsider code-level rollback.
