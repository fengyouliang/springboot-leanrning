# spring-core-beans-module Specification

## Purpose
Define the learning requirements for the `spring-core-beans` module, focusing on (1) runnable, assertion-based Labs that demonstrate advanced bean registration and Spring Boot auto-configuration mechanisms, and (2) a Chinese deep-dive documentation set (README index + `docs/*.md`) that teaches Spring Bean fundamentals and common pitfalls.
## Requirements
### Requirement: Import and Boot Auto-configuration Labs
The `spring-core-beans` module SHALL include enabled Labs (`*LabTest`) that teach advanced bean registration and Spring Boot auto-configuration mechanisms through runnable experiments with assertions, including:
- `@Import` importing additional configuration
- `ImportSelector` selecting imports based on environment/property
- `ImportBeanDefinitionRegistrar` registering `BeanDefinition` programmatically
- Spring Boot auto-configuration conditions and override strategies (at least `@ConditionalOnProperty`, `@ConditionalOnClass`, and `@ConditionalOnMissingBean`)

#### Scenario: Run labs by default
- **WHEN** a learner runs `mvn -q -pl spring-core-beans test`
- **THEN** the enabled lab tests pass without requiring exercises to be enabled

#### Scenario: Observe auto-configuration outcomes
- **WHEN** a learner runs the auto-configuration lab tests
- **THEN** the test output provides a small set of human-readable “what to observe” lines that explain which branch matched and which bean was ultimately selected

### Requirement: `spring-core-beans` Deep-Dive Bean Guide (README index + docs chapters)
The guide SHALL additionally cover injection-annotation variant topics required by the new lab set, including:
- `@Resource` name-based resolution mental model (and how it differs from `@Autowired`)
- candidate selection vs ordering mental model (`@Primary` / `@Priority` / `@Order`)
- `@Value` placeholder resolution semantics (non-strict vs strict via `PropertySourcesPlaceholderConfigurer`)

#### Scenario: Navigate the module by injection resolution mechanism
- **WHEN** a learner opens `spring-core-beans/README.md`
- **THEN** the learner can locate the new injection-annotation Labs via a “Concept → Lab/Test → Code file” map

### Requirement: Injection phase deep-dive labs (bridge to `@Autowired`)
The `spring-core-beans` module SHALL include at least one additional enabled Lab (`*LabTest`) that teaches the injection/property-population phase through runnable, assertion-based experiments.

The lab(s) SHALL demonstrate, at minimum:
- instantiation-aware post-processing during the property population phase (e.g., `postProcessProperties`)
- the relative timing between injection and initialization callbacks (e.g., `@PostConstruct`)
- a contrast between field injection and constructor injection that helps learners map both behaviors to container extension points
- a clear conceptual mapping to Spring’s infrastructure processors (notably `AutowiredAnnotationBeanPostProcessor` and `CommonAnnotationBeanPostProcessor`)

#### Scenario: Run injection phase labs by default
- **WHEN** a learner runs `mvn -q -pl spring-core-beans test`
- **THEN** the new injection phase Lab tests pass without requiring exercises to be enabled

### Requirement: Proxying phase deep-dive labs (bridge to AOP/Tx mental model)
The `spring-core-beans` module SHALL include at least one additional enabled Lab (`*LabTest`) that demonstrates the “proxying/wrapping” pattern as a container mechanism, through runnable, assertion-based experiments.

The lab(s) SHALL demonstrate, at minimum:
- a `BeanPostProcessor` returning a proxy/wrapper object after initialization as the final exposed bean
- the impact of proxy type exposure on type-based lookup/injection (interface vs class)
- a self-invocation pitfall explanation that is consistent with AOP/Tx behavior (call path must go through the proxy)

#### Scenario: Run proxying phase labs by default
- **WHEN** a learner runs `mvn -q -pl spring-core-beans test`
- **THEN** the new proxying phase Lab tests pass without requiring exercises to be enabled

### Requirement: One docs chapter per new lab (injection + proxying)
For every newly added injection/proxying/injection-annotation `*LabTest`, the module SHALL provide a corresponding Chinese deep-dive chapter under `spring-core-beans/docs/`.

Each chapter SHALL include:
- a link/path to the corresponding `*LabTest`
- the expected observable outcome (what to observe)
- the mechanism explanation (why it happens)
- debugging suggestions and common pitfalls
- cross-links to the relevant learning modules for follow-up learning (e.g., AOP/Tx when proxying is involved)

