#!/usr/bin/env node

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import pc from 'picocolors';
import ora from 'ora';

// Setup pure-ESM __dirname equivalent
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const sourceDir = path.resolve(__dirname, '..'); // The root of the NPM package (.agents)
const targetDir = path.resolve(process.cwd(), '.agents');

console.log(pc.cyan(`\n======================================================`));
console.log(pc.bold(pc.white(`🚀 ANTIGRAVITY COGNITIVE ENGINE V29.2 (MARCUS FLEET)`)));
console.log(pc.cyan(`======================================================\n`));

const initSpinner = ora('Initializing Multi-Agent Logic Matrix...').start();

try {
  if (fs.existsSync(targetDir)) {
    initSpinner.warn(pc.yellow(`The .agents ecosystem already exists in this directory. Aborting to prevent overwrite.`));
    process.exit(1);
  }

  // Pre-flight validation
  initSpinner.text = 'Extracting Neural Schemas & RAG Workflows...';
  
  // The filter function ensures we do not copy our own NPM internals or personal databases
  const filterFunc = (src, dest) => {
    const filename = path.basename(src);
    // Blacklisted items
    const blocked = ['node_modules', 'package.json', 'package-lock.json', 'bin', '.git', '.brain', 'neo4j_data', 'chromadb_data'];
    if (blocked.includes(filename)) return false;
    return true;
  };

  fs.cpSync(sourceDir, targetDir, { recursive: true, filter: filterFunc });

  initSpinner.succeed(pc.green('Neural Matrix successfully grafted into local repository!'));

  const skillCount = fs.readdirSync(path.join(targetDir, 'skills')).length;

  console.log(`\n${pc.bold('📦 Installation Verified:')}`);
  console.log(`${pc.gray('-')} Copied ${pc.magenta(skillCount + ' Active Skills')} into .agents/skills/`);
  console.log(`${pc.gray('-')} Injected ${pc.cyan('.clinerules')} (Supreme Manifesto)`);
  console.log(`${pc.gray('-')} Injected ${pc.cyan('TrustGraph')} Ecosystem\n`);

  console.log(pc.bold('⚡ NEXT STEPS FOR OPERATOR:'));
  console.log(` 1. Run ${pc.green('npx mcp start')} or leverage the Antigravity OS directly.`);
  console.log(` 2. Boot the TrustGraph Memory Core:`);
  console.log(pc.gray(`    $ cd .agents/trustgraph && docker-compose up -d`));
  console.log(` 3. Request a refactor in your prompt (e.g. "/refactor_project") to see it automatically query GraphQL prior to coding!\n`);

} catch (error) {
  initSpinner.fail(pc.red('Critical Failure during Neural Grafting...'));
  console.error(pc.red(error.message));
  process.exit(1);
}
