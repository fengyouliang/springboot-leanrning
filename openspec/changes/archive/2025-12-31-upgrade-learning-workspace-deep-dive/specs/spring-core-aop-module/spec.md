## ADDED Requirements

### Requirement: Spring AOP Proxy Internals Deep Dive
The `spring-core-aop` module SHALL include deep dive Labs and `@Disabled` Exercises that teach how Spring AOP proxying works, including:
- JDK dynamic proxies vs CGLIB proxies and selection rules
- pointcut matching and advice ordering basics
- self-invocation pitfalls and mitigation options
- proxy limitations (final classes/methods) and observable outcomes

#### Scenario: Verify deep dive labs are runnable
- **WHEN** a learner runs `mvn -q -pl spring-core-aop test`
- **THEN** the enabled lab tests pass without requiring exercises to be enabled

