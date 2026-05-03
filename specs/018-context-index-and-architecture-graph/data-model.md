# Data Model: Context Index and Architecture Graph

> Feature ID: `018-context-index-and-architecture-graph`

## Entities

- `ContextIndexManifest`
  - `generated_at` (ISO UTC timestamp)
  - `root` (string)
  - `agents_root` (string)
  - `scanned_files` (int)
  - `max_files` (int)
  - `max_code_files` (int)
  - `excludes` (string[])
  - `outputs` (string[])

## Validation Rules

- All listed `outputs` must exist and be non-empty.
- The manifest timestamp must be parseable and must not exceed the configured max age.

