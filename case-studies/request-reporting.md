# Request Reporting & Archival

## The problem

A shared-services workflow needed recurring visibility into incoming requests without requiring someone to manually rebuild reporting each time.

Cancellation handling created an important data-design question. Deleting cancelled requests would remove useful historical context. Keeping them indistinguishable from active work could distort current operational reporting.

## My role

I worked from the reporting need backward: what leadership needed to understand, what lifecycle states mattered, how cancelled work should be represented, and how the reporting layer could stay current without recurring manual maintenance.

## Solution

The workflow incorporated an archive for cancelled requests so historical activity could be retained without treating those requests as active work.

Automated reporting logic then refreshed the relevant metrics on a recurring schedule, creating a more reliable operational view without requiring a person to continually reconstruct it.

## Development and validation

The business rules and reporting structure were defined first. AI-assisted development was then used to help implement the automation.

Testing used dry-run behavior to inspect proposed changes against the expected workflow before production execution. Edge cases and platform/API behavior discovered during implementation were documented for reuse.

## Outcome

The system preserved historical request information while improving the usefulness and freshness of current reporting.

## Skills demonstrated

Reporting architecture · Data lifecycle design · Archival strategy · Python automation · API integration · Scheduled workflows · Data quality · Documentation

## Confidentiality

This case study is intentionally generalized. Internal reporting dimensions, business-unit names, production code, identifiers, and company data are not included.
