# spring-core-validation-module Specification

## Purpose
TBD - created by archiving change add-spring-core-additional-modules. Update Purpose after archive.
## Requirements
### Requirement: Spring Core Validation Module
The workspace SHALL provide a learning module named `spring-core-validation` that demonstrates Bean Validation usage and Spring integration patterns, with at least one runnable example and at least one passing test.

#### Scenario: Validate input and observe errors
- **WHEN** a learner runs `mvn -q -pl spring-core-validation test`
- **THEN** the tests pass and prove a validation behavior (for example: constraint violations or a validation exception)
- **AND** the learner can run the module via `mvn -pl spring-core-validation spring-boot:run` to observe a validation-related output

### Requirement: Spring Validation Internals Deep Dive
The `spring-core-validation` module SHALL include deep dive Labs and `@Disabled` Exercises that teach validation mechanics beyond basic constraints, including:
- method validation behavior and how it is applied (proxying interaction)
- validation groups basics
- custom constraints (intro-level) and common pitfalls

#### Scenario: Verify deep dive labs are runnable
- **WHEN** a learner runs `mvn -q -pl spring-core-validation test`
- **THEN** the enabled lab tests pass without requiring exercises to be enabled

