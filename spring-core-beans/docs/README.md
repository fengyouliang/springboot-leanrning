# spring-core-beans 文档目录（Book Style）

本目录的目标是把 `spring-core-beans` 的知识点组织成“像书本一样可连续阅读”的结构：

- 从目录开始：先知道有哪些 Part，每个 Part 学什么
- 按主线顺读：章节之间有稳定承接（上一章｜目录｜下一章）
- 按问题跳读：遇到具体异常/现象，能在 1–2 次跳转内定位到章节与 Lab
- 每章统一契约：A–G（定位/结论/主线/源码/实验/坑点/小结预告）
- 可复现：每个关键机制都能在本仓库的 Labs/Exercises 中验证

> 参考风格（结构与叙事方式）：Spring Framework / Spring Boot 官方 Reference Docs。  
> - Spring Framework Reference: https://docs.spring.io/spring-framework/reference/index.html  
> - Spring Boot Reference: https://docs.spring.io/spring-boot/documentation.html

---

## 如何阅读（推荐主线）

如果你只想“像读书一样一路读下去”，按下面顺序即可：

1. Part 00：学习方法与深挖路线（可选，但强烈推荐）
2. Part 01：IoC Container 主线（定义 → 注册 → 注入 → scope → 生命周期 → 扩展点 → 循环依赖）
3. Part 02：Spring Boot 自动装配与可观察性（把“为什么有这个 bean/为什么没生效”讲清楚）
4. Part 03：容器内部机制与扩展点（bootstrap/排序/短路/early reference）
5. Part 04：装配语义与边界（lazy/dependsOn/resolvable/层级/命名/FactoryBean/覆盖/手工注册/回调钩子/注入阶段/代理/值解析/merged definition）
6. Part 05：AOT/真实世界补齐（RuntimeHints/XML/容器外对象/SpEL/自定义 Qualifier）
7. Appendix：常见坑与自测题（用于复盘与巩固）

---

## 快速定位（按问题找章节）

如果你是“遇到问题再来查”，建议按下面的症状快速跳转（每条都尽量同时给到章节与可跑 Lab）：

- 注入失败（NoSuch/NoUnique/UnsatisfiedDependency）→ [03](part-01-ioc-container/03-dependency-injection-resolution.md) / [33](part-04-wiring-and-boundaries/33-autowire-candidate-selection-primary-priority-order.md) / [11](part-02-boot-autoconfig/11-debugging-and-observability.md)
  - Lab：`SpringCoreBeansInjectionAmbiguityLabTest` / `SpringCoreBeansAutowireCandidateSelectionLabTest` / `SpringCoreBeansExceptionNavigationLabTest`
- prototype 注入 singleton 后“像单例” → [04](part-01-ioc-container/04-scope-and-prototype.md)
  - Lab：`SpringCoreBeansLabTest`（prototype 用例）/ Exercises（改造题）
- `@Value("${missing}")` 没失败，值变成 `"${...}"` → [34](part-04-wiring-and-boundaries/34-value-placeholder-resolution-strict-vs-non-strict.md)
  - Lab：`SpringCoreBeansValuePlaceholderResolutionLabTest`
- 代理导致行为“不符合直觉”（最终对象不是原始实例/self-invocation）→ [31](part-04-wiring-and-boundaries/31-proxying-phase-bpp-wraps-bean.md)
  - Lab：`SpringCoreBeansProxyingPhaseLabTest`
- 循环依赖：constructor 无解、setter 有时能救 → [09](part-01-ioc-container/09-circular-dependencies.md) / [16](part-03-container-internals/16-early-reference-and-circular.md)
  - Lab：`SpringCoreBeansContainerLabTest` / `SpringCoreBeansEarlyReferenceLabTest`
- 字符串为何能注入为 int/自定义类型（类型转换）→ [36](part-04-wiring-and-boundaries/36-type-conversion-and-beanwrapper.md)
  - Lab：`SpringCoreBeansTypeConversionLabTest`
- 泛型匹配按 `Handler<String>` 找不到（代理丢失类型信息）→ [37](part-04-wiring-and-boundaries/37-generic-type-matching-pitfalls.md)
  - Lab：`SpringCoreBeansGenericTypeMatchingPitfallsLabTest`
