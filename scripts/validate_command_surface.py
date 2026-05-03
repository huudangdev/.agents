#!/usr/bin/env python3
"""Validate that public slash commands are wired to workflows and scripts."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

from path_utils import resolve_from_root


@dataclass(frozen=True)
class CommandContract:
    command: str
    workflow_relpath: str
    workflow_markers: tuple[str, ...]
    usage_markers: tuple[str, ...]
    readme_markers: tuple[str, ...]
    registry_markers: tuple[str, ...]


COMMON_README_MARKERS = (
    "SLASH_COMMAND_REGISTRY.md",
    "validate_command_surface.py",
)

COMMON_USAGE_MARKERS = (
    "SLASH_COMMAND_REGISTRY.md",
    "validate_command_surface.py",
)

COMMAND_CONTRACTS = (
    CommandContract(
        command="/init_brain",
        workflow_relpath=".agents/workflows/init_brain.md",
        workflow_markers=(
            "run_harness_preflight.py --root . --phase bootstrap",
            "validate_specs.py --feature <feature-path>",
            "validate_execution_readiness.py --root . --feature <feature-path>",
        ),
        usage_markers=("/init_brain", "run_harness_preflight.py --root . --phase bootstrap"),
        readme_markers=("/init_brain", "run_harness_preflight.py --phase bootstrap"),
        registry_markers=("/init_brain", "run_harness_preflight.py", "validate_execution_readiness.py"),
    ),
    CommandContract(
        command="/marcus.specify",
        workflow_relpath=".agents/workflows/marcus_specify.md",
        workflow_markers=(
            "create_feature_spec.py",
            "validate_specs.py --feature .agents/specs/<feature-id> --allow-clarifications",
        ),
        usage_markers=("/marcus.specify", "creates the workspace through `create_feature_spec.py`"),
        readme_markers=("/marcus.specify", "must create the feature workspace through `create_feature_spec.py`"),
        registry_markers=("/marcus.specify", "create_feature_spec.py", "validate_specs.py"),
    ),
    CommandContract(
        command="/marcus.clarify",
        workflow_relpath=".agents/workflows/marcus_clarify.md",
        workflow_markers=("validate_specs.py --feature .agents/specs/<feature-id>",),
        usage_markers=("/marcus.clarify",),
        readme_markers=("/marcus.clarify",),
        registry_markers=("/marcus.clarify", "validate_specs.py"),
    ),
    CommandContract(
        command="/marcus.plan",
        workflow_relpath=".agents/workflows/marcus_plan.md",
        workflow_markers=("validate_specs.py --feature .agents/specs/<feature-id>",),
        usage_markers=("/marcus.plan", "finishes with `validate_specs.py`"),
        readme_markers=("/marcus.plan", "must end with a passing `validate_specs.py`"),
        registry_markers=("/marcus.plan", "validate_specs.py"),
    ),
    CommandContract(
        command="/marcus.tasks",
        workflow_relpath=".agents/workflows/marcus_tasks.md",
        workflow_markers=(
            "build_execution_brief.py",
            "validate_specs.py --feature .agents/specs/<feature-id>",
            "validate_execution_brief_freshness.py --root . --feature .agents/specs/<feature-id>",
            "validate_execution_readiness.py --root . --feature .agents/specs/<feature-id>",
        ),
        usage_markers=("/marcus.tasks", "creates `execution-brief.md` through `build_execution_brief.py`"),
        readme_markers=("/marcus.tasks", "must build `execution-brief.md` through `build_execution_brief.py`"),
        registry_markers=("/marcus.tasks", "build_execution_brief.py", "validate_execution_readiness.py"),
    ),
    CommandContract(
        command="/marcus.review",
        workflow_relpath=".agents/workflows/marcus_review.md",
        workflow_markers=(
            "build_execution_brief.py",
            "validate_specs.py --feature .agents/specs/<feature-id>",
            "validate_execution_brief_freshness.py --root . --feature .agents/specs/<feature-id>",
            "validate_execution_readiness.py --root . --feature .agents/specs/<feature-id>",
        ),
        usage_markers=("/marcus.review", "rebuilds the brief if findings changed scope or docs-to-read"),
        readme_markers=("/marcus.review", "must rebuild the brief if review findings change scope, evidence, or docs-to-read"),
        registry_markers=("/marcus.review", "build_execution_brief.py", "validate_execution_readiness.py"),
    ),
    CommandContract(
        command="/marcus.rehearse",
        workflow_relpath=".agents/workflows/marcus_rehearse.md",
        workflow_markers=(
            "build_execution_brief.py",
            "validate_execution_brief_freshness.py --root . --feature .agents/specs/<feature-id>",
            "validate_execution_readiness.py --root . --feature .agents/specs/<feature-id>",
        ),
        usage_markers=("/marcus.rehearse", "must preserve passing execution readiness before `/develop`"),
        readme_markers=("/marcus.rehearse", "must preserve a passing readiness gate before `/develop`"),
        registry_markers=("/marcus.rehearse", "build_execution_brief.py", "validate_execution_readiness.py"),
    ),
    CommandContract(
        command="/marcus.verify",
        workflow_relpath=".agents/workflows/marcus_verify.md",
        workflow_markers=(
            "run_harness_postflight.py --root . --phase execution --feature .agents/specs/<feature-id>",
            "validate_specs.py --feature .agents/specs/<feature-id>",
            "validate_development_docs.py --strict-counts",
            "validate_doc_sync.py --strict",
        ),
        usage_markers=("/marcus.verify",),
        readme_markers=("/marcus.verify",),
        registry_markers=("/marcus.verify", "run_harness_postflight.py", "validate_doc_sync.py"),
    ),
    CommandContract(
        command="/marcus.routecheck",
        workflow_relpath=".agents/workflows/marcus_routecheck.md",
        workflow_markers=("validate_routing_regression.py --root .",),
        usage_markers=("/marcus.routecheck", "validate_routing_regression.py --root ."),
        readme_markers=("/marcus.routecheck", "validate_routing_regression.py --root ."),
        registry_markers=("/marcus.routecheck", "validate_routing_regression.py"),
    ),
    CommandContract(
        command="/design",
        workflow_relpath=".agents/workflows/design.md",
        workflow_markers=(
            "validate_design_readiness.py --root .",
            'python3 .agents/adapters/trustgraph_query.py --task "Design Phase Boot"',
            "validate_design_outputs.py --root .",
        ),
        usage_markers=("/design", "validate_design_readiness.py", "validate_design_outputs.py"),
        readme_markers=("/design", "validate_design_readiness.py", "validate_design_outputs.py"),
        registry_markers=("/design", "validate_design_readiness.py", "validate_design_outputs.py"),
    ),
    CommandContract(
        command="/marcus_init",
        workflow_relpath=".agents/workflows/marcus_init.md",
        workflow_markers=(
            "mkdir -p projects/$PROJECT_NAME/docs",
            "cp -r .agents projects/$PROJECT_NAME/",
            "cp .agents/.clinerules projects/$PROJECT_NAME/.clinerules",
            "docker-compose up -d",
            "validate_marcus_init_outputs.py --root projects/$PROJECT_NAME",
        ),
        usage_markers=("/marcus_init", "validate_marcus_init_outputs.py"),
        readme_markers=("/marcus_init", "validate_marcus_init_outputs.py"),
        registry_markers=("/marcus_init", "validate_marcus_init_outputs.py", "projects/$PROJECT_NAME/docs/prd_draft.md"),
    ),
    CommandContract(
        command="/refactor-planning",
        workflow_relpath=".agents/workflows/refactor-planning.md",
        workflow_markers=(
            "validate_refactor_planning_readiness.py --root .",
            'python3 .agents/adapters/trustgraph_query.py --task "refactor"',
            "validate_refactor_planning_toolchain.py --root .",
            "npx understand-anything",
            "npx tsc --noEmit",
            "eslint --fix",
            "npm run dev",
            "validate_refactor_planning_outputs.py --root .",
        ),
        usage_markers=(
            "/refactor-planning",
            "validate_refactor_planning_readiness.py",
            "validate_refactor_planning_toolchain.py",
            "validate_refactor_planning_outputs.py",
        ),
        readme_markers=(
            "/refactor-planning",
            "validate_refactor_planning_readiness.py",
            "validate_refactor_planning_toolchain.py",
            "validate_refactor_planning_outputs.py",
        ),
        registry_markers=(
            "/refactor-planning",
            "validate_refactor_planning_readiness.py",
            "validate_refactor_planning_toolchain.py",
            "validate_refactor_planning_outputs.py",
        ),
    ),
    CommandContract(
        command="/develop",
        workflow_relpath=".agents/workflows/develop.md",
        workflow_markers=(
            "run_harness_preflight.py --root . --phase execution --feature .agents/specs/<feature-id>",
            "validate_execution_readiness.py --root . --feature .agents/specs/<feature-id>",
            "create_development_docs.py --name",
            "create_doc_sync_note.py --name",
            "validate_development_docs.py --strict-counts",
            "validate_doc_sync.py --strict",
            "run_harness_postflight.py --root . --phase execution --feature .agents/specs/<feature-id>",
        ),
        usage_markers=("/develop", "reads `execution-brief.md` first"),
        readme_markers=("/develop", "should run `python3 .agents/scripts/run_harness_preflight.py --root . --phase execution --feature .agents/specs/<feature-id>` before behavior-changing edits"),
        registry_markers=("/develop", "create_development_docs.py", "validate_doc_sync.py"),
    ),
    CommandContract(
        command="/quick_fix",
        workflow_relpath=".agents/workflows/quick_fix.md",
        workflow_markers=(
            "run_harness_preflight.py --root . --phase execution --feature .agents/specs/<feature-id>",
            "validate_execution_readiness.py --root . --feature .agents/specs/<feature-id>",
            "create_doc_sync_note.py --name",
            "validate_doc_sync.py --strict",
        ),
        usage_markers=("/quick_fix", "stops if `validate_execution_readiness.py` fails for that workspace"),
        readme_markers=("/quick_fix", "must stop if that workspace fails `validate_execution_readiness.py`"),
        registry_markers=("/quick_fix", "run_harness_preflight.py", "create_doc_sync_note.py"),
    ),
    CommandContract(
        command="/planning",
        workflow_relpath=".agents/workflows/planning.md",
        workflow_markers=(
            "create_feature_spec.py \"Project Planning - <Project Name>\"",
            "validate_specs.py --feature .agents/specs/<feature-id>",
            "validate_planning_research.py --root . --strict-outputs",
        ),
        usage_markers=("/planning", "validate_planning_research.py --root . --strict-outputs"),
        readme_markers=("/planning", "validate_planning_research.py",),
        registry_markers=("/planning", "create_feature_spec.py", "validate_planning_research.py"),
    ),
    CommandContract(
        command="/doc_reconcile",
        workflow_relpath=".agents/workflows/doc_reconcile.md",
        workflow_markers=(
            "audit_development_docs.py --root .",
            "create_doc_sync_note.py --name \"Doc Reconcile <scope>\"",
            "validate_development_docs.py --strict-counts",
            "validate_doc_sync.py --strict",
        ),
        usage_markers=("/doc_reconcile", "audit_development_docs.py --root ."),
        readme_markers=("/doc_reconcile", "audit_development_docs.py --root ."),
        registry_markers=("/doc_reconcile", "audit_development_docs.py", "validate_doc_sync.py"),
    ),
    CommandContract(
        command="/bootstrap",
        workflow_relpath=".agents/workflows/bootstrap.md",
        workflow_markers=(
            "chmod +x .agents/bootstrap.sh .agents/setup_git_hooks.sh",
            "./.agents/bootstrap.sh",
            "./.agents/setup_git_hooks.sh",
        ),
        usage_markers=("/bootstrap",),
        readme_markers=("/bootstrap",),
        registry_markers=("/bootstrap", "./.agents/bootstrap.sh", "./.agents/setup_git_hooks.sh"),
    ),
    CommandContract(
        command="/update_brain",
        workflow_relpath=".agents/workflows/update_brain.md",
        workflow_markers=(
            "curl -sL https://raw.githubusercontent.com/huudangdev/.agents/main/update.sh | bash",
            "/init_brain",
        ),
        usage_markers=("/update_brain",),
        readme_markers=("/update_brain",),
        registry_markers=("/update_brain", "update.sh", "/init_brain"),
    ),
    CommandContract(
        command="/mobile_init",
        workflow_relpath=".agents/workflows/mobile_init.md",
        workflow_markers=("validate_specs.py", "validate_execution_readiness.py"),
        usage_markers=("/mobile_init",),
        readme_markers=("/mobile_init",),
        registry_markers=("/mobile_init", "validate_specs.py", "validate_execution_readiness.py"),
    ),
)


def missing_markers(text: str, markers: tuple[str, ...]) -> list[str]:
    return [marker for marker in markers if marker not in text]


def read_text(root: Path, relpath: str) -> str:
    return resolve_from_root(root, relpath).read_text(encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate public slash-command wiring.")
    parser.add_argument("--root", default=".", help="Project root containing .agents/")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors: list[str] = []

    readme_path = resolve_from_root(root, ".agents/README.md")
    usage_path = resolve_from_root(root, ".agents/USAGE_GUIDE.md")
    registry_path = resolve_from_root(root, ".agents/SLASH_COMMAND_REGISTRY.md")

    for path in (readme_path, usage_path, registry_path):
        if not path.exists():
            errors.append(f"Missing command-surface file: {path}")

    if errors:
        print("COMMAND SURFACE VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    readme_text = readme_path.read_text(encoding="utf-8")
    usage_text = usage_path.read_text(encoding="utf-8")
    registry_text = registry_path.read_text(encoding="utf-8")

    for marker in COMMON_README_MARKERS:
        if marker not in readme_text:
            errors.append(f"README command surface missing `{marker}`")

    for marker in COMMON_USAGE_MARKERS:
        if marker not in usage_text:
            errors.append(f"USAGE command surface missing `{marker}`")

    for contract in COMMAND_CONTRACTS:
        workflow_path = resolve_from_root(root, contract.workflow_relpath)
        if not workflow_path.exists():
            errors.append(f"{contract.command}: missing workflow `{contract.workflow_relpath}`")
            continue

        workflow_text = workflow_path.read_text(encoding="utf-8")
        missing_workflow = missing_markers(workflow_text, contract.workflow_markers)
        if missing_workflow:
            errors.append(
                f"{contract.command}: workflow `{contract.workflow_relpath}` missing markers -> "
                + ", ".join(missing_workflow)
            )

        missing_usage = missing_markers(usage_text, contract.usage_markers)
        if missing_usage:
            errors.append(f"{contract.command}: `USAGE_GUIDE.md` missing markers -> " + ", ".join(missing_usage))

        missing_readme = missing_markers(readme_text, contract.readme_markers)
        if missing_readme:
            errors.append(f"{contract.command}: `README.md` missing markers -> " + ", ".join(missing_readme))

        missing_registry = missing_markers(registry_text, contract.registry_markers)
        if missing_registry:
            errors.append(
                f"{contract.command}: `SLASH_COMMAND_REGISTRY.md` missing markers -> "
                + ", ".join(missing_registry)
            )

    if errors:
        print("COMMAND SURFACE VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("COMMAND SURFACE VALIDATION PASSED")
    print("- README, USAGE, and the slash-command registry agree on the public surface")
    print("- published slash commands point to workflow files with the required scripts or gates")
    print("- workflow-backed commands remain deterministic instead of relying on model guesswork")


if __name__ == "__main__":
    main()
