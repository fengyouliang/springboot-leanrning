## 1. Deep Dive Track (Workspace-wide Conventions)
- [ ] 1.1 Define a consistent experiment taxonomy: “Lab” (enabled) vs “Exercise” (`@Disabled`)
- [ ] 1.2 Apply a consistent test naming convention across modules (`*LabTest`, `*ExerciseTest`)
- [ ] 1.3 Ensure exercises never break default builds (`mvn -q test` stays green)
- [ ] 1.4 Update each module README (Chinese) to include “Labs” and “Exercises” sections

## 2. Capstone Module: `boot-business-case`
- [ ] 2.1 Add new module `boot-business-case` and wire it into the root `pom.xml`
- [ ] 2.2 Implement a minimal end-to-end business flow (MVC + validation → service → JPA)
- [ ] 2.3 Add labs demonstrating: validation boundary, transactional behavior, events, and AOP
- [ ] 2.4 Add `@Disabled` exercises to extend the labs (propagation, transactional events, proxy pitfalls)
- [ ] 2.5 Add module `README.md` (Chinese): run, test, labs, exercises, debugging tips
- [ ] 2.6 Update root `README.md` catalog (Chinese) to include the capstone module

## 3. Upgrade Spring Core Modules (Deep Dive + Exercises)
- [ ] 3.1 `spring-core-beans`: container internals labs + 15+ experiments total
- [ ] 3.2 `spring-core-aop`: proxy internals labs + 15+ experiments total
- [ ] 3.3 `spring-core-events`: async/transactional events labs + 15+ experiments total
- [ ] 3.4 `spring-core-tx`: propagation/rollback internals labs + 15+ experiments total
- [ ] 3.5 `spring-core-validation`: method validation internals labs + 15+ experiments total
- [ ] 3.6 `spring-core-resources`: resource resolution pitfalls labs + 15+ experiments total
- [ ] 3.7 `spring-core-profiles`: conditional evaluation labs + 15+ experiments total

## 4. Upgrade Spring Boot Modules (Deep Dive + Exercises)
- [ ] 4.1 `boot-basics`: environment/property ordering labs + 15+ experiments total
- [ ] 4.2 `boot-web-mvc`: MVC internals entry points labs + 15+ experiments total
- [ ] 4.3 `boot-data-jpa`: JPA mechanics labs + 15+ experiments total
- [ ] 4.4 `boot-actuator`: actuator discovery/customization labs + 15+ experiments total
- [ ] 4.5 `boot-testing`: test-slice patterns labs + 15+ experiments total

## 5. Validation
- [ ] 5.1 Run all workspace tests: `mvn -q test`
- [ ] 5.2 Spot-check module builds: `mvn -q -pl spring-core-beans test`, `mvn -q -pl boot-business-case test`, etc.
- [ ] 5.3 Smoke-run a module (optional): `mvn -pl boot-business-case spring-boot:run`

