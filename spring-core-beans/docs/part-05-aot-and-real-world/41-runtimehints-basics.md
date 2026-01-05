# 41. RuntimeHints 入门：把构建期契约跑通

这一章的目标只有一个：把 RuntimeHints 从“听说过”变成“能断言证明”。

> **你不需要先会构建 native image，也能理解 RuntimeHints。**  
> 因为 RuntimeHints 本质上是“契约数据结构”：你能在 JVM 测试里构造它、注册它、断言它。

---

## 1. RuntimeHints 是什么？

你可以把 RuntimeHints 理解为：

- “在 AOT/Native 下仍然需要的运行期能力清单”
- 这些能力必须在构建期声明出来（否则 native image 里可能缺少元信息）

Spring 的 hints 典型包括：

- Reflection hints：哪些类/构造器/方法/字段需要可反射访问
- Proxy hints：哪些接口/类需要生成代理
- Resource hints：哪些 classpath 资源需要被打包

---

## 2. 最小实践：RuntimeHintsRegistrar

学习阶段最推荐的入口是：

- `RuntimeHintsRegistrar`

它表达了一个非常工程化的契约：

> “我负责把某个模块/某个能力运行所需的 hints 注册进去。”

---

## 3. 复现入口（可运行）

本模块提供了最小对照实验：

- **没有注册 hints**：断言 hints 不命中
- **注册了 hints**：断言 hints 命中

入口测试：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansAotRuntimeHintsLabTest.java`

推荐运行命令：

```bash
mvn -pl spring-core-beans -Dtest=SpringCoreBeansAotRuntimeHintsLabTest test
```

---

## 4. Debug / 断点建议

建议先把断点打在你最容易控制的地方：

- `RuntimeHintsRegistrar#registerHints`：观察你往 `RuntimeHints` 里写了什么

当你需要更“体系化”的视角（例如：Spring Boot 的 AOT 流程如何收集多个 hints 来源），再把断点扩展到 AOT 生成器与处理器链。

---

## 5. 常见误区（面试/排障高频）

1) **误区：RuntimeHints 是运行时才生效**
   - 更准确：RuntimeHints 是构建期用于生成/裁剪元数据的输入，运行时只是享受结果。
2) **误区：只要有反射就一定需要 hints**
   - JVM 模式下不一定；AOT/Native 下通常必须显式声明（否则运行期信息不可得）。

---

## 6. 小结

你应该能回答：

- 为什么 RuntimeHints 是 AOT/Native 的核心契约？
- 你如何用一个 JVM 单测证明 hints “有/没有”？

下一章开始，我们把“真实世界里容易被忽略的机制”补齐成可运行实验：

- XML → BeanDefinitionReader → BeanDefinition 元信息/错误分型

---

上一章：[40. AOT / Native 总览：为什么“JVM 能跑”不等于“Native 能跑”](40-aot-and-native-overview.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[42. XML → BeanDefinitionReader：定义层解析与错误分型](42-xml-bean-definition-reader.md)

