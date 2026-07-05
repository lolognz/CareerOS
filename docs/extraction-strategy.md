# CareerOS Extraction Strategy

This document defines how CareerOS should extract structured knowledge from long-form raw interviews.

It does not extract personal information. It defines the pipeline agents should follow when raw interview content exists.

## Source Inputs

The canonical raw interview is:

- `knowledge/raw/interviews/master-career-interview.md`

Templates for structured entities live in:

- `templates/`

The current master interview contains no career content yet. Future extraction must start only after raw interview material is added under the `# Interview` section.

## Extraction Goal

The goal is to transform raw interview material into structured, traceable knowledge without losing context or inventing facts.

Extraction should preserve:

- Original chronology.
- User voice.
- Evidence and source references.
- Distinction between facts, interpretations, and unresolved claims.
- Relationships between entities.

Extraction should not produce final CVs, bios, LinkedIn text, interview answers, or portfolio pages. Those belong to the generated output layer.

## Entity Types To Extract First

Extract entities in the order that creates stable anchors before dependent details.

1. `companies`
2. `roles`
3. `projects`
4. `education`
5. `publications`
6. `talks`
7. `awards`
8. `stories`
9. `technologies`
10. `skills`
11. `principles`

This order minimizes duplicate work because companies, roles, projects, education, publications, talks, and awards provide factual anchors. Stories, technologies, skills, and principles can then reference those anchors instead of repeating their context.

## Entity Dependencies

### Companies

Companies are primary context anchors.

They may be referenced by:

- Roles
- Projects
- Stories
- Publications
- Talks
- Awards

Companies should not depend on detailed project or story extraction.

### Roles

Roles depend on companies when the role occurred inside or for an organization.

Roles may be referenced by:

- Projects
- Stories
- Skills
- Technologies
- Publications
- Talks
- Awards

### Projects

Projects may depend on companies and roles.

Projects may be referenced by:

- Stories
- Skills
- Technologies
- Publications
- Talks
- Awards
- Principles

### Education

Education may reference skills, technologies, projects, publications, talks, and awards, but it should first be created as its own factual record when raw material supports it.

### Publications, Talks, And Awards

Publications, talks, and awards may depend on companies, roles, projects, education, skills, and technologies.

When their surrounding context is unclear, create the entity with source traceability and leave uncertain relationships unresolved.

### Stories

Stories depend on raw narrative fragments and may reference companies, roles, projects, skills, technologies, and principles.

Stories should not be used as the only place to store company, role, or project facts.

### Technologies

Technologies should be extracted from demonstrated use, not from generic lists.

They may reference roles, projects, stories, education, publications, and talks.

### Skills

Skills depend on evidence-bearing entities.

They should reference projects, roles, stories, technologies, education, publications, talks, and awards that demonstrate the skill.

### Principles

Principles should be extracted last.

They depend on repeated patterns across stories, projects, roles, and raw interview fragments. They should not be created from generic values or isolated statements unless the user explicitly frames them as durable principles.

## Extraction Order That Minimizes Duplication

Use this staged order:

1. Identify raw fragments and assign stable fragment references.
2. Extract organization anchors into `companies`.
3. Extract time-bound responsibility anchors into `roles`.
4. Extract work units into `projects`.
5. Extract education, publications, talks, and awards as factual artifacts.
6. Extract concrete examples into `stories`.
7. Extract technologies from demonstrated usage.
8. Extract skills from evidence-bearing usage.
9. Extract principles from repeated evidence and user-stated philosophy.
10. Create relationships between entities.
11. Review unresolved ambiguities before continuing.

This avoids copying the same company, role, or project context into every downstream entity.

## Information That Must Never Be Duplicated

Do not duplicate:

- Company descriptions across roles, projects, and stories.
- Role titles, dates, employment type, or location outside role entities.
- Project summaries, outcomes, architecture, or decisions inside skills or technology files.
- Story narratives inside project, role, skill, or principle files.
- Skill definitions inside every project that demonstrates the skill.
- Technology usage lists across multiple entity bodies when references can express the relationship.
- Evidence links across unrelated entities unless the same evidence directly supports each one.
- Generated phrasing from outputs into structured knowledge.
- Raw interview wording into many structured files when a source fragment reference is enough.

Use stable IDs and relationship fields instead.

