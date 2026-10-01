# Team Capacity Planning Demo

This independently recreated demo shows how a workload model can account for work that is not represented by project tasks.

## Scenario

A fictional marketing team plans work in recurring sprints. Task points provide a useful starting signal, but some roles also carry substantial meetings, coaching, coordination, or leadership work. Treating every role as if all capacity should appear as project tasks can produce misleading comparisons.

The demo combines task points with a configurable **task-capacity baseline** for each fictional team member. The baseline is not a judgment about productivity; it represents how much of that role's capacity is expected to appear in the task system.

## Run it

```bash
python calculate_capacity.py
```

The script defaults to dry-run/display behavior. It reads fictional sprint data and role assumptions, calculates utilization against the task baseline, and assigns a planning signal.

## Design principles

- Keep role assumptions in configuration rather than hard-coding them.
- Use a year-plus-sprint key so recurring sprint numbers remain unique.
- Do not force meetings and coaching into fake project tasks simply to make a metric look complete.
- Treat the output as a planning signal, not a performance score.
- Flag unusual workload for conversation rather than automating a people decision.

## Files

- `calculate_capacity.py` — capacity calculation
- `data/sprint_work.csv` — fictional workload
- `config/capacity_baselines.json` — fictional role-aware assumptions
- `examples/expected_output.csv` — example results

## What this demonstrates

Capacity modeling · Operational discovery · Configurable business logic · Python · Data validation · Human-centered automation

All people, workloads, thresholds, and data are fictional.
