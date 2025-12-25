## 1. Workspace Bootstrap
- [x] 1.1 Create a root Maven multi-module `pom.xml` (packaging `pom`) with a clear module list
- [x] 1.2 Add root `README.md` describing goals, prerequisites (JDK + Maven), and how to build/run modules

## 2. Module Template
- [x] 2.1 Define a minimal, repeatable module layout (src/main, src/test, resources)
- [x] 2.2 Ensure each module is runnable as a standalone Spring Boot application
- [x] 2.3 Ensure each module has at least one passing test that demonstrates the topic
- [x] 2.4 Add a per-module `README.md` template (learning goals, run steps, exercises, references)

## 3. Initial Learning Modules
- [x] 3.1 Add `boot-basics` (application startup, configuration properties, profiles)
- [x] 3.2 Add `boot-web-mvc` (REST controller, validation, error handling)
- [x] 3.3 Add `boot-data-jpa` (H2, entity, repository, basic CRUD)
- [x] 3.4 Add `boot-actuator` (Actuator endpoints + one custom health indicator)
- [x] 3.5 Add `boot-testing` (Spring Boot test basics: `@SpringBootTest`, `@WebMvcTest` or similar)

## 4. Validation
- [x] 4.1 Verify root build: `mvn -q test`
- [x] 4.2 Verify module build: `mvn -q -pl boot-web-mvc test`
- [x] 4.3 Verify at least one module runs: `mvn -pl boot-basics spring-boot:run`
- [x] 4.4 Add short troubleshooting notes in root `README.md` (JDK/Maven setup, common errors)

