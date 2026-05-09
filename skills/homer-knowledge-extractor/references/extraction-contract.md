# Knowledge Extraction Contract

Use this skill when raw text must become faithful structured data.

## Required Inputs

- The source artifact
- The expected schema or interface
- Any parser or OCR limitations

## Decision Rules

- Extract only what is explicitly present.
- Preserve traceability to the source.
- Validate the JSON output before handoff.

## Output Contract

- State the schema or extraction shape.
- Identify inaccessible data if parsing limits exist.
- Produce deterministic structured output only.
