# 32. `@Resource` 注入：为什么它更像“按名称找 Bean”？

这一章补齐一个非常高频、也非常容易踩坑的点：`@Resource`（Jakarta / JSR-250）注入到底是怎么解析候选的？

很多人会把它当成 “另一个 `@Autowired`”，但它更像：

> **先按名称（name）找，再按类型（type）兜底。**

对应实验（可运行 + 可断言）：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansResourceInjectionLabTest.java`

建议直接跑：

```bash
mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansResourceInjectionLabTest test
```

## 1. 现象：没注册 annotation processors 时，`@Resource` 会“失效”

实验第一段故意使用一个“什么处理器都不注册”的最小容器：`GenericApplicationContext`。

你会观察到：

- Bean 能创建出来（容器照常实例化）
- 但 `@Resource` 标注的字段仍然是 `null`

这不是因为 `@Resource` “不稳定”，而是因为：

> **注解不是语言层魔法，注入是容器通过处理器（BPP）做出来的。**

对照阅读：

- [12. 容器启动与基础设施处理器：为什么注解能工作？](12-container-bootstrap-and-infrastructure.md)

## 2. 现象：注册 processors 后，`@Resource` 默认按字段名注入（name-first）

实验第二段调用：

- `AnnotationConfigUtils.registerAnnotationConfigProcessors(context)`

之后再 `refresh()`，你会看到：

- `@Resource` 注入生效
- 即使容器里有多个同类型候选，依然能稳定注入正确对象（因为按名称先锁定了候选）

在 Lab 里我们同时验证了两种常见写法：

1) `@Resource`（不写 name）：默认使用 **字段名** 当 beanName
2) `@Resource(name = "...")`：显式指定 beanName

这也是为什么很多项目里你会看到：

- `@Resource(name="xxx")`

因为它把“我要哪个 bean”写得非常明确（本质上就是按名称拿）。

## 3. 为什么会这样？`CommonAnnotationBeanPostProcessor`

`@Resource` 属于 JSR-250 / Jakarta Common Annotations，Spring 处理它的核心基础设施是：

- `CommonAnnotationBeanPostProcessor`

它是一个 `BeanPostProcessor`，在 bean 的创建过程中参与属性填充 / 注入阶段，把 `@Resource` 这种注解“翻译”为实际的依赖解析与赋值动作。

这也是 Lab 里 “注册 processors 前后行为差异” 的根因：**你有没有把这个处理器注册进容器**。

## 4. Debug / 观察建议

当你在真实项目里遇到 “`@Resource` 怎么没注入？” 时，建议按这个顺序排查：

1) 先确认容器是不是“注解能力完整”的容器
   - Boot 应用一般没问题
   - 纯 `GenericApplicationContext` / 手工容器很容易漏注册 processors
2) 明确你的解析到底想走 name 还是 type
   - `@Resource` 默认 name-first：字段名要和 beanName 对上
3) 观察注入失败的方式
   - name 找不到时是否兜底按 type
   - type 兜底时如果同类型多个候选，仍可能出现歧义（参考第 33 章）

## 5. 常见坑与实践建议

- **不要把 `@Resource` 当成 “按类型注入” 的默认选择**：它更偏 name-first
- 如果你希望“按类型 + 规则选胜者”：优先 `@Autowired` + `@Qualifier/@Primary`
- 如果你希望“按名称精确绑定”：`@Resource(name="...")` 往往更直观

## 6. 延伸阅读（把注入模型连起来）

- DI 候选选择（类型/名称/Qualifier/Primary）：[03. 依赖注入解析](03-dependency-injection-resolution.md)
- 注入发生在容器的哪个阶段：[`postProcessProperties` 与 field vs constructor](30-injection-phase-field-vs-constructor.md)
- 注解能力从哪来：[`registerAnnotationConfigProcessors`](12-container-bootstrap-and-infrastructure.md)

## 源码锚点（建议从这里下断点）

- `AnnotationConfigUtils#registerAnnotationConfigProcessors`：把 `CommonAnnotationBeanPostProcessor` 等基础设施装进容器的入口
- `CommonAnnotationBeanPostProcessor#postProcessProperties`：处理 `@Resource` 注入的关键阶段（属性填充阶段）
- `AbstractAutowireCapableBeanFactory#populateBean`：属性填充主流程（`@Autowired/@Resource` 都在这里发生）
- `AbstractBeanFactory#doGetBean`：name-first 的常见落点（`@Resource` 往往会先按 beanName 走 name-based lookup）
- `DefaultListableBeanFactory#doResolveDependency`：当 name 找不到或需要按 type 兜底时，会回到 type-based 候选解析

## 断点闭环（用本仓库 Lab/Test 跑一遍）

入口：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansResourceInjectionLabTest.java`

建议断点：

1) `AnnotationConfigUtils#registerAnnotationConfigProcessors`：对照“注册前/注册后”差异，确认 `CommonAnnotationBeanPostProcessor` 是否存在
2) `CommonAnnotationBeanPostProcessor#postProcessProperties`：观察 `@Resource` 是如何把 name/type 解析翻译成实际赋值动作的
3) `AbstractBeanFactory#doGetBean`：观察 name-first 时的 beanName 解析（字段名 / `@Resource(name=...)`）
4) （可选）`DefaultListableBeanFactory#doResolveDependency`：观察 type 兜底在多候选下为什么仍可能歧义

## 排障分流：这是定义层问题还是实例层问题？

- “`@Resource` 字段一直为 null” → **优先定义层/基础设施问题**：容器是否注册了 `CommonAnnotationBeanPostProcessor`？（看 `registerAnnotationConfigProcessors`）
- “注入到了错误的 bean / name 对不上” → **实例层（name-first 解析）**：字段名/显式 name 是否真的对应 beanName？（本章第 2 节）
- “name 找不到后兜底 type 还是报多候选” → **实例层（候选解析）**：转到 [33](33-autowire-candidate-selection-primary-priority-order.md) 的选择规则
- “以为它等价于 `@Autowired`” → **概念差异**：`@Resource` 默认 name-first，`@Autowired` 默认 type-first（对照 [03](03-dependency-injection-resolution.md)）
对应 Lab/Test：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansResourceInjectionLabTest.java`
推荐断点：`CommonAnnotationBeanPostProcessor#postProcessProperties`、`CommonAnnotationBeanPostProcessor#autowireResource`、`DefaultListableBeanFactory#doResolveDependency`

## 面试常问（`@Resource` vs `@Autowired`）

- 常问：`@Resource` 与 `@Autowired` 的核心差异是什么？
  - 答题要点：`@Resource` 更偏 name-first（字段名/指定 name），`@Autowired` 更偏 type-first；两者由不同的 BPP 处理，语义与排障路径不同。
- 常见追问：为什么很多团队更推荐“构造注入 + `@Autowired`（可省略）”？
  - 答题要点：依赖显式、可测试性更好；避免 name-first 在重构字段/beanName 时引入隐性回归。
