"""Fictional team-capacity planning demonstration."""

from __future__ import annotations
import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def signal(utilization: float) -> str:
    if utilization > 100:
        return "Review Load"
    if utilization < 70:
        return "Capacity Available"
    return "Balanced"

with (BASE_DIR / "config" / "capacity_baselines.json").open(encoding="utf-8") as f:
    baselines = json.load(f)

with (BASE_DIR / "data" / "sprint_work.csv").open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

print("TEAM CAPACITY PLANNING — FICTIONAL DATA")
print("-" * 72)
for row in rows:
    member = row["team_member"].strip()
    if member not in baselines:
        print(f"{member}: missing baseline — manual review")
        continue
    points = float(row["task_points"])
    baseline = float(baselines[member])
    utilization = round(points / baseline * 100, 1)
    print(f"{row['sprint_label']} | {member}: {points:g}/{baseline:g} = {utilization}% | {signal(utilization)}")
