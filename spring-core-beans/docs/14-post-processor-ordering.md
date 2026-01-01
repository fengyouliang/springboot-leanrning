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

## 源码最短路径（call chain）

> 目标：当你怀疑“顺序导致结果反直觉”时，用最短调用链把问题归位：到底是 **BFPP（定义层）** 的顺序，还是 **BPP（实例层）** 的顺序？

容器启动主链路（只列最关键节点）：

- `AbstractApplicationContext#refresh`
  - `PostProcessorRegistrationDelegate#invokeBeanFactoryPostProcessors`  
    - **BFPP/BDRPP 在这里执行**（定义层：改 `BeanDefinition`）
  - `PostProcessorRegistrationDelegate#registerBeanPostProcessors`  
    - **BPP 在这里注册进 BeanFactory**（实例层：决定“谁先作用于实例”）
  - `AbstractApplicationContext#finishBeanFactoryInitialization`
    - `DefaultListableBeanFactory#preInstantiateSingletons`（批量创建非 lazy 单例）
      - `AbstractAutowireCapableBeanFactory#doCreateBean`
        - `initializeBean`
          - `applyBeanPostProcessorsBeforeInitialization`
          - `applyBeanPostProcessorsAfterInitialization`

一个非常实用的“断点分流口诀”：

- 你要看“谁先改定义” → 去 `invokeBeanFactoryPostProcessors`
- 你要看“谁先包/谁后包（代理叠加顺序）” → 去 `registerBeanPostProcessors` + `applyBeanPostProcessorsAfterInitialization`

> 注意：这里的“先包/后包”说的是 **容器阶段的 BPP 包裹顺序**。  
> 它会影响是否出现“多层 proxy（套娃）”以及外层/内层 proxy 的归属。
>
> AOP/事务/缓存/安全这类能力内部还有另一套“链条顺序”（advisor/interceptor 顺序），不要混在一起：
>
> - advisor 顺序与 `proceed()` 嵌套：见 `spring-core-aop/docs/06-debugging.md`
> - 多切面/多代理叠加与顺序（两套顺序分流）：见 `spring-core-aop/docs/09-multi-proxy-stacking.md`
>
> 对应可运行闭环：
>
> - beans（BPP 注册顺序）：`SpringCoreBeansPostProcessorOrderingLabTest`
> - aop（多 advisor vs 套娃 proxy）：`SpringCoreAopMultiProxyStackingLabTest`

## 固定观察点（watch list）

> 目标：不靠猜，直接用 debugger 的固定观察点回答“顺序到底怎么来的、最终谁先执行”。

在 `PostProcessorRegistrationDelegate#invokeBeanFactoryPostProcessors` 里建议 watch/evaluate：

- `processedBeans`（或同等含义的集合）：哪些 processor 已经处理过（避免重复执行）
- “三组 processor 集合”（概念上）：`PriorityOrdered` / `Ordered` / others 的分组结果  
  - 你不必强记变量名，但要确认：同一类 processor 是否被按三段执行

在 `PostProcessorRegistrationDelegate#registerBeanPostProcessors` 里建议 watch/evaluate：

- `beanFactory.getBeanPostProcessors()`：**最终 BPP 列表（顺序就是执行顺序）**
- `internalPostProcessors`（概念上）：容器会把一些 internal BPP 放到最后重新注册（这会影响“包裹顺序”）

在 `AbstractAutowireCapableBeanFactory#applyBeanPostProcessorsAfterInitialization` 里建议 watch/evaluate：

- `beanName`：给断点加条件只看目标 bean（否则会非常吵）
- `result`（或等价变量）：BPP 链路的中间/最终返回值
- `result == bean`：是否发生了“替换/包装”

> 小技巧：你只要把 `beanFactory.getBeanPostProcessors()` 的顺序看清楚，很多“为什么代理是这样叠加的”就不再神秘了。

## 反例（counterexample）

**反例：我明明让 BPP 实现了 `PriorityOrdered/Ordered`，为什么顺序还是不生效？**

最小复现入口（必现）：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansProgrammaticBeanPostProcessorLabTest.java`
  - `programmaticBppExecutionOrder_isRegistrationOrder_notOrderedInterface()`

你在断点里应该看到什么（用于纠错）：

- 手工 `beanFactory.addBeanPostProcessor(...)` 注册的 BPP  
  - **不会**走 `PostProcessorRegistrationDelegate#registerBeanPostProcessors` 的排序流程
  - 执行顺序只按“注册顺序”，不是按 `Ordered`
- 因此你会看到：`beanFactory.getBeanPostProcessors()` 里手工注册的 BPP 在更前面  
  ⇒ 最终包裹/增强顺序也跟着变（很多“反直觉”就是从这里来的）

把这个反例看懂，你就能把两个顺序体系彻底分开：

- “容器自动发现 + 排序”体系：见本章（`registerBeanPostProcessors`）
- “手工注册绕过排序”体系：见 [25](25-programmatic-bpp-registration.md)

## 5. 一句话自检

- 你能解释清楚：为什么我们只断言“相对顺序”，而不去断言“容器内所有处理器的全序列”？
对应 Lab/Test：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansPostProcessorOrderingLabTest.java`
推荐断点：`PostProcessorRegistrationDelegate#invokeBeanFactoryPostProcessors`、`PostProcessorRegistrationDelegate#registerBeanPostProcessors`、`AnnotationAwareOrderComparator#sort`
