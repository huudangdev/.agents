# Slash Command Registry

This file is the public source of truth for slash-command execution inside
`.agents`.

A slash command is considered supported only when all of the following are true:

- The command is published in `README.md` and `USAGE_GUIDE.md`.
- A workflow file exists under `.agents/workflows/`.
- The workflow names the required local scripts, gates, or shell entrypoints.
- `python3 .agents/scripts/validate_command_surface.py --root .` passes.

If a command is described in prose but missing from this registry, treat it as
underspecified and do not improvise missing script calls.

## Script-Backed Commands

### `/init_brain`

- Workflow: `.agents/workflows/init_brain.md`
- Required invocations:
  - `python3 .agents/scripts/run_harness_preflight.py --root . --phase bootstrap`
  - `python3 .agents/scripts/validate_specs.py --feature <feature-path>`
  - `python3 .agents/scripts/validate_execution_readiness.py --root . --feature <feature-path>`
- Produced or consumed artifacts:
  - `.mcp.json`
  - `.agents/logs/harness/preflight.jsonl`

### `/marcus.specify`

- Workflow: `.agents/workflows/marcus_specify.md`
- Required invocations:
  - `python3 .agents/scripts/create_feature_spec.py "<Feature Title>" --prompt "<operator prompt>"`
  - `python3 .agents/scripts/validate_specs.py --feature .agents/specs/<feature-id> --allow-clarifications`
- Produced or consumed artifacts:
  - `.agents/specs/<feature-id>/spec.md`

### `/marcus.clarify`

- Workflow: `.agents/workflows/marcus_clarify.md`
- Required invocations:
  - `python3 .agents/scripts/validate_specs.py --feature .agents/specs/<feature-id>`
- Produced or consumed artifacts:
  - `.agents/specs/<feature-id>/spec.md`

### `/marcus.plan`

- Workflow: `.agents/workflows/marcus_plan.md`
- Required invocations:
  - `python3 .agents/scripts/validate_specs.py --feature .agents/specs/<feature-id>`
- Produced or consumed artifacts:
  - `.agents/specs/<feature-id>/plan.md`
  - `.agents/specs/<feature-id>/contracts/`
  - `.agents/specs/<feature-id>/data-model.md`
  - `.agents/specs/<feature-id>/quickstart.md`
  - `.agents/specs/<feature-id>/agent-routing.md`

### `/marcus.tasks`

- Workflow: `.agents/workflows/marcus_tasks.md`
- Required invocations:
  - `python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/<feature-id> --task-shape <ui-only|frontend-behavior|backend-api|data-contract|architecture-refactor|general>`
  - `python3 .agents/scripts/validate_specs.py --feature .agents/specs/<feature-id>`
  - `python3 .agents/scripts/validate_execution_brief_freshness.py --root . --feature .agents/specs/<feature-id>`
  - `python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/<feature-id>`
- Produced or consumed artifacts:
  - `.agents/specs/<feature-id>/tasks.md`
  - `.agents/specs/<feature-id>/execution-brief.md`

### `/marcus.review`

- Workflow: `.agents/workflows/marcus_review.md`
- Required invocations:
  - `python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/<feature-id> --task-shape <task-shape>`
  - `python3 .agents/scripts/validate_specs.py --feature .agents/specs/<feature-id>`
  - `python3 .agents/scripts/validate_execution_brief_freshness.py --root . --feature .agents/specs/<feature-id>`
  - `python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/<feature-id>`
- Produced or consumed artifacts:
  - `.agents/specs/<feature-id>/verification.md`
  - `.agents/specs/<feature-id>/execution-brief.md`

### `/marcus.rehearse`

- Workflow: `.agents/workflows/marcus_rehearse.md`
- Required invocations:
  - `python3 .agents/scripts/build_execution_brief.py --feature .agents/specs/<feature-id> --task-shape <task-shape>`
  - `python3 .agents/scripts/validate_execution_brief_freshness.py --root . --feature .agents/specs/<feature-id>`
  - `python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/<feature-id>`
