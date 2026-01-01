# boot-actuator-module Specification

## Purpose
TBD - created by archiving change upgrade-learning-workspace-deep-dive. Update Purpose after archive.
## Requirements
### Requirement: Actuator Deep Dive Track
The `springboot-actuator` module SHALL include deep dive Labs and `@Disabled` Exercises that teach how Actuator endpoints are discovered and exposed, including:
- endpoint exposure configuration basics
- custom health indicators/contributors
- understanding what is visible and why (minimal, beginner-friendly)

#### Scenario: Verify deep dive labs are runnable
- **WHEN** a learner runs `mvn -q -pl springboot-actuator test`
- **THEN** the enabled lab tests pass without requiring exercises to be enabled

