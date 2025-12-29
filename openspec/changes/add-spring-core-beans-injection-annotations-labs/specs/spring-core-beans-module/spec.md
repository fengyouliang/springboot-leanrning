## ADDED Requirements

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

## MODIFIED Requirements

### Requirement: `spring-core-beans` Deep-Dive Bean Guide (README index + docs chapters)
The guide SHALL additionally cover injection-annotation variant topics required by the new lab set, including:
- `@Resource` name-based resolution mental model (and how it differs from `@Autowired`)
- candidate selection vs ordering mental model (`@Primary` / `@Priority` / `@Order`)
- `@Value` placeholder resolution semantics (non-strict vs strict via `PropertySourcesPlaceholderConfigurer`)

#### Scenario: Navigate the module by injection resolution mechanism
- **WHEN** a learner opens `spring-core-beans/README.md`
- **THEN** the learner can locate the new injection-annotation Labs via a “Concept → Lab/Test → Code file” map

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
