## 1. spring-core-beans
- [x] 1.1 Add module `spring-core-beans` with a minimal `pom.xml` and Spring Boot plugin
- [x] 1.2 Implement examples for: component scanning, constructor injection, `@Qualifier`, bean scopes, and lifecycle callbacks
- [x] 1.3 Add at least one focused test that proves bean behavior (e.g., scope differences or lifecycle hooks)
- [x] 1.4 Add module `README.md` (goals, run steps, test steps, exercises, references)

## 2. spring-core-aop
- [x] 2.1 Add module `spring-core-aop` with `spring-boot-starter-aop`
- [x] 2.2 Implement an aspect that intercepts a service method and produces an observable outcome (e.g., timing/metrics log, call counter)
- [x] 2.3 Add a test proving that advice is applied (and document a common pitfall like self-invocation)
- [x] 2.4 Add module `README.md` (goals, run steps, test steps, exercises, references)

## 3. spring-core-events
- [x] 3.1 Add module `spring-core-events` with an example publisher + `@EventListener`
- [x] 3.2 Include a simple observable flow: publish event → listener reacts → record/output result
- [x] 3.3 Add a test proving listener invocation on the happy path
- [x] 3.4 Add module `README.md` (goals, run steps, test steps, exercises, references)

## 4. Workspace Integration
- [x] 4.1 Add new modules to the root `pom.xml` `<modules>` list
- [x] 4.2 Update root `README.md` module catalog table to include the new `spring-core-*` modules

## 5. Validation
- [x] 5.1 Run workspace tests: `mvn -q test`
- [x] 5.2 Run each new module test: `mvn -q -pl spring-core-beans test`, etc.
- [x] 5.3 Smoke-run at least one new module: `mvn -pl spring-core-aop spring-boot:run`
