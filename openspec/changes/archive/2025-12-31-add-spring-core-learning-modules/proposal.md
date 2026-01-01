# Change: Add Spring Core Learning Modules (Beans, AOP, Events)

## Why
The current workspace focuses on Spring Boot topics (startup/configuration, MVC, JPA, Actuator, testing). Beginners often struggle because Spring Boot examples implicitly rely on Spring Framework fundamentals (IoC container, bean lifecycle, proxies/AOP, and application events).

Adding a small set of Spring Core-focused modules creates a smoother learning path: learn the core container concepts first, then see how Spring Boot builds on top of them.

## What Changes
- Add new learning modules that teach Spring Framework fundamentals while still using the same Spring Boot multi-module conventions:
  - `spring-core-beans` (IoC/DI, bean scopes, lifecycle, qualifiers)
  - `spring-core-aop` (proxies, aspects, pointcuts, advice ordering, common pitfalls)
  - `spring-core-events` (publishing events, `@EventListener`, synchronous vs asynchronous basics)
- Keep each module runnable and self-contained (no shared `common` module).
- Update the root module catalog to include the new modules.

## Impact
- Affected specs:
  - `spring-core-beans-module`
  - `spring-core-aop-module`
  - `spring-core-events-module`
  - `learning-module-catalog`
- Affected code (apply stage):
  - Root build module list (`pom.xml`)
  - Root module catalog (`README.md`)
  - New module directories with code, tests, and docs:
    - `spring-core-beans/`
    - `spring-core-aop/`
    - `spring-core-events/`

