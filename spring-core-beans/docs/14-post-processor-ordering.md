# 14. 顺序（Ordering）：PriorityOrdered / Ordered / 无序

当容器里存在多个 BFPP/BPP 时，“谁先运行”会直接决定最终结果。

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansPostProcessorOrderingLabTest.java`

## 1. 规则总览（记住这三层就够）

Spring 在同一类 post-processor 内，常用的排序规则是：

1) `PriorityOrdered`（最优先）
2) `Ordered`
3) 没实现顺序接口（最后）

> 这套规则适用于 BFPP 与 BPP（以及很多“插件式扩展点”）。

## 2. BFPP 的顺序：先改谁的定义？

对应测试：

- `SpringCoreBeansPostProcessorOrderingLabTest.beanFactoryPostProcessors_areInvokedInPriorityOrderedThenOrderedThenUnorderedOrder()`

它只断言我们自己注册的三个 BFPP 的相对顺序：

- `bfpp:priority` → `bfpp:ordered` → `bfpp:unordered`

这样做的原因是：

- 容器内部也可能有自己的处理器
- 断言内部处理器的完整顺序容易随版本变化而变得不稳定

学习重点：**你能控制你自己的扩展点顺序**。

## 3. BPP 的顺序：谁先“动手”改实例？

对应测试：

- `SpringCoreBeansPostProcessorOrderingLabTest.beanPostProcessors_areAppliedInPriorityOrderedThenOrderedThenUnorderedOrder()`

同样只断言我们自己注册的三个 BPP 的相对顺序。

学习重点：

- 多个 BPP 对同一个 bean 做增强时，“顺序”是结果的一部分。

## 4. 常见误解

- **误解：`@Order` 能影响单依赖注入的选择**
  - 单个依赖（注入一个 `T`）的选择通常看：`@Primary`、`@Qualifier`、beanName 等。
  - `@Order` 更常见的影响是：集合注入（`List<T>`）、拦截链、处理器链。

## 源码锚点（建议从这里下断点）

- `PostProcessorRegistrationDelegate#invokeBeanFactoryPostProcessors`：BFPP/BDRPP 的执行入口（排序与分组都在这一段完成）
- `PostProcessorRegistrationDelegate#registerBeanPostProcessors`：BPP 的注册入口（这里决定“谁先作用于实例”）
- `AnnotationAwareOrderComparator#sort`：Spring 常用的排序器（会综合 `PriorityOrdered/Ordered/@Order/@Priority` 等信息）
- `Ordered#getOrder`：顺序接口的关键语义点（数字越小通常越靠前）
- `DefaultListableBeanFactory#addBeanPostProcessor`：BPP 最终进入 BeanFactory 的地方（注册顺序会影响调用顺序）

## 断点闭环（用本仓库 Lab/Test 跑一遍）

入口：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansPostProcessorOrderingLabTest.java`
  - `beanFactoryPostProcessors_areInvokedInPriorityOrderedThenOrderedThenUnorderedOrder()`
  - `beanPostProcessors_areAppliedInPriorityOrderedThenOrderedThenUnorderedOrder()`

建议断点：

1) `PostProcessorRegistrationDelegate#invokeBeanFactoryPostProcessors`：观察 BFPP 分组与排序（PriorityOrdered → Ordered → others）
2) `PostProcessorRegistrationDelegate#registerBeanPostProcessors`：观察 BPP 的同样排序逻辑以及注册到 BeanFactory 的时机
3) `AnnotationAwareOrderComparator#sort`：观察排序输入（候选集合）与排序输出（最终顺序）
4) 你在 Lab 中定义的三个 processor（priority/ordered/unordered）入口方法：观察断言里记录的执行顺序是怎么来的

## 排障分流：这是定义层问题还是实例层问题？

- “某个 BFPP 改定义没生效/被覆盖了” → **定义层 + 顺序问题**：先确认它是否实现了 `PriorityOrdered/Ordered`，再看它是否比其他 BFPP 更早执行（本章 Lab）
- “某个 BPP 的代理/增强消失了或包裹顺序不对” → **实例层 + 顺序问题**：看 `registerBeanPostProcessors` 的排序与注册时机（对照 [31](31-proxying-phase-bpp-wraps-bean.md)）
- “我手工 `addBeanPostProcessor` 后，`Ordered` 反而不生效” → **实例层 + 注册方式问题**：手工注册的 BPP 不会走容器的排序流程（见 [25](25-programmatic-bpp-registration.md)）
- “我以为 `@Order` 能解决单依赖注入歧义” → **不是顺序问题，是候选选择问题**：转到 [33](33-autowire-candidate-selection-primary-priority-order.md)

## 5. 一句话自检

- 你能解释清楚：为什么我们只断言“相对顺序”，而不去断言“容器内所有处理器的全序列”？
