# 32. `@Resource` 注入：为什么它更像“按名称找 Bean”？

这一章补齐一个非常高频、也非常容易踩坑的点：`@Resource`（Jakarta / JSR-250）注入到底是怎么解析候选的？

很多人会把它当成 “另一个 `@Autowired`”，但它更像：

> **先按名称（name）找，再按类型（type）兜底。**

对应实验（可运行 + 可断言）：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansResourceInjectionLabTest.java`

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

