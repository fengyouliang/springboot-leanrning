# 90. 常见坑清单（建议反复对照）

这份清单不是为了“背”，而是为了让你在遇到问题时能快速定位：到底是概念没建立，还是机制没搞清。

## 1) 以为“prototype 每次方法调用都是新对象”

典型症状：

- prototype 注入 singleton 后怎么一直不变？

正确理解：

- prototype 是“每次向容器获取都新建”
- 直接注入只获取了一次

解决方案：

- `ObjectProvider`
- `@Lookup`
- scoped proxy（谨慎）

见：[04. Scope 与 prototype 注入陷阱](04-scope-and-prototype.md)

## 2) 以为 `@Order` 能解决“单个依赖注入的歧义”

事实：

- `@Order` 更常用于集合注入的排序
- 单依赖选择优先看 `@Primary`、`@Qualifier` 等

见：[03. 依赖注入解析](03-dependency-injection-resolution.md)

## 3) 在 `@Configuration(proxyBeanMethods=false)` 里互相调用 `@Bean` 方法

典型症状：

- 明明是单例，却出现多个实例（或者行为像多例）

推荐写法：

- 用 `@Bean` 方法参数声明依赖

见：[07. @Configuration 增强](07-configuration-enhancement.md)

## 4) 把 `FactoryBean` 当作“普通 bean”

典型症状：

- `getBean("name")` 拿到的类型不对
- “怎么注入工厂本身？”

核心记忆：

- `"name"` → product
- `"&name"` → factory

见：[08. FactoryBean](08-factorybean.md)

## 5) 认为“循环依赖能跑起来就没问题”

事实：

- setter 循环能成功不代表设计合理
- 半初始化对象、代理、生命周期都会让问题变复杂
- Boot 环境里可能默认更严格，直接不让你启动

见：[09. 循环依赖](09-circular-dependencies.md)

## 6) 认为“自动装配就是自动注入”

事实：

- 自动装配主要是在启动时“导入配置并注册 BeanDefinition”
- 依赖注入解析仍遵循 Spring 容器规则

建议：

- 学会看条件报告（`--debug` / `debug=true`）

见：[10. Boot 自动装配](10-spring-boot-auto-configuration.md) 与 [11. 调试](11-debugging-and-observability.md)

## 7) 把 `applicationContext.getBean()` 当成日常依赖注入方式

事实：

- 这是 service locator 风格，会隐藏依赖关系，降低可测试性

建议：

- 默认用构造器注入
- 只有在确实需要“延迟/可选/按需获取”时才用 `ObjectProvider`
对应 Lab/Test：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansLabTest.java`
推荐断点：`DefaultListableBeanFactory#doResolveDependency`、`AbstractAutowireCapableBeanFactory#populateBean`、`AbstractAutowireCapableBeanFactory#applyBeanPostProcessorsAfterInitialization`

## 8) 以为 `@Qualifier` 是“写了就行”

典型症状：

- 明明写了 `@Qualifier("xxx")`，还是注入失败
- 或者注入到了“看起来不对的那个实现”

事实：

- `@Qualifier` 的作用是 **缩小候选集合**，它不是“让容器更聪明”，而是“让你把依赖关系写清楚”
- `@Qualifier` 匹配规则取决于 `AutowireCandidateResolver`（一般是 qualifier 元数据/beanName 等）

建议：

- 多实现时优先使用：**`@Qualifier`（精确）** 或 **`@Primary`（默认实现）**
- 不要指望 `@Order` 解决单依赖歧义（见坑 2）

如何验证：

- 对应 Lab/Test：`SpringCoreBeansAutowireCandidateSelectionLabTest#primaryOverridesPriority_forSingleInjection`

见：[03. 依赖注入解析](03-dependency-injection-resolution.md)

## 9) 以为 `@Primary` 能“覆盖一切”

事实：

- `@Primary` 只是在“没有更强限定条件”时提供默认选择
- 一旦你引入更强信号（例如 `@Qualifier`、`@Resource` 的 name-first），实际选择会以限定条件为准

如何验证：

- 对应 Lab/Test：`SpringCoreBeansAutowireCandidateSelectionLabTest`（优先级/primary 的对比）

