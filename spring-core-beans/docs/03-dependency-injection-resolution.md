# 03. 依赖注入解析：类型/名称/@Qualifier/@Primary

这一章回答：**当你写下 `private final X x;`，Spring 到底是怎么找到并注入那个 `X` 的？**

在学习阶段，建议把注入问题拆成两类：

1) **有没有候选**（NoSuchBeanDefinition）
2) **候选太多怎么选**（NoUniqueBeanDefinition）

## 1. 本模块里的最小例子：两个 `TextFormatter`

代码位置：

- 接口：`src/main/java/com/learning/springboot/springcorebeans/TextFormatter.java`
- 实现：
  - `UpperCaseTextFormatter`（bean name：`upperFormatter`）
  - `LowerCaseTextFormatter`（bean name：`lowerFormatter`）
- 注入点：`FormattingService`

`FormattingService` 的构造器是：

```java
public FormattingService(@Qualifier("upperFormatter") TextFormatter textFormatter) { ... }
```

它解决的是一个经典问题：**同一类型有多个 Bean，按类型注入会歧义**。

## 2. Spring 的候选选择：先收集，再缩小

在高层层面，可以这样理解：

1) 先按“类型”找候选（所有 `TextFormatter`）
2) 根据限定条件缩小候选
   - `@Qualifier`：显式指定（最常用）
   - `@Primary`：默认胜出者
   - beanName 匹配（在某些场景可作为一种缩小方式）
3) 仍然不唯一就报错（这是好事：避免静默注错）

重点：**`@Qualifier` 是“缩小候选集合”的规则**，而不是“把某个 bean 改名”的方式。

## 3. `@Qualifier` vs `@Primary` 怎么选？

建议的工程决策：

- 业务上“默认实现”明显存在：用 `@Primary`
- 需要按场景明确选择实现：用 `@Qualifier`

常见实践组合：

- 给默认实现加 `@Primary`
- 对“非默认实现”的注入点显式加 `@Qualifier`

Exercises 里也专门有题让你把 `@Qualifier` 改成 `@Primary` 来体会差异：

- `src/test/java/.../SpringCoreBeansExerciseTest.java`
  - `exercise_resolveMultipleBeansViaPrimaryInsteadOfQualifier()`

## 4. 可选依赖与延迟获取：`ObjectProvider`

当你不想“容器启动时就必须有这个 bean”，或者你希望每次都能获取“最新/新的实例”，可以用：

- `ObjectProvider<T>`

本模块已有例子：

- `ProviderPrototypeConsumer` 注入 `ObjectProvider<PrototypeIdGenerator>`

这类方式本质上是在说：

- 我不要求你立刻注入一个具体对象
- 我要求你给我一个“将来可以向容器要对象”的入口

这对 prototype 注入 singleton 尤其重要，[04 章](04-scope-and-prototype.md)会详细解释。

## 5. 集合注入与排序（你以后一定会遇到）

当你注入：

- `List<T>`：容器会把所有 `T` 类型的 bean 都注入进来
- `Map<String, T>`：key 通常是 beanName

这通常用于“插件式扩展”：

- 多个实现按顺序执行（过滤器链、策略链）

顺序控制常见手段：

- `@Order` / `Ordered`：影响集合注入的顺序（不是“单 bean 选择”的规则）

> 常见误解：很多人以为给 bean 加了 `@Order(1)` 就能“优先被注入到单个依赖里”。通常不是这样：单依赖选择优先看 `@Primary`、`@Qualifier` 等。

## 6. 你应该能从报错里读出什么

当你遇到类似异常时：

- `NoSuchBeanDefinitionException`：没有候选
- `NoUniqueBeanDefinitionException`：候选太多且无法唯一化

你应该能顺着异常信息反推：

1) 注入点需要的类型是什么？
2) 容器里有哪些候选？
3) 缺少的限定条件是什么？（`@Qualifier` / `@Primary` / beanName 等）

本模块的 lab 已经覆盖：

- `SpringCoreBeansLabTest.usesQualifierToResolveMultipleBeans()`

下一章我们会把 “候选是怎么创建出来的” 和 “什么时候创建” 结合起来讲：Scope。

