# Project Intake Routing Demo

This is an independently recreated demonstration of a marketing-operations pattern I have used professionally: routing incoming work according to established ownership rules.

The company, people, requests, categories, and data in this demo are fictional. This is not employer production code.

## Scenario

A fictional marketing team receives requests through a shared intake process. Different request types have established owners, but manually assigning every request creates unnecessary administrative work.

This demo separates the process into three parts:

1. **Intake data** — new requests waiting to be routed.
2. **Routing rules** — the team's explicit ownership map.
3. **Automation** — Python applies those rules, validates the request, and records the proposed or completed routing decision.

That separation matters. The automation does not decide who *should* own the work. The team defines ownership; the automation consistently applies the rule.

## Try it safely

The script defaults to dry-run mode:

```bash
python route_requests.py
```

Dry run shows the proposed changes without writing a routed output file.

To simulate an approved live run against the fictional dataset:

```bash
python route_requests.py --apply
```

This creates `output/routed_requests.csv`.

## Example

An incoming request for a product launch is matched to the fictional Product Marketing owner. An unmatched category is not guessed; it is flagged for manual review.

That behavior reflects an important automation principle: when the business rule is unknown, escalate rather than invent.

## Files

- `route_requests.py` — routing and validation logic
- `data/incoming_requests.csv` — fictional intake records
- `config/routing_rules.json` — fictional ownership map
- `examples/expected_output.csv` — example applied result
- `.github/workflows/intake-routing-demo.yml` — manual GitHub Actions demonstration

## What this demonstrates

Requirements translation · Business-rule design · Python · JSON · CSV processing · Dry-run validation · Exception handling · GitHub Actions

## Production context

In a real implementation, the input and update layers could be replaced with API calls to a work-management platform. Credentials would be stored as repository secrets rather than committed to source control.

The point of this demo is the workflow pattern and validation approach, not a specific vendor integration.