见：[03. 依赖注入解析](03-dependency-injection-resolution.md) 与 [`@Resource` 注入](32-resource-injection-name-first.md)

## 10) 以为集合注入的顺序“默认就稳定”

典型症状：

- `List<MySPI>` 注入后顺序在不同机器/不同版本下变化

事实：

- 不显式指定顺序时，顺序不应被依赖（你很容易学到错误结论）
- `@Order`/`Ordered` 才是你做“确定性顺序”的工具

如何验证：

- 对应 Lab/Test：`SpringCoreBeansAutowireCandidateSelectionLabTest#orderAnnotation_affectsCollectionInjectionOrder`

见：[03. 依赖注入解析](03-dependency-injection-resolution.md)

## 11) 以为 `@PostConstruct` 发生在“构造器之前”

事实：

- `@PostConstruct` 发生在：实例化完成 + 依赖注入完成之后（属于初始化阶段的一部分）
- 它依赖后处理器触发（不是 Java 语法自带能力），见 docs/12

如何验证：

- 对应 Lab/Test：`SpringCoreBeansLifecycleCallbackOrderLabTest#singletonLifecycleCallbacks_happenInAStableOrderAroundInitialization`

见：[05. 生命周期：初始化、销毁与回调](05-lifecycle-and-callbacks.md) 与 [12. 容器启动与基础设施处理器](12-container-bootstrap-and-infrastructure.md)

## 12) 以为 BPP “只是改属性”，不会把 bean 换成另一个对象

事实：

- `BeanPostProcessor#postProcessAfterInitialization` 可以直接返回另一个对象（最常见就是 proxy）
- 因此容器最终对外暴露的 bean，可能不是你写的那个原始实例

如何验证：

- 对应 Lab/Test：`SpringCoreBeansProxyingPhaseLabTest#beanPostProcessorCanReturnAProxyAsTheFinalExposedBean_andSelfInvocationStillBypassesTheProxy`

见：[31. 代理/替换阶段：BPP 如何把 Bean 换成 Proxy](31-proxying-phase-bpp-wraps-bean.md)

## 13) 以为循环依赖“只要能启动就等于没问题”

事实：

- setter 循环能救，靠的是“提前暴露引用”（early singleton exposure），这意味着你可能拿到半初始化对象
- 一旦代理介入，early 与 final 不一致会让问题更隐蔽（见 docs/16）

如何验证：

- 对应 Lab/Test：`SpringCoreBeansEarlyReferenceLabTest#getEarlyBeanReference_canProvideEarlyProxyDuringCircularDependencyResolution`

见：[09. 循环依赖](09-circular-dependencies.md) 与 [16. early reference 与循环依赖](16-early-reference-and-circular.md)

## 14) 以为 `FactoryBean` 只影响 `getBean("name")` 的返回值

事实：

- `FactoryBean` 还会影响：type matching、缓存语义、按类型发现（尤其 `getObjectType()`）
- `getObjectType=null` + `allowEagerInit=false` 会导致“按类型找不到但按名字能拿到”的边界

如何验证：

- 对应 Lab/Test：`SpringCoreBeansFactoryBeanEdgeCasesLabTest#factoryBeanWithNullObjectType_isNotDiscoverableByTypeWithoutEagerInit_butCanStillBeRetrievedByName`

见：[08. FactoryBean](08-factorybean.md)、[23. FactoryBean 深潜](23-factorybean-deep-dive.md)、[29. FactoryBean 边界](29-factorybean-edge-cases.md)

## 15) 以为 `proxyBeanMethods=false` 只是“性能优化”，不会影响语义

事实：

- `proxyBeanMethods=false` 会让配置类内部的 `@Bean` 方法互调变成普通 Java 调用，可能 new 出额外对象
- 推荐写法是用 `@Bean` 方法参数声明依赖（两种模式都正确）

如何验证：

- 对应 Lab/Test：
  - `SpringCoreBeansContainerLabTest#configurationProxyBeanMethodsTruePreservesSingletonSemanticsForBeanMethodCalls`
  - `SpringCoreBeansContainerLabTest#configurationProxyBeanMethodsFalseAllowsDirectMethodCallToCreateExtraInstance`

见：[07. @Configuration 增强](07-configuration-enhancement.md)
