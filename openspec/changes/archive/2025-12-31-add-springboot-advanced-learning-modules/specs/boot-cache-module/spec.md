## ADDED Requirements

### Requirement: Cache Deep Dive Track (Spring Cache + Caffeine)
The `springboot-cache` module SHALL provide a Deep Dive Track that teaches Spring Cache abstraction and common pitfalls, including:
- `@Cacheable`, `@CachePut`, `@CacheEvict` semantics
- default vs custom cache keys, and SpEL-based key/condition/unless usage
- cache eviction patterns and consistency pitfalls
- cache stampede mitigation via `sync = true`
- deterministic cache expiry experiments using an in-memory cache implementation (Caffeine)

The module SHALL include at least **18 experiments**, including at least **10 Labs** (enabled) and at least **8 Exercises** (`@Disabled`).

#### Scenario: Run cache labs by default
- **WHEN** a learner runs `mvn -q -pl springboot-cache test`
- **THEN** the enabled Lab tests pass without requiring exercises to be enabled

### Requirement: Cache Docs Map to Experiments
The module SHALL include Chinese deep-dive chapters under `springboot-cache/docs/` that link to runnable experiments.

#### Scenario: Navigate from docs to tests
- **WHEN** a learner opens a `springboot-cache/docs/*.md` chapter
- **THEN** the chapter links to at least one corresponding `*LabTest` or `*ExerciseTest`

