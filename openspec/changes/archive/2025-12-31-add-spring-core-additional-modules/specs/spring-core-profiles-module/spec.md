## ADDED Requirements

### Requirement: Spring Core Profiles Module
The workspace SHALL provide a learning module named `spring-core-profiles` that demonstrates profile-based and property/condition-based bean registration, with at least one runnable example and at least one passing test.

#### Scenario: Select beans based on profile or property
- **WHEN** a learner runs `mvn -q -pl spring-core-profiles test`
- **THEN** the tests pass and prove bean selection across at least two scenarios (for example: default vs dev profile)
- **AND** the learner can run the module via `mvn -pl spring-core-profiles spring-boot:run` to observe which beans are active

