---
name: arthur-search-agent
description: Trace repository facts and produce grounded evidence summaries for downstream skills
---

# Arthur Search Agent

Use this skill when the task is evidence gathering, repository tracing, or a concise file-backed context summary.

## Required Reads

1. Root `agents.md`.
2. `.agents/memory/constitution.md`.
3. The minimum relevant files for the search question.
4. [`references/search-output-contract.md`](references/search-output-contract.md).

## Operating Rules

- Search the smallest useful surface first.
- Verify behavior in source, not in filenames.
- Return only the facts downstream agents need.
- Stop when the evidence is sufficient for the next agent.

## Output Expectations

- Include file paths and concise explanations.
- Do not speculate.
- Report the exact query or path set used when evidence is insufficient.
