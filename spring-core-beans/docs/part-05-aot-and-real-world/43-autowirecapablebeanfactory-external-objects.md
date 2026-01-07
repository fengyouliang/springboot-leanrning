# 43. 容器外对象注入：AutowireCapableBeanFactory

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**43. 容器外对象注入：AutowireCapableBeanFactory**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

真实项目里你一定会遇到这种场景：

> “这个对象不是 Spring 创建的，但我希望它能用到 Spring 的依赖注入/回调能力。”

典型例子：

- 某些第三方框架创建对象（非 Spring 托管）
- 你手工 new 了对象（工具类/策略对象/回调对象）
- 测试里构造了对象，但想复用容器的注入能力

这类问题的核心是：**区分“容器管理的 bean”与“容器外对象”**。

---

## 1. 结论先行：注入 ≠ 生命周期托管 ≠ 代理替换

对容器外对象，你能做到的事情通常分成三层：

1) **注入（populate）**：把 `@Autowired/@Value` 等依赖填进去
2) **初始化（initialize）**：执行 Aware、`@PostConstruct`、`afterPropertiesSet`、以及 BeanPostProcessor
3) **销毁（destroy）**：触发 `@PreDestroy` 等销毁回调

在 Spring 里，这三层能力对外的入口就是：

一个非常容易踩的点是：`initializeBean(...)` **可能返回一个“被 BPP 包装/替换后的对象”**（例如代理）。  
因此在“容器外对象”场景里，如果你想要 AOP/代理语义，必须使用 `initializeBean` 的返回值，而不是继续拿原始对象用。

---

- 只做 `autowireBean`：依赖可能已注入，但 `@PostConstruct` 还没跑
- 再做 `initializeBean`：`@PostConstruct` 才会被触发（因为它依赖 BPP）
- 最后 `destroyBean`：触发销毁回调（用于你理解“prototype 默认不销毁”的反面）

入口测试：

---

你只需要记住两个入口就能覆盖大多数排障（注入 vs 初始化）：

当你想对照“容器外对象”与“容器管理 bean”的差异时，再回到：

---

---

这一章你应该能回答：

- autowireBean / initializeBean / destroyBean 分别解决什么问题？
- 为什么 `@PostConstruct` 不会在 autowireBean 之后自动发生？

- SpEL 与 `@Value("#{...}")` 的表达式解析链路

---

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreBeansAutowireCapableBeanFactoryLabTest`
- 建议命令：`mvn -pl spring-core-beans test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 2. 复现入口（可运行）

本模块提供一个最小对照实验，帮助你建立直觉：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansAutowireCapableBeanFactoryLabTest.java`

推荐运行命令：

```bash
mvn -pl spring-core-beans -Dtest=SpringCoreBeansAutowireCapableBeanFactoryLabTest test
```

## 3. 源码 / 断点建议（把“容器外对象”放回统一生命周期主线）

当你要进一步解释“到底是谁在做注入/谁在触发 @PostConstruct”时，常用加深断点：

## F. 常见坑与边界

- [25. 手工添加 BeanPostProcessor：顺序与 Ordered 的陷阱](../part-04-wiring-and-boundaries/25-programmatic-bpp-registration.md)
- [05. 初始化、销毁与回调](../part-01-ioc-container/05-lifecycle-and-callbacks.md)

## 4. 常见误区

1) **误区：autowireBean 之后就等同于容器管理**
   - 实际：它只是“尽力帮你补上部分管道”，你仍要对生命周期与代理替换保持警惕。
2) **误区：容器外对象一定不能用 @PostConstruct**
   - 可以，但你要显式调用 initialize 链路（否则 BPP 不会触发）。

## G. 小结与下一章

- `AutowireCapableBeanFactory#autowireBean`（偏“只做注入”）
- `AutowireCapableBeanFactory#initializeBean`（触发初始化链路）
- `AutowireCapableBeanFactory#destroyBean`（触发销毁链路）

- `AbstractAutowireCapableBeanFactory#populateBean`（注入发生点）
- `AbstractAutowireCapableBeanFactory#initializeBean`（Aware/BPP/init callbacks 串联点）

- `AutowiredAnnotationBeanPostProcessor#postProcessProperties`（`@Autowired/@Value` 等注入入口）
- `InitDestroyAnnotationBeanPostProcessor#postProcessBeforeInitialization`（`@PostConstruct` 入口之一）
- `AbstractAutowireCapableBeanFactory#applyBeanPostProcessorsAfterInitialization`（BPP 可能在这里返回 proxy）

## 5. 小结与下一章预告

下一章我们补齐另一个真实项目高频点：

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreBeansAutowireCapableBeanFactoryLabTest`
- Test file：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansAutowireCapableBeanFactoryLabTest.java`

上一章：[42. XML → BeanDefinitionReader：定义层解析与错误分型](42-xml-bean-definition-reader.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[44. SpEL 与 `@Value("#{...}")`：表达式解析链路](44-spel-and-value-expression.md)

<!-- BOOKIFY:END -->
