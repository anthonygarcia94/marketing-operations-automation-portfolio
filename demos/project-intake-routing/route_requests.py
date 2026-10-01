"""Fictional marketing project-intake routing demonstration.

This script is independently recreated for portfolio use. It does not contain
employer source code, internal mappings, IDs, credentials, or production data.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = BASE_DIR / "data" / "incoming_requests.csv"
DEFAULT_RULES = BASE_DIR / "config" / "routing_rules.json"
DEFAULT_OUTPUT = BASE_DIR / "output" / "routed_requests.csv"


def load_rules(path: Path) -> dict[str, str]:
    with path.open(encoding="utf-8") as file:
        rules = json.load(file)

    if not isinstance(rules, dict):
        raise ValueError("Routing rules must be a JSON object.")

    return {str(project_type).strip(): str(owner).strip()
            for project_type, owner in rules.items()}


def load_requests(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def route_request(request: dict[str, str], rules: dict[str, str]) -> dict[str, str]:
    routed = dict(request)
    project_type = request.get("project_type", "").strip()
    existing_owner = request.get("current_owner", "").strip()

    if existing_owner:
        routed["routing_status"] = "Already Assigned"
        return routed

    owner = rules.get(project_type)
    if owner:
        routed["current_owner"] = owner
        routed["routing_status"] = "Routed"
    else:
        routed["routing_status"] = "Manual Review"

    return routed


def write_output(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "request_id",
        "request_name",
        "project_type",
        "current_owner",
        "routing_status",
    ]

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Route fictional marketing requests.")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write the routed output. Without this flag, the script is dry-run only.",
    )
    args = parser.parse_args()

    rules = load_rules(DEFAULT_RULES)
    requests = load_requests(DEFAULT_INPUT)
    routed_requests = [route_request(request, rules) for request in requests]

    print("PROJECT INTAKE ROUTING")
    print(f"Mode: {'APPLY' if args.apply else 'DRY RUN'}")
    print("-" * 72)

    for before, after in zip(requests, routed_requests):
        previous = before.get("current_owner", "").strip() or "(unassigned)"
        proposed = after.get("current_owner", "").strip() or "(unassigned)"
        print(
            f"{before.get('request_id', '(missing id)')}: "
            f"{before.get('project_type', '(missing type)')} | "
            f"{previous} -> {proposed} | {after['routing_status']}"
        )

    if not args.apply:
        print("\nNo files changed. Re-run with --apply to write the fictional output.")
        return

    write_output(DEFAULT_OUTPUT, routed_requests)
    print(f"\nWrote routed results to: {DEFAULT_OUTPUT.relative_to(BASE_DIR)}")


if __name__ == "__main__":
    main()
