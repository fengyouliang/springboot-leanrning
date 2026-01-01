## Context
This repository teaches Spring Boot and Spring Framework topics by using a Maven multi-module workspace. Each module is a self-contained example that is runnable, observable, and testable.

We already added foundational Spring Core modules (beans, AOP, events). This change expands the curriculum with four additional “high-frequency” core topics: validation, resources, transactions, and profiles/conditional bean registration.

## Goals / Non-Goals

### Goals
- Provide four new single-topic modules:
  - `spring-core-validation`: validate objects and demonstrate Spring integration patterns
  - `spring-core-resources`: load resources from the classpath and via patterns
  - `spring-core-tx`: demonstrate `@Transactional` and rollback semantics using an embedded DB
  - `spring-core-profiles`: demonstrate `@Profile` and conditional bean registration in a systematic way
- Keep modules runnable with `mvn -pl <module> spring-boot:run`.
- Provide at least one focused happy-path test per module.
- Keep the root catalog flat (no prescribed learning path).

### Non-Goals
- Add a shared module for common utilities (defer).
- Introduce external services (Docker, real DB servers) on the happy path.
- Provide an exhaustive treatment of each topic in this single change.

## Decisions
- **Naming**: Continue using the `spring-core-*` prefix for Spring Framework fundamentals.
- **Dependencies**:
  - Validation uses `spring-boot-starter-validation` (Bean Validation implementation included)
  - Transactions use `spring-boot-starter-jdbc` + embedded H2 for a minimal DB-backed example
  - Other modules default to `spring-boot-starter` without web dependencies
- **Observability**: Use console output and simple in-memory state as “visible behavior” to keep examples beginner-friendly.
- **Profiles module**: Demonstrate mutually exclusive configuration using `@Profile` at the `@Configuration` class level and a property-based toggle for alternative behavior.

## Risks / Trade-offs
- Validation and transaction behavior can be version-sensitive. Mitigate by keeping tests focused on stable outcomes (e.g., “throws a validation exception”, “rolls back inserted rows”).
- Profiles/conditions can become complex. Mitigate by keeping exactly one active bean choice per scenario to avoid ambiguous injection.

## Migration Plan
Not applicable (additive learning modules).

## Open Questions
None (scope is confirmed: flat catalog + exactly 4 modules).