- Produced or consumed artifacts:
  - `.agents/specs/<feature-id>/quickstart.md`
  - `.agents/specs/<feature-id>/verification.md`

### `/marcus.verify`

- Workflow: `.agents/workflows/marcus_verify.md`
- Required invocations:
  - `python3 .agents/scripts/run_harness_postflight.py --root . --phase execution --feature .agents/specs/<feature-id>`
  - `python3 .agents/scripts/validate_specs.py --feature .agents/specs/<feature-id>`
  - `python3 .agents/scripts/validate_development_docs.py --strict-counts`
  - `python3 .agents/scripts/validate_doc_sync.py --strict`
  - `python3 .agents/scripts/validate_docs_substance.py --root . --include-development`
- Produced or consumed artifacts:
  - `.agents/logs/harness/postflight.jsonl`
  - `.agents/specs/<feature-id>/verification.md`

### `/marcus.routecheck`

- Workflow: `.agents/workflows/marcus_routecheck.md`
- Required invocations:
  - `python3 .agents/scripts/validate_routing_regression.py --root .`
- Produced or consumed artifacts:
  - `.agents/ROUTING_REGRESSION_CHECKLIST.md`

### `/develop`

- Workflow: `.agents/workflows/develop.md`
- Required invocations:
  - `python3 .agents/scripts/run_harness_preflight.py --root . --phase execution --feature .agents/specs/<feature-id>`
  - `python3 .agents/scripts/build_context_index.py --root .`
  - `python3 .agents/scripts/validate_context_index.py --root .`
  - `python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/<feature-id>`
  - `python3 .agents/scripts/create_development_docs.py --name "<epic-or-feature-name>" --feature-id "<optional-feature-id>" --epic-number 001 --child-number 001 --task-number 001`
  - `python3 .agents/scripts/create_doc_sync_note.py --name "<code-slice-name>" --changed-files "<comma-separated-files>"`
  - `python3 .agents/scripts/validate_development_docs.py --strict-counts`
  - `python3 .agents/scripts/validate_doc_sync.py --strict`
  - `python3 .agents/scripts/validate_docs_substance.py --root . --include-development`
  - `python3 .agents/scripts/run_harness_postflight.py --root . --phase execution --feature .agents/specs/<feature-id>`
- Produced or consumed artifacts:
  - `.agents/specs/<feature-id>/execution-brief.md`
  - `docs/development/`
  - `docs/development/sync/`

### `/quick_fix`

- Workflow: `.agents/workflows/quick_fix.md`
- Required invocations:
  - `python3 .agents/scripts/run_harness_preflight.py --root . --phase execution --feature .agents/specs/<feature-id>`
  - `python3 .agents/scripts/build_context_index.py --root .`
  - `python3 .agents/scripts/validate_context_index.py --root .`
  - `python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/<feature-id>`
  - `python3 .agents/scripts/create_doc_sync_note.py --name "QuickFix <scope>" --changed-files "<changed-source-and-doc-files>"`
  - `python3 .agents/scripts/validate_doc_sync.py --strict`
  - `python3 .agents/scripts/validate_docs_substance.py --root . --include-development`
- Produced or consumed artifacts:
  - `.agents/logs/harness/preflight.jsonl`
  - `docs/development/sync/`

### `/planning`

- Workflow: `.agents/workflows/planning.md`
- Required invocations:
  - `python3 .agents/scripts/create_feature_spec.py "Project Planning - <Project Name>" --prompt "<original operator request>"`
  - `python3 .agents/scripts/validate_specs.py --feature .agents/specs/<feature-id>`
  - `python3 .agents/scripts/validate_planning_research.py --root . --strict-outputs`
  - `python3 .agents/scripts/validate_docs_substance.py --root . --strict-planning --require-docs`
- Produced or consumed artifacts:
  - `.agents/specs/<feature-id>/spec.md`
  - `docs/research/`
  - `docs/planning/`

### `/doc_reconcile`

