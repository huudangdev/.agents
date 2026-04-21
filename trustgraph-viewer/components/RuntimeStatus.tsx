"use client";

import { useEffect, useMemo, useState } from "react";
import type { RuntimeHealthResponse } from "../lib/graphTypes";

type RuntimeStatusState = Partial<Omit<RuntimeHealthResponse, "status">> & {
  status: RuntimeHealthResponse["status"] | "checking";
  checkedAt?: string;
  services?: RuntimeHealthResponse["services"];
};

function statusClass(status: RuntimeStatusState["status"]): string {
  if (status === "online") return "bg-emerald-500";
  if (status === "degraded") return "bg-yellow-400";
  if (status === "offline") return "bg-red-500";
  return "bg-cyan-500";
}

function statusLabel(status: RuntimeStatusState["status"]): string {
  if (status === "online") return "TRUSTGRAPH ONLINE";
  if (status === "degraded") return "TRUSTGRAPH DEGRADED";
  if (status === "offline") return "TRUSTGRAPH OFFLINE";
  return "CHECKING TRUSTGRAPH";
}

export default function RuntimeStatus() {
  const [health, setHealth] = useState<RuntimeStatusState>({ status: "checking" });

  useEffect(() => {
    let isMounted = true;

    async function refresh() {
      try {
        const response = await fetch("/api/health", { cache: "no-store" });
        const data = (await response.json()) as RuntimeHealthResponse;
        if (isMounted) setHealth(data);
      } catch {
        if (isMounted) setHealth({ status: "offline" });
      }
    }

    void refresh();
    const interval = window.setInterval(refresh, 30000);

    return () => {
      isMounted = false;
      window.clearInterval(interval);
    };
  }, []);

  const title = useMemo(() => {
    if (!health.services) return "Checking Neo4j and ChromaDB";
    const neo4j = health.services.neo4j.status;
    const chroma = health.services.chroma.status;
    return `Neo4j: ${neo4j} | ChromaDB: ${chroma}`;
  }, [health]);

  return (
    <div className="flex items-center gap-2" title={title}>
      <span className="relative flex h-2.5 w-2.5">
        {health.status === "online" && (
          <span className={`absolute inline-flex h-full w-full rounded-full ${statusClass(health.status)} opacity-75 animate-ping`}></span>
        )}
        <span className={`relative inline-flex rounded-full h-2.5 w-2.5 ${statusClass(health.status)}`}></span>
      </span>
      <span className="text-xs text-gray-400 font-mono">{statusLabel(health.status)}</span>
    </div>
  );
}
