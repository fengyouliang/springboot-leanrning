## ADDED Requirements

### Requirement: Workspace-Wide Deep Dive Coverage
The workspace SHALL provide a consistent Deep Dive Track across every learning module, as defined in `learning-module-template`.

#### Scenario: Build and test the workspace by default
- **WHEN** a learner runs `mvn -q test` from the repository root
- **THEN** the build passes without requiring any Exercise tests to be enabled

