# Professional knowledge verification — 2026-11-08

Recorded from the new verification round supplied by Manuel. The date records capture of this verification; individual examples have no exact dates. “Current” and “recent” refer to this round. Previous raw interviews remain historical sources.

## Deutsche Bank — technical ownership

Current team structure:
- Small senior team; effectively two developers.
- A third team member acts more as a business/technical liaison.
- Junior developers are uncommon because the team is critical.

Recent concrete example:
- A new microservice was required to act as a proxy between mainframe and an API owned by another team.
- Manuel initially received only the Swagger/OpenAPI definition of the external API.
- From that starting point, Manuel produced the technical document, designed/created the new microservice, coordinated with the mainframe team, agreed how both sides would communicate and the message/data structure, implemented the solution, implemented/performed its testing, and brought it into the development environment.
- It has NOT reached production yet. Production is waiting on other teams. This example does not support production deployment or a production outcome.

## Deutsche Bank — code review

- There are effectively two developers in the team. Every PR is reviewed by the other developer.
- Manuel's approval is required for his colleague's PRs, and the colleague's approval is required for Manuel's PRs.
- Reviews include functional correctness/errors, unnecessary code, unused dependencies, maintainability, and whether the proposed solution is technically the best/simplest sustainable option.
- The relationship is peer-to-peer. The other developer has more years of experience and is technically strong. They learn from each other.
- This is not formal Tech Lead authority, managerial approval authority or people management.

## Mentoring / knowledge transfer

- Manuel prefers helping people understand WHY something is done rather than giving only mechanical instructions.

Mercury:
- Worked closely with the Tech Lead when designing new functionality.
- Also produced some technical designs that were implemented by less experienced developers.
- Those developers sometimes needed his support; he explained design reasoning and good practices.

Deutsche Bank:
- During a period when a less experienced developer was in the team, Manuel accompanied her across several developments.
- He helped explain how to approach implementations.
- During code review he explained why a solution could be functionally correct but still not be the best option in design or maintainability.

Recent peer example:
- A colleague became confused between steps required to move a development to production.
- Manuel explained each step, its purpose, and why the sequence matters.

Boundary: mentoring, technical guidance and knowledge transfer; no formal people management.

## Cross-team technical coordination

- Teams are organizationally independent.
- When another team consumes an API from Manuel's team's microservices, Manuel regularly participates in coordinating how they communicate/integrate.
- It is also common for other teams to contact his team when an integration does not work. Manuel participates in diagnosing those issues.
- In his experience, most of those integration failures are caused by incorrect data content or structure on the consuming side.
- This does not establish organizational API governance or ownership of other teams.

## Testing — current professional practice

- Professional testing currently includes unit testing, integration testing, Acceptance Testing (ACT), and end-to-end testing.
- Current professional tools include JUnit, Mockito, Spring Boot Test, WireMock, SOAPUI, Bruno, and Karate.
- ACT explicitly means Acceptance Testing. Karate is used for Acceptance Testing. ACT is not an unknown internal acronym.
- E2E testing at Deutsche Bank can require coordination with several teams.
- Manuel also owns testing for the solutions he develops.
- TDD is used occasionally, is not habitual, and is not a preferred/core positioning claim.
- Sonar exists in the current environment but currently receives relatively little emphasis. It had significantly more importance in previous projects.
- Waltz and Prisma are also used in the current environment. Manuel described them in the context of vulnerability analysis. Preserve these names and that user-described context without inferring a broader product-specific scope.

## English — professional usage

- Written professional work is largely in English: documentation, code, Jira, and emails involving non-Spanish-speaking participants.
- A significant part of TDI is based in India, so Manuel regularly participates in professional/technical meetings in English.
- Listening comprehension is the main difficulty; some accents are harder. He usually understands the overall context, but sometimes misses a key word or question and needs the speaker to repeat it.
- Supported: habitual professional written and spoken use of English.
- Unsupported: CEFR B2/C1/C2, native/bilingual, or unrestricted “fluent”. No formal language level is assigned.
