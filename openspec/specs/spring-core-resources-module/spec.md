# spring-core-resources-module Specification

## Purpose
TBD - created by archiving change add-spring-core-additional-modules. Update Purpose after archive.
## Requirements
### Requirement: Spring Core Resources Module
The workspace SHALL provide a learning module named `spring-core-resources` that demonstrates Spring’s `Resource` abstraction and loading resources from the classpath, with at least one runnable example and at least one passing test.

#### Scenario: Read resources from the classpath
- **WHEN** a learner runs `mvn -q -pl spring-core-resources test`
- **THEN** the tests pass and prove a resource-loading behavior (for example: reading a classpath file)
- **AND** the learner can run the module via `mvn -pl spring-core-resources spring-boot:run` to observe a resource-related output

### Requirement: Spring Resource Loading Deep Dive
The `spring-core-resources` module SHALL include deep dive Labs and `@Disabled` Exercises that teach Spring’s `Resource` abstraction and classpath loading mechanics, including:
- `Resource` types and when each appears (classpath vs filesystem)
- classpath pattern resolution basics
- common pitfalls when loading resources (path formats, jar packaging)

#### Scenario: Verify deep dive labs are runnable
- **WHEN** a learner runs `mvn -q -pl spring-core-resources test`
- **THEN** the enabled lab tests pass without requiring exercises to be enabled

