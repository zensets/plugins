# Builtgraph Research Guidance

Use Builtgraph as an evidence source for questions about AEC and real-estate actors, work, places,
and relationships. Use the MCP descriptions as the authoritative contract for current capabilities
and request formats.

## Choose a task-oriented path

- **Research an actor or place:** resolve the subject, review its available facts, then follow only
  the relationships relevant to the user's decision.
- **Understand a firm or market:** establish observed work and roles, compare relevant peers or
  buyers, and investigate the few organizations that materially affect the conclusion.
- **Assess current activity:** define a geography and time window, identify relevant activity, then
  enrich selected results with participants and relationship context.
- **Investigate a building or project:** establish the correct identity, examine the observed team
  and activity, and follow ownership, design, construction, financing, or affiliation paths only as
  needed.
- **Review planning or environmental activity:** identify recent movement, inspect the applications
  that fit the question, and research the applicants and specialists that appear in the evidence.
- **Trace a person or organization:** preserve ambiguous identities and distinguish observed
  affiliation from verified current employment, control, or influence.

Prefer the shortest sequence that answers the question. Follow an adjacent path only when it could
materially change the decision or reveal a useful contradiction.

## Work with the available evidence

- Choose research actions from the current MCP descriptions. Do not turn the answer into a tool log
  or repeat implementation details that do not help the user decide.
- Preserve returned identifiers, aliases, and identity uncertainty when they affect traceability.
- Request only evidence relevant to the question. Carry material freshness, missingness, and scope
  qualifications into the conclusion.
- Treat an empty result as inconclusive until identity, scope, and time window have been checked.

## Public evidence standards

- Separate `Observed`, `Claimed`, `User-provided`, `Inferred`, and `Unknown` evidence when the
  distinction changes the conclusion.
- Historical participation or co-occurrence does not prove a bid, loss, endorsement, preferred
  status, current team membership, legal control, an available role, or future selection.
- Never describe an unnamed participant, missing relationship, or unfilled evidence field as
  `open`, `available`, or `unassigned`. Say that Builtgraph does not name a participant and that
  actual procurement status is unknown. If a returned field uses one of those labels, translate it
  into this evidence-safe language; do not repeat the source label in the answer, even in a caveat.
- Counts describe the observed dataset and chosen scope. Do not convert them into market share,
  total-market claims, or calibrated probabilities without representative evidence and validation.
- Preserve point-in-time boundaries. Unknown freshness, missing dates, and incomplete history must
  remain visible rather than becoming negative findings.
- When external research is necessary, label it separately from Builtgraph evidence and retain its
  provenance. Never imply an external discovery result came from Builtgraph.
- If Builtgraph cannot substantiate part of a request, state that narrowly and offer a useful next
  step without describing internal architecture or publishing a capability-gap catalog.

## Validate an active architect or incumbent

When the question concerns an active architect, incumbent, or architectural opportunity, validate
the specific `building + scope + sponsor + capital event + time window`. A building-level architect
list alone does not establish who holds the commission under investigation.

Before judging the incumbent, establish the resolved building and project identity, current sponsor,
target scope, triggering acquisition, financing, filing, announcement, or procurement event, and the
as-of date. Inspect filing-level details rather than relying only on a team summary. Preserve each
relevant filing or project id, date, status, scope description, license type, professional, firm
mapping and its evidence, and whether the work predates or postdates the triggering event.

Treat a permit-side `architect_of_record` value as a filing-role label. A PE is a design professional
on that filing, not necessarily an architect. An RA on a filing is not necessarily the prime
architect for the building or capital program. Resolve an RA to a firm only when the returned
evidence or a dated authoritative source supports that identity.

Classify the result as one of:

- `Confirmed active architect`: dated evidence explicitly connects the firm to the target scope and
  sponsor, such as an owner announcement, executed award, current firm project page, or
  scope-matching filing with a supported firm identity.
- `Strong active indication`: a recent scope-matching filing names an RA, the RA-to-firm mapping is
  supported, and the timing aligns with the current sponsor and capital event. Seek a second source
  when practical.
- `Filing professional only`: a recent filing names an RA or PE, but the evidence does not connect
  that professional to the target commission.
- `Historical architect`: the evidence predates the current sponsor or capital event and no source
  demonstrates continuation.
- `Unknown`: no evidence establishes the architecture firm responsible for the target scope;
  procurement status remains unknown.

Record `scope_match` as `exact`, `adjacent`, `unrelated`, or `unknown`, and
`capital_event_alignment` as `after_event`, `before_event`, `continuation_confirmed`, or `unknown`.
Tenant improvements, signage, routine facade work, engineering systems, temporary construction, and
other unrelated filings do not establish the architect for a whole-building conversion or
repositioning. Evidence predating a sponsor change does not establish continuation unless a source
explicitly confirms it.

Do not describe a commission as claimed, unclaimed, open, available, or unassigned. When sources
conflict, report the competing scopes, dates, and identities rather than selecting an incumbent
silently.

## Answer shape

Lead with the decision-relevant finding. Show the most useful few results rather than an exhaustive
record dump, followed by claim-specific evidence, subject identifiers where useful, scope and as-of
date, material adjacent findings, and only the limitations that affect confidence. Recommend at most
a few concrete next investigations. Offer an appendix when the user would benefit from exhaustive
records or a detailed evidence trail.
