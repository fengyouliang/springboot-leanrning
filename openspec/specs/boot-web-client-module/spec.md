# boot-web-client-module Specification

## Purpose
TBD - created by archiving change add-springboot-advanced-learning-modules. Update Purpose after archive.
## Requirements
### Requirement: Web Client Deep Dive Track (RestClient vs WebClient)
The `springboot-web-client` module SHALL provide a Deep Dive Track that teaches HTTP client mechanics and test strategies, including:
- a side-by-side comparison of RestClient (blocking) and WebClient (reactive)
- JSON request/response mapping
- error handling (4xx/5xx → domain exception)
- timeouts and retry behavior (deterministic and testable)
- client interceptors/filters for cross-cutting concerns (e.g., headers/correlation id)
- test strategies using an in-process mock HTTP server

The module SHALL include at least **20 experiments**, including at least **12 Labs** (enabled) and at least **8 Exercises** (`@Disabled`).

#### Scenario: Run web-client labs by default
- **WHEN** a learner runs `mvn -q -pl springboot-web-client test`
- **THEN** the enabled Lab tests pass without requiring exercises to be enabled

### Requirement: Web Client Docs Map to Experiments
The module SHALL include Chinese deep-dive chapters under `springboot-web-client/docs/` that link to runnable experiments.

#### Scenario: Navigate from docs to tests
- **WHEN** a learner opens a `springboot-web-client/docs/*.md` chapter
- **THEN** the chapter links to at least one corresponding `*LabTest` or `*ExerciseTest`

