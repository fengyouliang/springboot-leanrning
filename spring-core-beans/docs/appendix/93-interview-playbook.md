# 93. 面试复述模板（决策树 → Lab → 断点入口）

本章目标：把 `spring-core-beans` 变成你的“面试答题脚本”。

约束：**不靠背概念**，而是靠“可复述的决策树 + 可运行的 Lab + 可下断点证明”。

---

## 0. 一句话总纲（通用开场）

> Spring 的 Bean 机制可以用“三层模型”统一：**定义层（BeanDefinition）→ 实例层（create/populate/initialize）→ 最终暴露对象（可能是 proxy/early reference）**。  
> 面试里所有“为什么注入的是它/为什么会 proxy/为什么循环依赖有时能救”，都能落到这三层的某个阶段。

对应入口：

- 深挖指南：`docs/part-00-guide/00-deep-dive-guide.md`
- 排障主入口：`docs/part-02-boot-autoconfig/11-debugging-and-observability.md`

---

## 1) 依赖解析（DI）：候选收集 → 候选收敛 → 最终注入

### 复述模板（可背）

1. 先按类型收集候选（Map<beanName, candidate>）  
2. 再按规则收敛候选：Qualifier → name 匹配 → Primary → Priority/Ordered（部分场景）  
3. 收敛成 1 个就注入；收敛不下来就 fail-fast（NoUnique）  

### 对应 Lab（可证明）

- `SpringCoreBeansInjectionAmbiguityLabTest`
- `SpringCoreBeansAutowireCandidateSelectionLabTest`

### 推荐断点（够用版）

- `DefaultListableBeanFactory#doResolveDependency`
- `DefaultListableBeanFactory#findAutowireCandidates`
- `DefaultListableBeanFactory#determineAutowireCandidate`
- `QualifierAnnotationAutowireCandidateResolver#isAutowireCandidate`

---

## 2) BFPP / BDRPP / BPP：改定义 vs 改实例（以及它们能/不能做什么）

### 复述模板（可背）

- **BDRPP**：可以“注册/修改 BeanDefinition”（定义层入口更早）  
- **BFPP**：可以“修改 BeanDefinition”（仍在定义层）  
- **BPP**：可以“处理实例”甚至“替换成 proxy”（实例层/最终暴露对象）  

### 对应 Lab（可证明）

- `SpringCoreBeansRegistryPostProcessorLabTest`
- `SpringCoreBeansPostProcessorOrderingLabTest`
- `SpringCoreBeansProxyingPhaseLabTest`

### 推荐断点

- `PostProcessorRegistrationDelegate#invokeBeanFactoryPostProcessors`
- `PostProcessorRegistrationDelegate#registerBeanPostProcessors`
- `AbstractAutowireCapableBeanFactory#applyBeanPostProcessorsBeforeInitialization`
- `AbstractAutowireCapableBeanFactory#applyBeanPostProcessorsAfterInitialization`

---

## 3) 生命周期：创建/注入/初始化/销毁（以及回调顺序）

### 复述模板（可背）

- 创建主线：instantiate → populate → initialize  
- 注入发生在 populate（而不是构造器之后“自然发生”）  
- `@PostConstruct` 属于初始化阶段（依赖 BPP）  
- prototype 默认不走容器销毁（除非你显式 destroy）  

### 对应 Lab（可证明）

- `SpringCoreBeansLifecycleCallbackOrderLabTest`
- `SpringCoreBeansBeanCreationTraceLabTest`

### 推荐断点

- `AbstractAutowireCapableBeanFactory#doCreateBean`
- `AbstractAutowireCapableBeanFactory#populateBean`
- `AbstractAutowireCapableBeanFactory#initializeBean`
- `DisposableBeanAdapter#destroy`

---

## 4) 循环依赖：为什么 constructor 无解、setter 有时能救？

### 复述模板（可背）

- constructor 循环：需要“先有对象才能注入”，因此无解  
- setter 循环：单例创建时存在 early exposure 窗口（三级缓存），可能救回来  
- 一旦代理/包装介入，early reference 可能变成 proxy，行为会变化  

### 对应 Lab（可证明）

- `SpringCoreBeansContainerLabTest`
- `SpringCoreBeansEarlyReferenceLabTest`

### 推荐断点

- `DefaultSingletonBeanRegistry#getSingleton`
- `DefaultSingletonBeanRegistry#addSingletonFactory`
- `AbstractAutowireCapableBeanFactory#getEarlyBeanReference`

---

## 5) Spring Boot 自动装配：为什么有/为什么没有/为什么没退让？

### 复述模板（可背）

- auto-config 本质是：配置导入（@Import）+ 条件评估（@Conditional...）+ bean 注册  
- 条件评估发生在注册阶段（refresh 前半段），不是看“最终容器状态”  
- 覆盖/back-off 要求“覆盖 bean 在条件评估时可见”，否则会出现重复候选/注入失败  

### 对应 Lab（可证明）

- `SpringCoreBeansConditionEvaluationReportLabTest`
- `SpringCoreBeansAutoConfigurationOrderingLabTest`
- `SpringCoreBeansAutoConfigurationBackoffTimingLabTest`
- `SpringCoreBeansAutoConfigurationOverrideMatrixLabTest`

### 推荐断点

- `ConditionEvaluator#shouldSkip`
- `OnBeanCondition#getMatchOutcome`
- `AbstractApplicationContext#refresh`

---

## 6) AOT/Native：RuntimeHints（构建期契约）

### 复述模板（可背）

- AOT/Native 的关键是把“运行期反射/代理/资源需求”前移为“构建期契约”  
- Spring 用 RuntimeHints 表达这种契约：reflection/proxy/resource 等  
- 你可以在 JVM 单测里验证 hints 的存在性（不必构建 native image）  

### 对应章节 + Lab（可证明）

- 章节：`docs/part-05-aot-and-real-world/40-aot-and-native-overview.md`
- 章节：`docs/part-05-aot-and-real-world/41-runtimehints-basics.md`
- Lab：`SpringCoreBeansAotRuntimeHintsLabTest`

### 推荐断点

- `RuntimeHintsRegistrar#registerHints`

---

## 7) 真实世界补齐（面试加分：你能解释“容器外对象/SpEL/自定义 Qualifier”）

- XML → BeanDefinitionReader：`docs/part-05-aot-and-real-world/42-xml-bean-definition-reader.md` + `SpringCoreBeansXmlBeanDefinitionReaderLabTest`
- 容器外对象注入：`docs/part-05-aot-and-real-world/43-autowirecapablebeanfactory-external-objects.md` + `SpringCoreBeansAutowireCapableBeanFactoryLabTest`
- SpEL：`docs/part-05-aot-and-real-world/44-spel-and-value-expression.md` + `SpringCoreBeansSpelValueLabTest`
- 自定义 Qualifier：`docs/part-05-aot-and-real-world/45-custom-qualifier-meta-annotation.md` + `SpringCoreBeansCustomQualifierLabTest`

---

上一章：[92. 知识点地图（Concept → Chapter → Lab）](92-knowledge-map.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[94. 生产排障清单（异常分型 → 入口 → 观察点 → 修复策略）](94-production-troubleshooting-checklist.md)

