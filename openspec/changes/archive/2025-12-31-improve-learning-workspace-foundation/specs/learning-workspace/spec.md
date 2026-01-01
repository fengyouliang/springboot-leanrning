## ADDED Requirements

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

