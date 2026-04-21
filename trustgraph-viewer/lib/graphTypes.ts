export type GraphNodeType = "Module" | "Run" | "Skill" | string;

export type GraphProperties = Record<string, string | number | boolean | null | undefined>;

export type GraphNode = {
  id: string;
  type: GraphNodeType;
  group: string;
  properties: GraphProperties;
  val: number;
  incomingCount: number;
  outgoingCount: number;
  x?: number;
  y?: number;
  z?: number;
};

export type GraphLink = {
  source: string | GraphNode;
  target: string | GraphNode;
  type: string;
  properties?: GraphProperties;
};

export type GraphData = {
  nodes: GraphNode[];
  links: GraphLink[];
};

export type FilterMode =
  | "all"
  | "core"
  | "isolated"
  | "coupling"
  | "external"
  | "edge"
  | "logic";

export type VectorSearchResult = {
  source: string;
  chunk_id: number;
  distance: number;
  content: string;
};

export type VectorSearchResponse = {
  query: string;
  results: VectorSearchResult[];
};

export type RuntimeServiceHealth = {
  status: "online" | "offline";
  latencyMs?: number;
  error?: string;
};

export type RuntimeHealthResponse = {
  status: "online" | "degraded" | "offline";
  checkedAt: string;
  services: {
    neo4j: RuntimeServiceHealth;
    chroma: RuntimeServiceHealth;
  };
};