- Workflow: `.agents/workflows/doc_reconcile.md`
- Required invocations:
  - `python3 .agents/scripts/audit_development_docs.py --root .`
  - `python3 .agents/scripts/create_doc_sync_note.py --name "Doc Reconcile <scope>" --epic-id "E-001-description" --changed-files "<changed-doc-files>"`
  - `python3 .agents/scripts/validate_development_docs.py --strict-counts`
  - `python3 .agents/scripts/validate_doc_sync.py --strict`
  - `python3 .agents/scripts/validate_docs_substance.py --root . --strict-planning --include-development --require-docs`
- Produced or consumed artifacts:
  - `docs/development/`
  - `docs/development/audits/`
  - `docs/development/sync/`

### `/bootstrap`

- Workflow: `.agents/workflows/bootstrap.md`
- Required invocations:
  - `chmod +x .agents/bootstrap.sh .agents/setup_git_hooks.sh`
  - `./.agents/bootstrap.sh`
  - `./.agents/setup_git_hooks.sh`
- Produced or consumed artifacts:
  - `.agents/venv/`
  - `.agents/trustgraph/`

### `/update_brain`

- Workflow: `.agents/workflows/update_brain.md`
- Required invocations:
  - `curl -sL https://raw.githubusercontent.com/huudangdev/.agents/main/update.sh | bash`
  - `/init_brain`
- Produced or consumed artifacts:
  - `update.sh`

### `/mobile_init`

- Workflow: `.agents/workflows/mobile_init.md`
- Required invocations:
  - `validate_specs.py`
  - `validate_execution_readiness.py`
- Produced or consumed artifacts:
  - `.agents/specs/<feature-id>/`

### `/design`

- Workflow: `.agents/workflows/design.md`
- Required invocations:
  - `python3 .agents/scripts/validate_design_readiness.py --root .`
  - `python3 .agents/adapters/trustgraph_query.py --task "Design Phase Boot"`
  - `python3 .agents/scripts/validate_design_outputs.py --root .`
- Produced or consumed artifacts:
  - `docs/BRAND_GUIDELINES.md`
  - `docs/UI_COMPONENTS_STATE.md`

### `/marcus_init`

- Workflow: `.agents/workflows/marcus_init.md`
- Required invocations:
  - `mkdir -p projects/$PROJECT_NAME/docs`
  - `cp -r .agents projects/$PROJECT_NAME/`
  - `cp .agents/.clinerules projects/$PROJECT_NAME/.clinerules`
  - `docker-compose up -d`
  - `python3 .agents/scripts/validate_marcus_init_outputs.py --root projects/$PROJECT_NAME`
- Produced or consumed artifacts:
  - `projects/$PROJECT_NAME/docs/`
  - `projects/$PROJECT_NAME/.agents/`
  - `projects/$PROJECT_NAME/.clinerules`
  - `projects/$PROJECT_NAME/agents.md`
  - `projects/$PROJECT_NAME/.agents/agents.md`
  - `projects/$PROJECT_NAME/docs/prd_draft.md`

### `/refactor-planning`

- Workflow: `.agents/workflows/refactor-planning.md`
- Required invocations:
  - `python3 .agents/adapters/trustgraph_query.py --task "refactor"`
  - `python3 .agents/scripts/build_context_index.py --root .`
  - `python3 .agents/scripts/validate_context_index.py --root .`
  - `python3 .agents/scripts/validate_refactor_planning_readiness.py --root .`
  - `python3 .agents/scripts/validate_refactor_planning_toolchain.py --root .`
  - `npx understand-anything`
  - `npx tsc --noEmit`
  - `eslint --fix`
  - `npm run dev`
  - `python3 .agents/scripts/validate_refactor_planning_outputs.py --root .`
- Produced or consumed artifacts:
  - `docs/ADR_REFACTOR_LOG.md`
  - `agents.md`

## Workflow-Only Commands

These commands are still part of the public surface, but they do not yet have a
single deterministic local script chain beyond the workflow narrative. They
must not be described as script-backed until that changes.

No additional workflow-only commands remain in the current published surface.
