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

## 4. 一句话自检

- 你能解释清楚：为什么手工注册的 BPP 不受 Ordered 影响吗？（提示：容器不会再对它排序，只按注册顺序调用）
