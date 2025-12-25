# Change: Update `spring-core-beans` Documentation to a Deep-Dive Bean Guide

## Why
The current `spring-core-beans/README.md` is runnable and correct, but it is still too “overview-level” for learners who want to **build a solid mental model** of Spring Beans.

In particular:
- The module already contains valuable container-internals labs (`SpringCoreBeansContainerLabTest`), but the README does not explain *why* those experiments matter or *how* they connect to Spring’s lifecycle.
- Key “concept boundaries” (BeanDefinition vs instance, BFPP vs BPP, `@Configuration` enhancement, `FactoryBean`, circular dependency behavior) are easy to misunderstand without an explicit conceptual map and pitfalls section.

This change upgrades the module documentation so that a learner can read the guide end-to-end and gain a thorough understanding of Spring beans, then verify the understanding through the existing labs and exercises.

## What Changes
- Restructure documentation into:
  - `spring-core-beans/README.md` as a **navigation index** (Chinese)
  - `spring-core-beans/docs/*.md` as **deep-dive chapters** (Chinese)
- Write a structured, deep-dive guide covering:
  - the bean mental model (definition vs instance, container responsibility boundaries)
  - bean registration “entry points” beyond the basics:
    - `@Configuration`/`@Bean`
    - `@ComponentScan`
    - `@Import` and configuration class processing
    - `ImportSelector` and `ImportBeanDefinitionRegistrar` (what they do, when they run, why they exist)
    - how Spring Boot auto-configuration contributes bean definitions and affects the final context
  - dependency injection resolution (type, name, `@Qualifier`, `@Primary`)
  - scope semantics and prototype-in-singleton pitfalls (`ObjectProvider`, `@Lookup`)
  - lifecycle ordering and callbacks (initialization vs destruction)
  - container internals entry points (BFPP/BPP) and what they can/cannot change
  - `@Configuration(proxyBeanMethods=...)` enhancement and `@Bean` method semantics
  - `FactoryBean`: product vs factory and the `"&"` prefix
  - circular dependencies: why constructors fail and setters may succeed
- Add an explicit “Concept → Where to see it in this module” map linking each topic to:
  - code files under `spring-core-beans/src/main/java/...`
  - lab tests under `spring-core-beans/src/test/java/...`
- Add a “Common Pitfalls” + “Self-check” section so learners can verify mastery without leaving the repo.

## Impact
- Affected specs:
  - `spring-core-beans-module`
- Affected code/docs (apply stage):
  - `spring-core-beans/README.md`
  - `spring-core-beans/docs/*.md` deep-dive chapters

## Out of Scope
- Adding new runtime features or changing existing module behavior
- Expanding container-internals labs beyond what already exists (this change is documentation-first)
- Cross-module topics (e.g., transactions) except brief “where to learn next” pointers