- `BeanDefinitionStoreException`（例如 invalid XML）→ [42](part-05-aot-and-real-world/42-xml-bean-definition-reader.md) / [11](part-02-boot-autoconfig/11-debugging-and-observability.md)
  - Lab：`SpringCoreBeansXmlBeanDefinitionReaderLabTest` / `SpringCoreBeansExceptionNavigationLabTest`
- `@Value("#{...}")`（SpEL）注入不符合预期 → [44](part-05-aot-and-real-world/44-spel-and-value-expression.md) / [36](part-04-wiring-and-boundaries/36-type-conversion-and-beanwrapper.md)
  - Lab：`SpringCoreBeansSpelValueLabTest`

更完整的跳读地图见： [92. 知识点地图](appendix/92-knowledge-map.md)

---

## 章节 ↔ Lab/Test 对照表（精选）

> 目的：让你每章都能“立刻跑起来”，把概念落到断点与断言。

| 章节 | 你要看清的关键点 | 对应 Lab/Test（可精确到方法跑） |
| --- | --- | --- |
| [01](part-01-ioc-container/01-bean-mental-model.md) | 定义层 vs 实例层 vs 最终暴露对象 | `SpringCoreBeansContainerLabTest` / `SpringCoreBeansProxyingPhaseLabTest` |
| [02](part-01-ioc-container/02-bean-registration.md) | scan/@Bean/@Import 注册入口 | `SpringCoreBeansComponentScanLabTest` / `SpringCoreBeansImportLabTest` |
| [03](part-01-ioc-container/03-dependency-injection-resolution.md) | 候选收集与收敛（Qualifier/Primary/名称回退） | `SpringCoreBeansInjectionAmbiguityLabTest` / `SpringCoreBeansAutowireCandidateSelectionLabTest` |
| [09](part-01-ioc-container/09-circular-dependencies.md) | 循环依赖现象分类（constructor vs setter） | `SpringCoreBeansContainerLabTest` / `SpringCoreBeansEarlyReferenceLabTest` |
| [14](part-03-container-internals/14-post-processor-ordering.md) | PriorityOrdered/Ordered 分段与排序 | `SpringCoreBeansPostProcessorOrderingLabTest` |
| [31](part-04-wiring-and-boundaries/31-proxying-phase-bpp-wraps-bean.md) | BPP 替换/包装为代理的阶段 | `SpringCoreBeansProxyingPhaseLabTest` |
| [34](part-04-wiring-and-boundaries/34-value-placeholder-resolution-strict-vs-non-strict.md) | non-strict vs strict 占位符解析 | `SpringCoreBeansValuePlaceholderResolutionLabTest` |
| [36](part-04-wiring-and-boundaries/36-type-conversion-and-beanwrapper.md) | BeanWrapper/ConversionService 类型转换 | `SpringCoreBeansTypeConversionLabTest` |
| [37](part-04-wiring-and-boundaries/37-generic-type-matching-pitfalls.md) | ResolvableType 泛型匹配边界 | `SpringCoreBeansGenericTypeMatchingPitfallsLabTest` |
| [41](part-05-aot-and-real-world/41-runtimehints-basics.md) | AOT/Native 的“构建期契约”如何表达与验证 | `SpringCoreBeansAotRuntimeHintsLabTest` |
| [42](part-05-aot-and-real-world/42-xml-bean-definition-reader.md) | XML → BeanDefinitionReader：定义层解析与错误分型 | `SpringCoreBeansXmlBeanDefinitionReaderLabTest` |

---

## Part 目录（TOC）

### Part 00：导读与深挖路线

- [00. 深挖指南：把“Bean 三层模型”落到源码与断点](part-00-guide/00-deep-dive-guide.md)

### Part 01：IoC Container 主线（从概念到可定位问题）

