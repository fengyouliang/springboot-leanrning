# 04. Dirty Checking（脏检查）：为什么改字段不用 save 也能落库？

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**04. Dirty Checking（脏检查）：为什么改字段不用 save 也能落库？**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

这是 JPA 最“神奇”但也最容易被误用的机制：脏检查。

## 现象

- 你拿到一个 managed entity
- 修改它的字段
- 没有再调用 `save()`
- flush/commit 之后，数据库值变了

1. `Book saved = repository.save(...)`
2. `saved.changeAuthor("B")`（只改字段）
3. `entityManager.flush()`（触发同步）
4. `entityManager.clear()`（清掉上下文，避免“一级缓存假象”）
5. 重新 `findById` 并断言 author 已经变成 B

## 你应该得到的结论

1. dirty checking 的前提是：实体必须是 managed（受 persistence context 管理）
2. flush/commit 是“把变化写进 DB”的时机
3. 清理 context（`clear()`）能避免你误把“一级缓存”当成“数据库状态”

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootDataJpaLabTest`
- 建议命令：`mvn -pl springboot-data-jpa test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 在本模块如何验证

看 `BootDataJpaLabTest#dirtyCheckingPersistsChangesOnFlush`：

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootDataJpaLabTest`

上一章：[part-01-data-jpa/03-flush-and-visibility.md](03-flush-and-visibility.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-01-data-jpa/05-fetching-and-n-plus-one.md](05-fetching-and-n-plus-one.md)

<!-- BOOKIFY:END -->
