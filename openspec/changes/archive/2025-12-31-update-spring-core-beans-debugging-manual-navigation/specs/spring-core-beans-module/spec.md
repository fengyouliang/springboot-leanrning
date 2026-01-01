## ADDED Requirements

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

