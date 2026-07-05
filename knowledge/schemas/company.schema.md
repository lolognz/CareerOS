# Company Entity Schema

## Purpose

A company entity represents a canonical organization within CareerOS.

It captures the stable knowledge needed to understand the organization's role in a professional career: identity, business context, chronology, related roles, projects, stories, technologies, skills, achievements, evidence, and links to other entities.

A company entity is not a resume section, employer summary, marketing description, or generated profile. It is the source record from which those outputs may be produced.

## Design Principles

Company entities are designed to preserve durable knowledge, not polished narrative.

Each company must have one canonical file. That file should identify the organization, locate it in time, connect it to related entities, and preserve the evidence needed to support claims about work performed there.

Company entities should favor explicit relationships over repeated prose. If a project, role, story, technology, skill, achievement, or evidence item has its own canonical entity, the company file should link to it by canonical ID instead of copying its content.

Company entities should remain useful over time. They should support future outputs without being shaped around any single resume, CV, website, or profile.

## Required Fields

| Field | Required | Description |
|---|---:|---|
| `id` | Yes | Stable canonical identifier for the company entity. |
| `name` | Yes | Canonical company name used throughout CareerOS. |
| `aliases` | Yes | Alternative names, abbreviations, former names, or commonly used variants. Use an empty list when none are known. |
| `industry` | Yes | Primary industry or industries associated with the company in the context of the career knowledge base. |
| `website` | Yes | Official company website when known. Use an explicit empty value when unknown. |
| `countries` | Yes | Countries relevant to the user's work, role, operations, or evidence for this company. |
| `chronology` | Yes | Time-bounded relationship between the user and the company, including known start dates, end dates, and uncertainty where applicable. |
| `business-context` | Yes | Factual context needed to understand the company, its domain, and the environment in which the user worked. |
| `roles` | Yes | Canonical IDs of roles associated with this company. |
| `projects` | Yes | Canonical IDs of projects associated with this company. |
| `stories` | Yes | Canonical IDs of stories associated with this company. |
| `technologies` | Yes | Canonical IDs of technologies associated with this company. |
| `skills` | Yes | Canonical IDs of skills associated with this company. |
| `achievements` | Yes | Canonical IDs of achievements associated with this company. |
| `evidence` | Yes | Canonical IDs of evidence items supporting facts in the company entity. |
| `related-entities` | Yes | Canonical IDs of related companies, people, publications, talks, awards, or other entities. |

## Optional Sections

Optional long-form sections may be included when they preserve source knowledge that cannot be represented clearly in the required fields alone.

Acceptable optional sections include:

- Background context that explains the company's relevance to the user's career.
- Notes on organizational changes, acquisitions, restructurings, or name changes.
- Source notes describing uncertainty, conflicting records, or evidence gaps.
- Historical context needed to interpret roles, projects, stories, or achievements.

Optional sections must remain factual, traceable, and source-oriented. They must not become generated summaries or output-ready prose.

## Relationships

Company entities relate to other CareerOS entities through canonical IDs.

Roles describe the user's position, responsibilities, team context, and time-bounded relationship to the company.

Projects describe bounded bodies of work associated with the company. A company file may list projects, but it must not duplicate project descriptions.

Stories preserve reusable professional narratives, decisions, challenges, conflicts, outcomes, and examples connected to the company. A company file may link to stories, but it must not duplicate story content.

Skills and technologies describe capabilities and tools used in the company context. A company file may link to them when the association is supported by roles, projects, stories, achievements, or evidence.

Achievements describe validated outcomes or accomplishments. A company file may link to achievements, but it must not restate them as resume bullets.

Evidence supports facts in the company entity and related entities. Claims about chronology, scope, role, work, impact, technologies, skills, or achievements must be traceable to evidence.

## Validation Rules

- Each company must have exactly one canonical company file.
- The `id` must be stable and unique across all company entities.
- Links to other entities must use canonical IDs.
- Required fields must be present, even when the value is explicitly empty or unknown.
- Chronology must preserve known dates, date ranges, and uncertainty.
- Facts must be supported by evidence or marked as unsupported.
- Stories must not be duplicated inside the company entity.
- Projects must not be duplicated inside the company entity.
- Role details must not be duplicated when a canonical role entity exists.
- Technologies, skills, achievements, and evidence must be linked rather than copied when canonical entities exist.
- Generated outputs must not introduce facts that are absent from the company entity or its linked canonical sources.
- Ambiguous or conflicting information must be recorded explicitly instead of silently resolved.

## Anti-patterns

The following must never appear inside a company entity:

- Resume bullets.
- Marketing language.
- Unsupported claims.
- Duplicate project descriptions.
- Duplicate story text.
- Generated summaries.
- Polished output prose intended for a resume, CV, website, profile, bio, or cover letter.
- Claims of impact without supporting evidence.
- Invented context used to make the career narrative more compelling.
- Copied content from related canonical entities when a link would preserve the relationship.

## Example Skeleton

```markdown
# Company: [Canonical Name]

## Canonical Fields

| Field | Value |
|---|---|
| id |  |
| name |  |
| aliases |  |
| industry |  |
| website |  |
| countries |  |
| chronology |  |
| business-context |  |
| roles |  |
| projects |  |
| stories |  |
| technologies |  |
| skills |  |
| achievements |  |
| evidence |  |
| related-entities |  |

## Background


## Source Notes


```
