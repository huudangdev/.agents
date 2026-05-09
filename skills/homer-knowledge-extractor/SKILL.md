---
name: homer-knowledge-extractor
description: Extract faithful structured data from raw text with traceability and schema discipline
---

# Knowledge Extractor & Information Parser

Use this skill when raw text must become faithful structured data.

## Required Reads

- [extraction-contract.md](references/extraction-contract.md)
- The source artifact and expected schema or interface when they exist.

## Operating Rules

- Extract only what is explicitly present.
- Preserve traceability to the source.
- Validate the JSON output before handoff.

## Output Expectations

- State the schema or extraction shape.
- Identify inaccessible data if parsing limits exist.
- Produce deterministic structured output only.
