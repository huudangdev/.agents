# Search Output Contract

Use this reference when `arthur-search-agent` needs to produce grounded search findings.

## Required Inputs

- The question being answered.
- The paths or symbols searched.
- The reason those paths were chosen.

## Output Structure

- Search scope.
- Findings.
- Confidence.
- Limits.
- Final answer.

## Evidence Rules

- Include file path, relevant symbol or line, and a short factual summary.
- Mark what was not found.
- State any remaining gap or follow-up search need.
