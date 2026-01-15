# 90. 常见坑清单（建议反复对照）

## 导读

- 本章主题：**90. 常见坑清单（建议反复对照）**
- 阅读方式建议：先看“本章要点”，再沿主线阅读；需要时穿插源码/断点，最后跑通实验闭环。

!!! summary "本章要点"

    - 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
    - 如果只看一眼：请先跑一次本章的最小实验，再回到主线对照阅读。


!!! example "本章配套实验（先跑再读）"

    - Lab：`SpringCoreResourcesLabTest` / `SpringCoreResourcesMechanicsLabTest`

## 机制主线

- （本章主线内容暂以契约骨架兜底；建议结合源码与测试用例补齐主线解释。）

## 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreResourcesLabTest` / `SpringCoreResourcesMechanicsLabTest`
- 建议命令：`mvn -pl spring-core-resources test`（或在 IDE 直接运行上面的测试类）

## 常见坑与边界

> 验证入口（可跑）：`SpringCoreResourcesLabTest` / `SpringCoreResourcesMechanicsLabTest`

## 坑 1：把 classpath 资源当成 File

- 现象：本地 OK，打包后失败
- 建议：优先 `getInputStream()`，不要依赖 `getFile()`

## 坑 2：以为 `getResource(...)` 会在不存在时返回 null

- 事实：它返回 handle，需要 `exists()` 判断（见 [04. exists-and-handles](../part-01-resource-abstraction/04-exists-and-handles.md)）

## 坑 3：pattern 扫描结果顺序不稳定导致 tests 抖动

- 建议：排序后再断言（本模块 service 已经这么做）

## 坑 4：忽略编码导致内容乱码

- 建议：读取文本时显式使用 UTF-8（见 [05. reading-and-encoding](../part-01-resource-abstraction/05-reading-and-encoding.md)）

## 坑 5：错误处理太粗糙

- 建议：区分“资源不存在”与“资源不可读”（Exercise 里会练）

## 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreResourcesLabTest` / `SpringCoreResourcesMechanicsLabTest`

上一章：[06-jar-vs-filesystem](../part-01-resource-abstraction/06-jar-vs-filesystem.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[99-self-check](99-self-check.md)

<!-- BOOKIFY:END -->
