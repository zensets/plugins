# Builtgraph canonical CSV contract

A bundle is a directory containing these UTF-8 CSV files. Extra columns are allowed.

## `projects.csv`

Required: `project_id`, `project_name`.

Recommended: `owner_org_id`, `city`, `state`, `country`, `sector`, `project_type`, `stage`, `announced_date`, `bid_date`, `start_date`, `completion_date`, `estimated_value`, `currency`, `source_date`, `source_url`.

Dates use ISO 8601. `source_date` is when the evidence was observed or published, not the project date. Money remains in its stated currency unless a documented conversion is applied.

## `organizations.csv`

Required: `organization_id`, `organization_name`.

Recommended: `organization_type`, `city`, `state`, `country`, `website`, `source_date`, `source_url`.

## `relationships.csv`

Required: `relationship_id`, `project_id`, `organization_id`, `role`.

Recommended: `status`, `effective_date`, `end_date`, `source_date`, `source_url`, `confidence`.

Use normalized roles such as `owner`, `architect`, `general_contractor`, `construction_manager`, `engineer`, `subcontractor`, `bidder`, and `awardee`. Keep source wording in an extra `role_raw` column.

## Point-in-time rule

For an as-of date `T`, include only rows with `source_date <= T`; if source date is absent, label the row temporally unverified rather than silently treating it as current.
