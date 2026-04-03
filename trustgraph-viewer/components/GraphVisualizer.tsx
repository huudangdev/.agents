"use client";

import dynamic from "next/dynamic";
import { useEffect, useRef, useMemo, useState } from "react";
import * as THREE from "three";

const ForceGraph3D = dynamic(() => import("react-force-graph-3d"), { ssr: false });

export default function GraphVisualizer({ 
  onNodeClick, 
  selectedNodeId,
  filterMode,
  searchQuery
}: { 
  onNodeClick?: (node: any) => void; 
  selectedNodeId?: string;
  filterMode: 'all' | 'core' | 'isolated' | 'coupling' | 'external' | 'edge' | 'logic';
  searchQuery?: string;
}) {
  const [originalData, setOriginalData] = useState<{ nodes: any[]; links: any[] } | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const fgRef = useRef<any>(null);

  const [highlightNodes, setHighlightNodes] = useState(new Set());
  const [highlightLinks, setHighlightLinks] = useState(new Set());

  useEffect(() => {
    fetch("/api/graph")
      .then((res) => res.json())
      .then((d) => {
        if (d.nodes) {
          setOriginalData(d);
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
      nodes = nodes.filter((n: any) => n.incomingCount > 3);
    } else if (filterMode === 'isolated') {
      nodes = nodes.filter((n: any) => n.incomingCount === 0 && n.outgoingCount === 0);
    } else if (filterMode === 'coupling') {
      nodes = nodes.filter((n: any) => n.outgoingCount > 7);
    } else if (filterMode === 'external') {
      nodes = nodes.filter((n: any) => {
        const name = n.properties?.name || n.id;
        return !name.includes('.') && !name.includes('/') && !name.includes('\\');
      });
    } else if (filterMode === 'edge') {
      nodes = nodes.filter((n: any) => n.incomingCount === 0 && n.outgoingCount > 0);
    } else if (filterMode === 'logic') {
      const allowedNodes = new Set();
      nodes.forEach((n:any) => {
        if (n.type === 'Run' || n.type === 'Skill') allowedNodes.add(n.id);
      });
      links.forEach((l:any) => {
         if (l.type === 'MODIFIED' || l.type === 'OPTIMIZED' || l.type === 'CAUSED_ERROR') {
           allowedNodes.add(typeof l.source === 'object' ? l.source.id : l.source);
           allowedNodes.add(typeof l.target === 'object' ? l.target.id : l.target);
         }
      });
      nodes = nodes.filter((n:any) => allowedNodes.has(n.id));
    }

    if (filterMode !== 'all') {
      const nodeIds = new Set(nodes.map((n: any) => n.id));
      links = links.filter((l: any) => {
        const sid = typeof l.source === 'object' ? l.source.id : l.source;
        const tid = typeof l.target === 'object' ? l.target.id : l.target;
        return nodeIds.has(sid) && nodeIds.has(tid);
      });
    }

    return { nodes, links };
  }, [originalData, filterMode]);

  useEffect(() => {
    const hNodes = new Set();
    const hLinks = new Set();

    if (searchQuery && data.nodes.length > 0) {
      const sq = searchQuery.toLowerCase();
      const matchedNodeIds = new Set();
      
      data.nodes.forEach((n: any) => {
         const name = (n.properties?.name || n.group || n.id || "").toLowerCase();
         if (name.includes(sq)) {
             matchedNodeIds.add(n.id);
             hNodes.add(n.id);
         }
      });

      data.links.forEach((link: any) => {
        const sourceId = typeof link.source === 'object' ? link.source.id : link.source;
        const targetId = typeof link.target === 'object' ? link.target.id : link.target;
        
        if (matchedNodeIds.has(sourceId) || matchedNodeIds.has(targetId)) {
          hLinks.add(link);
          hNodes.add(sourceId);
          hNodes.add(targetId);
        }
      });
    } else if (selectedNodeId && data.nodes.length > 0) {
      hNodes.add(selectedNodeId);
      data.links.forEach((link: any) => {
        const sourceId = typeof link.source === 'object' ? link.source.id : link.source;
        const targetId = typeof link.target === 'object' ? link.target.id : link.target;
        
        if (sourceId === selectedNodeId || targetId === selectedNodeId) {
          hLinks.add(link);
          hNodes.add(sourceId);
          hNodes.add(targetId);
        }
      });
    }

    setHighlightNodes(hNodes);
    setHighlightLinks(hLinks);
  }, [selectedNodeId, searchQuery, data]);

  const handleClick = (node: any) => {
    if (onNodeClick) onNodeClick(node);
    
    const distance = 80;
    const distRatio = 1 + distance/Math.hypot(node.x, node.y, node.z);
    
    if (fgRef.current) {
      fgRef.current.cameraPosition(
        { x: node.x * distRatio, y: node.y * distRatio, z: node.z * distRatio },
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
        nodeLabel={(node: any) => {
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
        nodeVal={(node: any) => node.val}
        nodeThreeObject={((node: any) => {
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
        }) as any}
        nodeColor={(node: any) => {
          if (highlightNodes.size > 0 && !highlightNodes.has(node.id)) {
            return "rgba(255,255,255,0.02)";
          }
          if (node.id === selectedNodeId) return "#FFFFFF";
          if (node.type === 'Run' || node.type === 'Skill') return "rgba(0,0,0,0)"; // hide sphere
          
          const index = Math.abs(node.group.split("").reduce((a: any, b: any) => { a = ((a << 5) - a) + b.charCodeAt(0); return a & a }, 0)) % nodeColorByGroup.length;
          return nodeColorByGroup[index];
        }}
        nodeOpacity={0.9}
        nodeResolution={16}
        linkWidth={(link: any) => highlightLinks.has(link) ? 2 : 0.5}
        linkColor={(link: any) => {
          if (link.type === 'OPTIMIZED') return '#00FFAA';
          if (link.type === 'CAUSED_ERROR') return '#FF3333';
          if (link.type === 'RETRY_OF') return '#E100FF';
          if (link.type === 'LEVERAGED') return '#FFB800';

          if (highlightLinks.size > 0) {
            return highlightLinks.has(link) ? "#00FFFF" : "rgba(255,255,255,0.01)";
          }
          return "rgba(255,255,255,0.08)";
        }}
        linkDirectionalParticles={(link: any) => {
           if (link.type === 'OPTIMIZED' || link.type === 'CAUSED_ERROR' || link.type === 'RETRY_OF') return 5;
           return highlightLinks.has(link) ? 3 : 1;
        }}
        linkDirectionalParticleWidth={(link: any) => {
           if (link.type === 'OPTIMIZED' || link.type === 'CAUSED_ERROR') return 3;
           if (link.type === 'RETRY_OF') return 2;
           return highlightLinks.has(link) ? 3 : 1;
        }}
        linkDirectionalParticleColor={(link: any) => {
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
