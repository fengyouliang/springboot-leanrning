## ADDED Requirements

### Requirement: Spring Validation Internals Deep Dive
The `spring-core-validation` module SHALL include deep dive Labs and `@Disabled` Exercises that teach validation mechanics beyond basic constraints, including:
- method validation behavior and how it is applied (proxying interaction)
- validation groups basics
- custom constraints (intro-level) and common pitfalls

#### Scenario: Verify deep dive labs are runnable
- **WHEN** a learner runs `mvn -q -pl spring-core-validation test`
- **THEN** the enabled lab tests pass without requiring exercises to be enabled

