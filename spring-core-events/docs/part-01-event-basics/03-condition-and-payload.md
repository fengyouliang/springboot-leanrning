# 03. condition 与 payload：监听器为什么能“按条件触发”甚至接收普通对象？

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**03. condition 与 payload：监听器为什么能“按条件触发”甚至接收普通对象？**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

Spring 事件有两个很实用的能力：

1) **按条件触发**：只在满足某些条件时才执行监听器  
2) **payload 事件**：发布普通对象，也可以被 `@EventListener` 接住

## 1) 条件触发：`@EventListener(condition = "...")`

本模块里条件是：

- `#event.username().startsWith('A')`

因此：

- `Bob` 不触发
- `Alice` 触发

学习建议：

- 条件尽量保持简单可读（学习阶段尤其重要）
- 把“条件”当作一种轻量的过滤器，而不是把复杂业务规则塞进 SpEL

## 2) payload：发布 String 也能被监听器接到

核心规则很简单：

> 监听方法参数的类型，与 publish 的对象类型匹配即可。

本模块里：

- publish：`eventPublisher.publishEvent("hello")`
- listen：`public void on(String payload)`

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreEventsLabTest`
- 建议命令：`mvn -pl spring-core-events test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

验证入口：`SpringCoreEventsLabTest#conditionalEventListenerOnlyRunsWhenConditionMatches`

验证入口：`SpringCoreEventsLabTest#publishingPlainObjectsAlsoWorks_asPayloadEvents`

- condition 让你更容易写“机制实验”（同一个发布动作，用不同输入触发不同监听器）
- payload 让事件机制更轻量：不一定每个动作都要建一个 event class

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

## 一句话总结

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreEventsLabTest`

上一章：[02-multiple-listeners-and-order](02-multiple-listeners-and-order.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[04-sync-and-exceptions](04-sync-and-exceptions.md)

<!-- BOOKIFY:END -->
