# Change: Upgrade Workspace to a Deep-Dive Learning Track

## Why
The current modules are intentionally minimal and runnable, but the examples are too shallow to support serious learning:
- Learners can run the code, but they do not build mental models of **how the container works** (bean definitions, post-processors, proxying).
- Most topics are presented as a single “happy path” with little coverage of common pitfalls and internal mechanics.
- There is no realistic “capstone” business flow that connects Validation, AOP, Events, JPA, and Transactions end-to-end.

This change introduces a consistent, repository-wide **Deep Dive Track** and a practical, realistic **Business Case** module.

## What Changes
- Introduce a repository-wide **Deep Dive Track**:
  - Every module provides **15+ experiments** with a consistent structure.
  - “Labs” remain enabled and always green (happy path + observable mechanism).
  - “Exercises” are provided as `@Disabled` tests that learners can enable manually.
- Add a new capstone module `springboot-business-case` to demonstrate a realistic flow that connects:
  - MVC boundary + Validation
  - transactional service layer
  - Events and listeners
  - AOP for cross-cutting concerns (tracing/metrics)
  - persistence via Spring Data JPA + embedded database
- Standardize learning documentation:
  - each module lists labs + exercises in its `README.md`
  - the root `README.md` highlights the Deep Dive Track and the new capstone module

## Impact
- Affected specs (this change):
  - `learning-module-template` (Deep Dive Track + disabled exercises conventions)
  - `learning-workspace` (workspace-level deep-dive coverage and build guarantees)
  - `learning-module-catalog` (catalog + deep-dive entry points)
  - Module capability specs for all existing modules (topic maps for deep-dive coverage)
  - `springboot-business-case-module` (new capstone module)
- Affected code (apply stage):
  - tests and documentation in every module
  - root `README.md` catalog updates (Chinese)
  - new module `springboot-business-case/` (code, tests, README, Maven module wiring)

## Out of Scope
- External infrastructure (Docker-based dependencies, Kafka, Redis, etc.)
- Production-grade observability stacks (tracing exporters, metrics backends)
- Build-system migration (e.g., Maven → Gradle) or adding Maven Wrapper
