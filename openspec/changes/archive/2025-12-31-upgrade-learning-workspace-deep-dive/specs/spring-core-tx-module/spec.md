## ADDED Requirements

### Requirement: Spring Transactions Internals Deep Dive
The `spring-core-tx` module SHALL include deep dive Labs and `@Disabled` Exercises that teach declarative transaction mechanics, including:
- proxy boundaries and what does/does not get wrapped
- propagation behavior (intro-level)
- rollback rules (runtime vs checked exceptions)
- transaction synchronization and observable side effects

#### Scenario: Verify deep dive labs are runnable
- **WHEN** a learner runs `mvn -q -pl spring-core-tx test`
- **THEN** the enabled lab tests pass without requiring exercises to be enabled

