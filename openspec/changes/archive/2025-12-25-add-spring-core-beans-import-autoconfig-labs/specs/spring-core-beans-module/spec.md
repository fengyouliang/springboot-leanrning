## ADDED Requirements

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

