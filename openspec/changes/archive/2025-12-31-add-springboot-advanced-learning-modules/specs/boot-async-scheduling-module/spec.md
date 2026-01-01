## ADDED Requirements

### Requirement: Async & Scheduling Deep Dive Track
The `springboot-async-scheduling` module SHALL provide a Deep Dive Track that teaches:
- `@Async` and proxy-based execution (including self-invocation pitfalls)
- executor configuration, thread naming, and sizing trade-offs
- exception propagation (`Future` vs `void`) and handling patterns
- basics of `@Scheduled` (fixedDelay/fixedRate/cron) and deterministic test approaches

The module SHALL include at least **18 experiments**, including at least **10 Labs** (enabled) and at least **8 Exercises** (`@Disabled`).

#### Scenario: Run async/scheduling labs by default
- **WHEN** a learner runs `mvn -q -pl springboot-async-scheduling test`
- **THEN** the enabled Lab tests pass without requiring exercises to be enabled

### Requirement: Async & Scheduling Docs Map to Experiments
The module SHALL include Chinese deep-dive chapters under `springboot-async-scheduling/docs/` that link to runnable experiments.

#### Scenario: Navigate from docs to tests
- **WHEN** a learner opens a `springboot-async-scheduling/docs/*.md` chapter
- **THEN** the chapter links to at least one corresponding `*LabTest` or `*ExerciseTest`

