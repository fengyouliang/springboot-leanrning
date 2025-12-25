## 1. Documentation Upgrade (`spring-core-beans`)
- [x] 1.1 Convert `spring-core-beans/README.md` into an index (Chinese): run/test + reading path + labs/exercises map
- [x] 1.2 Add deep-dive chapters under `spring-core-beans/docs/*.md` (Chinese) following the outline in `design.md`
- [x] 1.3 Add a “Concept → Lab/Test → Code file” mapping table to make the module navigable
- [x] 1.4 Add “Common Pitfalls” section (prototype-in-singleton, `@Configuration` proxying, `FactoryBean` confusion, circular deps, auto-config surprises)
- [x] 1.5 Add a “Self-check” section with short questions per topic (DI resolution, scope, lifecycle, BFPP/BPP, @Import/registrar, Boot auto-config, etc.)

## 2. Validation
- [x] 2.1 Validate docs remain accurate against existing labs: `mvn -q -pl spring-core-beans test`
- [x] 2.2 (Optional) Smoke-run: Verified via `mvn -q -pl spring-core-beans test` (runner output observed during test context startup)
