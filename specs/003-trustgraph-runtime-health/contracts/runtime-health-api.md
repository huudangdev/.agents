# Contract: Runtime Health API

## Endpoint

```http
GET /api/health
```

## Response

```json
{
  "status": "online",
  "checkedAt": "2026-04-20T00:00:00.000Z",
  "services": {
    "neo4j": {
      "status": "online",
      "latencyMs": 12
    },
    "chroma": {
      "status": "online",
      "latencyMs": 8
    }
  }
}
```

## Status Rules

- `online`: Neo4j and ChromaDB are online.
- `degraded`: exactly one service is online.
- `offline`: no service is online.

The endpoint returns HTTP 200 only for aggregate `online`; degraded/offline return
HTTP 503 with JSON body so the client can still render the status.