#### Scenario: Navigate from docs to runnable experiments
- **WHEN** a learner opens a new injection/proxying/injection-annotation `spring-core-beans/docs/` chapter
- **THEN** the chapter points to at least one runnable `*LabTest` that demonstrates the described mechanism

### Requirement: Spring Core Beans Module
The workspace SHALL provide a learning module named `spring-core-beans` that teaches Spring Framework IoC container fundamentals, including bean registration, dependency injection, bean scopes, and basic lifecycle callbacks.

#### Scenario: Build, test, and observe bean behavior
- **WHEN** a learner runs `mvn -q -pl spring-core-beans test`
- **THEN** the module tests pass and demonstrate at least one core bean behavior (for example: injection, scope, or lifecycle)
- **AND** the learner can run the module via `mvn -pl spring-core-beans spring-boot:run` to observe a topic-relevant output

### Requirement: Container internals labs (core)
The `spring-core-beans` module SHALL include additional enabled Labs (`*LabTest`) that teach container internals mechanisms through runnable, assertion-based experiments.

The lab set SHALL include, at minimum:
- container bootstrap and infrastructure processors (why annotations work)
- `BeanDefinitionRegistryPostProcessor` registration timing and capabilities
- ordering semantics for BFPP/BPP (`PriorityOrdered`/`Ordered`/unordered)
- pre-instantiation short-circuit via instantiation-aware post-processing
- early bean references and circular dependency interactions (early proxy/wrapper)
- lifecycle callback ordering (Aware/BPP/init/destroy) and scope interactions
- `@Lazy` semantics (bean-level vs injection-point lazy)
- `@DependsOn` semantics (forced initialization order)
- `registerResolvableDependency` injection semantics
- parent/child `ApplicationContext` hierarchy visibility rules
- bean name and alias resolution behaviors

#### Scenario: Run the container internals labs by default
- **WHEN** a learner runs `mvn -q -pl spring-core-beans test`
- **THEN** all enabled `*LabTest` tests pass without requiring exercises to be enabled

### Requirement: One docs chapter per Lab
For every newly added container-internals `*LabTest`, the module SHALL provide a corresponding Chinese deep-dive chapter under `spring-core-beans/docs/`.

Each chapter SHALL include:
- a link/path to the corresponding `*LabTest`
- the expected observable outcome (what to observe)
- the mechanism explanation (why it happens)
- common pitfalls and debugging suggestions

#### Scenario: Navigate from docs to runnable experiments
- **WHEN** a learner opens a new `spring-core-beans/docs/` chapter
- **THEN** the chapter points to at least one runnable `*LabTest` that demonstrates the described mechanism

### Requirement: Injection annotation variants labs (`@Resource`, `@Value`, `@Priority`)
The `spring-core-beans` module SHALL include additional enabled Labs (`*LabTest`) that teach injection-annotation variants and resolution rules through runnable, assertion-based experiments.

The lab set SHALL include, at minimum:
- `@Resource` name-based injection semantics and its relationship to `CommonAnnotationBeanPostProcessor`
- single-injection candidate selection semantics for `@Primary` vs `@Priority` (and clarify that `@Order` is primarily about collection injection ordering)
- `@Value("${...}")` placeholder resolution via embedded value resolvers and property sources, including a contrast between the default (non-strict) environment resolver and the strict behavior enabled by registering `PropertySourcesPlaceholderConfigurer`

#### Scenario: Run injection-annotation labs by default
- **WHEN** a learner runs `mvn -q -pl spring-core-beans test`
- **THEN** all enabled `*LabTest` tests pass without requiring exercises to be enabled

#### Scenario: Understand resolution outcomes without long logs
- **WHEN** a learner runs the new injection-annotation lab tests
- **THEN** each test provides a small set of human-readable “what to observe” lines and asserts the key resolution outcome (selected bean / injected value), without relying on long log output assertions

### Requirement: Merged BeanDefinition deep-dive lab + chapter
The `spring-core-beans` module SHALL include an enabled Lab (`*LabTest`) and a corresponding Chinese deep-dive chapter that teach `BeanDefinition` merging (merged `RootBeanDefinition`) through runnable, assertion-based experiments.

The Lab and chapter SHALL demonstrate, at minimum:
- that the “original” `BeanDefinition` retrieved from the registry is not always the final definition used for instantiation, due to merging into a `RootBeanDefinition`
- a deterministic parent/child `BeanDefinition` case where merged metadata is observable (e.g., property values, init/destroy method names, scope/lazy flags)
- the key entry points for deep debugging: `getMergedLocalBeanDefinition(...)` and `MergedBeanDefinitionPostProcessor#postProcessMergedBeanDefinition(...)`
- a conceptual bridge to injection/lifecycle metadata preparation (why annotation processors often rely on merged-definition hooks)

