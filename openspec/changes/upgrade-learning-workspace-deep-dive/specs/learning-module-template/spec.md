## ADDED Requirements

### Requirement: Deep Dive Track in Every Module
Each learning module SHALL include a “Deep Dive” track consisting of **15+ experiments** that go beyond the minimal happy path and teach underlying mechanisms (container internals and/or framework mechanics).

An experiment SHALL be represented by an automated test and SHALL be either:
- a **Lab**: enabled and always passing, or
- an **Exercise**: a learner task provided as a test annotated with `@Disabled`.

Each module SHALL include at least 10 Labs and at least 5 Exercises.

#### Scenario: Run module tests without enabling exercises
- **WHEN** a learner runs `mvn -q -pl <module> test`
- **THEN** the enabled Lab tests pass
- **AND** the module does not require any Exercise tests to be enabled to keep the build green

### Requirement: Disabled Exercises Are Learner-Enableable
Each Exercise test SHALL include:
- an `@Disabled` annotation with a short reason
- a clear prompt describing what the learner should change

#### Scenario: Enable and complete an exercise
- **WHEN** a learner removes `@Disabled` from an Exercise test and completes the required changes
- **THEN** the Exercise test passes and demonstrates the intended concept

### Requirement: Module README Lists Labs and Exercises
Each module `README.md` SHALL document:
- how to run the module
- how to run the tests
- a list of Labs (enabled) and what they demonstrate
- a list of Exercises (disabled) and how to enable them

#### Scenario: Discover deep dive content quickly
- **WHEN** a learner opens a module `README.md`
- **THEN** the learner can identify which tests are Labs vs Exercises and how to run/enable them

