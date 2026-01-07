# 90. 常见坑清单（LTW/CTW）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**90. 常见坑清单（LTW/CTW）**
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
- Lab：`AspectjCtwLabTest` / `AspectjLtwLabTest`
- 建议命令：`mvn -pl spring-core-aop-weaving test`（或在 IDE 直接运行上面的测试类）

## F. 常见坑与边界

> 验证入口（可跑）：`AspectjLtwLabTest` / `AspectjCtwLabTest`

## A. LTW 常见坑

- 只写了 `@Aspect`，但 JVM 没带 `-javaagent`（永远不生效）
- JVM 带了 `-javaagent`，但 classpath 上没有 `META-INF/aop.xml`
- `aop.xml` 有，但 `<include within="...">` 没覆盖到目标类（或包名写错）
- IDE 运行配置与 Maven 不一致：命令行能复现、IDE 不能（或反之）

## B. CTW 常见坑

- 插件没生效：看似配置了，但构建根本没执行织入
- 织入范围太大：导致“所有类都被织入”，排障噪声爆炸
- 织入范围太小：误判“CTW 不生效”
- 多套 weaving 同时存在（LTW + CTW）但范围没隔离：造成重复织入/重复触发

## C. `call` 误判

- 你以为 `call` 会拦截“方法体执行”，但它拦的是“调用点”
- 当你把 `call` 用在库代码/框架代码上时，很容易造成不可控影响（因为调用点太多）

## D. 建议的排障顺序（速查）

1. 先判断：proxy 还是 weaving？
2. LTW：确认 `-javaagent` → 确认 `aop.xml` → 确认 include 范围
3. CTW：确认构建是否织入 → 确认织入范围 → 确认运行时使用的是织入产物

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`AspectjCtwLabTest` / `AspectjLtwLabTest`

上一章：[04-join-point-cookbook](../part-04-join-points/04-join-point-cookbook.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[99-self-check](99-self-check.md)

<!-- BOOKIFY:END -->
