# Change: Add Spring Boot Learning Workspace

## Why
This repository is currently empty, which makes it hard for beginners to learn Spring Boot in a structured way.
A modular workspace (one module per topic) provides a low-friction path to explore Spring Boot features incrementally, similar in spirit to the structure used by Baeldung’s tutorials repository.

## What Changes
- Add a Maven multi-module workspace that hosts multiple focused Spring Boot learning modules.
- Define a consistent module template (runnable app, minimal tests, module-level README).
- Provide a root-level catalog so learners can quickly find the right module for a topic.

## Impact
- Affected specs:
  - `learning-workspace`
  - `learning-module-template`
  - `learning-module-catalog`
- Affected code (apply stage):
  - Root build files (e.g., `pom.xml`) (uses system `mvn`, no Maven Wrapper)
  - Module directories (`springboot-*`) with their own build, code, and docs
  - Root documentation (`README.md`)
