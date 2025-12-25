# Design: Import + Auto-configuration Labs for `spring-core-beans`

## Goals
- Provide runnable, deterministic labs demonstrating:
  - `@Import` / `ImportSelector` / `ImportBeanDefinitionRegistrar`
  - Spring Boot auto-configuration: conditions (match/no-match) and override strategies
- Ensure each lab:
  - is self-contained and readable
  - asserts the key outcome
  - prints a small, stable “what to observe” output (not megabytes of logs)
- Keep default builds green:
  - labs are enabled and always pass
  - exercises are `@Disabled` and never break CI

## Key Design Decisions

### 1) Prefer lightweight contexts over full `@SpringBootTest`
Use:
- `AnnotationConfigApplicationContext` for pure Spring container import/registrar labs
- `ApplicationContextRunner` for Boot auto-configuration labs

Rationale:
- faster tests
- easier control over properties and classpath simulation
- deterministic behavior and minimal side-effects

### 2) Use local minimal auto-config classes (test scope)
Implement a small `@AutoConfiguration` class inside the test suite to demonstrate Boot mechanics.

Rationale:
- avoids relying on “real” Boot auto-config classes that may change across versions
- keeps the learning focus on mechanisms rather than framework catalog memorization

### 3) Make behavior observable without brittle output assertions
Labs should:
- print only a few lines (bean names present, chosen implementation, which branch matched)
- optionally capture output via `OutputCaptureExtension` for a small, stable assertion (e.g., a single marker line)

Avoid:
- asserting on full Condition Evaluation Report text (too verbose and version-sensitive)

## Proposed Lab Coverage (Test Structure)

### A) Import & Registrar Labs (`*LabTest`)
Experiments (enabled):
- `@Import` importing an extra `@Configuration` and verifying imported beans exist
- `ImportSelector` selecting one of multiple configurations based on an environment property
- `ImportBeanDefinitionRegistrar` programmatically registering a bean and verifying its `BeanDefinition` metadata

Exercises (disabled):
- change selector rules to invert imports
- intentionally introduce ambiguous beans and resolve via `@Primary` / `@Qualifier`
- register a prototype bean and observe scope behavior

### B) Boot Auto-configuration Labs (`*LabTest`)
Experiments (enabled) using `ApplicationContextRunner`:
- `@ConditionalOnProperty` gates bean registration
- `@ConditionalOnClass` gates bean registration (use a `FilteredClassLoader` to simulate missing optional dependency)
- `@ConditionalOnMissingBean` allows user-provided bean to override default auto-config
- demonstrate exclusion/disable strategy via properties (where applicable for the runner setup)

Exercises (disabled):
- change conditions and re-run
- change override strategy to create conflict and resolve it

## Documentation Touchpoints
- Update `spring-core-beans/README.md` and relevant `docs/*.md` chapters to reference:
  - new lab test class names
  - which test method demonstrates which concept
  - “what to observe” lines (matching the printed output)

