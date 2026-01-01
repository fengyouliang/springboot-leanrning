## ADDED Requirements

### Requirement: Workspace Build Includes Advanced Modules
The workspace SHALL include the advanced learning modules in the root build, and the default build SHALL stay green.

#### Scenario: Build all modules by default
- **WHEN** a learner runs `mvn -q test` from the repository root
- **THEN** the build includes the new modules and completes successfully without enabling exercises

