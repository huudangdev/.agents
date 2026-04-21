"use client";

import dynamic from "next/dynamic";
import { useEffect, useRef, useMemo, useState } from "react";
import type { ForwardRefExoticComponent, RefAttributes } from "react";
import * as THREE from "three";
import type { FilterMode, GraphData, GraphLink, GraphNode } from "../lib/graphTypes";

type ForceGraphHandle = {
  cameraPosition: (
    position: { x: number; y: number; z: number },
    lookAt: GraphNode,
    transitionMs: number
  ) => void;
};

type ForceGraph3DProps = {
  graphData: GraphData;
  nodeLabel: (node: GraphNode) => string;
  nodeVal: (node: GraphNode) => number;
  nodeThreeObject: (node: GraphNode) => THREE.Object3D | undefined;
  nodeColor: (node: GraphNode) => string;
  nodeOpacity: number;
  nodeResolution: number;
  linkWidth: (link: GraphLink) => number;
  linkColor: (link: GraphLink) => string;
  linkDirectionalParticles: (link: GraphLink) => number;
  linkDirectionalParticleWidth: (link: GraphLink) => number;
  linkDirectionalParticleColor: (link: GraphLink) => string;
  linkDirectionalParticleSpeed: number;
  onNodeClick: (node: GraphNode) => void;
  onBackgroundClick: () => void;
  backgroundColor: string;
  controlType: "orbit";
};

const ForceGraph3D = dynamic(() => import("react-force-graph-3d"), { ssr: false }) as unknown as ForwardRefExoticComponent<
  ForceGraph3DProps & RefAttributes<ForceGraphHandle>
>;

function endpointId(endpoint: string | GraphNode): string {
  return typeof endpoint === "object" ? endpoint.id : endpoint;
}

