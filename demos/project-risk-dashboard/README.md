# Project Risk Dashboard Demo

This independently recreated demo translates task-level status into a concise project-health signal for a fictional leadership dashboard.

## Scenario

Leadership does not need to inspect every task to begin a daily-management conversation. It needs a consistent signal that identifies projects where a meaningful share of open work is overdue or at risk.

For each project, this demo calculates:

`Task Risk % = risky open tasks / all open tasks × 100`

A task is considered risky in this fictional example when its status is **Overdue** or **At Risk**. Completed tasks are excluded from the denominator.

The demo uses a fictional 10% attention threshold for illustration only. It is not a production threshold.

## Run it

```bash
python calculate_risk.py
```

## Design principles

- Define the denominator before presenting a percentage.
- Exclude completed work from an active-risk measure.
- Keep the threshold visible and configurable.
- Use the metric as a management signal, not as a substitute for context.
- Handle projects with no open tasks explicitly.

## What this demonstrates

Metric design · Project-health reporting · Python · Data aggregation · Leadership dashboards · Operational decision support

All projects, tasks, thresholds, and data are fictional.