- [01. Bean 心智模型：BeanDefinition vs Bean 实例](part-01-ioc-container/01-bean-mental-model.md)
- [02. Bean 注册入口：扫描、@Bean、@Import、registrar](part-01-ioc-container/02-bean-registration.md)
- [03. 依赖注入解析：类型/名称/@Qualifier/@Primary](part-01-ioc-container/03-dependency-injection-resolution.md)
- [04. Scope 与 prototype 注入陷阱（ObjectProvider / @Lookup / scoped proxy）](part-01-ioc-container/04-scope-and-prototype.md)
- [05. 生命周期：初始化、销毁与回调（@PostConstruct/@PreDestroy 等）](part-01-ioc-container/05-lifecycle-and-callbacks.md)
- [06. 容器扩展点：BFPP vs BPP（以及它们能/不能做什么）](part-01-ioc-container/06-post-processors.md)
- [07. @Configuration 增强：proxyBeanMethods 与 @Bean 语义](part-01-ioc-container/07-configuration-enhancement.md)
- [08. FactoryBean：product vs factory（& 前缀）](part-01-ioc-container/08-factorybean.md)
- [09. 循环依赖概览：三级缓存与现象分类](part-01-ioc-container/09-circular-dependencies.md)

### Part 02：Spring Boot 自动装配与可观察性

- [10. Spring Boot 自动装配如何影响 Bean（Auto-configuration）](part-02-boot-autoconfig/10-spring-boot-auto-configuration.md)
- [11. 调试与可观察性：从异常到断点入口](part-02-boot-autoconfig/11-debugging-and-observability.md)

### Part 03：Container Internals（把“魔法”讲成可复述算法）

- [12. 容器启动与基础设施处理器：为什么注解能工作](part-03-container-internals/12-container-bootstrap-and-infrastructure.md)
- [13. BeanDefinitionRegistryPostProcessor：定义注册再推进](part-03-container-internals/13-bdrpp-definition-registration.md)
- [14. 顺序（Ordering）：PriorityOrdered / Ordered / 无序](part-03-container-internals/14-post-processor-ordering.md)
- [15. 实例化前短路：还没 new 就拿到对象了？](part-03-container-internals/15-pre-instantiation-short-circuit.md)
- [16. early reference 与循环依赖：getEarlyBeanReference](part-03-container-internals/16-early-reference-and-circular.md)
- [17. 生命周期回调顺序：Aware/@PostConstruct/afterPropertiesSet/initMethod](part-03-container-internals/17-lifecycle-callback-order.md)

### Part 04：装配语义与边界（把规则讲成可验证的行为）

- [18. @Lazy 的真实语义：延迟的是谁、延迟到哪一步](part-04-wiring-and-boundaries/18-lazy-semantics.md)
- [19. dependsOn：强制初始化顺序与依赖关系记录](part-04-wiring-and-boundaries/19-depends-on.md)
- [20. registerResolvableDependency：能注入但它不是 Bean](part-04-wiring-and-boundaries/20-resolvable-dependency.md)
- [21. 父子 ApplicationContext：可见性与覆盖边界](part-04-wiring-and-boundaries/21-context-hierarchy.md)
- [22. beanName 与 alias：命名规则与别名本质](part-04-wiring-and-boundaries/22-bean-names-and-aliases.md)
- [23. FactoryBean 深挖：getObjectType/isSingleton 与缓存](part-04-wiring-and-boundaries/23-factorybean-deep-dive.md)
- [24. BeanDefinition 覆盖：同名定义的冲突策略](part-04-wiring-and-boundaries/24-bean-definition-overriding.md)
- [25. 手工添加 BeanPostProcessor：顺序与 Ordered 的陷阱](part-04-wiring-and-boundaries/25-programmatic-bpp-registration.md)
- [26. SmartInitializingSingleton：容器就绪后回调](part-04-wiring-and-boundaries/26-smart-initializing-singleton.md)
- [27. SmartLifecycle：phase 与 start/stop 顺序](part-04-wiring-and-boundaries/27-smart-lifecycle-phase.md)
- [28. 自定义 scope 与 scoped proxy：线程 scope 复现](part-04-wiring-and-boundaries/28-custom-scope-and-scoped-proxy.md)
- [29. FactoryBean 边界坑：泛型/代理/对象类型推断](part-04-wiring-and-boundaries/29-factorybean-edge-cases.md)
- [30. 注入发生在什么时候：field vs constructor](part-04-wiring-and-boundaries/30-injection-phase-field-vs-constructor.md)
- [31. 代理产生在哪个阶段：BPP 如何把 Bean 换成 Proxy](part-04-wiring-and-boundaries/31-proxying-phase-bpp-wraps-bean.md)
- [32. @Resource 的 name-first：CommonAnnotationBeanPostProcessor](part-04-wiring-and-boundaries/32-resource-injection-name-first.md)
- [33. 候选选择与优先级：@Primary/@Priority/@Order 的边界](part-04-wiring-and-boundaries/33-autowire-candidate-selection-primary-priority-order.md)
- [34. @Value 占位符解析：strict vs non-strict](part-04-wiring-and-boundaries/34-value-placeholder-resolution-strict-vs-non-strict.md)
- [35. MergedBeanDefinition：合并后的 RootBeanDefinition](part-04-wiring-and-boundaries/35-merged-bean-definition.md)
- [36. 类型转换：BeanWrapper / ConversionService / PropertyEditor 的边界](part-04-wiring-and-boundaries/36-type-conversion-and-beanwrapper.md)
- [37. 泛型匹配与注入坑：ResolvableType 与代理导致的类型信息丢失](part-04-wiring-and-boundaries/37-generic-type-matching-pitfalls.md)