#### Scenario: Learn merged-definition behavior via runnable lab
- **WHEN** a learner runs `mvn -q -pl spring-core-beans test`
- **THEN** the merged BeanDefinition Lab is enabled by default and passes with assertions

#### Scenario: Navigate from the chapter to breakpoints
- **WHEN** a learner opens the merged BeanDefinition chapter under `spring-core-beans/docs/`
- **THEN** the chapter links to the corresponding `*LabTest` and lists 1–3 recommended breakpoint entry points

### Requirement: Troubleshooting map (exception -> breakpoint entry points)
The `spring-core-beans` guide SHALL provide a concise “exception -> breakpoint entry points” mapping to shorten the path from an error message to the most effective debugging entry points.

The mapping SHALL include, at minimum:
- `UnsatisfiedDependencyException` -> dependency resolution entry points (e.g., `doResolveDependency`)
- `NoSuchBeanDefinitionException` -> missing candidate / definition lookup entry points
- `BeanCurrentlyInCreationException` -> singleton creation / circular dependency entry points (e.g., `getSingleton`, `preInstantiateSingletons`)

#### Scenario: Jump from error to the correct breakpoint
- **WHEN** a learner encounters one of the mapped exceptions while running labs
- **THEN** the guide provides a direct breakpoint recommendation and links to at least one relevant chapter and Lab

### Requirement: Consistent chapter footer (Lab/Test + breakpoints)
All `spring-core-beans/docs/*.md` chapters SHALL end with a consistent 1–2 line footer that turns reading into a runnable “challenge path”.

The footer SHALL include:
- `对应 Lab/Test：...` (a clickable file path)
- `推荐断点：...` (1–3 breakpoint entry points)

#### Scenario: Review any chapter and quickly re-run it as an experiment
- **WHEN** a learner scrolls to the end of any `spring-core-beans/docs/*.md` chapter
- **THEN** the learner can immediately locate a runnable `*LabTest` and 1–3 recommended breakpoint entry points

### Requirement: Bean graph debugging helper (print candidates + dependency chain)
The `spring-core-beans` module SHALL include a small, test-only debugging helper and an enabled Lab that print a compact “bean graph” view suitable for learning and troubleshooting.

The helper and Lab SHALL, at minimum:
- print the candidate set for at least one injection point (type-based lookup), and show which bean is ultimately injected
- print a short, human-readable dependency chain related to the injection point
- align with the `docs/11` troubleshooting flow (candidate set -> narrowing rules -> final injection result)

#### Scenario: Observe bean-graph output while keeping tests deterministic
- **WHEN** a learner runs the bean-graph debugging Lab
- **THEN** the output includes a small set of `OBSERVE:` lines and the test still asserts key invariants (no log-based assertions)

### Requirement: Mechanism deep-dive chapters use a heavy “source anchors + breakpoint loop” template
The `spring-core-beans` module SHALL standardize its mechanism deep-dive documentation chapters so that advanced learners can map concepts to Spring internals and close the loop via runnable Lab/Test breakpoints.

For this requirement, “mechanism deep-dive chapters” are defined as:

- `spring-core-beans/docs/12-*.md` … `spring-core-beans/docs/34-*.md`
- excluding list/self-check chapters (`spring-core-beans/docs/90-*`, `spring-core-beans/docs/99-*`)
- excluding foundation chapters (`spring-core-beans/docs/01-*` … `11-*`)

Each mechanism deep-dive chapter SHALL include the following sections (headings must match exactly for searchability):

1) `## 源码锚点（建议从这里下断点）`
   - SHALL list at least 3 “class#method” anchors (method-level preferred)
   - SHALL include a 1-line “why this anchor matters” hint per anchor (can be brief)

2) `## 断点闭环（用本仓库 Lab/Test 跑一遍）`
   - SHALL link to at least one runnable repository test entrypoint (typically a `*LabTest` file path; a specific test method is acceptable)
   - SHALL include a recommended breakpoint list (typically 3–6 points) and “what to observe” notes

3) `## 排障分流：这是定义层问题还是实例层问题？`
   - SHALL provide at least 3 symptom-to-layer triage bullets
   - SHALL cross-link to either the chapter’s own Lab/Test entrypoint or a relevant debugging chapter (e.g., container visibility / DI resolution)

