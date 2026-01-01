## ADDED Requirements

### Requirement: Spring Resource Loading Deep Dive
The `spring-core-resources` module SHALL include deep dive Labs and `@Disabled` Exercises that teach Spring’s `Resource` abstraction and classpath loading mechanics, including:
- `Resource` types and when each appears (classpath vs filesystem)
- classpath pattern resolution basics
- common pitfalls when loading resources (path formats, jar packaging)

#### Scenario: Verify deep dive labs are runnable
- **WHEN** a learner runs `mvn -q -pl spring-core-resources test`
- **THEN** the enabled lab tests pass without requiring exercises to be enabled

