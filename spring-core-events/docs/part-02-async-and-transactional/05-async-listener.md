# 05. 异步监听器：`@Async` 生效需要什么？线程会怎么变？

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**05. 异步监听器：`@Async` 生效需要什么？线程会怎么变？**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

异步监听器的目标是把“监听器逻辑”从发布方的线程里拆出去：

- 发布方更快返回
- 监听器在另一个线程执行（通常由线程池提供）

## 关键点：`@Async` 不是“写了就生效”

### 1) 开启 `@EnableAsync`：异步才会生效

看 `asyncListenerRunsOnDifferentThread_whenEnableAsyncIsOn`：

- 配置类加 `@EnableAsync`
- 提供 `ThreadPoolTaskExecutor`，并设置 `threadNamePrefix`
- 断言线程名以 `events-async-` 开头

### 2) 不开启 `@EnableAsync`：`@Async` 会被忽略

看 `asyncAnnotationIsIgnored_withoutEnableAsync`：

- 同样的 listener 方法加了 `@Async`
- 但由于没有 `@EnableAsync`，最终还是在当前线程执行

## 你应该得到的结论

- “我用了 `@Async`，为什么还是同步？”
  - 多半是没启用 async（或线程池没配置）

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreEventsMechanicsLabTest`
- 建议命令：`mvn -pl spring-core-events test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

验证入口：`SpringCoreEventsMechanicsLabTest`

- 异步不是事件的“默认能力”，而是另一个拦截器机制（`@Async`）叠加出来的
- 学习阶段最好用“线程名断言”来验证异步（比看日志稳定）

## F. 常见坑与边界

## 常见误区

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreEventsMechanicsLabTest`

上一章：[04-sync-and-exceptions](../part-01-event-basics/04-sync-and-exceptions.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[06-async-multicaster](06-async-multicaster.md)

<!-- BOOKIFY:END -->