### Part 05：AOT / 真实世界补齐（把“项目里真会遇到的坑”补成可复现实验）

- [40. AOT / Native 总览：为什么“JVM 能跑”不等于“Native 能跑”](part-05-aot-and-real-world/40-aot-and-native-overview.md)
- [41. RuntimeHints 入门：把构建期契约跑通](part-05-aot-and-real-world/41-runtimehints-basics.md)
- [42. XML → BeanDefinitionReader：定义层解析与错误分型](part-05-aot-and-real-world/42-xml-bean-definition-reader.md)
- [43. 容器外对象注入：AutowireCapableBeanFactory](part-05-aot-and-real-world/43-autowirecapablebeanfactory-external-objects.md)
- [44. SpEL 与 `@Value("#{...}")`：表达式解析链路](part-05-aot-and-real-world/44-spel-and-value-expression.md)
- [45. 自定义 Qualifier：meta-annotation 与候选收敛](part-05-aot-and-real-world/45-custom-qualifier-meta-annotation.md)

### Appendix：复盘与自测

- [90. 常见坑清单（建议反复对照）](appendix/90-common-pitfalls.md)
- [91. 术语表（Glossary）](appendix/91-glossary.md)
- [92. 知识点地图（Concept → Chapter → Lab）](appendix/92-knowledge-map.md)
- [93. 面试复述模板（决策树 → Lab → 断点入口）](appendix/93-interview-playbook.md)
- [94. 生产排障清单（异常分型 → 入口 → 观察点 → 修复策略）](appendix/94-production-troubleshooting-checklist.md)
- [99. 自测题（Self Check）](appendix/99-self-check.md)

---

## 章节映射表（旧 → 新）

> 用于追溯与检索：如果你在历史笔记/搜索结果里看到旧路径，可在这里找到对应的新路径。

