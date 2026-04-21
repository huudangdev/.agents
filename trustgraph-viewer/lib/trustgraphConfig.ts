import fs from "fs";
import path from "path";

type TrustGraphConfig = {
  neo4jUri: string;
  neo4jUser: string;
  neo4jPassword: string;
  chromaHost: string;
  chromaPort: number;
};

function readLocalEnv(): Record<string, string> {
  const envPath = path.resolve(process.cwd(), "../trustgraph.env");
  if (!fs.existsSync(envPath)) return {};

  return fs
    .readFileSync(envPath, "utf-8")
    .split(/\r?\n/)
    .reduce<Record<string, string>>((acc, rawLine) => {
      const line = rawLine.trim();
      if (!line || line.startsWith("#") || !line.includes("=")) return acc;

      const [rawKey, ...rawValue] = line.split("=");
      const key = rawKey.trim();
      const value = rawValue.join("=").trim().replace(/^['"]|['"]$/g, "");
      if (key) acc[key] = value;
      return acc;
    }, {});
}

export function getTrustGraphConfig(): TrustGraphConfig {
  const localEnv = readLocalEnv();

  return {
    neo4jUri: process.env.NEO4J_URI || localEnv.NEO4J_URI || "bolt://localhost:7687",
    neo4jUser: process.env.NEO4J_USER || localEnv.NEO4J_USER || "neo4j",
    neo4jPassword: process.env.NEO4J_PASSWORD || localEnv.NEO4J_PASSWORD || "trustgraph_secret",
    chromaHost: process.env.CHROMA_HOST || localEnv.CHROMA_HOST || "localhost",
    chromaPort: Number(process.env.CHROMA_PORT || localEnv.CHROMA_PORT || "8800"),
  };
}
