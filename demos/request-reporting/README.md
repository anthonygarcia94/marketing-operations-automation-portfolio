# Request Reporting & Archival Demo

This independently recreated demo shows how request lifecycle rules can preserve historical activity while keeping current reporting useful.

## Scenario

A fictional shared-services team tracks requests across multiple business groups. Leadership wants recurring monthly counts, but cancelled work creates a reporting problem: deleting it destroys history, while counting it as active work distorts current workload.

This demo classifies requests into **active reporting** and **archive history**, then produces a compact monthly summary.

## Run it

```bash
python build_report.py
```

The script does not alter the source file. It displays the archival decisions and aggregated reporting output.

## Design principles

- Preserve cancelled work as history.
- Separate lifecycle handling from reporting logic.
- Keep the source dataset unchanged in the demo.
- Make status rules explicit and reviewable.
- Aggregate only after lifecycle classification.

## What this demonstrates

Reporting architecture · Lifecycle design · Archival logic · Python · CSV processing · Data quality · Operational metrics

All organizations, requests, statuses, and data are fictional.
