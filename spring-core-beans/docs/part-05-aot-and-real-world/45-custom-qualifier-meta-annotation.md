# 45. 自定义 Qualifier：meta-annotation 与候选收敛

当你进入真实项目，`@Qualifier("beanName")` 常常不够用：

- 你希望限定条件有“业务语义”（例如 `@Cn` / `@Internal` / `@ReadOnly`）
- 你希望团队统一约束（避免到处写字符串 beanName）

这就需要你理解：**Qualifier 的本质是“候选收敛规则”**，而不是“改名”。

---

## 1. 结论先行：自定义 Qualifier 的本质

自定义 Qualifier 的做法通常是：

1) 定义一个注解（例如 `@Cn`）
2) 用 `@Qualifier` 做 meta-annotation
3) 在候选 bean 上标注 `@Cn`（作为候选元数据）
4) 在注入点也标注 `@Cn`（作为收敛条件）

因此你应该能把它放回依赖解析主线：

- 候选收集：`findAutowireCandidates`
- 候选收敛：`determineAutowireCandidate`
- Qualifier 匹配：`QualifierAnnotationAutowireCandidateResolver#isAutowireCandidate`

对照阅读：

- [03. 依赖注入解析：类型/名称/@Qualifier/@Primary](../part-01-ioc-container/03-dependency-injection-resolution.md)
- [33. 候选选择与优先级：@Primary/@Priority/@Order 的边界](../part-04-wiring-and-boundaries/33-autowire-candidate-selection-primary-priority-order.md)

---

## 2. 复现入口（可运行）

本模块提供一个最小实验：

- 两个同类型候选（两个实现）
- 通过自定义 Qualifier 把候选收敛到 1 个

入口测试：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansCustomQualifierLabTest.java`

推荐运行命令：

```bash
mvn -pl spring-core-beans -Dtest=SpringCoreBeansCustomQualifierLabTest test
```

---

## 3. Debug / 断点建议

只需要 2 个断点，你就能在真实项目里解释“为什么注入的是它”：

- `DefaultListableBeanFactory#findAutowireCandidates`（候选集合）
- `QualifierAnnotationAutowireCandidateResolver#isAutowireCandidate`（Qualifier 匹配过滤）

如果你要解释最终选中规则：

- `DefaultListableBeanFactory#determineAutowireCandidate`

---

## 4. 常见误区

1) **误区：自定义 Qualifier = 更好的 @Primary**
   - `@Primary` 是“默认胜出者”，自定义 Qualifier 是“按语义显式选择”，适用场景不同。
2) **误区：把 Qualifier 当作 beanName**
   - Qualifier 是过滤条件，beanName 只是可能参与收敛的一种信号。

---

## 5. 小结

你应该能回答：

- 自定义 Qualifier 是如何参与候选收敛的？
- 你会在哪两个方法下断点证明“候选集合如何被过滤”？

Part 05 到这里结束。下一步进入复盘与自测：

- [90. 常见坑清单（建议反复对照）](../appendix/90-common-pitfalls.md)

---

上一章：[44. SpEL 与 @Value(\"#{...}\")：表达式解析链路](44-spel-and-value-expression.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[90. 常见坑清单（建议反复对照）](../appendix/90-common-pitfalls.md)

