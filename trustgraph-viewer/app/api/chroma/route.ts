import { NextResponse } from 'next/server';
import { execFile } from 'child_process';
import { promisify } from 'util';
import path from 'path';

const execFileAsync = promisify(execFile);

type ChromaRequest = {
  query?: unknown;
};

function getErrorMessage(error: unknown): string {
  return error instanceof Error ? error.message : String(error);
}

export async function POST(req: Request) {
  try {
    const { query } = (await req.json()) as ChromaRequest;

    if (typeof query !== "string" || query.trim().length === 0) {
      return NextResponse.json({ error: "Missing query" }, { status: 400 });
    }

    const scriptPath = path.resolve(process.cwd(), '../adapters/trustgraph_vector_search.py');

    try {
      const { stdout, stderr } = await execFileAsync("python3", [
        scriptPath,
        "--query",
        query.trim(),
      ]);
      
      try {
        const result = JSON.parse(stdout);
        if (result.error) {
          return NextResponse.json({ error: result.error }, { status: 500 });
        }
        return NextResponse.json(result);
      } catch {
        console.error("Parse error:", stdout, stderr);
        return NextResponse.json({ error: "Invalid JSON response from python adapter", details: stdout }, { status: 500 });
      }

    } catch (cmdError: unknown) {
      console.error("Execution error:", cmdError);
      return NextResponse.json({ error: "Failed to execute python adapter", details: getErrorMessage(cmdError) }, { status: 500 });
    }

  } catch (err: unknown) {
    return NextResponse.json({ error: "Server error", message: getErrorMessage(err) }, { status: 500 });
  }
}
