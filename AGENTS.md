# CareerOS Agent Constitution

This document is the permanent operating contract for every AI agent working on CareerOS.

CareerOS is a Professional Knowledge Base. It is not a resume generator, not a CV editor, and not a collection of polished career documents. The knowledge base is the single source of truth. Everything else is generated from it.

## Purpose

CareerOS exists to preserve professional knowledge in a structured, durable, and reusable form.

The repository should capture the raw material of a career: experience, projects, companies, stories, skills, technologies, publications, evidence, chronology, and relationships between them.

Generated artifacts such as resumes, CVs, LinkedIn sections, portfolio pages, personal websites, interview answers, cover letters, and bios are outputs. They are views over the knowledge base, not sources of truth.

An agent's job is to protect the knowledge system first. Generation is secondary.

## Golden Rules

- Never duplicate information.
- Never edit generated outputs manually as if they were canonical.
- Always modify the source knowledge when facts need to change.
- Prefer linking over copying.
- Preserve chronology.
- Preserve evidence.
- Every fact must come from the knowledge base.
- Never invent information.
- Never summarize unless explicitly requested.
- Preserve the user's own voice whenever possible.

If a requested output cannot be supported by the knowledge base, say what is missing. Do not fill gaps with plausible-sounding details.

## Working Strategy

Always work in this order:

1. Raw knowledge
2. Structured knowledge
3. Generated outputs

Never skip layers.

### 1. Raw Knowledge

Raw knowledge is the uncompressed source material: notes, evidence, examples, dates, context, decisions, constraints, and user-provided facts.

Agents should preserve raw knowledge when it contains useful context that may be needed later. Do not prematurely compress it into resume-style bullets.

### 2. Structured Knowledge

Structured knowledge is the canonical representation under `knowledge/`.

Agents should organize raw knowledge into entities, relations, indexes, taxonomy entries, and evidence references. Use Markdown structures that are easy for both humans and tools to inspect.

### 3. Generated Outputs

Generated outputs belong under `generated/`.

Outputs may be created, deleted, and regenerated. They must not contain unique facts that are absent from the knowledge base.

When an output is wrong, fix the source layer first.

## Repository Principles

CareerOS is a knowledge system, not a documentation repository.

Documentation explains how the system works. It does not replace the knowledge base. Generated files demonstrate or export knowledge. They do not become knowledge.

The repository should favor:

- Canonical source files over duplicated prose.
- Explicit relationships over repeated context.
- Structured Markdown over opaque text.
- Chronology over flattened narrative.
- Evidence over unsupported claims.
- User voice over generic professional language.
- Reproducible generation over manual output editing.

## Agent Responsibilities

Before making changes, agents should read the relevant source files. Before generating outputs, agents should confirm that the requested claims are supported by source knowledge.

Agents must keep changes auditable and scoped. If a fact belongs in one source file, put it there and link to it elsewhere. If a new structure is needed, prefer extending existing templates and conventions instead of inventing an unrelated format.

The correct failure mode is explicit uncertainty. A missing fact is better than an invented one.
