# 01：`@Cacheable` 最小闭环

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**01：`@Cacheable` 最小闭环**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

## 你应该观察到什么

- 同一个 key（例如 name=alice）只计算一次，后续从 cache 直接返回
- 不同 key 会命中不同 entry

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootCacheLabTest`
- 建议命令：`mvn -pl springboot-cache test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 实验入口

- `springboot-cache/src/test/java/com/learning/springboot/bootcache/part01_cache/BootCacheLabTest.java`
  - `cacheableCachesResultForSameKey`
  - `cacheableUsesDifferentEntriesForDifferentKeys`

## F. 常见坑与边界

### 坑点 1：把 `@Cacheable` 方法当成“每次都会执行”，忽略了命中短路

- Symptom：你在方法里写了日志/计数/副作用，以为每次调用都会发生，但线上只发生一次或发生次数异常
- Root Cause：`@Cacheable` 命中后会短路方法执行（直接返回缓存值）
- Verification：`BootCacheLabTest#cacheableCachesResultForSameKey`（invocationCount 作为证据）
- Fix：缓存方法尽量保持纯函数/无副作用；副作用需要单独设计，不要依赖“方法一定会被调用”

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootCacheLabTest`
- Test file：`springboot-cache/src/test/java/com/learning/springboot/bootcache/part01_cache/BootCacheLabTest.java`

上一章：[part-00-guide/00-deep-dive-guide.md](../part-00-guide/00-deep-dive-guide.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-01-cache/02-cacheput-and-evict.md](02-cacheput-and-evict.md)

<!-- BOOKIFY:END -->
