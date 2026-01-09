# spring-core-beans 文档目录（Book Style）

本目录的目标是把 `spring-core-beans` 的知识点组织成“像书本一样可连续阅读”的结构：

- 从目录开始：先知道有哪些 Part，每个 Part 学什么
- 按主线顺读：章节之间有稳定承接（上一章｜目录｜下一章）
- 按问题跳读：遇到具体异常/现象，能在 1–2 次跳转内定位到章节与 Lab
- 章节结构：现有章节多采用 A–G（定位/结论/主线/源码/实验/坑点/小结预告），作为阅读辅助（后续不再作为写作规范/闸门）
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
6. Part 05：AOT/真实世界补齐（RuntimeHints/XML/容器外对象/SpEL/自定义 Qualifier/XML namespace 扩展/其它 Reader/方法注入/内置 FactoryBean/值解析）
7. Appendix：常见坑与自测题（用于复盘与巩固）

---

## 快速定位（按问题找章节）

如果你是“遇到问题再来查”，建议按下面的症状快速跳转（每条都尽量同时给到章节与可跑 Lab）：

- 注入失败（NoSuch/NoUnique/UnsatisfiedDependency）→ [03](part-01-ioc-container/03-dependency-injection-resolution.md) / [33](part-04-wiring-and-boundaries/33-autowire-candidate-selection-primary-priority-order.md) / [11](part-02-boot-autoconfig/11-debugging-and-observability.md)
  - Lab：`SpringCoreBeansInjectionAmbiguityLabTest` / `SpringCoreBeansAutowireCandidateSelectionLabTest` / `SpringCoreBeansExceptionNavigationLabTest`
  - 现象补充：没写 `@Qualifier/@Primary` 却没报歧义（by-name fallback：依赖名匹配 beanName）→ 见 33 章与 `SpringCoreBeansAutowireCandidateSelectionLabTest`（byNameFallback 用例）
- prototype 注入 singleton 后“像单例” → [04](part-01-ioc-container/04-scope-and-prototype.md)
  - Lab：`SpringCoreBeansLabTest`（prototype 用例）/ Exercises（改造题）
- `@Value("${missing}")` 没失败，值变成 `"${...}"` → [34](part-04-wiring-and-boundaries/34-value-placeholder-resolution-strict-vs-non-strict.md)
  - Lab：`SpringCoreBeansValuePlaceholderResolutionLabTest`
- 配置值“不生效/被覆盖/优先级不符合直觉”（Environment/PropertySource）→ [38](part-04-wiring-and-boundaries/38-environment-and-propertysource.md)
  - Lab：`SpringCoreBeansEnvironmentPropertySourceLabTest`
- 想按 API 名称直接定位到章节与 Lab（spring-beans Public API 索引）→ [95](appendix/95-spring-beans-public-api-index.md)
  - Gap 清单：`96`（用于按包/机制域分批深化）
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
- 自定义 XML namespace / `<tx:...>` 这类“自定义元素”怎么注册 BeanDefinition → [46](part-05-aot-and-real-world/46-xml-namespace-extension.md) / [42](part-05-aot-and-real-world/42-xml-bean-definition-reader.md)
  - Lab：`SpringCoreBeansXmlNamespaceExtensionLabTest`
- `@Value("#{...}")`（SpEL）注入不符合预期 → [44](part-05-aot-and-real-world/44-spel-and-value-expression.md) / [36](part-04-wiring-and-boundaries/36-type-conversion-and-beanwrapper.md)
  - Lab：`SpringCoreBeansSpelValueLabTest`
- “注解为什么不生效/为什么 plain BeanFactory 看起来缺能力”（BeanFactory API 边界）→ [39](part-04-wiring-and-boundaries/39-beanfactory-api-deep-dive.md) / [12](part-03-container-internals/12-container-bootstrap-and-infrastructure.md)
  - Lab：`SpringCoreBeansBeanFactoryApiLabTest`
- product vs factory（为什么 `getBean("x")` 不是你以为的那个对象？）→ [49](part-05-aot-and-real-world/49-built-in-factorybeans-gallery.md) / [08](part-01-ioc-container/08-factorybean.md)
  - Lab：`SpringCoreBeansBuiltInFactoryBeansLabTest`
