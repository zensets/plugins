---
name: score-builtgraph-opportunities
description: Compare and prioritize AEC opportunities using Builtgraph evidence about fit, observed relationships, timing, and coverage. Use for explainable lead tiers, incumbent context, cold-start detection, or pursuit research; do not present the result as a win probability.
---

# Score Builtgraph Opportunities

Read [../query-builtgraph/references/live-mcp-playbook.md](../query-builtgraph/references/live-mcp-playbook.md).

## Workflow

1. Define the target firm, role, candidate set, decision date, explicit exclusions, and decision the
   prioritization supports.
2. Use the current MCP schemas to gather only evidence available by the decision date: demonstrated
   fit, observed prior participation, relevant activity, team context, and coverage quality.
3. Keep fit, relationship evidence, timing, and confidence as separate dimensions. Expose cold
   starts and missing evidence instead of filling them with neutral values.
4. Return explainable tiers and evidence counts. Use qualitative tiers unless the user supplies an
   approved, documented scoring model and the inputs it requires.
5. Pair public evidence with private capacity, pricing, conflicts, and proposal-quality inputs only
   when the user provides or authorizes them.

## Guardrails

- Historical winners do not define the unsuccessful choice set. Never turn silence into a loss.
- Co-participation is familiarity evidence, not favoritism, access, or future selection.
- Call a score a win probability only when a separately governed model has documented calibration
  and out-of-time validation. Otherwise describe research priority and confidence.
- Keep the final pursuit decision with the user.
