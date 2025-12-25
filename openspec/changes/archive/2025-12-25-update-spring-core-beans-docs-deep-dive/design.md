# Design: `spring-core-beans` Deep-Dive Documentation

## Goals
- Turn the module docs into a **complete, learner-friendly deep dive** that builds a correct mental model of Spring Beans.
- Keep the guide **hands-on** by mapping each concept to an existing lab/exercise.
- Make the docs navigable:
  - `spring-core-beans/README.md` is a concise index (what to read, where to run, where the labs are)
  - `spring-core-beans/docs/*.md` holds the deep-dive chapters
- Stay **Spring Framework-first** (IoC container), while also explaining (at a practical level) how **Spring Boot auto-configuration** affects the final bean graph.

## Non-Goals
- Re-implement Spring reference docs inside this repository.
- Cover every advanced feature in exhaustive detail (e.g., AOT, custom scopes, full `BeanDefinition` API surface).

## Audience Assumptions
- Learner knows basic Java and has used Spring Boot at least once.
- Learner is new to Spring container internals and common bean pitfalls.

## Documentation Structure (Proposed Outline)
1. **Quick Start**
   - how to run: `mvn -pl spring-core-beans spring-boot:run`
   - how to run labs/exercises: `mvn -pl spring-core-beans test`
2. **Concept Map (What to Learn Here)**
   - A table mapping “Concept → Lab/Test → Code file → Takeaway”.
3. **Bean Mental Model**
   - BeanDefinition vs Bean instance
   - BeanFactory vs ApplicationContext (responsibility boundary)
   - “Container builds a dependency graph from definitions, then creates instances”
4. **Bean Registration Paths**
   - component scanning (`@Component`, `@Service`)
   - `@Bean` methods
   - `@Import` and what “configuration class processing” means
   - `ImportSelector` / `DeferredImportSelector` (high-level role)
   - `ImportBeanDefinitionRegistrar` (what it can do, and why it’s powerful)
   - Spring Boot auto-configuration entry points (how it imports configuration and registers beans)
   - naming basics (bean name, aliases) and why naming matters for debugging
5. **Dependency Injection Resolution**
   - why constructor injection is the default
   - ambiguity rules: type vs name vs `@Qualifier` vs `@Primary`
   - what to do when multiple implementations exist
6. **Scope Semantics**
   - singleton vs prototype: “singleton is one per container”, “prototype is one per request to container”
   - why “prototype injected into singleton” is confusing and how to solve it:
     - `ObjectProvider`
     - `@Lookup`
7. **Lifecycle Ordering**
   - initialization callbacks ordering (high-level, with the “why”)
   - destruction callbacks and what “prototype is not destroyed by container” means in practice
8. **Container Internals Entry Points**
   - BFPP: mutate definitions before instantiation
   - BPP: mutate instances around initialization
   - “What is safe to do” vs “What causes hard-to-debug behavior”
9. **`@Configuration` Enhancement**
   - `proxyBeanMethods=true` vs `false`
   - why calling one `@Bean` method from another behaves differently
   - how this relates to singleton semantics and performance trade-offs
10. **`FactoryBean`**
    - “bean name returns product, `&name` returns factory”
    - typical confusion points and debugging tips
11. **Circular Dependencies**
    - why constructor cycles fail fast
    - why setter cycles may work (early singleton exposure)
    - mitigation strategies and best practices
12. **Common Pitfalls**
    - checklist of mistakes learners commonly make and how to spot them
13. **Self-check Questions**
    - short questions per section to verify understanding
14. **Next Steps**
    - pointers to other modules in this workspace (AOP, Events, Tx, Profiles)
    - “how to keep digging” pointers: enabling Boot condition report/debugging for auto-config

## Content Principles
- Prefer **accurate mental models** over exhaustive API lists.
- Prefer **observable behaviors** (labs/tests) over abstract descriptions.
- Avoid “magic words”; explain the mechanism and the boundary of responsibility.
- Keep examples aligned with Spring Boot 3.x (Spring Framework 6.x) used in this workspace.