- String/引用/集合到底在哪一步“变成对象”（值解析与类型转换想下断点）→ [50](part-05-aot-and-real-world/50-property-editor-and-value-resolution.md) / [36](part-04-wiring-and-boundaries/36-type-conversion-and-beanwrapper.md)
  - Lab：`SpringCoreBeansPropertyEditorLabTest` / `SpringCoreBeansBeanDefinitionValueResolutionLabTest`

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
| [38](part-04-wiring-and-boundaries/38-environment-and-propertysource.md) | Environment/PropertySource：优先级与 @PropertySource 进入链路 | `SpringCoreBeansEnvironmentPropertySourceLabTest` |
| [39](part-04-wiring-and-boundaries/39-beanfactory-api-deep-dive.md) | BeanFactory API：接口族谱与手动 bootstrap 边界 | `SpringCoreBeansBeanFactoryApiLabTest` |
| [41](part-05-aot-and-real-world/41-runtimehints-basics.md) | AOT/Native 的“构建期契约”如何表达与验证 | `SpringCoreBeansAotRuntimeHintsLabTest` |
| [42](part-05-aot-and-real-world/42-xml-bean-definition-reader.md) | XML → BeanDefinitionReader：定义层解析与错误分型 | `SpringCoreBeansXmlBeanDefinitionReaderLabTest` |
| [46](part-05-aot-and-real-world/46-xml-namespace-extension.md) | XML 自定义元素如何注册 BeanDefinition（namespace 扩展） | `SpringCoreBeansXmlNamespaceExtensionLabTest` |
| [47](part-05-aot-and-real-world/47-beandefinitionreader-other-inputs-properties-groovy.md) | BeanDefinitionReader 的其它输入源（Properties/Groovy） | `SpringCoreBeansPropertiesBeanDefinitionReaderLabTest` / `SpringCoreBeansGroovyBeanDefinitionReaderLabTest` |
| [48](part-05-aot-and-real-world/48-method-injection-replaced-method.md) | 方法注入：replaced-method 的实例化策略分支 | `SpringCoreBeansReplacedMethodLabTest` |
| [49](part-05-aot-and-real-world/49-built-in-factorybeans-gallery.md) | 内置 FactoryBean：product/factory 与 & 前缀 | `SpringCoreBeansBuiltInFactoryBeansLabTest` |
| [50](part-05-aot-and-real-world/50-property-editor-and-value-resolution.md) | PropertyEditor 与值解析主线（BeanDefinitionValueResolver） | `SpringCoreBeansPropertyEditorLabTest` / `SpringCoreBeansBeanDefinitionValueResolutionLabTest` |

### Exercise ↔ Solution（练习与答案）对照表

> 设计原则（保证教学闭环 + 不破坏回归）：
> - Exercise：默认 `@Disabled`（不参与回归），读者自行移除 `@Disabled` 完成练习
> - Solution：默认参与回归（持续可验证），提供参考实现与断言闭环

| Part | Exercise（默认跳过） | Solution（默认运行） | 关联章节（建议从 docs 读起） |
| --- | --- | --- | --- |
| Part 00 | `src/test/java/.../part00_guide/SpringCoreBeansExerciseTest.java` | `src/test/java/.../part00_guide/SpringCoreBeansExerciseSolutionTest.java` | [00](part-00-guide/00-deep-dive-guide.md) / [03](part-01-ioc-container/03-dependency-injection-resolution.md) / [04](part-01-ioc-container/04-scope-and-prototype.md) |
| Part 01 | `src/test/java/.../part01_ioc_container/SpringCoreBeansImportExerciseTest.java` | `src/test/java/.../part01_ioc_container/SpringCoreBeansImportExerciseSolutionTest.java` | [02](part-01-ioc-container/02-bean-registration.md) |
| Part 02 | `src/test/java/.../part02_boot_autoconfig/SpringCoreBeansAutoConfigurationExerciseTest.java` | `src/test/java/.../part02_boot_autoconfig/SpringCoreBeansAutoConfigurationExerciseSolutionTest.java` | [10](part-02-boot-autoconfig/10-spring-boot-auto-configuration.md) / [11](part-02-boot-autoconfig/11-debugging-and-observability.md) |
| Part 03 | `src/test/java/.../part03_container_internals/SpringCoreBeansContainerInternalsExerciseTest.java` | `src/test/java/.../part03_container_internals/SpringCoreBeansContainerInternalsExerciseSolutionTest.java` | [14](part-03-container-internals/14-post-processor-ordering.md) / [16](part-03-container-internals/16-early-reference-and-circular.md) / Part 04 的边界章节（27–31） |

