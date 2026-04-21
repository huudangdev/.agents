# Contract: Vector Search API

## Endpoint

```http
POST /api/chroma
Content-Type: application/json
```

## Request

```json
{
  "query": "Where is auth logic?"
}
```

Validation:

- `query` must be a non-empty string after trimming.
- Query text is passed to Python as a subprocess argument.
- Query text must not be interpolated into a shell command string.

## Success Response

```json
{
  "query": "Where is auth logic?",
  "results": [
    {
      "source": "src/example.ts",
      "chunk_id": 0,
      "distance": 0.12,
      "content": "..."
    }
  ]
}
```

## Error Response

```json
{
  "error": "Failed to execute python adapter",
  "details": "..."
}
```
