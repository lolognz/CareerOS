# CareerOS Data Flow

CareerOS follows a source-first data flow:

```text
Raw Interview

      |
      v

Structured Knowledge

      |
      v

Generated Outputs
```

Each layer has a different responsibility. Agents and scripts must respect the direction of the flow.

## Raw Interview

The raw interview layer contains the canonical long-form source material.

Responsibilities:

- Preserve the user's original words and context.
- Store information before interpretation or compression.
- Keep uncertainty, chronology, nuance, and evidence intact.
- Avoid summarizing unless explicitly requested.
- Serve as the source material for structured knowledge.

Raw interview files should not be optimized for resumes, websites, or other outputs. They exist to preserve source truth.

## Structured Knowledge

The structured knowledge layer converts raw material into organized, reusable knowledge.

Responsibilities:

- Extract entities, relationships, timelines, skills, projects, companies, stories, publications, and evidence references.
- Preserve traceability back to raw interview fragments.
- Represent facts in structured Markdown and machine-readable metadata where appropriate.
- Link related knowledge instead of copying the same information into multiple places.
- Avoid adding claims that do not exist in raw knowledge.

Structured knowledge is not a place to invent, polish, or exaggerate. It is a bridge between raw source material and generated artifacts.

## Generated Outputs

The generated outputs layer contains disposable artifacts created from structured knowledge.

Responsibilities:

- Produce target-specific outputs such as CVs, bios, LinkedIn sections, portfolio pages, interview answers, cover letters, websites, or exports.
- Adapt tone, length, format, and selection for a specific purpose.
- Remain traceable to structured knowledge and, through it, to raw source material.
- Be regenerated when source knowledge changes.
- Avoid becoming the canonical source for future work.

Generated outputs are views over the knowledge base. If an output is inaccurate, the correction belongs upstream.

## Direction Of Change

Corrections should move upstream:

```text
Output problem -> Structured knowledge check -> Raw knowledge check -> Source update -> Regenerate output
```

Agents must never fix a generated output by adding unsupported facts directly to the output. They should update the earliest layer where the truth belongs, then allow later layers to be regenerated.
