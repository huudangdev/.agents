"use client";

import { useState } from "react";
import GraphVisualizer from "../components/GraphVisualizer";
import Inspector from "../components/Inspector";
import { BrainCircuit, Search, Filter, BoxSelect, Trash2, Library, GitMerge, AlertTriangle } from "lucide-react";

export default function Home() {
  const [selectedNode, setSelectedNode] = useState<any>(null);
  const [filterMode, setFilterMode] = useState<'all' | 'core' | 'coupling' | 'external' | 'edge' | 'isolated' | 'logic'>('all');
  const [searchQuery, setSearchQuery] = useState("");

  const handleNodeClick = (node: any) => {
    setSelectedNode(node);
  };

  const handleCloseInspector = () => {
    setSelectedNode(null);
  };

  return (
    <main className="flex h-screen w-screen flex-col overflow-hidden bg-gray-950 font-sans text-gray-200">
      {/* Header Panel */}
      <header className="absolute top-0 left-0 right-0 z-10 flex h-16 items-center justify-between px-6 bg-gradient-to-b from-gray-950/90 to-transparent pointer-events-none">
        <div className="flex items-center gap-3 pointer-events-auto shrink-0">
          <div className="p-2 bg-cyan-500/20 rounded-lg border border-cyan-500/30">
            <BrainCircuit className="text-cyan-400" size={24} />
          </div>
          <div>
            <h1 className="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-purple-500 hidden sm:block">
              TrustGraph Workbench
            </h1>
            <p className="text-xs text-gray-400 hidden sm:block">Antigravity 3D Memory Engine</p>
          </div>
        </div>

        <div className="flex items-center gap-4 pointer-events-auto flex-1 justify-end">
          {/* ACTION CONSOLE */}
          <div className="hidden lg:flex items-center gap-1.5 bg-gray-900/60 p-1.5 rounded-lg border border-gray-700/50 backdrop-blur-sm overflow-x-auto">
             <TabButton icon={<Filter size={14}/>} label="Full Galaxy" val="all" current={filterMode} set={setFilterMode} color="cyan"/>
             <TabButton icon={<BoxSelect size={14}/>} label="Core Pillars" val="core" current={filterMode} set={setFilterMode} color="purple"/>
             <TabButton icon={<AlertTriangle size={14}/>} label="High Coupling" val="coupling" current={filterMode} set={setFilterMode} color="orange"/>
             <TabButton icon={<Library size={14}/>} label="External Libs" val="external" current={filterMode} set={setFilterMode} color="blue"/>
             <TabButton icon={<GitMerge size={14}/>} label="Edge Nodes" val="edge" current={filterMode} set={setFilterMode} color="green"/>
             <TabButton icon={<Trash2 size={14}/>} label="Isolated" val="isolated" current={filterMode} set={setFilterMode} color="red"/>
             <TabButton icon={<BrainCircuit size={14}/>} label="Agent Logic" val="logic" current={filterMode} set={setFilterMode} color="yellow"/>
          </div>

          <div className="relative group shrink-0">
            <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
              <Search className="w-4 h-4 text-gray-400 group-focus-within:text-cyan-400 transition-colors" />
            </div>
            <input 
              type="text" 
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search nodes or libs..." 
              className="block w-48 p-2 pl-9 text-sm text-gray-200 bg-gray-900/80 border border-gray-600/50 rounded-lg focus:ring-cyan-500 focus:border-cyan-500 backdrop-blur-md transition-all focus:w-64 focus:bg-gray-800"
            />
          </div>
        </div>
      </header>

      {/* Main 3D Graph Container */}
      <div className="flex-1 relative w-full h-full cursor-grab active:cursor-grabbing">
        <GraphVisualizer 
          onNodeClick={handleNodeClick} 
          selectedNodeId={selectedNode?.id} 
          filterMode={filterMode}
          searchQuery={searchQuery}
        />
      </div>

      {/* Inspector Sidebar Overlay */}
      <Inspector 
        node={selectedNode} 
        onClose={handleCloseInspector} 
      />

      {/* Bottom Status Bar */}
      <footer className="absolute bottom-0 left-0 right-0 z-10 flex h-10 items-center justify-between px-6 bg-gradient-to-t from-gray-950/90 to-transparent pointer-events-none">
        <div className="flex items-center gap-4 pointer-events-auto">
          <div className="flex items-center gap-2">
            <span className="relative flex h-2.5 w-2.5">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-cyan-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-cyan-500"></span>
            </span>
            <span className="text-xs text-gray-400 font-mono">NEO4J CONNECTED</span>
          </div>
        </div>
        <div className="pointer-events-auto">
           <p className="text-xs text-gray-500 font-mono">
             Left Click Node: Focus Mode • Drag: Rotate • Scroll: Zoom
           </p>
        </div>
      </footer>
    </main>
  );
}

// Sub-component for Tabs
function TabButton({ icon, label, val, current, set, color }: any) {
  const isActive = current === val;
  
  // Custom Tailwind colors mapping based on string
  const colorMap: any = {
    cyan: "bg-cyan-500/20 text-cyan-400 border-cyan-500/30",
    purple: "bg-purple-500/20 text-purple-400 border-purple-500/30",
    orange: "bg-orange-500/20 text-orange-400 border-orange-500/30",
    blue: "bg-blue-500/20 text-blue-400 border-blue-500/30",
    green: "bg-green-500/20 text-green-400 border-green-500/30",
    red: "bg-red-500/20 text-red-400 border-red-500/30",
    yellow: "bg-yellow-500/20 text-yellow-400 border-yellow-500/30",
  };

  const activeClass = `border ${colorMap[color]}`;
  const inactiveClass = `text-gray-400 hover:text-gray-200 hover:bg-gray-800 border border-transparent`;

  return (
    <button 
      onClick={() => set(val)}
      className={`flex items-center gap-2 px-3 py-1.5 rounded text-xs font-semibold whitespace-nowrap transition-all ${isActive ? activeClass : inactiveClass}`}
    >
      {icon} {label}
    </button>
  );
}
