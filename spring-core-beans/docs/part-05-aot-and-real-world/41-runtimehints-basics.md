# 41. RuntimeHints 入门：把构建期契约跑通

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**41. RuntimeHints 入门：把构建期契约跑通**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

这一章的目标只有一个：把 RuntimeHints 从“听说过”变成“能断言证明”。

> **你不需要先会构建 native image，也能理解 RuntimeHints。**  
> 因为 RuntimeHints 本质上是“契约数据结构”：你能在 JVM 测试里构造它、注册它、断言它。

---

## 1. RuntimeHints 是什么？

你可以把 RuntimeHints 理解为：

Spring 的 hints 典型包括：

- Reflection hints：哪些类/构造器/方法/字段需要可反射访问
- Proxy hints：哪些接口/类需要生成代理
- Resource hints：哪些 classpath 资源需要被打包

---

## 2. 最小实践：RuntimeHintsRegistrar

学习阶段最推荐的入口是：

- `RuntimeHintsRegistrar`

它表达了一个非常工程化的契约：

---

- **没有注册 hints**：断言 hints 不命中
- **注册了 hints**：断言 hints 命中

入口测试：

---

- `RuntimeHintsRegistrar#registerHints`：观察你往 `RuntimeHints` 里写了什么

---

---

你应该能回答：

- 为什么 RuntimeHints 是 AOT/Native 的核心契约？
- 你如何用一个 JVM 单测证明 hints “有/没有”？

- XML → BeanDefinitionReader → BeanDefinition 元信息/错误分型

---

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreBeansAotRuntimeHintsLabTest`
- 建议命令：`mvn -pl spring-core-beans test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

- “在 AOT/Native 下仍然需要的运行期能力清单”
- 这些能力必须在构建期声明出来（否则 native image 里可能缺少元信息）

> “我负责把某个模块/某个能力运行所需的 hints 注册进去。”

## 3. 复现入口（可运行）

本模块提供了最小对照实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansAotRuntimeHintsLabTest.java`

推荐运行命令：

```bash
mvn -pl spring-core-beans -Dtest=SpringCoreBeansAotRuntimeHintsLabTest test
```

## 4. Debug / 断点建议

建议先把断点打在你最容易控制的地方：

当你需要更“体系化”的视角（例如：Spring Boot 的 AOT 流程如何收集多个 hints 来源），再把断点扩展到 AOT 生成器与处理器链。

1) **误区：RuntimeHints 是运行时才生效**
   - 更准确：RuntimeHints 是构建期用于生成/裁剪元数据的输入，运行时只是享受结果。
2) **误区：只要有反射就一定需要 hints**
   - JVM 模式下不一定；AOT/Native 下通常必须显式声明（否则运行期信息不可得）。

下一章开始，我们把“真实世界里容易被忽略的机制”补齐成可运行实验：

## F. 常见坑与边界

## 5. 常见误区（面试/排障高频）

## G. 小结与下一章

## 6. 小结

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreBeansAotRuntimeHintsLabTest`
- Test file：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansAotRuntimeHintsLabTest.java`

上一章：[40. AOT / Native 总览：为什么“JVM 能跑”不等于“Native 能跑”](40-aot-and-native-overview.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[42. XML → BeanDefinitionReader：定义层解析与错误分型](42-xml-bean-definition-reader.md)

<!-- BOOKIFY:END -->
