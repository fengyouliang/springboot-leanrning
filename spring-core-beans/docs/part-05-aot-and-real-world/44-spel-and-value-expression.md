# 44. SpEL 与 `@Value("#{...}")`：表达式解析链路

很多人知道 `@Value("${...}")`，但对 `@Value("#{...}")`（SpEL）没有清晰边界，导致两类问题：

1) 面试时答不清：`${...}` 与 `#{...}` 的链路差异是什么？  
2) 生产排障时误判：值注入失败到底是“占位符解析问题”、还是“表达式计算问题”、还是“类型转换问题”？

这一章的目标是把它拆开成可验证链路。

---

## 1. 结论先行：`${...}` 与 `#{...}` 分别做什么？

- `${...}`：占位符解析（通常来自 Environment / PropertySources）
- `#{...}`：SpEL 表达式解析（可以计算、可以引用 bean、可以调用方法）

但它们最终都会回到同一条主线：

> **解析出字符串/对象 → 再做类型转换 → 注入到目标类型**

对照阅读：

- [34. @Value 占位符解析：strict vs non-strict](../part-04-wiring-and-boundaries/34-value-placeholder-resolution-strict-vs-non-strict.md)
- [36. 类型转换：BeanWrapper / ConversionService](../part-04-wiring-and-boundaries/36-type-conversion-and-beanwrapper.md)

---

## 2. 复现入口（可运行）

本模块提供一个最小 SpEL 实验，覆盖两个你最需要的能力：

1) SpEL 能引用容器里的 bean（`@beanName`）
2) SpEL 的结果会进入类型转换（例如返回 `"42"` 仍可注入到 `int`）

入口测试：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansSpelValueLabTest.java`

推荐运行命令：

```bash
mvn -pl spring-core-beans -Dtest=SpringCoreBeansSpelValueLabTest test
```

---

## 3. 源码 / 断点建议（从“值注入失败”到“根因”）

把链路分成三段打断点，排障会非常快：

1) `AutowiredAnnotationBeanPostProcessor#postProcessProperties`（识别 `@Value` 的入口）
2) `AbstractBeanFactory#resolveEmbeddedValue`（`${...}` / `#{...}` 的字符串解析入口）
3) 类型转换（取决于注入点）：
   - `BeanWrapperImpl#setPropertyValue`（属性填充）
   - 或 `TypeConverter#convertIfNecessary`（注入点转换）

当你需要进一步看 SpEL 的执行细节时，再扩展到表达式解析器内部：

- `StandardBeanExpressionResolver#evaluate`（把 `#{...}` 交给 SpEL 计算）
- `SpelExpression#getValue` / `ExpressionParser#parseExpression`（表达式解析与求值）

建议观察点（断点时优先盯这些变量）：

- 原始字符串：到底是 `"${...}"` 还是 `"#\{...\}"`（两条链路的入口信号不同）
- `BeanExpressionContext`：SpEL 能不能访问到你期望的 bean（例如 `@beanName`）
- 最终值类型：SpEL 计算结果是 `String` 还是 `Integer`/对象（决定后续转换是否必需）

---

## 4. 常见误区

1) **误区：@Value 就是读 Environment**
   - `${...}` 的默认行为确实常来自 Environment resolver，但 `#{...}` 属于表达式系统。
2) **误区：SpEL 只会返回字符串**
   - SpEL 可以返回任何对象（包括 bean 引用结果）；最终是否需要转换取决于注入点类型。

---

## 5. 小结与下一章预告

你应该能回答：

- `${...}` 与 `#{...}` 的职责边界是什么？
- 值注入失败时，你怎么用 3 个断点把问题收敛到“解析 vs 计算 vs 转换”？

下一章我们补齐依赖注入体系的“自定义能力”：

- 自定义 Qualifier（meta-annotation）如何参与候选收敛

---

上一章：[43. 容器外对象注入：AutowireCapableBeanFactory](43-autowirecapablebeanfactory-external-objects.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[45. 自定义 Qualifier：meta-annotation 与候选收敛](45-custom-qualifier-meta-annotation.md)