#### Scenario: Find where to debug a mechanism chapter
- **WHEN** a learner opens any mechanism deep-dive chapter under `spring-core-beans/docs/12-*.md` … `34-*.md`
- **THEN** the learner can immediately locate “源码锚点” and identify at least 3 “class#method” anchors to set breakpoints on

#### Scenario: Close the loop with runnable experiments
- **WHEN** a learner follows a chapter’s “断点闭环” section and runs the referenced `*LabTest`
- **THEN** the learner can reproduce and observe the described mechanism using the suggested breakpoints, without needing a full Spring Boot application run

### Requirement: Key chapters provide a “debugging manual” block (call chain + watch list + counterexample)
The `spring-core-beans` guide SHALL deepen a small set of key chapters into “debugging-manual style” content so learners can quickly converge from a breakpoint to the correct internal branch and data structure.

The following chapters are in-scope for this requirement:

- `spring-core-beans/docs/03-dependency-injection-resolution.md`
- `spring-core-beans/docs/19-depends-on.md`
- `spring-core-beans/docs/35-merged-bean-definition.md`

Each in-scope chapter SHALL include the following three sections (headings must match exactly for searchability):

1) `## 源码最短路径（call chain）`
   - SHALL list a minimal call chain using `Class#method` nodes
   - SHALL annotate each node with a brief “what to observe here” hint

2) `## 固定观察点（watch list）`
   - SHALL provide a watch list that includes both local variables and one or more relevant container internal structures (e.g., maps/caches)
   - SHALL explain, briefly, what question each watch item answers

3) `## 反例（counterexample）`
   - SHALL include a minimal counterexample describing a common misinterpretation
   - SHALL link to a runnable repository test entrypoint (a `*LabTest` file path; a specific test method is acceptable)

Additionally:

- The `docs/03` chapter SHOULD describe `DefaultListableBeanFactory#doResolveDependency` narrowing rules as a step-by-step debugging manual (candidate collection -> narrowing -> final selection).
- The `docs/19` chapter SHALL retain the existing mechanism-template headings required by the module’s documentation pattern (source anchors / breakpoint loop / triage), and add the debugging-manual block in a compatible way.
- The `docs/35` chapter SHALL include an explicit placement of merged-definition computation and `MergedBeanDefinitionPostProcessor` hooks within the `createBean -> doCreateBean` chain.

#### Scenario: Jump from a concept to a minimal call chain
- **WHEN** a learner opens any of the in-scope chapters (`docs/03`, `docs/19`, `docs/35`)
- **THEN** the learner can immediately locate a minimal call chain and a watch list that map the chapter’s concept to concrete source-level debug steps

### Requirement: Exception navigation table includes high-frequency exceptions and runnable entrypoints
The `spring-core-beans` guide SHALL provide a concise “exception -> breakpoint entry points -> runnable Lab/Test” navigation table so learners can jump from an error message to the correct debugging entry points and a minimal reproducible experiment.

The table SHALL be located in:

- `spring-core-beans/docs/11-debugging-and-observability.md`

The table SHALL include, at minimum, the following exceptions:

- `NoSuchBeanDefinitionException`
- `NoUniqueBeanDefinitionException`
- `UnsatisfiedDependencyException`
- `BeanCurrentlyInCreationException`
- `BeanCreationException`
- `BeanDefinitionStoreException`

For each exception row, the table SHALL include:

- 1–3 recommended breakpoint entry points (method-level, `Class#method` preferred)
- a link to at least one relevant chapter
- a runnable repository test entrypoint (a `*LabTest` file path; a specific test method is acceptable)

#### Scenario: Navigate from an exception to a runnable reproduction
- **WHEN** a learner encounters one of the mapped exceptions while running module labs or exercises
- **THEN** the learner can use the table to pick a breakpoint entry point and run a minimal test that reproduces the exception

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

### Requirement: Spring Core Beans Container Internals Deep Dive
The `spring-core-beans` module SHALL include deep dive Labs and `@Disabled` Exercises that teach Spring IoC container internals, including:
- bean definition vs bean instance
- lifecycle ordering and initialization callbacks
- `BeanFactoryPostProcessor` vs `BeanPostProcessor`
- how `@Configuration` enhancement affects `@Bean` method semantics
- prototype injection strategies (`ObjectProvider`, `@Lookup`)
- `FactoryBean` basics and common confusion points
- circular dependency behavior and mitigation strategies

#### Scenario: Verify deep dive labs are runnable
- **WHEN** a learner runs `mvn -q -pl spring-core-beans test`
- **THEN** the enabled lab tests pass without requiring exercises to be enabled