运行建议：
- 先跑回归（包含 Solution）：`mvn -pl spring-core-beans test`
- 再做练习：打开对应 `*ExerciseTest.java`，移除某个方法上的 `@Disabled` 单题运行

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
- [38. Environment Abstraction：PropertySource / @PropertySource / 优先级与排障主线](part-04-wiring-and-boundaries/38-environment-and-propertysource.md)
- [39. BeanFactory API 深挖：接口族谱与手动 bootstrap 的边界](part-04-wiring-and-boundaries/39-beanfactory-api-deep-dive.md)

### Part 05：AOT / 真实世界补齐（把“项目里真会遇到的坑”补成可复现实验）

- [40. AOT / Native 总览：为什么“JVM 能跑”不等于“Native 能跑”](part-05-aot-and-real-world/40-aot-and-native-overview.md)
- [41. RuntimeHints 入门：把构建期契约跑通](part-05-aot-and-real-world/41-runtimehints-basics.md)
- [42. XML → BeanDefinitionReader：定义层解析与错误分型](part-05-aot-and-real-world/42-xml-bean-definition-reader.md)
- [43. 容器外对象注入：AutowireCapableBeanFactory](part-05-aot-and-real-world/43-autowirecapablebeanfactory-external-objects.md)
- [44. SpEL 与 `@Value("#{...}")`：表达式解析链路](part-05-aot-and-real-world/44-spel-and-value-expression.md)
- [45. 自定义 Qualifier：meta-annotation 与候选收敛](part-05-aot-and-real-world/45-custom-qualifier-meta-annotation.md)
- [46. XML namespace 扩展：NamespaceHandler / Parser / spring.handlers](part-05-aot-and-real-world/46-xml-namespace-extension.md)
- [47. BeanDefinitionReader：除了注解与 XML，还有 Properties / Groovy](part-05-aot-and-real-world/47-beandefinitionreader-other-inputs-properties-groovy.md)
- [48. 方法注入：replaced-method / MethodReplacer（实例化策略分支）](part-05-aot-and-real-world/48-method-injection-replaced-method.md)
- [49. 内置 FactoryBean 图鉴：MethodInvoking / ServiceLocator / & 前缀](part-05-aot-and-real-world/49-built-in-factorybeans-gallery.md)
- [50. PropertyEditor 与 BeanDefinition 值解析：值从定义层落到对象](part-05-aot-and-real-world/50-property-editor-and-value-resolution.md)

### Appendix：复盘与自测

- [90. 常见坑清单（建议反复对照）](appendix/90-common-pitfalls.md)
- [91. 术语表（Glossary）](appendix/91-glossary.md)
- [92. 知识点地图（Concept → Chapter → Lab）](appendix/92-knowledge-map.md)
- [93. 面试复述模板（决策树 → Lab → 断点入口）](appendix/93-interview-playbook.md)
- [94. 生产排障清单（异常分型 → 入口 → 观察点 → 修复策略）](appendix/94-production-troubleshooting-checklist.md)
- [95. spring-beans Public API 索引（按类型检索）](appendix/95-spring-beans-public-api-index.md)
- [96. spring-beans Public API Gap 清单（按包/机制域分批深化）](appendix/96-spring-beans-public-api-gap.md)
- [97. Explore/Debug 用例（可选启用，不影响默认回归）](appendix/97-explore-debug-tests.md)
- [99. 自测题（Self Check）](appendix/99-self-check.md)
