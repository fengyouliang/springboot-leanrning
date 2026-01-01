## ADDED Requirements

### Requirement: Security Deep Dive Track (AuthN → AuthZ → JWT)
The `springboot-security` module SHALL provide a Deep Dive Track that teaches Spring Security mechanisms end-to-end, including:
- authentication vs authorization (401 vs 403)
- request authorization rules (matchers) and role-based access control
- CSRF defaults and how to handle APIs vs browser flows
- method security (`@PreAuthorize` / `@PostAuthorize`) and its relationship to proxies
- filter chain composition and ordering (including inserting a custom filter)
- stateless authentication using JWT-style bearer tokens (learnable, testable baseline)

The module SHALL include at least **20 experiments**, including at least **12 Labs** (enabled) and at least **8 Exercises** (`@Disabled`).

#### Scenario: Run security labs by default
- **WHEN** a learner runs `mvn -q -pl springboot-security test`
- **THEN** the enabled Lab tests pass without requiring exercises to be enabled

### Requirement: Security Module Docs Map to Experiments
The `springboot-security` module SHALL include Chinese deep-dive chapters under `springboot-security/docs/` that map each topic to runnable experiments.

#### Scenario: Navigate from docs to tests
- **WHEN** a learner opens a `springboot-security/docs/*.md` chapter
- **THEN** the chapter links to at least one corresponding `*LabTest` or `*ExerciseTest`

### Requirement: Web Boundary Is Observable
The module SHALL provide at least one minimal HTTP boundary (endpoints) so learners can observe security behavior at the web layer.

#### Scenario: Observe security behavior via HTTP
- **WHEN** a learner runs `mvn -pl springboot-security spring-boot:run`
- **THEN** the module starts on its documented `server.port`
- **AND** learners can observe authentication/authorization behavior via HTTP requests

