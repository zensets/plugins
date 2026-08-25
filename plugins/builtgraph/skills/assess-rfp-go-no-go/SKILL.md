---
name: assess-rfp-go-no-go
description: Analyze an attached AEC RFP for pursuit risk and opportunity using a company ICP, Builtgraph relationships, teaming evidence, staffing inputs, and an explicit risk rubric. Use for go/no-go, bid/no-bid, teaming, hiring, compliance, or pursuit-readiness decisions; never make the final decision automatically.
---

# Assess RFP Go or No-Go

Read [references/risk-rubric.md](references/risk-rubric.md) before scoring. Treat the assessment as decision support for an accountable human reviewer.
Read [../query-builtgraph/references/live-mcp-playbook.md](../query-builtgraph/references/live-mcp-playbook.md)
before using Builtgraph evidence.

## Inputs

- attached RFP and addenda
- dated company ICP or enough firm context to assess fit
- company risk rubric when available
- current team capacity, hiring constraints, conflicts, pricing, and private CRM context only when provided or authorized

If the RFP or material pages are unavailable, stop and ask for them. If the company rubric is unavailable, use the provisional rubric and label it as not company policy.

## Workflow

1. Extract scope, disciplines, schedule, submission requirements, evaluation criteria, experience thresholds, team commitments, forms, commercial terms, insurance, and delivery obligations. Preserve page references.
2. Identify mandatory pass/fail requirements separately from scored considerations.
3. Compare the opportunity with the ICP and relevant observed experience.
4. Use the current MCP schemas to resolve the client and named team, review observed prior teams and
   relevant firm experience, and compare recent activity or project context when useful. Preserve
   completeness and identity limits rather than treating missing evidence as an open role.
5. Assess team completeness, named-person requirements, workload evidence supplied by the user, and hiring or specialist needs. Never infer internal capacity from public data.
6. Score each rubric dimension with evidence, confidence, and unresolved questions. A mandatory failure cannot be averaged away.
7. Return `Go`, `Conditional Go`, `No Go`, or `Insufficient Information`, with the conditions and accountable human decision explicitly shown.

## Output

Lead with the recommendation and a one-paragraph rationale. Include a pass/fail checklist, rubric scorecard, opportunity case, risk register, team-building options, staffing and hiring implications, submission requirements, unknowns, and next actions. Cite RFP page numbers and external evidence. Use tables and severity labels as the portable UI; do not imply an MCP-rendered component exists.

Flag legal, insurance, financial, safety, or contractual interpretations for qualified review rather than presenting them as professional advice.
Do not describe an RFP role as open merely because Builtgraph lacks a participant, or a historical
participant as an incumbent bidder. The RFP controls current requirements; Builtgraph supplies
observed context.
