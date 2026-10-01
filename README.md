# Marketing Operations Automation Portfolio

I build operational systems that help teams move work with less manual coordination and better visibility.

This repository documents selected patterns from my professional work in **marketing operations, workflow design, automation, reporting, and AI-assisted development**. The examples here are intentionally sanitized. They demonstrate how I approach operational problems without publishing employer-owned production code, credentials, internal data, proprietary documentation, or confidential configurations.

## The way I build

My work starts with the people doing the work—not with Python.

`Stakeholder need → Process discovery → Workflow design → AI-assisted development → Dry-run testing → Validation → Deployment → Documentation`

I first determine what the team actually needs, how the workflow should behave, what information needs to exist, where ownership belongs, and what should or should not be automated. I then use AI as a development partner to translate that logic into scripts, API interactions, formulas, and scheduled workflows.

Before an automation touches a live system, I test it in a controlled environment and review the proposed changes. Once validated, recurring workflows can be deployed through GitHub Actions so the background logic operates without someone manually running it.

## Start here

If you're reviewing this portfolio for an operations, program, or automation role, these are the fastest ways to explore it:

| Explore | What you'll see |
| --- | --- |
| **[Working Project Intake Routing Demo](demos/project-intake-routing/README.md)** | A runnable Python example with fictional data, configurable business rules, dry-run safeguards, exception handling, and a GitHub Actions workflow. |
| **[Team Capacity Planning](case-studies/team-capacity-planning.md)** | How I translated real working patterns into a more useful workload and capacity model. |
| **[Request Reporting & Archival](case-studies/request-reporting.md)** | How lifecycle states, historical reporting, and automated refresh logic were designed together. |
| **[Project Risk & Daily Management](case-studies/project-risk-dashboard.md)** | How detailed task data was translated into a leadership-level project-health signal. |

### Working demonstration

The **[Project Intake Routing Demo](demos/project-intake-routing/README.md)** is the best place to see the technical side of my approach. It is an independently recreated example—not employer production code—and shows the progression from a defined ownership model to a safe, testable automation.

```text
Fictional intake request
        ↓
Validate request fields
        ↓
Read configurable routing rules
        ↓
Known project type? ── No ──→ Manual Review
        │
       Yes
        ↓
Propose owner assignment
        ↓
DRY RUN by default
        ↓
Approved apply mode / scheduled workflow
```

## Selected case studies

### Team Capacity Planning

A task-count-only view of capacity can be misleading. Some roles spend substantial time in meetings, coaching, coordination, and other work that does not naturally appear as project tasks.

The system I designed combined task-based workload information with role-aware capacity assumptions rather than forcing every activity into the project-management system. It also accounted for recurring sprint identifiers and calendar-year resets.

**What this demonstrates:** operational discovery, capacity-model design, exception handling, scheduled automation, and translating how a team actually works into system logic.

[Read the sanitized case study](case-studies/team-capacity-planning.md)

### Project Intake Routing

New marketing projects need consistent ownership, but manually assigning every incoming request creates administrative work and increases the chance of routing errors.

I designed an intake workflow where project type and defined business rules determine the appropriate owner automatically. The automation handles the repetitive routing while the team retains ownership of the underlying process and exceptions.

**What this demonstrates:** intake architecture, business-rule translation, workflow automation, ownership mapping, and validation before production changes.

[Read the sanitized case study](case-studies/project-intake-routing.md)

### Request Reporting & Archival

A shared-services team needed recurring visibility into incoming work without manually rebuilding reports. A key complication was cancellation handling: removing cancelled requests entirely would make historical reporting inaccurate, while leaving them mixed with active work could distort current metrics.

The workflow incorporated archival logic so cancelled work could be retained historically while operational metrics remained useful. Reporting data could then refresh on a recurring schedule.

**What this demonstrates:** stakeholder requirements, reporting architecture, lifecycle states, archival strategy, scheduled automation, and data-quality thinking.

[Read the sanitized case study](case-studies/request-reporting.md)

### Project Risk & Daily Management

Leadership needed a simple way to understand whether active project work was drifting into risk.

I helped translate task-level status into a portfolio-level metric based on the share of open tasks flagged as overdue or at risk. That metric fed a daily-management view so leadership could see the signal without manually reviewing every task.

**What this demonstrates:** metric definition, leadership reporting, operational dashboards, data aggregation, and converting detailed project information into an actionable management signal.

[Read the sanitized case study](case-studies/project-risk-dashboard.md)

## Technical approach

Typical tools and methods in this work include:

- Smartsheet and structured project-management systems
- Python for workflow and data automation
- REST APIs for system interaction
- GitHub Actions for scheduled execution
- Google Colab for development and controlled testing
- Dry-run logic for validating proposed changes
- AI-assisted development for translating requirements into implementation
- Documentation of API behavior, edge cases, and reusable patterns

## AI-assisted development

I use AI as a development partner rather than treating generated code as the finished solution.

The operational problem, workflow architecture, business rules, exceptions, and validation criteria come first. AI helps accelerate implementation and troubleshooting. I review behavior against the intended workflow, test changes before production, and iterate when the real-world process exposes an edge case the initial implementation did not account for.

That distinction matters: the objective is not to generate code. The objective is to build a system that works for the people relying on it.

## What is intentionally not here

This repository does **not** contain production source code from my employer, API credentials, sheet or workspace IDs, internal employee mappings, internal datasets, proprietary business rules, or confidential screenshots.

Working demonstrations added to this portfolio use fictional data and independently recreated logic.

## About the work

The professional systems that informed these case studies were developed by me as part of my employment. This portfolio documents my role, decisions, problem-solving approach, and technical methods while respecting employer ownership and confidentiality.

For me, automation is successful when the technology fades into the background and the work becomes easier to run.
