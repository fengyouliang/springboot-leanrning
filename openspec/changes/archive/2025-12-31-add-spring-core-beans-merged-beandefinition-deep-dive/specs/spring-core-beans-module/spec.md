## ADDED Requirements

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
