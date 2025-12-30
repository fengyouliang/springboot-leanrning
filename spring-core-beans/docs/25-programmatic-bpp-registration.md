# 25. 手工添加 BeanPostProcessor：顺序与 Ordered 的陷阱

很多学习资料会只讲“把 BPP 声明成 bean，让容器自动发现”。

但容器还支持一种更底层的方式：

- `beanFactory.addBeanPostProcessor(...)`

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansProgrammaticBeanPostProcessorLabTest.java`

## 1. 现象：手工添加的 BPP 会比容器自动发现的 BPP 更早执行

对应测试：

- `SpringCoreBeansProgrammaticBeanPostProcessorLabTest.programmaticallyAddedBpp_runsBeforeBeanDefinedBpp_evenIfBeanDefinedIsPriorityOrdered()`

我们做了两件事：

1) 在 refresh 之前用 `addBeanPostProcessor` 手工注册一个 BPP
2) 同时再注册一个 `PriorityOrdered` 的 BPP（作为普通 bean）

你会观察到：

- 手工注册的 BPP 仍然先于“作为 bean 自动发现”的 BPP 执行

结论：

- **手工注册的 BPP 优先级非常高**

## 2. 更隐蔽的坑：手工注册的 BPP 不会按 Ordered 排序

对应测试：

- `SpringCoreBeansProgrammaticBeanPostProcessorLabTest.programmaticBppExecutionOrder_isRegistrationOrder_notOrderedInterface()`

即使你实现了 `PriorityOrdered` 并返回更高优先级：

- 手工注册的 BPP 仍然按“注册顺序”执行

这能解释很多工程里遇到的“我明明写了 order，但为什么不生效？”

## 3. 什么时候会用到？

学习阶段你只要知道它存在即可；工程里典型使用场景是：

- 框架需要在 refresh 之前根据条件动态决定是否注册某些 BPP

但要谨记：

- 这是强力扩展点，滥用会让系统难以推理。

## 源码锚点（建议从这里下断点）

- `ConfigurableListableBeanFactory#addBeanPostProcessor`：手工注册 BPP 的入口（绕过容器的自动发现与排序）
- `PostProcessorRegistrationDelegate#registerBeanPostProcessors`：容器自动发现并排序 BPP 的入口（与手工注册形成对照）
- `AbstractAutowireCapableBeanFactory#applyBeanPostProcessorsBeforeInitialization`：BPP(before) 的调用点（观察“谁先执行”）
- `AbstractAutowireCapableBeanFactory#applyBeanPostProcessorsAfterInitialization`：BPP(after) 的调用点（观察“谁后执行/谁包谁”）
- `AbstractApplicationContext#refresh`：把“BPP 注册时机”放回到容器时间线（手工注册通常发生在 refresh 前）

## 断点闭环（用本仓库 Lab/Test 跑一遍）

入口：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansProgrammaticBeanPostProcessorLabTest.java`
  - `programmaticallyAddedBpp_runsBeforeBeanDefinedBpp_evenIfBeanDefinedIsPriorityOrdered()`
  - `programmaticBppExecutionOrder_isRegistrationOrder_notOrderedInterface()`

建议断点：

1) 测试里 `addBeanPostProcessor(...)` 的调用行：确认手工注册发生在 refresh 之前
2) `PostProcessorRegistrationDelegate#registerBeanPostProcessors`：观察“作为 bean 自动发现”的 BPP 是何时被注册的
3) `AbstractAutowireCapableBeanFactory#applyBeanPostProcessorsAfterInitialization`：观察手工注册的 BPP 会先于自动发现的 BPP 执行
4) 对照第二个测试：观察手工注册的多个 BPP 为什么只按“注册顺序”执行，而不是按 `Ordered` 排序

## 排障分流：这是定义层问题还是实例层问题？

- “我实现了 `Ordered/@Order`，但某个 BPP 顺序不生效” → **实例层 + 注册方式问题**：它是不是被手工 `addBeanPostProcessor` 进去的？（本章第 2 节）
- “某个 BPP 完全没生效” → **实例层 + 时机问题**：目标 bean 是否在 BPP 注册之前就被提前实例化了？（结合 [14](14-post-processor-ordering.md) 与本章断点）
- “系统里出现很难追踪的代理/增强行为” → **实例层可观测性问题**：优先从 BPP 列表与注册方式入手（也可对照 [31](31-proxying-phase-bpp-wraps-bean.md)）
- “把这类手工注册当成常规手段到处用” → **设计风险**：它会绕开容器默认排序与可观测性，建议仅用于框架/基础设施层

## 4. 一句话自检

- 你能解释清楚：为什么手工注册的 BPP 不受 Ordered 影响吗？（提示：容器不会再对它排序，只按注册顺序调用）
