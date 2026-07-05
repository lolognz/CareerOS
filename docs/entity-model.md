# CareerOS Entity Model

CareerOS stores professional knowledge as entities because a career is not a single document. It is a network of organizations, roles, projects, stories, skills, technologies, publications, talks, and achievements.

Entities make each piece of knowledge addressable, reusable, and traceable.

## Why Entities

An entity is a canonical record for one professional thing.

Examples:

- A company.
- A role.
- A project.
- A concrete story.
- A skill.
- A technology.
- A publication.
- A talk.
- An achievement.

Storing knowledge this way prevents the same fact from being rewritten in many places. If a project date changes, the project entity changes once. Outputs that depend on it can be regenerated.

## Relationships Matter More Than Folders

Folders make the repository navigable, but relationships make the knowledge useful.

A project may belong to a company, happen during a role, demonstrate skills, use technologies, produce achievements, and contain stories. The folder path only says "this is a project." The relationships explain what the project means inside the career system.

AI agents should therefore prioritize entity IDs and relationship fields over folder location when reasoning about the knowledge base.

## One Project, Many Outputs

One project can generate dozens of outputs without duplicating the project itself.

For example, the same project entity can support:

- A short resume bullet.
- A long portfolio case study.
- A LinkedIn project entry.
- A technical interview answer.
- A behavioral interview story.
- A cover letter paragraph.
- A website page.
- A skills evidence map.
- A recruiter summary.

Each output selects and formats different parts of the same source entity. If the output is wrong, the source project or its relationships should be corrected, then the output should be regenerated.

## Why AI Should Edit Entities Instead Of CVs

CVs and resumes are generated views. They are compressed, audience-specific, and disposable.

If an AI edits a CV directly, it creates drift: the CV may say something that the knowledge base does not know, and future outputs will become inconsistent.

If an AI edits entities instead, it improves the source of truth. Every future CV, portfolio page, interview answer, or profile can benefit from the same correction.

The correct workflow is:

```text
Raw knowledge -> Entity update -> Relationship update -> Generated output
```

Never reverse that flow by treating a generated output as canonical knowledge.

## Design Rules

- Store each fact in the entity where it belongs.
- Use relationships instead of copying context.
- Preserve evidence and source traceability.
- Keep chronology explicit.
- Keep outputs disposable.
- Leave unsupported claims out of entities.
- Let folders organize files, but let relationships organize knowledge.
