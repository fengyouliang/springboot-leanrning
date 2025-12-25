## ADDED Requirements

### Requirement: Capstone Business Case Module
The workspace SHALL provide a capstone learning module named `springboot-business-case` that demonstrates a realistic end-to-end flow and how Spring mechanics compose across concerns:
- MVC boundary + validation
- transactional service layer
- Spring Data JPA persistence with an embedded database
- events and listeners (including transactional boundaries)
- AOP cross-cutting behavior applied via proxies

#### Scenario: Run the capstone module tests
- **WHEN** a learner runs `mvn -q -pl springboot-business-case test`
- **THEN** the tests pass and demonstrate the end-to-end flow with observable outcomes

#### Scenario: Run the capstone module
- **WHEN** a learner runs `mvn -pl springboot-business-case spring-boot:run`
- **THEN** the module starts and provides a topic-relevant behavior that can be observed (via logs, an endpoint, or a simple runner)
