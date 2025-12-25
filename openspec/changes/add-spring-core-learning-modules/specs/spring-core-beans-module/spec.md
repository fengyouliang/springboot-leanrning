## ADDED Requirements

### Requirement: Spring Core Beans Module
The workspace SHALL provide a learning module named `spring-core-beans` that teaches Spring Framework IoC container fundamentals, including bean registration, dependency injection, bean scopes, and basic lifecycle callbacks.

#### Scenario: Build, test, and observe bean behavior
- **WHEN** a learner runs `mvn -q -pl spring-core-beans test`
- **THEN** the module tests pass and demonstrate at least one core bean behavior (for example: injection, scope, or lifecycle)
- **AND** the learner can run the module via `mvn -pl spring-core-beans spring-boot:run` to observe a topic-relevant output

