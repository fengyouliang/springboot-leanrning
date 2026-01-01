## ADDED Requirements

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

