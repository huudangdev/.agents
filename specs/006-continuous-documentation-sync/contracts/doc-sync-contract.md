# Contract: Continuous Documentation Sync

## Producer

`/develop` after every material code slice.

## Consumer

PM review, future implementation agents, QA agents, CI gates, and TrustGraph.

## Required Root

```text
docs/development/sync/
```

## Required Files

- `sync_manifest.json`
- one or more `*.md` sync notes when source files changed

## Sync Note Requirements

Each sync note must include:

- Changed source files.
- Legacy planning docs reviewed or updated.
- Development ledger docs reviewed or updated.
- Targeted patch policy checklist.
- Verification command/result.

## Update Policy

- Append missing facts.
- Target-patch changed facts.
- Preserve old decisions by adding superseding notes.
- Do not replace whole PM docs unless explicitly requested.

## Validation

```bash
python3 .agents/scripts/validate_doc_sync.py --strict
```
