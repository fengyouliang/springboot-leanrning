## ADDED Requirements

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

