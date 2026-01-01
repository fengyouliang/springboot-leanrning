# learning-workspace Specification

## Purpose
TBD - created by archiving change add-springboot-learning-workspace. Update Purpose after archive.
## Requirements
### Requirement: Maven Multi-Module Workspace
The repository SHALL be organized as a Maven multi-module workspace with a single root build entry point.

#### Scenario: Build all modules from repository root
- **WHEN** a learner runs the root build command
- **THEN** all learning modules are built as part of the same workspace build

### Requirement: Modern Spring Boot Baseline
The workspace SHALL target Spring Boot `3.x` (pinned to the latest stable 3.x release at bootstrap, initially `3.5.9`) and Java `17`.

#### Scenario: Build on a supported JDK
- **WHEN** the learner builds the workspace using Java 17 or newer
- **THEN** the build completes successfully on the supported baseline

### Requirement: Use System Maven (No Wrapper)
The workspace SHALL be buildable using the system-installed `mvn` command and SHALL NOT require Maven Wrapper scripts.

#### Scenario: Build with system Maven
- **WHEN** a learner runs `mvn -q test` from the repository root
- **THEN** the workspace build completes without requiring `./mvnw`

### Requirement: Module Isolation
Each learning module SHALL be buildable and testable in isolation from the repository root.

#### Scenario: Build and test a single module
- **WHEN** a learner builds/tests a single module from the root workspace (e.g., using Maven module selection)
- **THEN** only that module (and its required dependencies) are built/tested

### Requirement: Workspace Build Includes Advanced Modules
The workspace SHALL include the advanced learning modules in the root build, and the default build SHALL stay green.

#### Scenario: Build all modules by default
- **WHEN** a learner runs `mvn -q test` from the repository root
- **THEN** the build includes the new modules and completes successfully without enabling exercises

### Requirement: CI Guarantees Default Build Stays Green
The workspace SHALL provide a GitHub Actions CI workflow that runs the default build (`mvn -q test`) on Java 17.

#### Scenario: Validate workspace build on every change
- **WHEN** a change is pushed to the repository
- **THEN** CI runs `mvn -q test` on Java 17
- **AND** the workflow fails if any enabled Lab test fails

### Requirement: Enforced Toolchain Baseline (Java + Maven)
The root build SHALL enforce a clear minimum toolchain baseline via Maven Enforcer:
- Java `17`
- Maven version aligned with repository documentation (at least `3.8+`)

#### Scenario: Fail fast on unsupported toolchain
- **WHEN** a learner runs `mvn -q test` with an unsupported Java or Maven version
- **THEN** the build fails with an actionable message explaining the supported baseline

### Requirement: Consistent Editor Defaults
The workspace SHALL provide a root `.editorconfig` to standardize line endings, indentation, and encoding to reduce non-learning-related diffs.

#### Scenario: Avoid noisy formatting diffs
- **WHEN** two learners edit files with different IDEs
- **THEN** the repository formatting defaults are consistent via `.editorconfig`

### Requirement: Low-Friction Common Commands
The workspace SHALL provide lightweight helper scripts under `scripts/` that encapsulate common commands:
- run all tests
- run a single module tests
- run a single module

#### Scenario: Run common commands without Maven flag memorization
- **WHEN** a learner wants to run tests or a module
- **THEN** the workspace provides simple scripts that map to the equivalent Maven commands

### Requirement: Workspace-Wide Deep Dive Coverage
The workspace SHALL provide a consistent Deep Dive Track across every learning module, as defined in `learning-module-template`.

#### Scenario: Build and test the workspace by default
- **WHEN** a learner runs `mvn -q test` from the repository root
- **THEN** the build passes without requiring any Exercise tests to be enabled

