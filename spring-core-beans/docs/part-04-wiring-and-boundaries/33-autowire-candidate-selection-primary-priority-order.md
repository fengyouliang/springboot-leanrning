# 33. 候选选择 vs 顺序：`@Primary` / `@Priority` / `@Order` 到底各管什么？

这一章专门解决一个“老是被误用”的问题：

> 我给 bean 加了 `@Order(1)`，为什么注入还是报 “候选太多（NoUniqueBeanDefinition）”？

答案是：**你把“集合排序”当成了“单依赖选择”。**

对应实验（可运行 + 可断言）：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansAutowireCandidateSelectionLabTest.java`

建议直接跑：

```bash
mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansAutowireCandidateSelectionLabTest test
```

## 1. 先把问题分清：你注入的是“一个”还是“一组”？

Spring 里很多“规则”只在特定场景成立。最关键的分界线就是：

| 场景 | 你的注入点长什么样 | 你想要的结果 |
| --- | --- | --- |
| 单依赖注入（single injection） | `private final T t;` / `T` 参数 | 必须选出 **唯一** 候选，否则应失败 |
| 集合注入（collection injection） | `List<T>` / `Map<String, T>` / `ObjectProvider<T>` | 把所有候选注入进来，并且尽量有“稳定顺序” |

### 面试常问：单注入 vs 集合注入（不要把排序当成选择）

- 题目：`@Primary` / `@Priority` / `@Order` 分别解决什么问题？哪些只影响“集合顺序”，哪些会影响“单依赖候选收敛”？
- 追问：
  - 为什么 `@Order` 不能解决“单注入歧义”（`NoUniqueBeanDefinitionException`）？你如何用断点证明它根本不参与 `determineAutowireCandidate`？
  - `@Primary` 与 `@Priority` 谁优先？在没有 `@Primary/@Qualifier` 时，`@Priority` 为什么有时能“打破平局”？
- 复现入口（可断言）：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansAutowireCandidateSelectionLabTest.java`
  - 单注入歧义：`orderAnnotation_doesNotResolveSingleInjectionAmbiguity()`
  - `@Primary` vs `@Priority`：`primaryOverridesPriority_forSingleInjection()`
  - tie-break：`priorityAnnotation_canBreakTieForSingleInjection_whenNoPrimaryOrQualifier()`
  - 集合顺序：`orderAnnotation_affectsCollectionInjectionOrder()`

## 2. 单依赖注入：**解决的是“选谁”**

当容器里有多个同类型候选时（`T` 有多个 bean），你需要的是 **候选选择规则**，常见工具是：

- `@Qualifier`：我明确指定要哪个（最直观，强确定性）
- `@Primary`：我指定一个默认胜者（默认实现）
- `@Priority`：在没有 `@Primary/@Qualifier` 时，用优先级“打破平局”

对应 Lab 的结论（可断言）：

1) **`@Order` 不能解决单依赖歧义**
   - 即使两个候选都有 `@Order`，单依赖注入仍应失败
2) **`@Priority` 可以在某些场景下作为单依赖的 tie-breaker**
   - 数字越小，优先级越高
3) **`@Primary` 的优先级高于 `@Priority`**
   - 即使另一个候选的 `@Priority` 更高，`@Primary` 仍会赢

> 你可以把它记成一句话：  
> **“明确指定（Qualifier） > 默认胜者（Primary） > 优先级（Priority） > 否则失败”**

## 3. 集合注入：**解决的是“按什么顺序给我”**

当你注入 `List<T>` 或者用 `ObjectProvider<T>.orderedStream()` 时，容器通常会对候选做排序。

这时才轮到“顺序相关”的注解/接口登场：

- `@Order` / `Ordered`
- `@Priority`（同样也会影响排序）

对应 Lab 的结论（可断言）：

- `@Order(0)` 的 bean 会排在 `@Order(1)` 前面（数字越小越靠前）

关键澄清：

> **集合注入需要排序；单依赖注入需要选择。**  
> 这两件事不是同一个问题。

## 4. Debug / 排查建议（非常实用）

遇到注入问题时，先问 3 个问题：

1) 这是单依赖还是集合注入？
2) 如果是单依赖：容器里有哪些候选？有没有 `@Qualifier/@Primary/@Priority`？
3) 如果是集合注入：排序规则来自哪里？你写了 `@Order` 还是实现了 `Ordered`？

并且记住一个常见误区：

- “我加了 `@Order`，它应该自动帮我选一个 bean”  
  ⇒ 这通常是不成立的（Lab 已固化为断言）

## 5. 延伸阅读（把规则放回更完整的 DI 体系）

- DI 解析总览：`@Qualifier/@Primary` 的基本语义：[03. 依赖注入解析](03-dependency-injection-resolution.md)
- 如果你在看容器扩展点顺序（BPP/BFPP）：顺序体系更复杂（另一个层面）：[14. 顺序：PriorityOrdered / Ordered / 无序](14-post-processor-ordering.md)

## 源码锚点（建议从这里下断点）

- `DefaultListableBeanFactory#doResolveDependency`：单依赖注入的主入口（候选收集 → 选胜者 → 注入）
- `DefaultListableBeanFactory#determineAutowireCandidate`：从多个候选里挑一个（会综合 qualifier/primary/priority/name 等）
- `DefaultListableBeanFactory#determinePrimaryCandidate`：`@Primary` 胜出的关键分支
- `DefaultListableBeanFactory#determineHighestPriorityCandidate`：`@Priority` 参与 tie-break 的关键分支
- `AnnotationAwareOrderComparator#sort`：集合注入排序入口（`@Order/@Priority/Ordered` 影响的是这里）

## 断点闭环（用本仓库 Lab/Test 跑一遍）

入口：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansAutowireCandidateSelectionLabTest.java`

建议断点：

1) `DefaultListableBeanFactory#doResolveDependency`：对照单依赖注入场景，观察候选集合与最终胜者
2) `DefaultListableBeanFactory#determinePrimaryCandidate`：观察 `@Primary` 为什么能压过 `@Priority`
3) `DefaultListableBeanFactory#determineHighestPriorityCandidate`：在没有 `@Primary/@Qualifier` 时观察 `@Priority` 如何打破平局
4) `AnnotationAwareOrderComparator#sort`：对照集合注入场景，观察 `@Order` 只影响排序，不影响单依赖选择

## 排障分流：这是定义层问题还是实例层问题？

- “`NoUniqueBeanDefinitionException`（候选太多）” → **实例层（候选选择失败）**：`@Order` 不会帮你选胜者；用 `@Qualifier/@Primary/@Priority`（本章 + `doResolveDependency`）
- “集合注入顺序不稳定/不符合预期” → **实例层（排序）**：看 `AnnotationAwareOrderComparator#sort`（本章第 3 节）
- “我以为 `@Priority` 会影响一切注入场景” → **实例层规则差异**：它既可能参与单依赖 tie-break，也会影响集合排序，但优先级低于 `@Primary`（本章第 2/3 节）
- “候选选择行为跟想象不一致” → **先确认注入点类型**：单依赖 vs 集合是两套规则（本章第 1 节）
对应 Lab/Test：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansAutowireCandidateSelectionLabTest.java`
推荐断点：`DefaultListableBeanFactory#determineAutowireCandidate`、`DefaultListableBeanFactory#doResolveDependency`、`AnnotationAwareOrderComparator#sort`
