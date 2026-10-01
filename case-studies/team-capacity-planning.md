# Team Capacity Planning

## The problem

A marketing team needed a clearer way to understand workload across recurring sprints. Counting tasks alone did not tell the full story. Some roles carried substantial meeting, coaching, coordination, and leadership responsibilities that were not represented as project tasks, which could make those people appear underutilized.

## My role

I worked through how the team actually operated before defining the automation logic. The goal was not to force every hour of work into the project-management system. It was to create a capacity model that produced a more useful planning signal.

## Design decisions

The workflow combined task-based workload data with role-aware capacity assumptions. Roles with significant non-task responsibilities could use a different baseline rather than requiring meetings and coaching work to be artificially converted into tasks.

The system also needed a stable sprint key. Because sprint numbers can repeat after an annual reset, the workflow uses a year-plus-sprint identifier rather than relying on the sprint number alone.

Scheduling was designed around the team's working day, including the practical issue of daylight-saving changes when scheduled automation is executed in UTC.

## Development and validation

The automation was developed with AI assistance after the workflow and business rules were defined. Changes were tested in a controlled environment using dry-run behavior before production execution.

Validation focused on whether the resulting capacity view matched the team's real operating context—not merely whether the script ran successfully.

## Outcome

The resulting system provided a more realistic workload signal for planning conversations while avoiding unnecessary administrative work for team members.

## Skills demonstrated

Workflow discovery · Capacity planning · Business-rule design · Python automation · API integration · GitHub Actions · Dry-run testing · Exception handling

## Confidentiality

This is a sanitized description of professional work. Names, internal thresholds, IDs, production code, datasets, and company-specific configuration are intentionally excluded.
