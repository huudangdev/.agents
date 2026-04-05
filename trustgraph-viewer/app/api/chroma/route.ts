import { NextResponse } from 'next/server';
import { exec } from 'child_process';
import { promisify } from 'util';
import path from 'path';

const execAsync = promisify(exec);

export async function POST(req: Request) {
  try {
    const { query } = await req.json();

    if (!query) {
      return NextResponse.json({ error: "Missing query" }, { status: 400 });
    }

    // Secure the query against basic bash injection (simple replacing of single quotes)
    const secureQuery = query.replace(/'/g, "");

    // Path to the python adapter
    const scriptPath = path.resolve(process.cwd(), '../adapters/trustgraph_vector_search.py');
    const command = `python3 "${scriptPath}" --query '${secureQuery}'`;

    try {
      const { stdout, stderr } = await execAsync(command);
      
      // Parse the JSON output from the python script
      try {
        const result = JSON.parse(stdout);
        if (result.error) {
          return NextResponse.json({ error: result.error }, { status: 500 });
        }
        return NextResponse.json(result);
      } catch (parseError) {
        console.error("Parse error:", stdout, stderr);
        return NextResponse.json({ error: "Invalid JSON response from python adapter", details: stdout }, { status: 500 });
      }

    } catch (cmdError: any) {
      console.error("Execution error:", cmdError);
      return NextResponse.json({ error: "Failed to execute python adapter", details: cmdError.message }, { status: 500 });
    }

  } catch (err: any) {
    return NextResponse.json({ error: "Server error", message: err.message }, { status: 500 });
  }
}
