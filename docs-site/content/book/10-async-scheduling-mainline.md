# 第 10 章：Async/Scheduling 主线

这一章解决的问题是：**为什么加上 `@Async` 方法就不在当前线程跑了、为什么定时任务会并发/堆积、线程池怎么选**。

---

## 主线（按时间线顺读）

1. `@Async` 的本质仍是代理：调用边界进入异步拦截器
2. 任务被提交到 `TaskExecutor`（线程池）执行
3. 异步返回值语义：`void`/`Future`/`CompletableFuture` 的差异
4. Scheduling：`@Scheduled` 把任务按 cron/fixedDelay/fixedRate 交给 scheduler
5. 常见坑：线程池默认值、异常吞掉、上下文传播（ThreadLocal）、测试中如何稳定断言异步

---

## 深挖入口（模块 docs）

- 模块目录页：[`springboot-async-scheduling/docs/README.md`](../springboot-async-scheduling/docs/README.md)
- 模块主线时间线（含可跑入口）：[`springboot-async-scheduling/docs/part-00-guide/03-mainline-timeline.md`](../springboot-async-scheduling/docs/part-00-guide/03-mainline-timeline.md)

---

## 下一章怎么接

异步的另一种常见形态是“发布事件”：我们进入 Events 主线。

- 下一章：[第 11 章：Events 主线](11-events-mainline.md)

