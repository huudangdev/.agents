import neo4j from "neo4j-driver";
import { getTrustGraphConfig } from "../../../lib/trustgraphConfig";

const { neo4jUri, neo4jUser, neo4jPassword } = getTrustGraphConfig();

const driver = neo4j.driver(neo4jUri, neo4j.auth.basic(neo4jUser, neo4jPassword));

export async function GET() {
  const session = driver.session();
  try {
    const result = await session.run(
      `MATCH (n)-[r]->(m) RETURN n, r, m LIMIT 8000`
    );

    const nodesMap = new Map();
    const links = [];

    const getGroup = (pathName: string) => {
        if (!pathName) return "Unknown";
        const parts = pathName.split('/');
        if (parts.length > 2 && parts[0] === ".agents") return `.agents/${parts[1]}`;
        if (parts.length > 1) return parts[0];
        return "Root";
    };

    for (const record of result.records) {
      const n = record.get("n");
      const r = record.get("r");
      const m = record.get("m");

      const nName = n.properties.name || n.properties.id || "Unknown";
      const mName = m.properties.name || m.properties.id || "Unknown";
      
      const nType = (n.labels && n.labels.length > 0) ? n.labels[0] : "Module";
      const mType = (m.labels && m.labels.length > 0) ? m.labels[0] : "Module";

      if (!nodesMap.has(n.elementId)) {
        nodesMap.set(n.elementId, {
          id: n.elementId,
          type: nType,
          group: nType === "Run" ? "AI_Run" : nType === "Skill" ? "AI_Skill" : getGroup(nName),
          properties: n.properties,
          val: nType === "Run" ? 3 : 1,
          incomingCount: 0,
          outgoingCount: 0,
        });
      }
      if (!nodesMap.has(m.elementId)) {
        nodesMap.set(m.elementId, {
          id: m.elementId,
          type: mType,
          group: mType === "Run" ? "AI_Run" : mType === "Skill" ? "AI_Skill" : getGroup(mName),
          properties: m.properties,
          val: mType === "Run" ? 3 : 1,
          incomingCount: 0,
          outgoingCount: 0,
        });
      }

      links.push({
        source: n.elementId,
        target: m.elementId,
        type: r.type,
        properties: r.properties,
      });

      nodesMap.get(m.elementId).incomingCount += 1;
      nodesMap.get(n.elementId).outgoingCount += 1;
    }

    // Isolated nodes
    const allNodesRes = await session.run(`MATCH (n) RETURN n LIMIT 1000`);
    for (const record of allNodesRes.records) {
      const n = record.get("n");
      const nName = n.properties.name || n.properties.id || "Unknown";
      const nType = (n.labels && n.labels.length > 0) ? n.labels[0] : "Module";
      
      if (!nodesMap.has(n.elementId)) {
        nodesMap.set(n.elementId, {
          id: n.elementId,
          type: nType,
          group: nType === "Run" ? "AI_Run" : nType === "Skill" ? "AI_Skill" : getGroup(nName),
          properties: n.properties,
          val: nType === "Run" ? 3 : 1,
          incomingCount: 0,
          outgoingCount: 0,
        });
      }
    }

    for (const node of nodesMap.values()) {
        if (node.type === "Run") {
            const score = node.properties.score || 0.5;
            node.val = Math.max(2, score * 10);
        } else if (node.type === "Skill") {
            node.val = 2;
        } else {
            node.val = Math.max(1, node.incomingCount * 0.5); 
        }
    }

    return Response.json({
      nodes: Array.from(nodesMap.values()),
      links,
    });
  } catch (error) {
    console.error("Neo4j queries error:", error);
    return Response.json({ error: String(error) }, { status: 500 });
  } finally {
    await session.close();
  }
}
