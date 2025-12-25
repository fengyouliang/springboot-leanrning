## 1. Import / Selector / Registrar Labs
- [x] 1.1 Add a new enabled `*LabTest` covering `@Import` with clear assertions and minimal “what to observe” output
- [x] 1.2 Add a lab covering `ImportSelector` (property-driven selection) and verify the selected configuration wins
- [x] 1.3 Add a lab covering `ImportBeanDefinitionRegistrar` registering a bean programmatically, plus a metadata assertion via `BeanDefinition`

## 2. Spring Boot Auto-configuration Labs
- [x] 2.1 Add a new enabled `*LabTest` using `ApplicationContextRunner` with a minimal local `@AutoConfiguration`
- [x] 2.2 Add labs for conditions:
  - `@ConditionalOnProperty` match/no-match
  - `@ConditionalOnClass` match/no-match (simulate missing class via `FilteredClassLoader`)
- [x] 2.3 Add labs for override strategies:
  - `@ConditionalOnMissingBean` (user bean prevents auto-config bean)
  - optional: demonstrate exclusion/disable via property/config where stable

## 3. Exercises (Optional but Recommended)
- [x] 3.1 Add `@Disabled` exercises to modify selector/registrar behavior and re-run tests
- [x] 3.2 Add `@Disabled` exercises to explore auto-config override and ambiguity resolution

## 4. Docs Linking
- [x] 4.1 Update `spring-core-beans/README.md` concept map to link new concepts to new labs
- [x] 4.2 Update `spring-core-beans/docs/02-bean-registration.md` and `spring-core-beans/docs/10-spring-boot-auto-configuration.md` to reference the new labs

## 5. Validation
- [x] 5.1 Run: `mvn -q -pl spring-core-beans test`
