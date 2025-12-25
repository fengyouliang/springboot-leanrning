## ADDED Requirements

### Requirement: Web MVC Deep Dive Track
The `springboot-web-mvc` module SHALL include deep dive Labs and `@Disabled` Exercises that teach Spring MVC mechanics beyond basic controller mapping, including:
- validation at the boundary and error mapping
- exception handling patterns and response shaping
- converters/formatters and request binding
- interceptors/filters introduction and ordering

#### Scenario: Verify deep dive labs are runnable
- **WHEN** a learner runs `mvn -q -pl springboot-web-mvc test`
- **THEN** the enabled lab tests pass without requiring exercises to be enabled