## Relationships To Create Automatically

When source evidence is clear, agents or scripts should create these relationships automatically:

- Company to role when a role names the company.
- Company to project when a project happened at or for the company.
- Role to project when the role performed or owned the project.
- Role to story when the story happened during that role.
- Project to story when the story describes a concrete project event.
- Project to technology when the technology was used in the project.
- Project to skill when the project demonstrates the skill.
- Story to skill when the story demonstrates the skill.
- Story to technology when a technology is part of the story.
- Story to principle when the story demonstrates a principle.
- Education to skill or technology when the raw source directly connects them.
- Publication to project, skill, or technology when the publication discusses or demonstrates them.
- Talk to project, skill, technology, or publication when the talk is about them.
- Award to the company, role, project, education, publication, talk, skill, or technology it recognizes.

Automatic relationships must include traceability to source fragments or evidence. If the relationship is plausible but not explicit, leave it unresolved.

## Ambiguities To Leave Unresolved

Do not guess:

- Exact dates when the raw interview gives only approximate timing.
- Whether two similar company names are the same organization.
- Whether a title was formal, informal, translated, or inferred.
- Whether a project was professional, academic, personal, open-source, or internal.
- Whether a technology was personally used, merely present in the environment, or used by others.
- Whether a result was caused by the user's work or only happened in the same period.
- Whether a metric is exact, estimated, or aspirational.
- Whether a story demonstrates a skill or principle without clear evidence.
- Whether a publication, talk, or award is public, internal, draft, or planned.
- Whether a claim should be included in generated outputs.

Represent unresolved items as review notes or pending relationship candidates. Do not convert them into facts.

## Merging Future Interviews

Future interviews should enrich existing entities instead of creating duplicates.

Use this merge process:

1. Segment the new interview into source fragments.
2. Compare each fragment against existing structured entities by name, alias, date range, company, role, project, and evidence.
3. If a clear match exists, update the existing entity with new source fragment references and missing details.
4. If a possible match exists, create a pending merge note for human review.
5. If no match exists, create a new entity from the relevant template.
6. Preserve conflicting information as unresolved until a human confirms the correct version.
7. Update relationship fields after entity matches are confirmed.

Do not create a new entity only because a future interview uses different wording for the same thing.

## Iterative Human-Reviewed Workflow

Extraction should happen in small, reviewable iterations.

### Iteration 0: Source Preparation

- Confirm the raw interview is present.
- Segment the interview into stable fragments.
- Do not extract entities yet.
- Human review: approve fragment boundaries and source IDs.

### Iteration 1: Anchors

- Extract companies, roles, and broad date ranges.
- Record unresolved date, title, and organization ambiguities.
- Human review: confirm identity, chronology, and naming.

### Iteration 2: Work Units

- Extract projects and education records.
- Link them to confirmed companies and roles where supported.
- Human review: confirm project boundaries and whether work units are distinct or merged.

### Iteration 3: External Artifacts

- Extract publications, talks, and awards.
- Link them to confirmed entities only when supported.
- Human review: confirm metadata, public/internal status, and evidence.

### Iteration 4: Stories

- Extract concrete stories from raw fragments.
- Link stories to confirmed companies, roles, projects, skills, technologies, and principles only where supported.
- Human review: confirm narrative boundaries and whether the story preserves the user's voice.

### Iteration 5: Technologies And Skills

- Extract technologies from demonstrated use.
- Extract skills from evidence-bearing roles, projects, stories, education, publications, talks, and awards.
- Human review: confirm skill labels, technology categories, and evidence strength.

### Iteration 6: Principles

- Extract principles only from repeated patterns or explicit user statements.
- Link principles to stories and projects that demonstrate them.
- Human review: confirm that principles reflect the user's actual philosophy, not generic branding.

### Iteration 7: Relationship Audit

- Check bidirectional and cross-entity references.
- Remove duplicated facts.
- Flag unsupported claims.
- Human review: approve the structured knowledge graph before any generated outputs are created.

## Completion Criteria

An extraction pass is complete only when:

- Every structured fact has a source fragment or evidence reference.
- No generated output has been created as part of extraction.
- Duplicated facts have been replaced with links.
- Ambiguities are explicitly marked for review.
- A human has reviewed the current iteration before the next layer is built.
