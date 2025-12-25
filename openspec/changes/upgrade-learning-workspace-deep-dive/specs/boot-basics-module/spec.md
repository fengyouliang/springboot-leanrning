## ADDED Requirements

### Requirement: Boot Basics Deep Dive Track
The `boot-basics` module SHALL include deep dive Labs and `@Disabled` Exercises that teach how Spring Boot config and environment mechanics work, including:
- `Environment` and property source ordering
- profile activation and precedence
- `@ConfigurationProperties` binding and type conversion basics
- common failure modes (missing properties, wrong types, unexpected overrides)

#### Scenario: Verify deep dive labs are runnable
- **WHEN** a learner runs `mvn -q -pl boot-basics test`
- **THEN** the enabled lab tests pass without requiring exercises to be enabled

