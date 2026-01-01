## ADDED Requirements

### Requirement: Spring Events Deep Dive
The `spring-core-events` module SHALL include deep dive Labs and `@Disabled` Exercises that teach Spring application event mechanics, including:
- synchronous default behavior and ordering
- asynchronous event listeners (intro-level)
- transactional event behavior using `@TransactionalEventListener` phases

#### Scenario: Verify deep dive labs are runnable
- **WHEN** a learner runs `mvn -q -pl spring-core-events test`
- **THEN** the enabled lab tests pass without requiring exercises to be enabled

