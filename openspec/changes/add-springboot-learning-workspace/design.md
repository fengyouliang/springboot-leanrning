## Context
The goal is to create a beginner-friendly Spring Boot learning repository. The repository should be easy to navigate and should encourage incremental learning by keeping each module narrowly focused.

## Goals / Non-Goals

### Goals
- Provide a multi-module workspace where each module teaches one Spring Boot topic.
- Keep modules easy to run locally with minimal prerequisites (prefer in-memory/embedded dependencies by default).
- Make module execution and testing consistent across the repository.

### Non-Goals
- Replicate the full size or breadth of Baeldung’s tutorials repository.
- Require Docker, external databases, or cloud services for the “happy path”.
- Build production-ready architectures; this is a learning sandbox.

## Decisions
- **Build system**: Use Maven multi-module to keep a single root build entry point and align with common Spring Boot learning material.
- **Baseline**: Pin Spring Boot to `3.5.9` (latest stable 3.x at bootstrap) and standardize on Java `17`.
- **Layout**: Keep modules flat at repository root (e.g., `springboot-web-mvc`).
- **Tooling**: Use system-installed Maven (`mvn`) only; do not include Maven Wrapper scripts.
- **Starter modules**: Bootstrap exactly 5 starter modules (exclude `springboot-security` for now).
- **Module independence**: Each `springboot-*` module is a standalone Spring Boot application to reduce cross-module coupling and simplify “run this module” learning.
- **Shared code**: Avoid a shared `common` module initially; duplication is acceptable for learning and keeps modules self-contained.
- **Data examples**: Use embedded/in-memory dependencies (e.g., H2) for database modules to avoid external setup.
- **Documentation**: Keep a root catalog plus per-module README files so learners can quickly choose a topic and follow a consistent run path.

## Risks / Trade-offs
- **Multi-module complexity**: Maven multi-module adds structure overhead; mitigate with a clear root README and consistent module conventions.
- **Duplication across modules**: Independent modules may repeat patterns; treat this as a learning aid (each module is a complete example).

## Migration Plan
Not applicable (repository bootstrap from an empty state).

## Open Questions
None for this change.
