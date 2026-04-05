#!/usr/bin/env python3
import os
import time
import argparse
from prometheus_client import start_http_server, Counter, Gauge

# Enterprise Prometheus O11y (Observability) Telemetry Exporter
# V29.4: Replaces flat JSON logs with a live HTTP metrics endpoint.

# Define Metrics
RAG_LATENCY_MS = Gauge('rag_retrieval_latency_ms', 'Semantic Vector Retrieval Latency in Milliseconds')
TOKENS_SAVED = Counter('rag_tokens_saved_total', 'Cumulative Context Tokens Saved by RAG Top-K Filtering')
FSM_TRIPS = Counter('agent_fsm_trips_total', 'Count of times the Circuit Breaker FSM halted an Agent')
AGENT_EXEC = Counter('agent_action_total', 'Count of physical operations an Agent executes', ['agent_id', 'action'])

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8000, help="Port to host the Prometheus exporter")
    parser.add_argument('--agent_id', type=str, default="system_core")
    parser.add_argument('--action', type=str, required=False, help="e.g. FSM_Halt, Ingestion_Pass")
    parser.add_argument('--tokens_saved', type=int, default=0)
    parser.add_argument('--latency_ms', type=int, default=0)
    parser.add_argument('--run_server', action='store_true', help="Keep the server running to expose metrics")
    return parser.parse_args()

def emit_metrics(args):
    """If invoked directly by an agent workflow, emit the requested metric anomaly."""
    if args.action == "FSM_Halt":
        FSM_TRIPS.inc()
    
    if args.action:
        AGENT_EXEC.labels(agent_id=args.agent_id, action=args.action).inc()

    if args.latency_ms > 0:
        RAG_LATENCY_MS.set(args.latency_ms)

    if args.tokens_saved > 0:
        TOKENS_SAVED.inc(args.tokens_saved)

def main():
    args = parse_args()
    
    # Start the Prometheus metrics server
    start_http_server(args.port)
    print(f"🚀 [O11y Telemetry] Prometheus Exporter listening on port {args.port}...")
    
    emit_metrics(args)
    
    if args.run_server:
        print("[O11y Telemetry] Server bounds established. Entering daemon loop.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Shutting down telemetry server.")
    else:
        # If not running as daemon, wait a moment for Prometheus to potentially scrape if in pipeline, then exit
        time.sleep(5) 

if __name__ == "__main__":
    main()
