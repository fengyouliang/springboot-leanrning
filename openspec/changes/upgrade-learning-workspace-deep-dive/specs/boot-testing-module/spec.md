## ADDED Requirements

### Requirement: Testing Deep Dive Track
The `boot-testing` module SHALL include deep dive Labs and `@Disabled` Exercises that teach test strategy and Spring test mechanics, including:
- slice tests vs full-context tests and when to use each
- `@MockBean` boundaries and when it hides problems
- test configuration patterns (`@TestConfiguration`, overrides, profiles)

#### Scenario: Verify deep dive labs are runnable
- **WHEN** a learner runs `mvn -q -pl boot-testing test`
- **THEN** the enabled lab tests pass without requiring exercises to be enabled

