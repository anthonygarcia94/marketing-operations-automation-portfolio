"""Fictional project-risk dashboard calculation."""

from __future__ import annotations
import csv
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RISK_STATUSES = {"Overdue", "At Risk"}
ATTENTION_THRESHOLD = 10.0

with (BASE_DIR / "data" / "tasks.csv").open(newline="", encoding="utf-8") as f:
    tasks = list(csv.DictReader(f))

projects = defaultdict(list)
for task in tasks:
    projects[(task["project_id"], task["project_name"])].append(task)

print("PROJECT RISK DASHBOARD — FICTIONAL DATA")
print("-" * 72)
for (_, name), project_tasks in sorted(projects.items()):
    open_tasks = [t for t in project_tasks if t["status"] != "Complete"]
    risky = [t for t in open_tasks if t["status"] in RISK_STATUSES]

    if not open_tasks:
        print(f"{name}: No open tasks | Complete/No active risk measure")
        continue

    risk_pct = round(len(risky) / len(open_tasks) * 100, 1)
    signal = "Attention" if risk_pct >= ATTENTION_THRESHOLD else "Monitor"
    print(f"{name}: {len(risky)}/{len(open_tasks)} risky open tasks = {risk_pct}% | {signal}")
