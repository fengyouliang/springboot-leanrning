# 主线时间线：Spring Boot Async & Scheduling

!!! summary
    - 这一模块关注：@Async/@Scheduled 如何通过代理与调度器把“并发执行”织入方法调用，以及线程池/异常/自调用的边界。
    - 读完你应该能复述：**方法调用 → 代理拦截 → 提交到 Executor → 执行/异常处理** 这一条主线（以及 scheduling 的触发链）。
    - 推荐顺序：先读《深挖导读》→ 本章 → Part 01 顺读 → 附录排坑。

!!! example "建议先跑的 Lab（把时间线变成证据）"

    - Lab：`BootAsyncSchedulingLabTest`

## 在 Spring 主线中的位置

- 异步能力依赖 AOP 代理：很多“不生效”的问题，本质是“没代理上”或“自调用绕过代理”。
- 调度是“按时间触发的入口”：问题常见于线程池饱和、异常吞掉、并发重入。

## 主线时间线（建议顺读）

1. 先建立心智模型：@Async 到底在代理链里做了什么
   - 阅读：[01. @Async 心智模型](../part-01-async-scheduling/01-async-proxy-mental-model.md)
2. 线程模型：Executor 选择、线程命名、上下文传递
   - 阅读：[02. Executor 与线程模型](../part-01-async-scheduling/02-executor-and-threading.md)
3. 异常处理：为什么你“看不到异常”，应该如何验证
   - 阅读：[03. 异常处理](../part-01-async-scheduling/03-exceptions.md)
4. 最常见坑：self-invocation（自调用）导致 @Async 不生效
   - 阅读：[04. self-invocation](../part-01-async-scheduling/04-self-invocation.md)
5. 调度主线：@Scheduled 的触发与执行边界
   - 阅读：[05. @Scheduled 基础](../part-01-async-scheduling/05-scheduling-basics.md)

## 排坑与自检

- 常见坑：[90-common-pitfalls.md](../appendix/90-common-pitfalls.md)
- 自检：[99-self-check.md](../appendix/99-self-check.md)
