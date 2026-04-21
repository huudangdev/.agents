import neo4j from "neo4j-driver";
import { getTrustGraphConfig } from "../../../lib/trustgraphConfig";
import type { RuntimeHealthResponse, RuntimeServiceHealth } from "../../../lib/graphTypes";

function errorMessage(error: unknown): string {
  return error instanceof Error ? error.message : String(error);
}

async function measure(check: () => Promise<void>): Promise<RuntimeServiceHealth> {
  const started = Date.now();
  try {
    await check();
    return { status: "online", latencyMs: Date.now() - started };
  } catch (error: unknown) {
    return { status: "offline", latencyMs: Date.now() - started, error: errorMessage(error) };
  }
}

export async function GET() {
  const config = getTrustGraphConfig();

  const [neo4jHealth, chromaHealth] = await Promise.all([
    measure(async () => {
      const driver = neo4j.driver(config.neo4jUri, neo4j.auth.basic(config.neo4jUser, config.neo4jPassword));
      const session = driver.session();
      try {
        await session.run("RETURN 1 AS ok");
      } finally {
        await session.close();
        await driver.close();
      }
    }),
    measure(async () => {
      const response = await fetch(`http://${config.chromaHost}:${config.chromaPort}/api/v1/heartbeat`, {
        cache: "no-store",
        signal: AbortSignal.timeout(2000),
      });
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }
    }),
  ]);

  const onlineCount = [neo4jHealth, chromaHealth].filter((service) => service.status === "online").length;
  const status: RuntimeHealthResponse["status"] =
    onlineCount === 2 ? "online" : onlineCount === 0 ? "offline" : "degraded";

  const body: RuntimeHealthResponse = {
    status,
    checkedAt: new Date().toISOString(),
    services: {
      neo4j: neo4jHealth,
      chroma: chromaHealth,
    },
  };

  return Response.json(body, { status: status === "online" ? 200 : 503 });
}