export default function GraphVisualizer({ 
  onNodeClick, 
  selectedNodeId,
  filterMode,
  searchQuery
}: { 
  onNodeClick?: (node: GraphNode | null) => void; 
  selectedNodeId?: string;
  filterMode: FilterMode;
  searchQuery?: string;
}) {
  const [originalData, setOriginalData] = useState<GraphData | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const fgRef = useRef<ForceGraphHandle | null>(null);

  useEffect(() => {
    fetch("/api/graph")
      .then((res) => res.json())
      .then((d) => {
        if (d.nodes) {
          setOriginalData(d as GraphData);
        }
        setIsLoading(false);
      })
      .catch((err) => {
        console.error("Failed to fetch graph data", err);
        setIsLoading(false);
      });
  }, []);

  const data = useMemo(() => {
    if (!originalData) return { nodes: [], links: [] };
    let nodes = originalData.nodes;
    let links = originalData.links;

    if (filterMode === 'core') {
      nodes = nodes.filter((n) => n.incomingCount > 3);
    } else if (filterMode === 'isolated') {
      nodes = nodes.filter((n) => n.incomingCount === 0 && n.outgoingCount === 0);
    } else if (filterMode === 'coupling') {
      nodes = nodes.filter((n) => n.outgoingCount > 7);
    } else if (filterMode === 'external') {
      nodes = nodes.filter((n) => {
        const name = n.properties?.name || n.id;
        return String(name).includes('.') === false && String(name).includes('/') === false && String(name).includes('\\') === false;
      });
    } else if (filterMode === 'edge') {
      nodes = nodes.filter((n) => n.incomingCount === 0 && n.outgoingCount > 0);
    } else if (filterMode === 'logic') {
      const allowedNodes = new Set<string>();
      nodes.forEach((n) => {
        if (n.type === 'Run' || n.type === 'Skill') allowedNodes.add(n.id);
      });
      links.forEach((l) => {
         if (l.type === 'MODIFIED' || l.type === 'OPTIMIZED' || l.type === 'CAUSED_ERROR') {
           allowedNodes.add(endpointId(l.source));
           allowedNodes.add(endpointId(l.target));
         }
      });
      nodes = nodes.filter((n) => allowedNodes.has(n.id));
    }

    if (filterMode !== 'all') {
      const nodeIds = new Set(nodes.map((n) => n.id));
      links = links.filter((l) => nodeIds.has(endpointId(l.source)) && nodeIds.has(endpointId(l.target)));
    }

    return { nodes, links };
  }, [originalData, filterMode]);

  const { highlightNodes, highlightLinks } = useMemo(() => {
    const hNodes = new Set<string>();
    const hLinks = new Set<GraphLink>();

    if (searchQuery && data.nodes.length > 0) {
      const sq = searchQuery.toLowerCase();
      const matchedNodeIds = new Set<string>();
      
      data.nodes.forEach((n) => {
         const name = String(n.properties?.name || n.group || n.id || "").toLowerCase();
         if (name.includes(sq)) {
             matchedNodeIds.add(n.id);
             hNodes.add(n.id);
         }
      });

      data.links.forEach((link) => {
        const sourceId = endpointId(link.source);
        const targetId = endpointId(link.target);
        
        if (matchedNodeIds.has(sourceId) || matchedNodeIds.has(targetId)) {
          hLinks.add(link);
          hNodes.add(sourceId);
          hNodes.add(targetId);
        }
      });
    } else if (selectedNodeId && data.nodes.length > 0) {
      hNodes.add(selectedNodeId);
      data.links.forEach((link) => {
        const sourceId = endpointId(link.source);
        const targetId = endpointId(link.target);
        
        if (sourceId === selectedNodeId || targetId === selectedNodeId) {
          hLinks.add(link);
          hNodes.add(sourceId);
          hNodes.add(targetId);
        }
      });
    }

    return { highlightNodes: hNodes, highlightLinks: hLinks };
  }, [selectedNodeId, searchQuery, data]);

  const handleClick = (node: GraphNode) => {
    if (onNodeClick) onNodeClick(node);
    
    const distance = 80;
    const x = node.x ?? 0;
    const y = node.y ?? 0;
    const z = node.z ?? 0;
    const distRatio = 1 + distance/Math.hypot(x, y, z);
    
    if (fgRef.current) {
      fgRef.current.cameraPosition(
        { x: x * distRatio, y: y * distRatio, z: z * distRatio },
        node, 
        2000
      );
    }
  };

  const nodeColorByGroup = useMemo(() => {
    return [
      "#FF007F", "#00F0FF", "#7000FF", "#00FF66", 
      "#FFB800", "#FF3333", "#0066FF", "#E100FF",
      "#00FFAA"
    ];
  }, []);

  if (isLoading) {
    return (
      <div className="w-full h-full flex items-center justify-center bg-gray-950 text-white">
        <div className="animate-pulse flex flex-col items-center">
          <div className="w-12 h-12 border-t-4 border-cyan-500 border-solid rounded-full animate-spin"></div>
          <p className="mt-4 text-cyan-500 font-mono">Loading Cognitive Vectors...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="w-full h-full bg-gray-950 overflow-hidden relative">
      <ForceGraph3D
        ref={fgRef}
        graphData={data}
        nodeLabel={(node: GraphNode) => {
          let label = `<div class="bg-gray-800 text-white px-2 py-1 rounded text-xs border border-gray-600">`;
          label += `<strong class="text-cyan-400">${node.type} | ${node.group}</strong><br/>`;
          label += `${node.properties?.name || node.id}<br/>`;
          if (node.type === 'Run') {
              label += `<span class="text-yellow-400">Score: ${node.properties.score}</span><br/>`;
              label += `<span class="text-gray-400">Reasoning: ${node.properties.reasoning}</span>`;
          } else {
              label += `<span class="text-gray-400">In: ${node.incomingCount} | Out: ${node.outgoingCount}</span>`;
          }
          label += `</div>`;
          return label;
        }}
        nodeVal={(node: GraphNode) => node.val}
        nodeThreeObject={((node: GraphNode) => {
          if (node.type === 'Run') {
             const geometry = new THREE.OctahedronGeometry(node.val);
             const material = new THREE.MeshLambertMaterial({ 
               color: node.properties.status === 'success' ? '#00FFAA' : '#FF3333', 
               transparent: true, opacity: 0.9 
             });
             return new THREE.Mesh(geometry, material);
          } else if (node.type === 'Skill') {
             const geometry = new THREE.BoxGeometry(node.val * 2, node.val * 2, node.val * 2);
             const material = new THREE.MeshLambertMaterial({ color: '#E100FF', transparent: true, opacity: 0.9 });
             return new THREE.Mesh(geometry, material);
          }
          return undefined; // fallback to sphere for modules
        })}
        nodeColor={(node: GraphNode) => {
          if (highlightNodes.size > 0 && !highlightNodes.has(node.id)) {
            return "rgba(255,255,255,0.02)";
          }
          if (node.id === selectedNodeId) return "#FFFFFF";
          if (node.type === 'Run' || node.type === 'Skill') return "rgba(0,0,0,0)"; // hide sphere
          
          const index = Math.abs(node.group.split("").reduce((a, b) => { a = ((a << 5) - a) + b.charCodeAt(0); return a & a }, 0)) % nodeColorByGroup.length;
          return nodeColorByGroup[index];
        }}
        nodeOpacity={0.9}
        nodeResolution={16}
        linkWidth={(link: GraphLink) => highlightLinks.has(link) ? 2 : 0.5}
        linkColor={(link: GraphLink) => {
          if (link.type === 'OPTIMIZED') return '#00FFAA';
          if (link.type === 'CAUSED_ERROR') return '#FF3333';
          if (link.type === 'RETRY_OF') return '#E100FF';
          if (link.type === 'LEVERAGED') return '#FFB800';

          if (highlightLinks.size > 0) {
            return highlightLinks.has(link) ? "#00FFFF" : "rgba(255,255,255,0.01)";
          }
          return "rgba(255,255,255,0.08)";
        }}
        linkDirectionalParticles={(link: GraphLink) => {
           if (link.type === 'OPTIMIZED' || link.type === 'CAUSED_ERROR' || link.type === 'RETRY_OF') return 5;
           return highlightLinks.has(link) ? 3 : 1;
        }}
        linkDirectionalParticleWidth={(link: GraphLink) => {
           if (link.type === 'OPTIMIZED' || link.type === 'CAUSED_ERROR') return 3;
           if (link.type === 'RETRY_OF') return 2;
           return highlightLinks.has(link) ? 3 : 1;
        }}
        linkDirectionalParticleColor={(link: GraphLink) => {
          if (link.type === 'OPTIMIZED') return '#00FFAA';
          if (link.type === 'CAUSED_ERROR') return '#FF3333';
          if (link.type === 'RETRY_OF') return '#E100FF';
          return ""; // fallback
        }}
        linkDirectionalParticleSpeed={0.005}
        onNodeClick={handleClick}
        onBackgroundClick={() => {
            if (onNodeClick) onNodeClick(null);
        }}
        backgroundColor="#030712"
        controlType="orbit"
      />
      <div className="absolute inset-0 pointer-events-none" style={{
        boxShadow: "inset 0 0 150px rgba(0,0,0,0.9)"
      }}></div>
    </div>
  );
}
