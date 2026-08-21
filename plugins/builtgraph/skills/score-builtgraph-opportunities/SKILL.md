---
name: score-builtgraph-opportunities
description: Rank and explain AEC project opportunities for contractors, architects, engineers, and subcontractors using Builtgraph project data and historical owner relationships. Use for lead prioritization, owner relationship risk, incumbent analysis, bid/no-bid support, cold-start detection, or estimating observed-market winnability from point-in-time evidence.
---

# Score Builtgraph Opportunities

## Workflow

1. Read `references/scoring-contract.md` and define the target firm, role, candidate projects, and decision date.
2. Build features only from evidence available before each decision date.
3. Run `scripts/score_opportunities.py` for the transparent baseline.
4. Review input coverage, identity matches, missing dates, and contribution-level explanations.
5. Rank projects as prioritization tiers. Do not call the score a win probability unless a calibrated model has passed documented out-of-time validation.
6. Pair the score with non-data considerations such as capacity, delivery model, procurement rules, scope fit, and conflicts when those inputs are actually available.

## Guardrails

- Treat prior co-participation as evidence of familiarity, not favoritism or guaranteed access.
- Never treat inferred candidates, planholders, or mentions as losses.
- Exclude award/winner evidence published after the decision date from predictive features.
- Expose cold starts and sparse evidence instead of assigning false precision.
- Keep public observed-market signals separate from private CRM, pricing, staffing, and proposal-quality signals.
- Return feature contributions, evidence counts, as-of date, model/version label, and limitations with every score.

## Command

```bash
python3 scripts/score_opportunities.py DATA_DIR \
  --firm-id firm-456 --role architect --as-of 2026-08-20 \
  --output scored-opportunities.csv
```

Use the result to prioritize research and outreach, not to automate bid decisions.

## Winner-only owner affinity

When historical winners are known but unsuccessful RFP respondents are not, use the
positive-only owner affinity analyzer. It reports recency-weighted historical selection
share, Bayesian-smoothed affinity, owner concentration, incumbent strength, context share,
and evidence confidence. It never labels unobserved firms as losers and never calls its
output a calibrated win probability.

```bash
python3 scripts/analyze_owner_affinity.py DATA_DIR \
  --owner-id org-related --firm-id org-hks --role architect \
  --as-of 2026-08-21 --sector mixed_use --state NY \
  --output related-hks-affinity.json
```
