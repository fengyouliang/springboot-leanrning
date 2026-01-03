# 99. 自测题：你是否真的理解了？

建议学习方式：

- 先不看代码，尝试回答问题
- 再去对应章节/实验里验证
- 最后再启用 Exercises 把理解落实成可运行的结论

## A. 心智模型（对应 01/06）

- 你能不能用一句话区分：`BeanDefinition`（定义元数据） vs bean instance（运行时对象）？
- BFPP/BPP/BDRPP 分别“改的是定义还是实例”？它们在哪个阶段发生？
- 你能不能复述 `ApplicationContext#refresh()` 的关键阶段（至少说清：什么时候跑 BFPP，什么时候注册/执行 BPP，什么时候开始创建非 lazy singleton）？

1) 用一句话解释：什么是 `BeanDefinition`？它与 Bean 实例的关系是什么？
2) BFPP 与 BPP 的差别是什么？它们分别作用在“定义层”还是“实例层”？
3) 为什么说“自动装配本质上也是在注册 BeanDefinition”？

## B. 注册入口（对应 02/10）

- 你能列出 4 条常见注册入口，并说明它们“注册的是谁/发生在什么时候”吗？
  - `@ComponentScan`
  - `@Configuration + @Bean`
  - `@Import`（含 `ImportSelector`）
  - `ImportBeanDefinitionRegistrar`
- Spring Boot 自动装配对“Bean 注册”的本质影响是什么？（提示：它更像“按条件批量 @Import”）

4) `@ComponentScan`、`@Bean`、`@Import` 这三种入口分别解决什么问题？
5) `ImportSelector` 与 `ImportBeanDefinitionRegistrar` 的角色差异是什么？
6) 你如何解释 Spring Boot 自动装配“从哪里拿到要导入的配置类列表”？

## C. 依赖注入（对应 03）

- 当一个接口有两个实现时，`@Autowired` 单注入会发生什么？你会优先用 `@Qualifier` 还是 `@Primary`，为什么？
- `@Order` 能不能解决单注入歧义？它主要解决什么问题？
- `@Priority` 能不能作为“默认实现”方案？它与 `@Primary` 的优先级如何？（建议用 Lab 验证，不要靠猜）
- 你能不能说出注入解析的“源码级决策树”：先收集候选，再缩小候选？关键断点打在哪里？

7) 同类型多个候选时，`@Qualifier` 与 `@Primary` 各自适合什么场景？
8) `ObjectProvider` 解决的是什么问题？它为什么有助于 prototype 注入？
9) 遇到 `NoUniqueBeanDefinitionException` 时，你的排查顺序是什么？

## D. Scope 与生命周期（对应 04/05）

- `singleton` 与 `prototype` 的真实语义分别是什么？它们的“创建时机/销毁时机”有什么根本区别？
- prototype 注入 singleton 后为什么“看起来像单例”？你能给出 2 种正确的解决方式吗？
- 你能不能写出（或复述）初始化阶段的回调顺序：BPP before-init / `@PostConstruct` / `afterPropertiesSet` / initMethod / BPP after-init？

10) prototype 的语义是什么？为什么“prototype 注入 singleton”会像单例？
11) `@PostConstruct` 在 bean 创建流程的哪个阶段触发？
12) 为什么 prototype 的 `@PreDestroy` 常常不会触发？

## E. 机制题（对应 07/08/09）

- 为什么 `@Configuration(proxyBeanMethods=false)` 下，配置类内部 `@Bean` 方法互调可能 new 出额外对象？最推荐的写法是什么？
- `FactoryBean` 的两条硬规则是什么？（提示：`name` vs `&name`）
- `FactoryBean#isSingleton()` 决定缓存的是什么？（提示：缓存的是 product）
- `getObjectType()` 返回 `null` 会导致什么边界问题？为什么 `allowEagerInit=false` 会放大它？
- 循环依赖为什么构造器基本救不了、setter 有时能救？early reference 的意义是什么？代理介入后为什么更复杂？

13) `proxyBeanMethods=false` 下，为什么在 `@Bean` 方法体里互相调用可能会 new 出额外实例？
14) 为什么 `getBean("sequence")` 拿到的是 Long 而不是 `SequenceFactoryBean`？
15) 构造器循环依赖为什么必然失败？setter 循环为什么有时能成功？

## F. 动手题（建议直接做 Exercises）

这些题都已经在本模块的 Exercises 里给出（默认 `@Disabled`）：

- 让 `FormattingService` 切换为 lower formatter（体会 `@Qualifier`）
- 去掉 `@Qualifier`，改用 `@Primary` 解决歧义
- 让 `DirectPrototypeConsumer` 每次都拿到新 id（体会 prototype 注入陷阱与解决方式）

对应文件：

- `src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansExerciseTest.java`
对应 Lab/Test：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansLabTest.java`
推荐断点：`DefaultListableBeanFactory#doResolveDependency`、`AbstractAutowireCapableBeanFactory#doCreateBean`、`AbstractAutowireCapableBeanFactory#initializeBean`

## G. First Pass（10 个最小闭环入口，按 Lab 自测）

如果你不想一次性把整套章节都读完，想先把“主线 + 常见坑点”跑通一遍，可以按下面 10 个入口做自测：每个入口只要求你写 1–2 句结论（定义层/实例层/时机/顺序/断点入口）。

1) 定义层 vs 实例层：`SpringCoreBeansContainerLabTest#beanDefinitionIsNotTheBeanInstance`
2) refresh 阶段感：从 `AbstractApplicationContext#refresh` 走一遍 BFPP/BPP 的关键阶段（同上测试即可）
3) 注册入口：`SpringCoreBeansBootstrapInternalsLabTest`（配合 [02](02-bean-registration.md)）
4) 注入歧义：`SpringCoreBeansInjectionAmbiguityLabTest`
5) 候选选择边界：`SpringCoreBeansAutowireCandidateSelectionLabTest`
6) prototype 注入陷阱：`SpringCoreBeansLabTest`（prototype 相关用例）
7) 生命周期回调顺序：`SpringCoreBeansLifecycleCallbackOrderLabTest`
8) post-processor 职责边界：`SpringCoreBeansRegistryPostProcessorLabTest` + `SpringCoreBeansPostProcessorOrderingLabTest`
9) early reference：`SpringCoreBeansEarlyReferenceLabTest`
10) 排障断点入口：`SpringCoreBeansExceptionNavigationLabTest` / `SpringCoreBeansBeanGraphDebugLabTest`
