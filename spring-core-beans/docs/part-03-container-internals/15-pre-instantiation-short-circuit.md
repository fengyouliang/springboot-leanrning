# 15. 实例化前短路：postProcessBeforeInstantiation 能让构造器根本不执行

## 0. 复现入口（可运行）

- 入口测试（推荐先跑通再下断点）：
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansPreInstantiationLabTest.java`
- 推荐运行命令：
  - `mvn -pl spring-core-beans -Dtest=SpringCoreBeansPreInstantiationLabTest test`

这一章讲一个“非常像魔法”的容器机制：

- `InstantiationAwareBeanPostProcessor#postProcessBeforeInstantiation`

它允许你在 bean 实例化之前返回一个对象，从而 **短路默认的创建路径**。

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansPreInstantiationLabTest.java`

## 1. 现象：构造器抛异常会让 refresh 直接失败

对应测试：

- `SpringCoreBeansPreInstantiationLabTest.withoutBeforeInstantiationShortCircuit_refreshFailsAndConstructorWasCalled()`

你会看到：

- `FailingService` 构造器被调用
- 构造器抛异常导致容器 refresh 失败

这说明：**默认情况下，单例会在 refresh 阶段被创建**（非 lazy）。

## 2. 现象：短路后，构造器不再执行

对应测试：

- `SpringCoreBeansPreInstantiationLabTest.postProcessBeforeInstantiation_canShortCircuitDefaultInstantiationPath()`

我们注册了一个 `InstantiationAwareBeanPostProcessor`：

- 当容器准备创建 `FailingService` 时
- `postProcessBeforeInstantiation` 直接返回一个 JDK proxy（实现了 `GreetingService`）
- 容器就把这个 proxy 当作最终 bean

因此：

- 构造器不会执行
- refresh 不会失败

## 3. 这个机制有什么现实意义？

理解它的价值在于：

- 你能理解“容器为什么能把某个 bean 变成代理/替身对象”
- 你能理解“实例层增强”的入口不仅仅是 AOP（很多能力都是类似机制）

## 4. 常见坑

- **坑 1：返回的对象类型不兼容**
  - 容器后续按类型注入、按类型 getBean 可能会失败（`BeanNotOfRequiredTypeException`）。

- **坑 2：短路会绕过一些正常生命周期**
  - 短路意味着你不走默认实例化流程，很多生命周期回调/依赖注入的时机都会改变。

- **坑 3：学习可以用，工程里要非常谨慎**
  - 它属于极强的扩展点：一旦用错，系统会变得难以推理。

## 源码锚点（建议从这里下断点）

- `DefaultListableBeanFactory#preInstantiateSingletons`：非 lazy 单例通常在 refresh 期间从这里开始批量创建（本章现象的触发点）
- `AbstractAutowireCapableBeanFactory#createBean`：创建入口（会先尝试“实例化前短路”）
- `AbstractAutowireCapableBeanFactory#resolveBeforeInstantiation`：调用 `postProcessBeforeInstantiation` 的关键钩子
- `InstantiationAwareBeanPostProcessor#postProcessBeforeInstantiation`：短路扩展点（在“还没走默认实例化”前直接返回对象）
- `AbstractAutowireCapableBeanFactory#doCreateBean`：默认创建主流程（短路成功时通常不会走到这里）

## 断点闭环（用本仓库 Lab/Test 跑一遍）

入口：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansPreInstantiationLabTest.java`
  - `withoutBeforeInstantiationShortCircuit_refreshFailsAndConstructorWasCalled()`
  - `postProcessBeforeInstantiation_canShortCircuitDefaultInstantiationPath()`

建议断点：

1) `FailingService` 构造器：对照两段测试，确认“默认路径一定会调用构造器”
2) 你在 Lab 里实现的 `InstantiationAwareBeanPostProcessor#postProcessBeforeInstantiation(...)`：观察它返回的对象（proxy）
3) `AbstractAutowireCapableBeanFactory#resolveBeforeInstantiation`：观察短路发生在默认实例化之前
4) `AbstractAutowireCapableBeanFactory#doCreateBean`：在短路成功的测试里，验证这里不会被命中（或不会为目标 bean 执行）

## 排障分流：这是定义层问题还是实例层问题？

- “我写了 before-instantiation 的 BPP，但构造器还是执行了” → **实例层（时机/注册方式）**：BPP 是否在 refresh 前注册？是否真的被当作 BPP 注册进 BeanFactory？（对照 [25](../part-04-wiring-and-boundaries/25-programmatic-bpp-registration.md)）
- “短路后出现 `BeanNotOfRequiredTypeException`” → **实例层（暴露类型）**：返回对象的类型是否与容器期望类型兼容？（JDK proxy 只实现接口）
- “短路后生命周期回调/注入行为变得反直觉” → **实例层（绕过默认流程）**：你返回对象意味着你可能绕过 `doCreateBean` 的部分阶段（可对照 [17](17-lifecycle-callback-order.md)、[30](../part-04-wiring-and-boundaries/30-injection-phase-field-vs-constructor.md)）
- “我以为这是 AOP/事务专属机制” → **实例层通用机制**：代理/替身的出现不止发生在 AOP（见 [31](../part-04-wiring-and-boundaries/31-proxying-phase-bpp-wraps-bean.md)）

## 5. 一句话自检

- 你能解释清楚：为什么短路后构造器不执行，但 bean 仍然可以被容器拿到并调用吗？
对应 Lab/Test：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part03_container_internals/SpringCoreBeansPreInstantiationLabTest.java`
推荐断点：`AbstractAutowireCapableBeanFactory#resolveBeforeInstantiation`、`AbstractAutowireCapableBeanFactory#applyBeanPostProcessorsBeforeInstantiation`、`AbstractAutowireCapableBeanFactory#createBeanInstance`

## 面试常问（实例化前短路的风险）

- 常问：`postProcessBeforeInstantiation` 能做什么？为什么它是高危扩展点？
  - 答题要点：可以在实例化前直接返回替身/proxy，短路后续创建流程；风险是打破注入/初始化回调的直觉，引入“看似没执行构造但对象可用”的误判。
- 常见追问：怎么证明某个 bean 命中了短路？断点怎么下？
  - 答题要点：以 `resolveBeforeInstantiation` 为入口，沿着 `applyBeanPostProcessorsBeforeInstantiation` 找到具体哪个 `InstantiationAwareBeanPostProcessor` 返回了替身。

上一章：[14. 顺序（Ordering）：PriorityOrdered / Ordered / 无序](14-post-processor-ordering.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[16. early reference 与循环依赖：getEarlyBeanReference 到底解决什么？](16-early-reference-and-circular.md)