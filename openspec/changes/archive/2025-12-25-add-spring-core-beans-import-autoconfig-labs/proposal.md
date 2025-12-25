# Change: Add Runnable Labs for `@Import` / `ImportSelector` / Registrar and Spring Boot Auto-configuration

## Why
The `spring-core-beans` module already documents advanced bean registration entry points (`@Import`, `ImportSelector`, `ImportBeanDefinitionRegistrar`) and Spring Boot auto-configuration concepts (conditions, overrides). However, learners currently lack **runnable labs** that:

- make these mechanisms observable (what gets registered, when, and why)
- include **assertions** that pin the expected outcomes
- produce a small amount of **console output** learners can read while the tests run

Adding focused labs turns the documentation into a hands-on deep dive where learners can verify mental models by running `mvn -q -pl spring-core-beans test`.

## What Changes
- Add new enabled `*LabTest` experiments in `spring-core-beans` that specifically cover:
  - `@Import` importing configuration classes
  - `ImportSelector` selecting imports based on environment/property
  - `ImportBeanDefinitionRegistrar` registering `BeanDefinition` programmatically (including reading annotation attributes)
  - Spring Boot auto-configuration behavior using a minimal local `@AutoConfiguration`, including:
    - condition match / no-match (`@ConditionalOnProperty`, `@ConditionalOnClass`)
    - override strategies (`@ConditionalOnMissingBean`, user-provided beans, exclusion/property toggles)
- Add `@Disabled` `*ExerciseTest` items for learners to extend the labs (change conditions, swap defaults, introduce ambiguity, etc.).
- Update `spring-core-beans` docs index and relevant chapters to link to the new labs and provide “what to observe” pointers.

## Impact
- Affected specs:
  - `spring-core-beans-module`
- Affected code/docs (apply stage):
  - `spring-core-beans/src/test/java/.../*LabTest.java` (new tests)
  - `spring-core-beans/src/test/java/.../*ExerciseTest.java` (optional new exercises)
  - `spring-core-beans/README.md` and/or `spring-core-beans/docs/*.md` (small navigation updates)

## Out of Scope
- Adding production features to the module runtime code (labs live in tests)
- Introducing external infrastructure dependencies
- Replacing existing labs or changing their semantics

