# spring-core-events-module Specification

## Purpose
TBD - created by archiving change add-spring-core-learning-modules. Update Purpose after archive.
## Requirements
### Requirement: Spring Core Events Module
The workspace SHALL provide a learning module named `spring-core-events` that teaches Spring application events (publishing and handling events) with an example publisher and at least one `@EventListener`.

#### Scenario: Verify an event listener reacts to an event
- **WHEN** a learner runs `mvn -q -pl spring-core-events test`
- **THEN** the module tests pass and prove that an event listener receives and handles a published event
- **AND** the learner can run the module via `mvn -pl spring-core-events spring-boot:run` to observe a topic-relevant output

### Requirement: Spring Events Deep Dive
The `spring-core-events` module SHALL include deep dive Labs and `@Disabled` Exercises that teach Spring application event mechanics, including:
- synchronous default behavior and ordering
- asynchronous event listeners (intro-level)
- transactional event behavior using `@TransactionalEventListener` phases

#### Scenario: Verify deep dive labs are runnable
- **WHEN** a learner runs `mvn -q -pl spring-core-events test`
- **THEN** the enabled lab tests pass without requiring exercises to be enabled

