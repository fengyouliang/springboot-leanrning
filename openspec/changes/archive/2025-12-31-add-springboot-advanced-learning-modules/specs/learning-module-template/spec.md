## ADDED Requirements

### Requirement: Test-Driven Modules Are First-Class
The learning module template SHALL support a tests-first learning path: a learning module MAY be primarily test-driven (i.e., the primary learning path is running `*LabTest` and reading `docs/`), as long as:
- the module still provides clear, observable outcomes through tests (assertions)
- the module `README.md` explicitly documents the recommended run path (tests-first or run-first)

#### Scenario: Learn without running a server
- **WHEN** a learner follows a test-driven module’s `README.md`
- **THEN** the learner can reproduce the learning outcomes by running module tests only

### Requirement: Explicit Port Policy for Web Modules
Any module that starts an HTTP server SHALL explicitly configure `server.port` in `application.properties` and document it in the module `README.md`, avoiding conflicts with other modules.

#### Scenario: Avoid port conflicts
- **WHEN** a learner runs two different web modules
- **THEN** the modules do not conflict on ports because each web module declares its own `server.port`

### Requirement: Deterministic Tests Without External Infrastructure
Deep-dive experiments SHALL avoid reliance on external infrastructure (Docker services, external HTTP endpoints, etc.) and SHALL use in-process or embedded substitutes (e.g., in-memory DB, in-process mock HTTP server) to keep tests deterministic.

#### Scenario: Run tests offline
- **WHEN** a learner runs `mvn -q -pl <module> test` without external services
- **THEN** the enabled Lab tests pass deterministically
