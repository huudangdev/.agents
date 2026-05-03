---
description: System Bootstrapping & Cognitive Initialization Matrix (V30.2 Enterprise Standard)
---

# System Bootstrapping & Cognitive Initialization Matrix

> Use this workflow to initialize project memory, local MCP wiring, and execution constraints before starting substantial work. Initialization is a control-plane step, not permission to run autonomous infrastructure changes.

---

## Node 0: Environment Classification
1. Confirm the current workspace root and whether `.agents` is present.
2. Decide whether the session needs:
   - docs/spec governance only
   - local MCP publishing and health checks
   - full TrustGraph bootstrap
3. Do not start Docker, graph ingestion, or other heavy infrastructure automatically. Surface those actions as explicit operator-reviewed steps when they are truly required.

## Node 1: Foundational Memory Binding
1. Read the project root `agents.md` first.
2. If legacy references still point to `.agents/agents.md`, treat that file only as a compatibility shim.
3. Read `.agents/memory/constitution.md` and the relevant workflow files before proposing implementation work.
4. Summaries are allowed, but they must preserve hard requirements, open questions, and blocking constraints.

## Node 1.5: MCP Project Registration
Project-local MCP servers bundled in `.agents/mcp/mcp.json` are not useful until
they are published to the client-visible project config.
1. Preferred one-command path:
   `python3 .agents/scripts/run_harness_preflight.py --root . --phase bootstrap`
2. That bootstrap preflight must run:
   - `sync_project_mcp.py`
   - `check_mcp_health.py`
   - `print_update_brief.py`
   - `validate_harness_contract.py`
   - `check_repo_setup.sh`
   - and append structured local evidence to `.agents/logs/harness/preflight.jsonl`
3. Confirm that project-local MCP servers such as `playwright` become visible to compatible clients after synchronization.
4. Classify MCP results:
   - core MCP missing -> initialization warning that must be surfaced
   - optional MCP missing env -> yellow warning only, never block the full boot

## Node 2: Cross-Session State Inheritance
1. Read the project root `agents.md` first, then use the `.agents/agents.md` shim only when a workflow references it.
2. Audit `/docs` or equivalent documentation directories for PRD, SDD, ADR, verification notes, and brand guidance.
3. If the task changes behavior or architecture, identify the current feature workspace under `.agents/specs/` and read:
   - `spec.md`
   - `plan.md`
   - `tasks.md`
   - `verification.md`
   - `agent-routing.md`

## Node 3: Skill Ingestion
1. Read `.agents/skills/SKILLS_INDEX.md`.
2. Choose only the relevant skills for the task. Default to the smallest set that covers planning, implementation, QA, or research.
3. Read the selected `SKILL.md` files directly from disk. Avoid broad loading of unrelated skills.
4. If a skill suggests external tooling not already available in the repo, convert that into an operator-reviewed recommendation rather than an autonomous install action.

## Node 4: Role Selection
- Requirements and scope shaping: use `sophia-product-manager`, `noah-agile-product-owner`, or `aurora-plan-challenger`.
- Architecture and design decisions: use `david-systems-architect`, `alan-tech-lead`, or the relevant architecture skill.
- QA, verification, and readiness: use `ada-qa-agent`, `eve-qa-approver`, and security review skills as blocking evaluators, not ceremonial sign-offs.
- Research, design, or mobile work: load only the supporting skills that directly match the task.

## Node 5: Readiness and Telemetry
1. If the session involves behavior-changing work, run:
   - `python3 .agents/scripts/run_harness_preflight.py --root . --phase execution --feature <feature-path>`
   - `python3 .agents/scripts/validate_specs.py --feature <feature-path>`
   - `python3 .agents/scripts/validate_execution_readiness.py --root . --feature <feature-path>`
2. If either gate fails, stop implementation planning and surface the missing docs or evidence.
3. Report a concise readiness summary:
   - memory sources read
   - workflows and skills loaded
   - MCP health status
   - spec/execution readiness status
   - harness log location when preflight or postflight wrappers were used
