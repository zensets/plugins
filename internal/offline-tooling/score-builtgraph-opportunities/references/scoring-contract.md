# Transparent scoring contract

## Inputs

Use canonical `projects.csv`, `organizations.csv`, and `relationships.csv` as described by the Builtgraph bundle. Relationships need `project_id`, `organization_id`, `role`, and preferably `effective_date`, `source_date`, and `status`.

## Baseline features

The deterministic baseline scores each candidate project from 0 to 100:

- 35 points: target firm's prior projects with the owner, capped at five.
- 20 points: target firm's same-sector project history, capped at ten.
- 15 points: target firm's same-state project history, capped at ten.
- 20 points: role fit, based on prior projects in the requested role, capped at ten.
- 10 points: recency, when the most recent prior relationship is within three years.

The baseline is an interpretable prioritization heuristic called `observed-market-baseline-v1`. It is not calibrated and must not be labeled as win probability.

`relationship_risk = 100 - owner_relationship_points / 35 * 100`. This measures sparse observed owner history only. It is not a claim about the owner's behavior, procurement fairness, project risk, or the firm's actual ability to win.

## Time boundary

For a candidate decision date `T`, include only historical projects and relationship evidence with an effective/project date before `T` and `source_date <= T`. Exclude the candidate project itself.

## Future model validation

Train only on known candidate sets and outcomes. Keep inferred candidates scoring-only. Use chronological holdouts, compare against uniform and incumbent baselines, report calibration and log loss, and retain an untouched later cohort.

## Winner-only history

If awards identify selected firms but do not identify the unsuccessful respondents, do not
construct negative labels. Estimate an owner's role-specific historical selection distribution
instead. Report candidate selection count, recency-weighted share, smoothed affinity, owner
concentration, incumbent share, context fit, sample size, and temporal coverage. Normalize
scores across firms only when the user supplies a comparison set, and label the result as a
relative modeled share rather than unconditional win probability.
