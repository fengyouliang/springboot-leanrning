# 00. 深挖指南：把 weaving 的“结论 → 实验 → 排障路径”跑通

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**00. 深挖指南：把 weaving 的“结论 → 实验 → 排障路径”跑通**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

本模块分两条线：

它们都属于 **AspectJ weaving**，与 `spring-core-aop`（Spring AOP 代理）是两个世界：

- Proxy：改调用链（必须走 proxy）
- Weaving：改字节码（不依赖 proxy）

---

## 1. 最短闭环：先跑测试

> 如果你在 IDE 单独跑 LTW 的某个测试，需要手动在 Run Configuration 里添加 `-javaagent:` 参数；命令行已由 surefire 自动处理。

---

## 2. LTW 的关键开关：`META-INF/aop.xml`

- **有没有 agent**：JVM 是否带 `-javaagent:aspectjweaver.jar`
- **有没有织入配置**：classpath 上是否存在 `META-INF/aop.xml`
- **织入范围对不对**：`<include within="...">` 是否覆盖到目标类

本模块的 `aop.xml` 放在：

---

## 3. CTW 的关键开关：构建期织入产物

CTW 的核心结论是：

> **不带 `-javaagent`，也能触发 advice**，因为目标类的字节码已经在构建期被改写。

因此 CTW 的排障路径通常是：

---

## 4. 你需要会的排障分流（最重要）

当你遇到“拦截没发生”的现象时，先问自己一句话：

1. 我是在 proxy 世界，还是 weaving 世界？
2. 如果是 proxy：是不是没走 proxy（call path 问题）？
3. 如果是 weaving：
   - LTW：是不是没带 agent / 没加载到 aop.xml / include 范围没覆盖？
   - CTW：是不是构建没织入 / 织入范围不对 / 跑的是未织入 class？

---

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`AspectjCtwLabTest` / `AspectjLtwLabTest`
- 建议命令：`mvn -pl spring-core-aop-weaving test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

> 验证入口（可跑）：
> - `AspectjLtwLabTest`
> - `AspectjCtwLabTest`

1. **LTW（Load-Time Weaving）**：通过 `-javaagent` 在类加载时织入（更接近“运行时开关”）
2. **CTW（Compile-Time Weaving）**：通过编译期织入（更接近“构建期产物”）

```bash
mvn -pl spring-core-aop-weaving test
```

你会看到两套 tests 都跑：

- `*Ltw*Test`：带 `-javaagent:.../aspectjweaver.jar`
- `*Ctw*Test`：不带 `-javaagent`（用于证明 CTW 独立于 agent）

LTW 是否生效，最常见的判断点不是“有没有写 @Aspect”，而是：

- `src/test/resources/META-INF/aop.xml`

因此它只影响测试运行，不影响你 `spring-boot:run` 的默认启动。

- 确认构建是否真的执行了织入（插件是否生效）
- 确认织入范围是否正确（只织入目标包/目标类）
- 确认运行时 classpath 上使用的是“织入后的 class”（而不是未织入版本）

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

下一章：[`01-proxy-vs-weaving`](../part-01-mental-model/01-proxy-vs-weaving.md)

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`AspectjCtwLabTest` / `AspectjLtwLabTest`

上一章：[Docs TOC](../README.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[01-proxy-vs-weaving](../part-01-mental-model/01-proxy-vs-weaving.md)

<!-- BOOKIFY:END -->
