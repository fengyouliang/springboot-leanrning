## ADDED Requirements

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
For every newly added injection/proxying `*LabTest`, the module SHALL provide a corresponding Chinese deep-dive chapter under `spring-core-beans/docs/`.

Each chapter SHALL include:
- a link/path to the corresponding `*LabTest`
- the expected observable outcome (what to observe)
- the mechanism explanation (why it happens)
- debugging suggestions and common pitfalls
- cross-links to the relevant AOP/Tx learning modules for follow-up learning

#### Scenario: Navigate from docs to runnable experiments
- **WHEN** a learner opens a new injection/proxying `spring-core-beans/docs/` chapter
- **THEN** the chapter points to at least one runnable `*LabTest` that demonstrates the described mechanism

## MODIFIED Requirements

### Requirement: `spring-core-beans` Deep-Dive Bean Guide (README index + docs chapters)
The guide SHALL additionally cover injection and proxying mental-model topics required by the new lab set, including:
- injection/property population timing and its relationship to `@Autowired`
- proxying/wrapping as a container mechanism that explains AOP/Tx “must go through proxy” behavior

#### Scenario: Navigate the module by injection/proxying mechanism
- **WHEN** a learner opens `spring-core-beans/README.md`
- **THEN** the learner can locate the new injection/proxying Labs via a “Concept → Lab/Test → Code file” map
