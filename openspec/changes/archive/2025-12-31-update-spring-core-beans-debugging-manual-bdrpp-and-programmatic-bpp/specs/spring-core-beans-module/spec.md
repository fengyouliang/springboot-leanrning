# spring-core-beans-module Spec Delta

## ADDED Requirements

### Requirement: Debugging-manual blocks for BDRPP and programmatic BPP chapters
The `spring-core-beans` module SHALL upgrade the following deep-dive chapters to include a “debugging manual” block that enables fast breakpoint-driven learning:

- `docs/13-bdrpp-definition-registration.md` (BeanDefinitionRegistryPostProcessor / definition registration phase)
- `docs/25-programmatic-bpp-registration.md` (programmatic BeanPostProcessor registration)

Each chapter SHALL include:

- `## 源码最短路径（call chain）` describing the minimal call chain from the typical entry point to the critical mechanism branch
- `## 固定观察点（watch list）` listing a small set of debugger watch/evaluate items that let the learner verify the mechanism quickly
- `## 反例（counterexample）` describing a common pitfall, including at least one runnable Lab/Test entry that reproduces the pitfall (or demonstrates the correction)

#### Scenario: Navigate from symptom to runnable debug entry
- **WHEN** a learner opens the docs/13 or docs/25 chapter
- **THEN** the learner can locate the “call chain / watch list / counterexample” sections and run at least one referenced `*LabTest` (preferably a method-level entry) to reproduce the described behavior

