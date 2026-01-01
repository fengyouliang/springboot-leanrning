## 1. Deep Dive Track (Workspace-wide Conventions)
- [x] 1.1 Define a consistent experiment taxonomy: “Lab” (enabled) vs “Exercise” (`@Disabled`)
- [x] 1.2 Apply a consistent test naming convention across modules (`*LabTest`, `*ExerciseTest`)
- [x] 1.3 Ensure exercises never break default builds (`mvn -q test` stays green)
- [x] 1.4 Update each module README (Chinese) to include “Labs” and “Exercises” sections

## 2. Capstone Module: `springboot-business-case`
- [x] 2.1 Add new module `springboot-business-case` and wire it into the root `pom.xml`
- [x] 2.2 Implement a minimal end-to-end business flow (MVC + validation → service → JPA)
- [x] 2.3 Add labs demonstrating: validation boundary, transactional behavior, events, and AOP
- [x] 2.4 Add `@Disabled` exercises to extend the labs (propagation, transactional events, proxy pitfalls)
- [x] 2.5 Add module `README.md` (Chinese): run, test, labs, exercises, debugging tips
- [x] 2.6 Update root `README.md` catalog (Chinese) to include the capstone module

## 3. Upgrade Spring Core Modules (Deep Dive + Exercises)
- [x] 3.1 `spring-core-beans`: container internals labs + 15+ experiments total
- [x] 3.2 `spring-core-aop`: proxy internals labs + 15+ experiments total
- [x] 3.3 `spring-core-events`: async/transactional events labs + 15+ experiments total
- [x] 3.4 `spring-core-tx`: propagation/rollback internals labs + 15+ experiments total
- [x] 3.5 `spring-core-validation`: method validation internals labs + 15+ experiments total
- [x] 3.6 `spring-core-resources`: resource resolution pitfalls labs + 15+ experiments total
- [x] 3.7 `spring-core-profiles`: conditional evaluation labs + 15+ experiments total

## 4. Upgrade Spring Boot Modules (Deep Dive + Exercises)
- [x] 4.1 `springboot-basics`: environment/property ordering labs + 15+ experiments total
- [x] 4.2 `springboot-web-mvc`: MVC internals entry points labs + 15+ experiments total
- [x] 4.3 `springboot-data-jpa`: JPA mechanics labs + 15+ experiments total
- [x] 4.4 `springboot-actuator`: actuator discovery/customization labs + 15+ experiments total
- [x] 4.5 `springboot-testing`: test-slice patterns labs + 15+ experiments total

## 5. Validation
- [x] 5.1 Run all workspace tests: `mvn -q test`
- [x] 5.2 Spot-check module builds: `mvn -q -pl spring-core-beans test`, `mvn -q -pl springboot-business-case test`, etc.
- 5.3 Smoke-run a module (optional): `mvn -pl springboot-business-case spring-boot:run`
