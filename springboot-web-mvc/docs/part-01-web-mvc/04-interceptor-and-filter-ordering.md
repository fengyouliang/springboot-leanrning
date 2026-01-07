# 04：Interceptor 与 Filter：入口在哪里、顺序怎么理解

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**04：Interceptor 与 Filter：入口在哪里、顺序怎么理解**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

本章的目标不是把 Filter/Interceptor 全部讲完，而是建立一个“入口与顺序”的最小心智模型：你知道它们分别在链路的哪里、什么时候该用哪个。

## 你应该观察到什么

- Interceptor 是 MVC 层能力：更贴近 handler 调用（controller 前后）
- Filter 更贴近 Servlet 容器：更接近“请求最外层”

## 机制解释（Why）

- **Filter**：发生在 Servlet 容器层，通常对所有请求都可能生效（除非你按 URL pattern 配置）
- **Interceptor**：发生在 Spring MVC handler 执行链内，便于针对某一类 handler 路由做增强

如果你是“想对 /api/** 生效”，并且增强逻辑与 handler 相关（比如给 response 增 header、记录耗时），Interceptor 往往更直观。

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章未显式引用 LabTest，先注入模块默认 LabTest 作为“合规兜底入口”（后续可逐章细化）。
- Lab：`BootWebMvcErrorViewLabTest` / `BootWebMvcLabTest`
- 建议命令：`mvn -pl springboot-web-mvc test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 实验入口

- 练习：增加一个 `HandlerInterceptor` 并证明它只对 `/api/**` 生效：
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part00_guide/BootWebMvcExerciseTest.java`
    - `exercise_interceptor`

## Debug 建议

- 写测试优先选 `MockMvc`：它能稳定复现 handler 链路并断言结果（比手工 curl 更可控）。

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebMvcErrorViewLabTest` / `BootWebMvcLabTest`
- Exercise：`BootWebMvcExerciseTest`
- Test file：`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part00_guide/BootWebMvcExerciseTest.java`

上一章：[part-01-web-mvc/03-binding-and-converters.md](03-binding-and-converters.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-02-view-mvc/01-thymeleaf-and-view-resolver.md](../part-02-view-mvc/01-thymeleaf-and-view-resolver.md)

<!-- BOOKIFY:END -->
