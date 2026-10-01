"""Fictional request reporting and archival demonstration."""

from __future__ import annotations
import csv
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CANCELLED = "Cancelled"

with (BASE_DIR / "data" / "requests.csv").open(newline="", encoding="utf-8") as f:
    requests = list(csv.DictReader(f))

archive = [r for r in requests if r["status"] == CANCELLED]
reportable = [r for r in requests if r["status"] != CANCELLED]

summary = defaultdict(lambda: {"total": 0, "open": 0, "complete": 0})
for request in reportable:
    key = (request["created_month"], request["business_group"])
    summary[key]["total"] += 1
    if request["status"] == "Complete":
        summary[key]["complete"] += 1
    else:
        summary[key]["open"] += 1

print("REQUEST REPORTING — FICTIONAL DATA")
print(f"Active/reportable records: {len(reportable)}")
print(f"Archived cancelled records: {len(archive)}")
print("-" * 72)
for (month, group), metrics in sorted(summary.items()):
    print(f"{month} | {group}: {metrics['total']} total | {metrics['open']} open | {metrics['complete']} complete")
