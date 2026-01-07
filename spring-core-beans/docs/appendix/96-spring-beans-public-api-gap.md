# 96 spring beans public api gap

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**96 spring beans public api gap**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

<!--
⚠️ GENERATED FILE - 请勿手工编辑。
- Generator: scripts/generate-spring-beans-public-api-index.py
- Source: /home/feng/.m2/repository/org/springframework/spring-beans/6.2.15/spring-beans-6.2.15-sources.jar
- Generated at: 2026-01-06 13:58:36
-->

# 96. spring-beans Public API 覆盖差距（Gap）清单（Spring Framework 6.2.15）

本文件用于把“还缺什么”变成显式清单，配合：
- 索引：`/home/feng/code/project/springboot-leanrning/spring-core-beans/docs/appendix/95-spring-beans-public-api-index.md`
- 分批补齐策略：HelloAGENTS 方案包 task.md

---
## 概览

## 结论

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreBeansBuiltInFactoryBeansLabTest`
- 建议命令：`mvn -pl spring-core-beans test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

> 验证入口（可跑）：`SpringCoreBeansBuiltInFactoryBeansLabTest`

- 总 public 顶层类型（按 sources.jar 统计）：**320**
- 未映射（unmapped）：**0**
- partial 覆盖（需要后续补齐/深化）：**0**
- 索引指向缺失的 chapter：**0**
- 索引指向缺失的 lab：**0**

- 当前索引规则无缺口（0 unmapped），且索引指向的 chapter/lab 均存在。

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreBeansBuiltInFactoryBeansLabTest`

上一章：[95. spring-beans Public API 索引（按类型检索）](95-spring-beans-public-api-index.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[97. Explore/Debug 用例（可选启用，不影响默认回归）](97-explore-debug-tests.md)

<!-- BOOKIFY:END -->
