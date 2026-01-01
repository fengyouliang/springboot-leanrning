## ADDED Requirements

### Requirement: Profiles and Conditional Evaluation Deep Dive
The `spring-core-profiles` module SHALL include deep dive Labs and `@Disabled` Exercises that teach conditional bean creation and environment selection, including:
- profile selection and precedence
- conditional creation based on properties
- basic mental model for why conditions match or not

#### Scenario: Verify deep dive labs are runnable
- **WHEN** a learner runs `mvn -q -pl spring-core-profiles test`
- **THEN** the enabled lab tests pass without requiring exercises to be enabled

