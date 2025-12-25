## ADDED Requirements

### Requirement: Spring Core AOP Module
The workspace SHALL provide a learning module named `spring-core-aop` that teaches Spring AOP fundamentals (proxies and advice) using `spring-boot-starter-aop`, and includes at least one example aspect applied to application code.

#### Scenario: Verify advice is applied on the happy path
- **WHEN** a learner runs `mvn -q -pl spring-core-aop test`
- **THEN** the module tests pass and prove that an aspect advice is applied to a target method call
- **AND** the learner can run the module via `mvn -pl spring-core-aop spring-boot:run` to observe a topic-relevant output

