# spring-core-tx-module Specification

## Purpose
TBD - created by archiving change add-spring-core-additional-modules. Update Purpose after archive.
## Requirements
### Requirement: Spring Core Transactions Module
The workspace SHALL provide a learning module named `spring-core-tx` that demonstrates declarative transaction management (`@Transactional`) and rollback behavior using an embedded database, with at least one runnable example and at least one passing test.

#### Scenario: Verify rollback on runtime exception
- **WHEN** a learner runs `mvn -q -pl spring-core-tx test`
- **THEN** the tests pass and prove that a transactional operation rolls back on a runtime exception
- **AND** the learner can run the module via `mvn -pl spring-core-tx spring-boot:run` to observe a transaction-related output

### Requirement: Spring Transactions Internals Deep Dive
The `spring-core-tx` module SHALL include deep dive Labs and `@Disabled` Exercises that teach declarative transaction mechanics, including:
- proxy boundaries and what does/does not get wrapped
- propagation behavior (intro-level)
- rollback rules (runtime vs checked exceptions)
- transaction synchronization and observable side effects

#### Scenario: Verify deep dive labs are runnable
- **WHEN** a learner runs `mvn -q -pl spring-core-tx test`
- **THEN** the enabled lab tests pass without requiring exercises to be enabled