| 旧路径（迁移前） | 新路径（迁移后） |
| --- | --- |
| `docs/00-deep-dive-guide.md` | `docs/part-00-guide/00-deep-dive-guide.md` |
| `docs/01-bean-mental-model.md` | `docs/part-01-ioc-container/01-bean-mental-model.md` |
| `docs/02-bean-registration.md` | `docs/part-01-ioc-container/02-bean-registration.md` |
| `docs/03-dependency-injection-resolution.md` | `docs/part-01-ioc-container/03-dependency-injection-resolution.md` |
| `docs/04-scope-and-prototype.md` | `docs/part-01-ioc-container/04-scope-and-prototype.md` |
| `docs/05-lifecycle-and-callbacks.md` | `docs/part-01-ioc-container/05-lifecycle-and-callbacks.md` |
| `docs/06-post-processors.md` | `docs/part-01-ioc-container/06-post-processors.md` |
| `docs/07-configuration-enhancement.md` | `docs/part-01-ioc-container/07-configuration-enhancement.md` |
| `docs/08-factorybean.md` | `docs/part-01-ioc-container/08-factorybean.md` |
| `docs/09-circular-dependencies.md` | `docs/part-01-ioc-container/09-circular-dependencies.md` |
| `docs/10-spring-boot-auto-configuration.md` | `docs/part-02-boot-autoconfig/10-spring-boot-auto-configuration.md` |
| `docs/11-debugging-and-observability.md` | `docs/part-02-boot-autoconfig/11-debugging-and-observability.md` |
| `docs/12-container-bootstrap-and-infrastructure.md` | `docs/part-03-container-internals/12-container-bootstrap-and-infrastructure.md` |
| `docs/13-bdrpp-definition-registration.md` | `docs/part-03-container-internals/13-bdrpp-definition-registration.md` |
| `docs/14-post-processor-ordering.md` | `docs/part-03-container-internals/14-post-processor-ordering.md` |
| `docs/15-pre-instantiation-short-circuit.md` | `docs/part-03-container-internals/15-pre-instantiation-short-circuit.md` |
| `docs/16-early-reference-and-circular.md` | `docs/part-03-container-internals/16-early-reference-and-circular.md` |
| `docs/17-lifecycle-callback-order.md` | `docs/part-03-container-internals/17-lifecycle-callback-order.md` |
| `docs/18-lazy-semantics.md` | `docs/part-04-wiring-and-boundaries/18-lazy-semantics.md` |
| `docs/19-depends-on.md` | `docs/part-04-wiring-and-boundaries/19-depends-on.md` |
| `docs/20-resolvable-dependency.md` | `docs/part-04-wiring-and-boundaries/20-resolvable-dependency.md` |
| `docs/21-context-hierarchy.md` | `docs/part-04-wiring-and-boundaries/21-context-hierarchy.md` |
| `docs/22-bean-names-and-aliases.md` | `docs/part-04-wiring-and-boundaries/22-bean-names-and-aliases.md` |
| `docs/23-factorybean-deep-dive.md` | `docs/part-04-wiring-and-boundaries/23-factorybean-deep-dive.md` |
| `docs/24-bean-definition-overriding.md` | `docs/part-04-wiring-and-boundaries/24-bean-definition-overriding.md` |
| `docs/25-programmatic-bpp-registration.md` | `docs/part-04-wiring-and-boundaries/25-programmatic-bpp-registration.md` |
| `docs/26-smart-initializing-singleton.md` | `docs/part-04-wiring-and-boundaries/26-smart-initializing-singleton.md` |
| `docs/27-smart-lifecycle-phase.md` | `docs/part-04-wiring-and-boundaries/27-smart-lifecycle-phase.md` |
| `docs/28-custom-scope-and-scoped-proxy.md` | `docs/part-04-wiring-and-boundaries/28-custom-scope-and-scoped-proxy.md` |
| `docs/29-factorybean-edge-cases.md` | `docs/part-04-wiring-and-boundaries/29-factorybean-edge-cases.md` |
| `docs/30-injection-phase-field-vs-constructor.md` | `docs/part-04-wiring-and-boundaries/30-injection-phase-field-vs-constructor.md` |
| `docs/31-proxying-phase-bpp-wraps-bean.md` | `docs/part-04-wiring-and-boundaries/31-proxying-phase-bpp-wraps-bean.md` |
| `docs/32-resource-injection-name-first.md` | `docs/part-04-wiring-and-boundaries/32-resource-injection-name-first.md` |
| `docs/33-autowire-candidate-selection-primary-priority-order.md` | `docs/part-04-wiring-and-boundaries/33-autowire-candidate-selection-primary-priority-order.md` |
| `docs/34-value-placeholder-resolution-strict-vs-non-strict.md` | `docs/part-04-wiring-and-boundaries/34-value-placeholder-resolution-strict-vs-non-strict.md` |
| `docs/35-merged-bean-definition.md` | `docs/part-04-wiring-and-boundaries/35-merged-bean-definition.md` |
| `docs/90-common-pitfalls.md` | `docs/appendix/90-common-pitfalls.md` |
| `docs/99-self-check.md` | `docs/appendix/99-self-check.md` |
