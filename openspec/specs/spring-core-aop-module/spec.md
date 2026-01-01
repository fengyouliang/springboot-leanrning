# spring-core-aop-module Specification

## Purpose
TBD - created by archiving change add-spring-core-learning-modules. Update Purpose after archive.
## Requirements
### Requirement: Spring Core AOP Module
The workspace SHALL provide a learning module named `spring-core-aop` that teaches Spring AOP fundamentals (proxies and advice) using `spring-boot-starter-aop`, and includes at least one example aspect applied to application code.

#### Scenario: Verify advice is applied on the happy path
- **WHEN** a learner runs `mvn -q -pl spring-core-aop test`
- **THEN** the module tests pass and prove that an aspect advice is applied to a target method call
- **AND** the learner can run the module via `mvn -pl spring-core-aop spring-boot:run` to observe a topic-relevant output

### Requirement: Spring AOP Proxy Internals Deep Dive
The `spring-core-aop` module SHALL include deep dive Labs and `@Disabled` Exercises that teach how Spring AOP proxying works, including:
- JDK dynamic proxies vs CGLIB proxies and selection rules
- pointcut matching and advice ordering basics
- self-invocation pitfalls and mitigation options
- proxy limitations (final classes/methods) and observable outcomes

#### Scenario: Verify deep dive labs are runnable
- **WHEN** a learner runs `mvn -q -pl spring-core-aop test`
- **THEN** the enabled lab tests pass without requiring exercises to be enabled

