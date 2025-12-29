## 1. Spec & Docs

- [x] 1.1 Update spec delta for beans module (injection + proxying bridge)
- [x] 1.2 Add docs chapters (one chapter per new Lab)
- [x] 1.3 Update `spring-core-beans/README.md` reading order + concept map

## 2. Labs (enabled by default)

- [x] 2.1 Add Injection Phase Lab (field vs constructor injection; `postProcessProperties` timing + contrast with `@Autowired`)
- [x] 2.2 Add Proxying Phase Lab (BPP returns proxy after initialization + self-invocation pitfall)

## 3. Exercises (disabled by default)

- [x] 3.1 Add an exercise: implement a tiny “proxying” BPP with assertions (optional)
- [x] 3.2 Add an exercise: extend injection lab to cover optional/required semantics (optional)

## 4. Verification

- [x] 4.1 Run `mvn -q -pl spring-core-beans test`
- [ ] 4.2 Run `mvn -q test` (note: tests that start embedded web servers require an environment that allows binding server sockets)
