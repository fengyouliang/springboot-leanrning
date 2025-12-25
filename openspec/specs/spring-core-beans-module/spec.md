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
The `spring-core-beans` module SHALL provide a deep-dive learning guide (Chinese) that enables a learner to build a correct mental model of Spring beans, where:
- `spring-core-beans/README.md` is a navigable index for the module (run/test, reading path, and concept map)
- `spring-core-beans/docs/*.md` contain the deep-dive chapters

The guide SHALL cover, at minimum:
- bean definition vs bean instance
- bean registration entry points, including `@ComponentScan`, `@Bean`, and `@Import`
- advanced registration hooks: `ImportSelector` and `ImportBeanDefinitionRegistrar` (conceptual role and typical use cases)
- how Spring Boot auto-configuration influences the final bean graph (high-level mechanism + practical debugging/override techniques)
- dependency injection resolution and ambiguity handling (`@Qualifier`, `@Primary`)
- scope semantics and prototype injection strategies (`ObjectProvider`, `@Lookup`)
- lifecycle ordering and callbacks (initialization vs destruction)
- container extension points (`BeanFactoryPostProcessor` vs `BeanPostProcessor`)
- `@Configuration(proxyBeanMethods=...)` impact on `@Bean` method semantics
- `FactoryBean` product vs factory and the `"&"` prefix
- circular dependency behavior and common mitigation strategies

#### Scenario: Navigate the module by concept
- **WHEN** a learner opens `spring-core-beans/README.md`
- **THEN** the learner can find a “Concept → Lab/Test → Code file” map to locate the relevant runnable experiments for each topic
- **AND** the learner can navigate into `spring-core-beans/docs/*.md` chapters for deeper explanations

#### Scenario: Verify guide content is runnable
- **WHEN** a learner follows the guide and runs `mvn -q -pl spring-core-beans test`
- **THEN** the enabled lab tests pass without requiring exercises to be enabled
