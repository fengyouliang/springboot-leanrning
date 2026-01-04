# 06. 异步广播：让事件“默认异步”而不是靠 `@Async`

上一章（`@Async`）的做法是：**让监听器方法异步执行**。

还有另一种思路是：让事件分发器（multicaster）本身就异步。

> 这会让“所有事件监听器”默认异步执行（除非你显式选择同步）。

## 为什么这是一个好练习？

它能帮你理解：事件机制不是黑盒，Spring 通过一个 `ApplicationEventMulticaster` 把事件分发到监听器。

## 在本模块的练习入口

看 `SpringCoreEventsExerciseTest#exercise_asyncMulticaster`：

- 目标：把事件改为“默认异步分发”
- 然后更新/补充断言，证明它确实不再是同步线程

## 实现思路（提示，不直接给最终代码）

你需要在 Spring 容器里提供一个自定义的 multicaster，并为它设置 `TaskExecutor`。

学习建议：

- 先让 thread name 可控（线程池 prefix），再写断言
- 再回头对照 `@Async` 方案：它们解决的“异步点”其实不同

## 一句话总结

- `@Async`：让“某个监听器方法”异步
- multicaster async：让“事件分发过程”默认异步

