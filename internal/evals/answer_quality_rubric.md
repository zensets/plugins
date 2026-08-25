# Builtgraph Answer Quality Rubric

Use this rubric for forward tests of public Builtgraph skills. Score each dimension from 0 to 2.
The maximum score is 14.

## Dimensions

1. **Decision relevance**
   - 0: Repeats records without answering the user's decision.
   - 1: Answers indirectly or buries the conclusion.
   - 2: Leads with a clear, appropriately bounded conclusion.
2. **Specificity**
   - 0: Generic advice or unsupported generalities.
   - 1: Some named evidence, but important claims remain vague.
   - 2: Names the relevant actors, work, roles, dates, and scope.
3. **Traceability**
   - 0: Material claims cannot be traced.
   - 1: Sources or IDs are present but detached from claims.
   - 2: Material claims carry nearby Builtgraph record IDs or clearly labeled external evidence.
4. **Interpretation**
   - 0: A record dump or invalid inference.
   - 1: Useful synthesis with limited adjacent discovery.
   - 2: Explains why findings matter and surfaces adjacent evidence likely to change the decision.
5. **Evidence discipline**
   - 0: Conflates observed evidence with procurement, control, current employment, or probability.
   - 1: Mostly disciplined but misses a material qualification.
   - 2: Separates observed, claimed, inferred, and unknown evidence and preserves identity/time bounds.
6. **Next-action quality**
   - 0: No action or an unsupported recommendation.
   - 1: Generic follow-up.
   - 2: A few concrete follow-ups tied to unresolved evidence or the user's decision.
7. **Concision and scanability**
   - 0: The useful answer is buried in exhaustive detail.
   - 1: Understandable but longer or denser than necessary.
   - 2: Decision-first, prioritized, and easy to scan; exhaustive detail is optional.

## Interpretation

- 12-14: useful for the stated decision with no material correction needed
- 9-11: useful with a notable omission, inference problem, or presentation cost
- 6-8: partially useful but requires analyst repair
- 0-5: unsuitable for decision support

Any unsupported procurement claim, current-team claim, legal-control claim, market-share claim, or
win probability is a critical failure regardless of total score.

