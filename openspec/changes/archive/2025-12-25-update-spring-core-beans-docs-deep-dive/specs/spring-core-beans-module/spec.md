## ADDED Requirements

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
