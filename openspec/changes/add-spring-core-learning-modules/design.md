## Context
This workspace is structured as “one module per topic” to help beginners learn incrementally. The existing modules focus on Spring Boot features. To make those modules easier to understand, we want dedicated modules for Spring Framework fundamentals that Spring Boot builds upon.

## Goals / Non-Goals

### Goals
- Teach Spring Core fundamentals with runnable, observable examples:
  - IoC container basics and bean behavior
  - AOP / proxies and how advice is applied
  - Application events and listeners
- Keep the “happy path” simple (no external services, no Docker).
- Keep modules consistent with the existing workspace conventions (Maven multi-module, module README, minimal tests).

### Non-Goals
- Cover every Spring feature in one change (this change is a starter set).
- Build production-grade architectures or introduce heavy abstractions.
- Add a shared `common` module at this stage.

## Decisions
- **Module naming**: Use `spring-core-*` to distinguish Spring Framework fundamentals from `boot-*` modules.
- **Runtime model**: Each module remains a standalone Spring Boot application for consistency and ease of running (`mvn -pl <module> spring-boot:run`).
- **No web server by default**: Prefer `spring-boot-starter` over `spring-boot-starter-web` to avoid port conflicts and keep focus on container behavior.
- **Observability for learning**: Each module should have at least one user-visible behavior (startup logs/console output and/or a minimal test that asserts the behavior).
- **Tests**: Provide at least one focused test per module that demonstrates the module’s topic on the happy path.

## Risks / Trade-offs
- **Mixing “Spring” and “Spring Boot”**: Using Spring Boot to teach Spring Core can blur boundaries. Mitigate by explicitly calling out what is Spring Framework vs what is Spring Boot in each module README.
- **Scope creep**: “Spring basics” can expand quickly. Mitigate by keeping this change limited to three modules and deferring additional topics to follow-up changes.

## Migration Plan
Not applicable (additive modules in a learning workspace).

## Open Questions
- Should the Spring Core modules be introduced as a prerequisite sequence in the root README (recommended learning order), or kept as a flat catalog only?
- Do we want to include an optional fourth module in this change (e.g., `spring-core-resources` or `spring-core-validation`), or keep the starter set strictly to 3 modules?

