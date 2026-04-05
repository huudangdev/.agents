#!/usr/bin/env python3
import os
import time
import argparse
from prometheus_client import start_http_server, Counter, Gauge

# Enterprise Prometheus O11y (Observability) Telemetry Exporter
# V29.4: Replaces flat JSON logs with a live HTTP metrics endpoint.

# Define Enterprise Granular Metrics
RAG_LATENCY_MS = Gauge('rag_retrieval_latency_ms', 'Semantic Vector Retrieval Latency in Milliseconds', ['agent_id', 'tenant_id', 'repo'])
TOKENS_SAVED = Counter('rag_tokens_saved_total', 'Cumulative Context Tokens Saved by RAG Top-K Filtering', ['agent_id', 'tenant_id'])
FSM_TRIPS = Counter('agent_fsm_errors_total', 'Count of times the Circuit Breaker FSM halted an Agent', ['agent_id', 'fsm_state', 'tenant_id'])
AGENT_EXEC = Counter('agent_action_total', 'Count of physical operations an Agent executes', ['agent_id', 'action', 'tenant_id', 'task_type'])
TASK_SUCCESS = Counter('agent_task_success_total', 'Successful resolution of AI Tasks', ['agent_id', 'task_type', 'tenant_id'])

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8000)
    parser.add_argument('--agent_id', type=str, default="system_core")
    parser.add_argument('--tenant_id', type=str, default="default_org")
    parser.add_argument('--repo', type=str, default="frontend-monolith")
    parser.add_argument('--fsm_state', type=str, default="execution", help="State of FSM when error occurred")
    parser.add_argument('--task_type', type=str, default="refactor", help="e.g. bugfix, feature, planning")
    parser.add_argument('--action', type=str, required=False)
    parser.add_argument('--tokens_saved', type=int, default=0)
    parser.add_argument('--latency_ms', type=int, default=0)
    parser.add_argument('--run_server', action='store_true')
    return parser.parse_args()

def emit_metrics(args):
    """If invoked directly by an agent workflow, emit the requested enterprise metric anomaly."""
    if args.action == "FSM_Halt":
        FSM_TRIPS.labels(agent_id=args.agent_id, fsm_state=args.fsm_state, tenant_id=args.tenant_id).inc()
    
    if args.action == "Task_Success":
        TASK_SUCCESS.labels(agent_id=args.agent_id, task_type=args.task_type, tenant_id=args.tenant_id).inc()
    elif args.action:
        AGENT_EXEC.labels(agent_id=args.agent_id, action=args.action, tenant_id=args.tenant_id, task_type=args.task_type).inc()

    if args.latency_ms > 0:
        RAG_LATENCY_MS.labels(agent_id=args.agent_id, tenant_id=args.tenant_id, repo=args.repo).set(args.latency_ms)

    if args.tokens_saved > 0:
        TOKENS_SAVED.labels(agent_id=args.agent_id, tenant_id=args.tenant_id).inc(args.tokens_saved)

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
