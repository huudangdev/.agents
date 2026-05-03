---
description: Bypass Protocol for rapid bug patching or micro-feature insertion without triggering the massive continuous execution chain.
---
# ⚡ THE RAPID PATCH CYCLE (QUICK FIX V30.2)

> **CORE MANDATE:** Unlock pure velocity. Only invoke this protocol when the User explicitly requests the neutralization of a localized Bug, a trivial UI color mutation, or a single functional logic block on an ALREADY EXISTING architecture.

// turbo-all

## 🔸 STAGE 1: RAG WEAPONIZATION (FOCUSED CONTEXT RETRIEVAL)
*🧠 Mandatory Directives:* 
- Build and consult the context index first so the quick fix stays narrow and does not waste tokens:
  ```bash
  python3 .agents/scripts/build_context_index.py --root .
  python3 .agents/scripts/validate_context_index.py --root .
  ```
- Use `.agents/index/docs_index.md`, `.agents/index/code_index.md`, and `.agents/index/skills_index.md` to pick the smallest credible read set.
- Read `.clinerules` and root `agents.md` first (fallback: legacy `.agents/agents.md` shim) to establish the macro-context.
- Rapidly scan `SKILLS_INDEX.md` and dynamically summon **ONLY 1 to 2 SKILLS** to preserve the Token limits (e.g., UI Glitch $\rightarrow$ Load `sleek-design` or `maya-ui-ux-designer`).
- Dig into the localized `.agents/brain/` state associated with the failing Component to understand structural legacy context.
- If the fix changes behavior and the brownfield project has missing planning docs, only a boilerplate `README.md`, missing `docs/development/`, or template-only/stale implementation docs, abort `/quick_fix` and route to `/doc_reconcile` first. Quick velocity never overrides doc readiness.
- If the fix is attached to a feature-scoped spec workspace, the quick fix must
  still respect that workspace's requirements and verification commitments.
- If the fix is attached to a feature-scoped spec workspace, read that
  workspace's `execution-brief.md` first and do not widen beyond the
  `docs/development/` notes named there unless failing evidence forces it.
- In that brief, treat `### Task Shape Decision`, `### Required Reads`,
  `### Forbidden Default Reads`, and `### Expansion Triggers` as the binding
  context contract for the quick fix.
- Before a behavior-changing quick fix tied to a feature workspace, run:
  ```bash
  python3 .agents/scripts/run_harness_preflight.py --root . --phase execution --feature .agents/specs/<feature-id>
  python3 .agents/scripts/validate_execution_readiness.py --root . --feature .agents/specs/<feature-id>
  ```
- Inspect `.agents/logs/harness/preflight.jsonl` when the wrapper fails and you
  need the first failing command plus per-command status without replaying the
  whole console transcript.
- If the readiness gate fails or the brief is stale, stop `/quick_fix` and
  repair the spec/docs package before editing source.

## 🔸 STAGE 2: SURGICAL MUTATION & ISOLATED DAEMON TEST
*📦 Execution Vector:* Edit Source Logic. 
- Mount a silent Server Daemon locally and utilize `curl` or headless Playwright tools to physically verify the output ONCE.
- **[The Circuit Breaker Rule]:** If the terminal throws a red fatal crash, you are restricted to a **MAXIMUM OF 3 TRY-CATCH LOOPS**. Exceeding 3 failure loops yields an immediate Red Flag 🚩 to the Operator. Infinite loops are banned.
- **[Fallback Protocol]:** If visual abstraction tools (Draw.io, Understand-Anything) crash on initialization, immediately fallback to raw `grep` arrays and text-based `mermaid` generation to avoid stalling.

## 🔸 STAGE 3: STATE SYNCHRONIZATION & EJECTION
*📦 Execution Vector:* Document the specific Bug Patch or Bypass vector directly into the global `agents.md` and the localized `.agents/brain/` node of that component. Tick `[x]` on the active task list.

If the quick fix changes source behavior, it must still preserve PM continuity:

```bash
python3 .agents/scripts/create_doc_sync_note.py --name "QuickFix <scope>" --changed-files "<changed-source-and-doc-files>"
python3 .agents/scripts/validate_doc_sync.py --strict
```

Use targeted append/patch updates only. Do not replace planning or development
docs wholesale. Execute `python3 .agents/adapters/trustgraph_write.py --run_id "QuickFix" --status "success" --target "Patched_File" --skills "quick-fix" --score 0.85 --reasoning "Patched localized bug and synchronized docs"` to save the RAG context. Emit a dense, single-sentence success report to the Executive User. Terminate action sequence.

If PM continuity cannot be preserved because the brownfield docs package is
absent or misleading, `/quick_fix` must fail closed and redirect to
`/doc_reconcile` instead of inventing context.
