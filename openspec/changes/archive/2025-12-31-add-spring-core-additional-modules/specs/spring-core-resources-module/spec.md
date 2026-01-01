## ADDED Requirements

### Requirement: Spring Core Resources Module
The workspace SHALL provide a learning module named `spring-core-resources` that demonstrates Spring’s `Resource` abstraction and loading resources from the classpath, with at least one runnable example and at least one passing test.

#### Scenario: Read resources from the classpath
- **WHEN** a learner runs `mvn -q -pl spring-core-resources test`
- **THEN** the tests pass and prove a resource-loading behavior (for example: reading a classpath file)
- **AND** the learner can run the module via `mvn -pl spring-core-resources spring-boot:run` to observe a resource-related output

