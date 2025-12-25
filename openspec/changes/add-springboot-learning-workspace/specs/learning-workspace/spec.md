## ADDED Requirements

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

