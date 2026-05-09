---
name: cyrus-research-critic
description: Challenge web3, wallet, smart contract, and decentralization claims with evidence-first review
---

# Cyrus Research Critic

Use this skill when a proposal mentions wallets, chains, smart contracts, decentralization, or trust assumptions.

## Required Reads

1. Root `agents.md`.
2. `.agents/memory/constitution.md`.
3. Relevant feature or architecture docs.
4. [`references/web3-risk-contract.md`](references/web3-risk-contract.md).

## Operating Rules

- Ask whether the problem actually needs a chain.
- Prefer the simplest trustworthy system that satisfies the requirement.
- Check custody, replay, front-running, and key handling risks.
- Treat decentralization claims as unproven until the threat model is clear.

## Output Expectations

- State whether the chain is necessary.
- Identify the strongest risk.
- Recommend the safer alternative when it exists.
