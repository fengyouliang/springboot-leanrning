## Context
This repository is a Maven multi-module Spring Boot learning workspace. The current code is intentionally minimal, but learners now want a **deep, detailed** learning track that:
- explains Spring container internals (not just “how to use annotations”)
- connects multiple Spring topics via a realistic business flow
- remains runnable and testable as a learning lab

## Goals / Non-Goals

### Goals
- Add a **Deep Dive Track** to every existing module:
  - at least 15 experiments per module (labs + exercises)
  - labs are enabled and always green
  - exercises are `@Disabled` tests, manually enabled by learners
- Teach **container/internal mechanics** explicitly, not implicitly:
  - bean definitions vs instances
  - post-processors
  - proxying behavior and limitations
  - how Spring Boot “wraps” Spring Core
- Add a **capstone business-case module** that integrates the common building blocks:
  - Web + Validation
  - JPA persistence
  - `@Transactional` boundaries and rollback behavior
  - Events (including transactional boundaries)
  - AOP cross-cutting concerns
- Keep the workspace consistent and beginner-friendly:
  - still “one module per topic”
  - still runnable via `mvn -pl <module> spring-boot:run`
  - still testable via `mvn -q -pl <module> test`

### Non-Goals
- Building a production-grade architecture (DDD mega-structure, hexagonal framework, etc.)
- Introducing external systems (Kafka/Redis/containers) as mandatory dependencies
- Documenting every Spring feature; focus is on container mechanics + a practical learning loop

## Key Decisions

### Deep Dive Track Structure
- Define **experiment** as a small, focused learning unit that is verified by a test:
  - **Lab**: enabled test, always green; demonstrates a mechanism with clear assertions.
  - **Exercise**: `@Disabled` test; contains prompts/TODOs for learners to implement or fix.
- Keep the default build green:
  - `mvn -q test` from the root MUST pass without learners enabling exercises.
- Prefer deterministic signals:
  - tests SHOULD assert behaviors rather than relying on console output ordering.

### Testing Strategy (to keep runtime reasonable)
To support 15+ experiments per module without a very slow build:
- Prefer minimal contexts where possible:
  - `AnnotationConfigApplicationContext` for Spring Core internals
  - Spring Boot `ApplicationContextRunner` for small, isolated bootstraps
- Use `@SpringBootTest` only when the topic requires full auto-configuration integration.

### Documentation Pattern
- Each module `README.md` (Chinese) will contain:
  - a “Labs” section listing enabled experiments and what to observe
  - an “Exercises” section listing `@Disabled` tests and how to enable them
  - a “Debugging / Introspection Tips” section for container-level inspection

### Capstone Business Case Module
- Add `springboot-business-case` as a “capstone” module with a single clear topic:
  - “Realistic end-to-end flow and how Spring mechanics compose”
- The module will include:
  - a thin MVC boundary (request → validation → response)
  - a service layer with explicit `@Transactional` boundaries
  - domain events and listeners, including transactional event behavior
  - AOP tracing/metrics as cross-cutting concerns
  - persistence via Spring Data JPA + embedded DB

## Deep Dive Topic Map (Target State)
This is the intended “deep” content focus per module. Each item becomes one or more lab/exercise experiments.

- `spring-core-beans`: bean definition vs instance, lifecycle ordering, post-processors, `@Configuration` enhancement, `FactoryBean`, prototype injection, circular dependencies.
- `spring-core-aop`: JDK vs CGLIB proxies, pointcut matching, advice ordering, self-invocation, proxy limitations (final methods/classes), proxy exposure.
- `spring-core-events`: synchronous default behavior, ordering, async listeners, `@TransactionalEventListener` phases.
- `spring-core-tx`: proxy boundaries, propagation behaviors, rollback rules, checked vs runtime exceptions, transaction synchronization.
- `spring-core-validation`: method validation mechanism, proxying interaction, groups, custom constraints.
- `spring-core-resources`: `Resource` abstraction, classpath pattern resolution, loading pitfalls, jar vs filesystem behavior.
- `spring-core-profiles`: profile selection, `@Conditional*` evaluation, property precedence, conditional bean creation.
- `springboot-basics`: `Environment` and property source ordering, configuration property binding and conversion, profile activation.
- `springboot-web-mvc`: validation at boundary, exception mapping, converters/formatters, interceptors/filters, argument resolvers (intro-level).
- `springboot-data-jpa`: entity states, flush behavior, transactional reads, N+1 pitfalls, query methods vs JPQL.
- `springboot-actuator`: endpoint exposure, custom health contributors, info contributors, basics of security/visibility (minimal).
- `springboot-testing`: slice tests vs full context, `@MockBean` boundaries, test configuration patterns.

## Risks / Trade-offs
- **Internal APIs can shift across Spring versions**: mitigated by pinning to a stable Boot baseline and writing tests against stable public types where possible.
- **Test runtime growth**: mitigated by using minimal contexts and avoiding unnecessary `@SpringBootTest`.
- **Cognitive load**: mitigated by a consistent experiment format (lab/exercise) and clear README navigation.

## Migration Plan
Additive. Existing passing tests remain passing. Exercises are disabled by default so the workspace remains green.

## Open Questions
- Should the capstone module include a real HTTP API by default, or prefer a CLI-style runner to avoid additional port management?
- Do we want a strict convention for experiment naming (e.g., `Lab01_...`) to keep ordering stable in IDEs?
