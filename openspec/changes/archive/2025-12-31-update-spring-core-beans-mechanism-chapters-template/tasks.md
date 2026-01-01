## 1. Docs updates (mechanism deep-dive chapters only)

- [x] 1.1 Apply the heavy template block to container bootstrap & post-processor internals chapters (`docs/12`–`docs/16`)
- [x] 1.2 Apply the heavy template block to lifecycle semantics chapters (`docs/17`–`docs/20`)
- [x] 1.3 Apply the heavy template block to context visibility & naming chapters (`docs/21`–`docs/22`)
- [x] 1.4 Apply the heavy template block to FactoryBean / overriding / programmatic processor chapters (`docs/23`–`docs/25`, `docs/29`)
- [x] 1.5 Apply the heavy template block to lifecycle hook & scope chapters (`docs/26`–`docs/28`)
- [x] 1.6 Apply the heavy template block to injection/proxying/annotation resolution chapters (`docs/30`–`docs/34`)

## 2. Consistency checks

- [x] 2.1 Ensure every `docs/12-34` chapter contains the three headings:
  - `## 源码锚点（建议从这里下断点）`
  - `## 断点闭环（用本仓库 Lab/Test 跑一遍）`
  - `## 排障分流：这是定义层问题还是实例层问题？`
- [x] 2.2 Ensure each chapter links to at least one runnable `*LabTest` path (or an explicit existing test method)
- [x] 2.3 Ensure each chapter includes at least 3 “class#method” anchors (method-level preferred)

## 3. Validation

- [x] 3.1 Run module tests to ensure nothing regressed: `mvn -q -pl spring-core-beans test`
- [x] 3.2 Re-run proposal validation: `openspec validate update-spring-core-beans-mechanism-chapters-template --strict`
