# 00 - Deep Dive Guide（springboot-web-mvc）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**00 - Deep Dive Guide（springboot-web-mvc）**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

- （本章主线内容暂以契约骨架兜底；建议结合源码与测试用例补齐主线解释。）

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootWebMvcLabTest` / `BootWebMvcSpringBootLabTest`
- 建议命令：`mvn -pl springboot-web-mvc test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 推荐学习目标
1. 能说清一次请求在 MVC 中的关键阶段：handler mapping → argument resolve/binding → validation → exception → response
2. 能写出“可复现”的错误塑形与异常处理策略，并用测试断言锁住行为
3. 能解释 Filter/Interceptor 的顺序与影响范围

## 如何跑实验
- 运行本模块测试：`mvn -pl springboot-web-mvc test`

## 对应 Lab（可运行）

- `BootWebMvcLabTest`
- `BootWebMvcSpringBootLabTest`
- `BootWebMvcExerciseTest`

## F. 常见坑与边界

## 推荐阅读顺序
1. [01-validation-and-error-shaping](../part-01-web-mvc/01-validation-and-error-shaping.md)
2. [02-exception-handling](../part-01-web-mvc/02-exception-handling.md)
3. [03-binding-and-converters](../part-01-web-mvc/03-binding-and-converters.md)
4. [04-interceptor-and-filter-ordering](../part-01-web-mvc/04-interceptor-and-filter-ordering.md)
5. [01-thymeleaf-and-view-resolver](../part-02-view-mvc/01-thymeleaf-and-view-resolver.md)
6. [02-form-binding-validation-prg](../part-02-view-mvc/02-form-binding-validation-prg.md)
7. [03-error-pages-and-content-negotiation](../part-02-view-mvc/03-error-pages-and-content-negotiation.md)
8. [90-common-pitfalls](../appendix/90-common-pitfalls.md)
9. [99-self-check](../appendix/99-self-check.md)

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebMvcLabTest` / `BootWebMvcSpringBootLabTest`
- Exercise：`BootWebMvcExerciseTest`

上一章：[Docs TOC](../README.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-01-web-mvc/01-validation-and-error-shaping.md](../part-01-web-mvc/01-validation-and-error-shaping.md)

<!-- BOOKIFY:END -->
