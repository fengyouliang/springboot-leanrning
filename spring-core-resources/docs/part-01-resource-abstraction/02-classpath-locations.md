# 02. classpath 路径：`classpath:data/x` vs `classpath:/data/x` 有什么区别？

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**02. classpath 路径：`classpath:data/x` vs `classpath:/data/x` 有什么区别？**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

- 有的人写 `classpath:data/hello.txt`
- 有的人写 `classpath:/data/hello.txt`

- `readsClasspathResourceContent`：`classpath:data/hello.txt`
- `supportsLeadingSlashInClasspathLocation`：`classpath:/data/hello.txt`

两者都能读到 `Hello from classpath`。

## 你应该得到的结论

- 学习阶段你可以把它们当作等价写法（在常见 classpath 场景下）
- 更重要的是：别把 classpath 资源当作 `File` 路径使用（尤其是打包成 jar 后）

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreResourcesLabTest`
- 建议命令：`mvn -pl spring-core-resources test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 在本模块如何验证

看 `SpringCoreResourcesLabTest`：

## F. 常见坑与边界

学习阶段最容易踩的坑之一是 classpath 路径写法不一致：

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreResourcesLabTest`

上一章：[01-resource-abstraction](01-resource-abstraction.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[03-classpath-star-and-pattern](03-classpath-star-and-pattern.md)

<!-- BOOKIFY:END -->
