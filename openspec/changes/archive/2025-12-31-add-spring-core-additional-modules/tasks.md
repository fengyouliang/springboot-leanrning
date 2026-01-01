## 1. spring-core-validation
- [x] 1.1 Add module `spring-core-validation` with dependencies for Bean Validation
- [x] 1.2 Implement a small validation example with an observable outcome (violations / exceptions)
- [x] 1.3 Add at least one focused test demonstrating validation behavior
- [x] 1.4 Add module `README.md` (goals, run steps, test steps, exercises, references)

## 2. spring-core-resources
- [x] 2.1 Add module `spring-core-resources` (no web) with example classpath resources
- [x] 2.2 Implement a resource reader (classpath + pattern scan) with observable output
- [x] 2.3 Add at least one focused test verifying resource content is read
- [x] 2.4 Add module `README.md` (goals, run steps, test steps, exercises, references)

## 3. spring-core-tx
- [x] 3.1 Add module `spring-core-tx` using `spring-boot-starter-jdbc` + H2
- [x] 3.2 Add schema initialization and a transactional service method that rolls back on runtime exception
- [x] 3.3 Add tests verifying commit vs rollback outcomes
- [x] 3.4 Add module `README.md` (goals, run steps, test steps, exercises, references)

## 4. spring-core-profiles
- [x] 4.1 Add module `spring-core-profiles` (no web)
- [x] 4.2 Implement `@Profile` + conditional bean selection scenarios with a visible outcome
- [x] 4.3 Add tests verifying bean selection across scenarios (default, dev profile, property toggle)
- [x] 4.4 Add module `README.md` (goals, run steps, test steps, exercises, references)

## 5. Workspace Integration
- [x] 5.1 Add new modules to root `pom.xml` `<modules>` list
- [x] 5.2 Update root `README.md` module catalog table (flat) with the new modules

## 6. Validation
- [x] 6.1 Run workspace tests: `mvn -q test`
- [x] 6.2 Run each new module test (one-by-one)
- [x] 6.3 Smoke-run at least one new module: `mvn -pl spring-core-tx spring-boot:run`
