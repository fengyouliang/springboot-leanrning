# springboot-async-scheduling 文档

本模块聚焦 `@Async` 的代理心智模型、线程与执行器、异常传播、自调用陷阱，以及 `@Scheduled` 的基本语义。

## Start Here
- 导读：[part-00-guide/00-deep-dive-guide.md](part-00-guide/00-deep-dive-guide.md)

## Part 01 - Async & Scheduling（主线机制）
- 01 `@Async` 代理心智模型：[part-01-async-scheduling/01-async-proxy-mental-model.md](part-01-async-scheduling/01-async-proxy-mental-model.md)
- 02 Executor 与线程：[part-01-async-scheduling/02-executor-and-threading.md](part-01-async-scheduling/02-executor-and-threading.md)
- 03 异常：[part-01-async-scheduling/03-exceptions.md](part-01-async-scheduling/03-exceptions.md)
- 04 自调用陷阱：[part-01-async-scheduling/04-self-invocation.md](part-01-async-scheduling/04-self-invocation.md)
- 05 `@Scheduled` 基础：[part-01-async-scheduling/05-scheduling-basics.md](part-01-async-scheduling/05-scheduling-basics.md)

## Appendix
- 常见坑：[appendix/90-common-pitfalls.md](appendix/90-common-pitfalls.md)
- 自测题：[appendix/99-self-check.md](appendix/99-self-check.md)

## Labs & Exercises（最小可复现入口）
- Labs：`springboot-async-scheduling/src/test/java/com/learning/springboot/bootasyncscheduling/part01_async_scheduling/BootAsyncSchedulingLabTest.java`
- Exercises：`springboot-async-scheduling/src/test/java/com/learning/springboot/bootasyncscheduling/part00_guide/BootAsyncSchedulingExerciseTest.java`
