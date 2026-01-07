# 90：常见坑清单（Web MVC）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**90：常见坑清单（Web MVC）**
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

## F. 常见坑与边界

## 400/校验相关

- DTO 上写了约束注解，但 controller 入参没加 `@Valid`：校验不会触发。
- 400 不等于校验失败：也可能是 JSON 解析失败/绑定失败（建议把两类错误响应区分开）。

## `@WebMvcTest` 相关

- `@WebMvcTest` 只加载 Web 层：如果 controller 依赖 service/repository，通常需要 `@MockBean` 或显式 `@Import`。
- `@WebMvcTest` 的“更快”来自加载范围更小：如果你把太多东西 `@Import` 进来，它就不再快了。

## 404/路由相关

- 路由拼错：确认类级 `@RequestMapping` 与方法级 `@GetMapping/@PostMapping` 的组合。
- path variable 名称不匹配：`@PathVariable("id") Long id`

## 建议的排查顺序

1. 先用测试把“现象”固化（状态码 + 响应形状）
2. 再回到 controller / handler / advice 看“为什么”
3. 需要更接近真实链路时，再用 `@SpringBootTest(webEnvironment=RANDOM_PORT)`

## 对应 Lab（可运行）

- `BootWebMvcLabTest`
- `BootWebMvcSpringBootLabTest`

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebMvcLabTest` / `BootWebMvcSpringBootLabTest`

上一章：[part-02-view-mvc/03-error-pages-and-content-negotiation.md](../part-02-view-mvc/03-error-pages-and-content-negotiation.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[appendix/99-self-check.md](99-self-check.md)

<!-- BOOKIFY:END -->
