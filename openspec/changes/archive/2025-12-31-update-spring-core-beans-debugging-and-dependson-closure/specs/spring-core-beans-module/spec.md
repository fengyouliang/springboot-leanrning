## ADDED Requirements

### Requirement: `docs/11` provides an advanced “source-level closure” troubleshooting playbook
The `spring-core-beans` guide SHALL enhance `spring-core-beans/docs/11-debugging-and-observability.md` so experienced learners can debug container behavior by following a repeatable, source-level loop rather than relying on logs or guesswork.

The chapter SHALL include, at minimum:

1) An “observation objects overview” that frames container debugging as inspecting a small set of object/data-structure categories, including:
   - `BeanDefinition` (registry/original definition)
   - merged `RootBeanDefinition` (final recipe)
   - bean instance vs proxy/wrapper (final exposed object)
   - dependency graph structures (`dependentBeanMap` / `dependenciesForBeanMap`)
   - singleton caches (including early references for circular dependency behavior)

2) A “proxy diagnosis loop” describing a minimal, runnable path to answer:
   - how to confirm the object is a proxy (JDK vs CGLIB at a high level)
   - where proxy replacement typically happens in the create/initialize chain
   - how to identify the specific `BeanPostProcessor` that performed the replacement

3) A triage decision tree that routes common symptoms to:
   - a recommended breakpoint entry point
   - a recommended watch list
   - a runnable minimal Lab/Test entrypoint

#### Scenario: Navigate from a symptom to a runnable closure
- **WHEN** a learner encounters a container symptom (wrong candidate injected, bean missing, proxy shape unexpected, ordering surprising)
- **THEN** the learner can use `docs/11` to pick an observation category, set a breakpoint, and run a minimal Lab/Test that reproduces the symptom

### Requirement: Exception navigation includes dependsOn topology-cycle identification
The exception navigation table in `spring-core-beans/docs/11-debugging-and-observability.md` SHALL include a dedicated entry for the dependsOn topology-cycle signature:

- `Circular depends-on relationship`

The entry SHALL:

- identify it as a definition-layer topology cycle (distinct from runtime circular dependencies/early references)
- recommend 1–3 breakpoint entry points (method-level `Class#method` preferred)
- link to `spring-core-beans/docs/19-depends-on.md`
- link to a runnable minimal Lab/Test entrypoint:
  - `SpringCoreBeansDependsOnLabTest.dependsOn_cycle_failsFast()`

#### Scenario: Avoid misclassifying dependsOn cycles as circular dependency caching issues
- **WHEN** a learner sees an exception message containing `Circular depends-on relationship`
- **THEN** the learner can use the navigation table to jump to the dependsOn topology-cycle reproduction and debug entry points

### Requirement: `docs/19` covers advanced dependsOn interactions and provides runnable closures
The `spring-core-beans` guide SHALL enhance `spring-core-beans/docs/19-depends-on.md` to cover high-frequency advanced interactions that experienced learners commonly misinterpret.

The chapter SHALL include:

- an explicit section describing `dependsOn` × `@Lazy` (or lazy-init) interaction, stating that dependsOn can force instantiation via `getBean(dep)` before creating the dependent
- a brief mechanism explanation of why dependsOn does not influence DI candidate selection (create-time precondition vs injection-time resolution)
- a “write-in timing” comparison for how `dependsOn` metadata enters `BeanDefinition` (component scanning, `@Bean` parsing, programmatic registration)
- at least one runnable Lab/Test entrypoint per advanced interaction

#### Scenario: Reproduce and verify dependsOn interactions
- **WHEN** a learner follows `docs/19` advanced interaction sections
- **THEN** the learner can run a minimal Lab/Test that reproduces the described behavior and observe/verify it with breakpoints and assertions

### Requirement: Provide closure-style Labs for dependsOn × lazy instantiation and destroy ordering
The `spring-core-beans` module SHALL include enabled Labs (`*LabTest`) that provide minimal, assertion-based reproductions for:

- dependsOn forcing instantiation of a lazy dependency during refresh/creation
- dependsOn influencing destroy order via dependency graph recording

#### Scenario: Run dependsOn closure labs by default
- **WHEN** a learner runs `mvn -q -pl spring-core-beans test`
- **THEN** the new dependsOn closure labs pass by default (without enabling exercises)

