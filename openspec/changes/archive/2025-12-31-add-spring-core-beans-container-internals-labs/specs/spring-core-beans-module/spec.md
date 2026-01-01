## ADDED Requirements

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

## MODIFIED Requirements

### Requirement: `spring-core-beans` Deep-Dive Bean Guide (README index + docs chapters)
The guide SHALL additionally cover container internals topics required by the new lab set, including bootstrap/infrastructure processors, ordering, early references, lazy semantics, depends-on, resolvable dependencies, context hierarchy, and bean name/alias behavior.

#### Scenario: Navigate the module by container mechanism
- **WHEN** a learner opens `spring-core-beans/README.md`
- **THEN** the learner can locate the new container internals Labs via a “Concept → Lab/Test → Code file” map
