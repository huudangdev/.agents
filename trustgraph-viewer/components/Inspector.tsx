"use client";

import { X } from "lucide-react";
import type { GraphNode } from "../lib/graphTypes";

export default function Inspector({ node, onClose }: { node: GraphNode | null, onClose: () => void }) {
  if (!node) return null;

  const nodeName = String(node.properties?.name || node.id);

  return (
    <div className="absolute top-4 right-4 w-80 bg-gray-900/80 backdrop-blur-md border border-gray-700/50 rounded-xl shadow-2xl p-5 text-gray-200 z-10 transition-all">
      <div className="flex items-center justify-between border-b border-gray-700/50 pb-3 mb-4">
        <div>
          <h2 className="text-sm font-semibold tracking-wide text-cyan-400 uppercase">
            {node.group}
          </h2>
          <p className="text-xl font-bold truncate text-white" title={nodeName}>
            {nodeName}
          </p>
        </div>
        <button 
          onClick={onClose}
          className="p-1 hover:bg-gray-800 rounded-full transition-colors"
        >
          <X size={20} className="text-gray-400 hover:text-white" />
        </button>
      </div>

      <div className="space-y-4 max-h-[60vh] overflow-y-auto custom-scrollbar">
        <div>
          <h3 className="text-xs font-semibold text-gray-400 mb-2 uppercase tracking-wider">Properties</h3>
          {Object.entries(node.properties || {}).map(([key, value]) => (
            <div key={key} className="mb-2 bg-gray-950/50 rounded-lg p-2 border border-gray-800/50">
              <span className="block text-xs text-gray-500 font-mono mb-1">{key}</span>
              <span className="block text-sm break-words whitespace-pre-wrap">
                {typeof value === 'object' ? JSON.stringify(value, null, 2) : String(value)}
              </span>
            </div>
          ))}
          {(!node.properties || Object.keys(node.properties).length === 0) && (
            <div className="text-sm text-gray-500 italic">No properties available</div>
          )}
        </div>
        
        <div>
          <h3 className="text-xs font-semibold text-gray-400 mb-2 uppercase tracking-wider">Metadata</h3>
          <div className="bg-gray-950/50 rounded-lg p-2 border border-gray-800/50">
             <span className="block text-xs text-gray-500 font-mono mb-1">Element ID</span>
             <span className="block text-sm font-mono break-words">{node.id}</span>
          </div>
        </div>
      </div>
    </div>
  );
}
