# CareerOS Agent System

This file defines how AI agents must work with this repository.

CareerOS is a Professional Knowledge Base. It is not a resume repository. Agents must preserve the repository as a source-of-truth system where generated outputs are derived from structured knowledge.

## Prime Directive

Every professional statement must come from the knowledge base.

If a fact is missing, do not invent it. Add the missing source knowledge only when the user provides it or when it already exists elsewhere in the repository and can be referenced accurately.

## Operating Rules

### Never Duplicate Information

Do not copy the same professional fact into multiple canonical places.

If a fact belongs to a company, project, story, technology, or other entity, place it in the correct source file and link to it through relations or indexes.

Duplication creates drift.

### Always Edit Source Knowledge

When information is missing, stale, or incorrect, update the relevant file under `knowledge/`.

Do not patch a generated CV, bio, website page, or interview answer as if it were canonical. Fix the source and regenerate.

### Outputs Are Disposable

Files under `generated/` are outputs.

They may be deleted, overwritten, or recreated at any time. They must not contain unique career facts that do not exist in the knowledge base.

### Source Files Are Immutable Truth

Source files under `knowledge/` are the canonical record.

"Immutable" does not mean they can never change. It means they must be treated as authoritative. Changes to them should be deliberate, grounded, and made only to improve the truth of the record.

### Prefer Structured Markdown

Use Markdown with YAML frontmatter for source knowledge.

Frontmatter should contain stable metadata. Body sections should contain human-readable context, evidence, and explanation. Prefer existing templates in `templates/` before creating a new structure.

### Preserve Chronology

Career knowledge is temporal.

Keep dates, ordering, transitions, and sequence clear. Do not collapse chronology in a way that changes meaning. If dates are unknown, mark them as unknown rather than guessing.

### Preserve Evidence

Evidence matters.

Keep links, references, artifacts, assets, and supporting notes attached to the source knowledge they support. If evidence is unavailable, do not imply that a claim is proven.

### Ground Every Statement

Generated statements must be traceable to source files.

Before generating an output, read the relevant knowledge files, relations, indexes, and taxonomy entries. If the requested output needs information that is not present, say what is missing.

## Agent Workflow

1. Identify the requested output or repository change.
2. Read the relevant source files under `knowledge/`.
3. Read related templates, relations, indexes, and taxonomy files when needed.
4. Determine whether the knowledge base supports the requested result.
5. If source knowledge is missing, ask for it or create only a framework placeholder.
6. Edit canonical source files when facts need to be added or corrected.
7. Generate outputs only into `generated/`.
8. Treat generated files as replaceable artifacts.
9. Do not introduce claims that cannot be traced to the knowledge base.

## Prohibited Behavior

Agents must not:

- Invent companies, projects, roles, dates, technologies, metrics, publications, awards, or achievements.
- Generate fake work experience.
- Use a generated output as the source for future source knowledge.
- Store canonical facts only in `generated/`.
- Duplicate the same fact across several entity files.
- Rewrite chronology to make a narrative more convenient.
- Remove evidence because it does not fit a short output.
- Convert the repository into a resume-first structure.

## Preferred Behavior

Agents should:

- Keep source files structured and easy to parse.
- Add relationships instead of repeating prose.
- Separate facts from generated phrasing.
- Maintain stable IDs.
- Keep outputs target-specific and reproducible.
- Surface uncertainty clearly.
- Make small, auditable changes.
- Preserve private or sensitive material unless the user explicitly asks to remove it.

## When In Doubt

Prefer the knowledge base over the output.

Prefer evidence over polish.

Prefer a missing-data note over an invented claim.

Prefer structured source edits over generated text edits.
