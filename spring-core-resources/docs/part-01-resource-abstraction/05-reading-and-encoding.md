# 05. 读取资源：InputStream、编码与“可观察性”

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**05. 读取资源：InputStream、编码与“可观察性”**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

资源读取看起来简单，但学习阶段建议你建立两个习惯：

1) 始终明确编码（尤其文本）  
2) 把错误转换成“更好理解的异常/提示”

- `resource.getInputStream()`
- 读 bytes
- 用 `StandardCharsets.UTF_8` 构建字符串

看 `ResourceReadingService#readClasspathText`：

`Resource#getDescription()` 很有用：

- 它能告诉你这个 resource 是从哪里来的
- 在 classpath/jar 相关问题里，description 往往比 path 更可信

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreResourcesMechanicsLabTest`
- 建议命令：`mvn -pl spring-core-resources test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 在本模块如何验证“读取方式”

看 `SpringCoreResourcesMechanicsLabTest#classpathResourceCanBeReadAsBytes`：

- 把 `IOException` 包成 `UncheckedIOException`（学习阶段更容易写 tests）

## Debug/观察建议

验证入口：`SpringCoreResourcesMechanicsLabTest#resourceDescriptionsHelpWithDebugging`

## F. 常见坑与边界

### 坑点 1：依赖平台默认编码读取文本，导致“本地正常、线上乱码”

- Symptom：在某台机器上中文/特殊字符乱码，换环境又正常
- Root Cause：平台默认编码不可控；文本读取必须显式指定 charset
- Verification：`SpringCoreResourcesMechanicsLabTest#classpathResourceCanBeReadAsBytes`（bytes → UTF-8 text）
- Fix：读取文本时始终显式指定 `StandardCharsets.UTF_8`；并把 `Resource#getDescription()` 打进异常或日志，提升可观察性

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreResourcesMechanicsLabTest`

上一章：[04-exists-and-handles](04-exists-and-handles.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[06-jar-vs-filesystem](06-jar-vs-filesystem.md)

<!-- BOOKIFY:END -->
