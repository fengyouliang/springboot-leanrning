# learning-module-template Specification

## Purpose
TBD - created by archiving change add-springboot-learning-workspace. Update Purpose after archive.
## Requirements
### Requirement: Standalone Runnable Module
Each learning module SHALL be a standalone Spring Boot application that can be run independently.

#### Scenario: Run a single module
- **WHEN** a learner runs a specific module
- **THEN** the module starts without requiring other modules to be running

### Requirement: Topic-Focused Example Behavior
Each learning module SHALL demonstrate its primary topic via at least one user-visible behavior (for example: an HTTP endpoint, a configuration-driven feature, an actuator endpoint, or a data access operation).

#### Scenario: Observe the module’s learning outcome
- **WHEN** a learner follows the module README run steps
- **THEN** the learner can observe at least one concrete behavior that matches the module’s topic

### Requirement: Module Documentation
Each learning module SHALL include a module-level `README.md` that explains:
- the learning goal(s)
- prerequisites (JDK, build tool usage)
- how to run the module
- how to run the module tests

#### Scenario: Navigate module documentation
- **WHEN** a learner opens the module directory
- **THEN** a `README.md` is present and contains the required sections

### Requirement: Minimal Automated Test
Each learning module SHALL include at least one automated test that passes on the happy path.

#### Scenario: Run module tests
- **WHEN** a learner runs the module test command from the workspace
- **THEN** the module’s tests pass

### Requirement: Test-Driven Modules Are First-Class
The learning module template SHALL support a tests-first learning path: a learning module MAY be primarily test-driven (i.e., the primary learning path is running `*LabTest` and reading `docs/`), as long as:
- the module still provides clear, observable outcomes through tests (assertions)
- the module `README.md` explicitly documents the recommended run path (tests-first or run-first)

#### Scenario: Learn without running a server
- **WHEN** a learner follows a test-driven module’s `README.md`
- **THEN** the learner can reproduce the learning outcomes by running module tests only

### Requirement: Explicit Port Policy for Web Modules
Any module that starts an HTTP server SHALL explicitly configure `server.port` in `application.properties` and document it in the module `README.md`, avoiding conflicts with other modules.

#### Scenario: Avoid port conflicts
- **WHEN** a learner runs two different web modules
- **THEN** the modules do not conflict on ports because each web module declares its own `server.port`

### Requirement: Deterministic Tests Without External Infrastructure
Deep-dive experiments SHALL avoid reliance on external infrastructure (Docker services, external HTTP endpoints, etc.) and SHALL use in-process or embedded substitutes (e.g., in-memory DB, in-process mock HTTP server) to keep tests deterministic.

#### Scenario: Run tests offline
- **WHEN** a learner runs `mvn -q -pl <module> test` without external services
- **THEN** the enabled Lab tests pass deterministically

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

