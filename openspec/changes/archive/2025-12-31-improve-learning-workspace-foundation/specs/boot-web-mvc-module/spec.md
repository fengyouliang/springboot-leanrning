## ADDED Requirements

### Requirement: Web MVC Minimal Deep-Dive Docs
The `springboot-web-mvc` module SHALL provide a minimal set of Chinese deep-dive docs under `springboot-web-mvc/docs/` to support its Deep Dive Track, covering at least:
- validation boundary and error shaping
- exception handling mechanics and common pitfalls
- request binding and converters/formatters
- interceptor/filter ordering entry points

#### Scenario: Navigate from README to mechanism chapters
- **WHEN** a learner opens `springboot-web-mvc/README.md`
- **THEN** the README links to the recommended `docs/` reading order for the deep-dive topics

### Requirement: Docs Link Back to Runnable Experiments
Each added `springboot-web-mvc/docs/*.md` chapter SHALL link to at least one corresponding `*LabTest` or `*ExerciseTest` that demonstrates the described mechanism.

#### Scenario: Jump from explanation to experiment
- **WHEN** a learner reads a `docs/` chapter
- **THEN** the chapter points to the runnable test(s) that reproduce the described behavior

