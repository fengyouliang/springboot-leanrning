## ADDED Requirements

### Requirement: Spring Core Transactions Module
The workspace SHALL provide a learning module named `spring-core-tx` that demonstrates declarative transaction management (`@Transactional`) and rollback behavior using an embedded database, with at least one runnable example and at least one passing test.

#### Scenario: Verify rollback on runtime exception
- **WHEN** a learner runs `mvn -q -pl spring-core-tx test`
- **THEN** the tests pass and prove that a transactional operation rolls back on a runtime exception
- **AND** the learner can run the module via `mvn -pl spring-core-tx spring-boot:run` to observe a transaction-related output

