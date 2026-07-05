# CareerOS

CareerOS is a Professional Knowledge Base for a complete career.

It is not a resume, a portfolio, or a LinkedIn profile. Those are outputs. CareerOS is the source of truth from which those outputs can be generated.

The goal of this repository is to store professional knowledge once, in a structured and auditable form, then generate every downstream artifact from that source: CVs, bios, portfolio pages, interview answers, cover letters, website content, LinkedIn sections, and other career materials.

## Why It Exists

Most career material is edited backwards.

People maintain several disconnected versions of the same professional facts: one resume for one role, another CV for another market, a portfolio with different wording, LinkedIn with stale dates, interview notes in a separate document, and cover letters that slowly drift away from the truth.

That creates duplication, inconsistency, and loss of evidence.

CareerOS treats a career as knowledge infrastructure. The repository preserves companies, projects, stories, skills, technologies, evidence, chronology, and relationships as reusable source material. Outputs are generated from that knowledge instead of manually rewritten.

## Problem It Solves

CareerOS is designed to solve five recurring problems:

- Career information gets duplicated across too many documents.
- Resumes flatten complex work into short, lossy bullets.
- Professional stories lose context, evidence, and chronology over time.
- AI-generated career material invents or exaggerates details when it is not grounded in a trusted source.
- Every new application, interview, or profile update requires manual editing from scratch.

The repository gives humans and AI agents one place to read from, one place to update, and one rule: edit the source knowledge, then regenerate the output.

## Repository Structure

```text
CareerOS/
|-- assets/              # Supporting media and evidence assets
|-- docs/                # Project documentation
|-- generated/           # Disposable generated outputs, ignored by git
|-- knowledge/           # Source professional knowledge
|   |-- entities/        # Canonical entities: companies, projects, stories, etc.
|   |-- indexes/         # Navigation and lookup indexes
|   |-- relations/       # Cross-entity relationship maps
|   `-- taxonomy/        # Shared vocabularies and classification lists
|-- scripts/             # Future automation and generation scripts
|-- templates/           # Structured markdown templates for source files
|-- AGENTS.md            # Permanent constitution for AI agents
|-- SYSTEM.md            # Operating rules for AI agents
|-- ROADMAP.md           # Project roadmap
`-- CHANGELOG.md         # Project history
```

## Core Concepts

- **Knowledge Base:** the canonical source under `knowledge/`.
- **Entities:** structured files for companies, projects, stories, technologies, talks, publications, and related concepts.
- **Relations:** explicit links between entities, such as projects to technologies or companies to stories.
- **Taxonomy:** controlled vocabulary for skills, domains, roles, values, and technologies.
- **Generated outputs:** disposable files created from source knowledge.
- **AI workflows:** agents must read and update source knowledge before producing any output.

See [docs/architecture.md](docs/architecture.md) for the full architecture.
See [AGENTS.md](AGENTS.md) for the permanent rules every AI agent must follow.

## Example Workflow

1. Add or update source knowledge in `knowledge/entities/` using the relevant template from `templates/`.
2. Link that knowledge in `knowledge/relations/`.
3. Update the relevant index in `knowledge/indexes/`.
4. Preserve evidence in the source file or in `assets/` when appropriate.
5. Generate an output into `generated/`.
6. Review the generated output.
7. If something is wrong, fix the source knowledge and regenerate.

The generated file should not become the new source of truth.

## Future Roadmap

CareerOS is currently a repository framework. Future work should add:

- Schema validation for frontmatter and required sections.
- Consistency checks across entities, indexes, relations, and taxonomies.
- Generation scripts for CVs, bios, LinkedIn profiles, interview answers, and websites.
- Evidence tracking and provenance validation.
- AI-agent workflows for safe edits and grounded generation.
- Export targets for Markdown, PDF, DOCX, HTML, JSON, and static sites.
- Test fixtures and examples that do not contain private personal information.

## Contributing

Contributions should improve the framework without inventing personal data.

Good contributions include:

- Better templates.
- Clearer documentation.
- Validation scripts.
- Generation pipelines.
- Tests for consistency and provenance.
- Example fixtures using fictional or anonymized data.

Contributions should not:

- Add fake professional experience.
- Duplicate information across source files.
- Treat generated output as canonical.
- Mix private career facts with public examples.

Before changing generation behavior, read [AGENTS.md](AGENTS.md) and [SYSTEM.md](SYSTEM.md).

## License

No license has been selected yet.

Until a license is added, all rights are reserved by default. Add a `LICENSE` file before distributing or accepting external contributions under an open-source license.
