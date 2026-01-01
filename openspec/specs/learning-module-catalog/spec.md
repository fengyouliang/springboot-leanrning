# learning-module-catalog Specification

## Purpose
TBD - created by archiving change add-springboot-learning-workspace. Update Purpose after archive.
## Requirements
### Requirement: Root Module Catalog
The repository SHALL provide a root-level module catalog that lists every learning module with a short description and a link to the module documentation.

#### Scenario: Find a learning module by topic
- **WHEN** a learner opens the repository root documentation
- **THEN** the learner can find the relevant module and navigate to its README

### Requirement: Initial Starter Modules
At initial bootstrap, the workspace SHALL include the following starter modules:
- `springboot-basics`
- `springboot-web-mvc`
- `springboot-data-jpa`
- `springboot-actuator`
- `springboot-testing`

#### Scenario: Verify starter modules exist
- **WHEN** a learner views the workspace module list
- **THEN** each starter module is present and can be built as part of the workspace

### Requirement: Single-Topic Module Scope
Each learning module SHALL declare its primary topic in its module `README.md` and keep its scope focused on that topic.

#### Scenario: Understand module scope quickly
- **WHEN** a learner reads a module `README.md`
- **THEN** the primary topic is stated clearly and the examples align with that topic

### Requirement: Spring Core Modules in Root Catalog
The repository SHALL extend the root module catalog to include Spring Core learning modules:
- `spring-core-beans`
- `spring-core-aop`
- `spring-core-events`

#### Scenario: Find Spring Core modules by topic
- **WHEN** a learner opens the root `README.md`
- **THEN** the learner can find the Spring Core modules in the catalog and navigate to each module README

### Requirement: Additional Spring Core Modules in Root Catalog
The repository SHALL extend the root module catalog (flat list) to include these additional Spring Core modules:
- `spring-core-validation`
- `spring-core-resources`
- `spring-core-tx`
- `spring-core-profiles`

#### Scenario: Find the added modules in the catalog
- **WHEN** a learner opens the root `README.md`
- **THEN** the learner can find the new modules in the catalog and navigate to each module README

### Requirement: Catalog Includes Advanced Modules
The root module catalog SHALL list the advanced learning modules:
- `springboot-security`
- `springboot-web-client`
- `springboot-async-scheduling`
- `springboot-cache`

The catalog SHALL indicate whether a module is:
- a web module (and its port), or
- primarily test-driven.

#### Scenario: Pick a module by learning need
- **WHEN** a learner reads the root module catalog
- **THEN** the learner can identify the four advanced modules and how to run them (port or tests-first)

### Requirement: Progress Entry Point
The root documentation SHALL provide a single, explicit entry point for tracking learning progress (e.g., a `docs/progress.md` checklist) and link it from the root `README.md`.

#### Scenario: Track progress across modules
- **WHEN** a learner opens the root `README.md`
- **THEN** the learner can find and navigate to the progress checklist

### Requirement: Workspace Debug Toolbox Entry Point
The root `README.md` SHALL include a short “Debug 工具箱” section that links to common debugging approaches used across modules (logs/断点/断言/常用命令).

#### Scenario: Find debugging guidance quickly
- **WHEN** a learner encounters a failing Lab test
- **THEN** the learner can find a root-level debug guidance entry point without hunting across modules

### Requirement: Root Catalog Highlights Deep Dive Track
The root `README.md` SHALL explain the Deep Dive Track conventions (Labs vs `@Disabled` Exercises) and direct learners to at least one module that demonstrates the pattern clearly.

#### Scenario: Understand how to use exercises from the catalog
- **WHEN** a learner reads the root module catalog
- **THEN** the learner can find instructions for running Labs and enabling Exercises

### Requirement: Root Catalog Includes Capstone Module
The root `README.md` SHALL include the capstone module `springboot-business-case` in the module catalog.

#### Scenario: Find the capstone module
- **WHEN** a learner opens the root `README.md`
- **THEN** the learner can find `springboot-business-case` and navigate to its module README

