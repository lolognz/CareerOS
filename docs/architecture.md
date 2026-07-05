# CareerOS Architecture

CareerOS is organized as a source-first professional knowledge system.

The architecture separates canonical knowledge from generated outputs. Source files describe what is true. Generation tools decide how that truth should be shaped for a specific audience, format, or goal.

## System Overview

```text
knowledge/ + assets/
        |
        v
templates/ + validation + AI workflows
        |
        v
generation layer
        |
        v
generated outputs
```

The central rule is simple: outputs never become authoritative. If an output is inaccurate, incomplete, or poorly phrased, the source knowledge is corrected first and the output is generated again.

## Knowledge Base

The `knowledge/` directory contains the canonical professional record.

It should store:

- Professional profile information.
- Companies and roles.
- Projects and initiatives.
- Stories and concrete examples.
- Skills, technologies, domains, values, and roles.
- Talks, publications, awards, and other professional artifacts.
- Chronology and timeline information.
- Evidence and references.

Knowledge files should be structured Markdown: frontmatter for machine-readable metadata, followed by human-readable sections.

## Data Model

CareerOS uses a lightweight file-based data model.

### Entities

Entities live under `knowledge/entities/`. Each entity should have a stable `id`, a `type`, and structured metadata in frontmatter.

Typical entity types include:

- `company`
- `project`
- `story`
- `technology`
- `skill`
- `talk`
- `publication`
- `person`

Entity files are the canonical place for facts about that entity.

### Relations

Relations live under `knowledge/relations/`.

They make cross-entity links explicit, for example:

- Companies to projects.
- Companies to skills.
- Projects to technologies.
- Projects to stories.
- Technologies to skills.

Relations prevent the system from copying the same fact into many files. When a generator needs context, it can traverse relations instead of relying on duplicated prose.

### Indexes

Indexes live under `knowledge/indexes/`.

They are navigation aids and lookup surfaces. They should help humans and tools find relevant knowledge quickly, but they should not replace canonical entity files.

### Taxonomy

Taxonomy files live under `knowledge/taxonomy/`.

They define shared vocabulary for classification. This keeps generation consistent across outputs and reduces small variations that become hard to maintain over time.

## Generation Layer

The generation layer is responsible for turning source knowledge into useful career outputs.

It may eventually include:

- Scripts in `scripts/`.
- Prompt templates.
- Schema validators.
- Static site generators.
- Document exporters.
- AI-agent workflows.
- Tests that verify source coverage and output provenance.

Generation should be deterministic where possible and grounded where AI is used. Generated content must be traceable back to the knowledge base.

## Outputs

Outputs belong in `generated/`.

Examples include:

- CVs and resumes.
- LinkedIn profile sections.
- Personal website content.
- Portfolio pages.
- Short and long bios.
- Interview answer banks.
- Cover letters.
- Recruiter summaries.
- JSON or API-ready exports.

Generated outputs are disposable. They can be deleted and recreated. They should not contain unique professional facts that are missing from `knowledge/`.

## AI Workflows

AI agents working with CareerOS must act as maintainers of a knowledge system, not as resume writers.

They should:

- Read source files before generating anything.
- Update source knowledge when facts are missing or wrong.
- Preserve chronology, evidence, and relationships.
- Avoid inventing achievements, dates, metrics, titles, or technologies.
- Keep generated outputs separate from canonical knowledge.
- Explain when the knowledge base lacks enough information to support a requested output.

The operating contract for agents is defined in `SYSTEM.md`.
