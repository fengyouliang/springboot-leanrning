# spring-core-beans 文档目录（Book Style）

本目录的目标是把 `spring-core-beans` 的知识点组织成“像书本一样可连续阅读”的结构：

- spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansBootstrapInternalsLabTest.javaspring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansBootstrapInternalsLabTest.java从目录开始spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansBootstrapInternalsLabTest.javaspring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansBootstrapInternalsLabTest.java：先知道有哪些 Part，每个 Part 学什么
- spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansBootstrapInternalsLabTest.javaspring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansBootstrapInternalsLabTest.java按主线顺读spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansBootstrapInternalsLabTest.javaspring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansBootstrapInternalsLabTest.java：章节之间有稳定承接（上一章｜目录｜下一章）
- spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansBootstrapInternalsLabTest.javaspring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansBootstrapInternalsLabTest.java每章统一契约spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansBootstrapInternalsLabTest.javaspring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansBootstrapInternalsLabTest.java：A–G（定位/结论/主线/源码/实验/坑点/小结预告）
- spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansBootstrapInternalsLabTest.javaspring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansBootstrapInternalsLabTest.java可复现spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansBootstrapInternalsLabTest.javaspring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansBootstrapInternalsLabTest.java：每个关键机制都能在本仓库的 Labs/Exercises 中验证

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
6. Appendix：常见坑与自测题（用于复盘与巩固）

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

### Appendix：复盘与自测

- [90. 常见坑清单（建议反复对照）](appendix/90-common-pitfalls.md)
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
