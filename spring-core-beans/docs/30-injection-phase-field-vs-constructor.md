# 30. 注入阶段：field injection vs constructor injection（以及 `postProcessProperties`）

这一章解决两个“非常折磨人但非常核心”的问题：

1. 为什么我在构造器里访问 `@Autowired` 字段时，它永远是 `null`？
2. 为什么构造器注入（constructor injection）却能在构造器里拿到依赖？

关键结论先给出：

> **field injection 发生在“实例化之后”的属性填充阶段**，而 **constructor injection 发生在“实例化之前”的构造器解析阶段**。

对应实验（可运行 + 可断言）：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansInjectionPhaseLabTest.java`

建议直接跑：

```bash
mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansInjectionPhaseLabTest test
```

## 1. 现象：field injection 在构造器里拿不到依赖

在实验里 `FieldInjectedTarget` 使用 field injection：

- 构造器里记录“依赖是否为 null” → **会是 null**
- 容器完成注入后（在初始化阶段之前）依赖变为非 null
- `@PostConstruct` 里再次检查 → **依赖已经可用**

你可以把它记成一条时间线：

1) **构造器执行**（对象刚被 `new` 出来）  
2) **属性填充 / 注入阶段**（field/method injection 发生在这里）  
3) **初始化回调**（例如 `@PostConstruct`）

## 2. 现象：constructor injection 在构造器里就能拿到依赖

实验里 `ConstructorInjectedTarget` 同时提供：

- 一个无参构造器（`no-arg`）
- 一个带参数的构造器，并用 `@Autowired` 标记为注入构造器（`autowired`）

当容器具备注解处理能力时（见第 12 章），它会：

- 在实例化之前先决定“用哪个构造器”
- 再解析构造器参数依赖
- 然后创建对象

因此：constructor injection 的依赖在对象构造完成时就已经存在。

## 3. `postProcessProperties(...)` 在哪里起作用？

这一点是把“注解不是魔法”落地成可解释机制的关键：

- **field injection 并不是语言层做的**，而是容器在属性填充阶段调用了一组处理器完成的
- 其中一个关键扩展点就是：
  - `InstantiationAwareBeanPostProcessor#postProcessProperties(...)`
- Spring 的 `AutowiredAnnotationBeanPostProcessor`（一个基础设施 BPP）就是靠这条路径处理 `@Autowired` 字段/方法注入

本章的 Lab 额外加了一个“探针 BPP”，在 `postProcessProperties(...)` 里记录快照，帮助你在断点里“看见注入发生在这一段”。

> 注意：**多个 BPP 的顺序会影响你在 `postProcessProperties(...)` 里看到的 bean 状态**。  
> 你需要把重点放在“注入发生在属性填充阶段”这个结论上，而不是纠结某一个 BPP 是先还是后（顺序规则见第 14/25 章）。

## 4. Debug / 观察建议

建议你用断点把“阶段感”建立起来：

1. 在 `FieldInjectedTarget` 的构造器里下断点：你会看到依赖为 `null`
2. 在 `InjectionPhaseProbePostProcessor#postProcessProperties(...)` 下断点：这是属性填充阶段的入口之一
3. 在 `FieldInjectedTarget#init(@PostConstruct)` 下断点：你会看到依赖已可用
4. 对照 `ConstructorInjectedTarget`：依赖在构造器内就已可用，并且会选择 `@Autowired` 构造器

如果你想把“注解能力从哪来”也串起来，请回看：

- [12. 容器启动与基础设施处理器：为什么注解能工作？](12-container-bootstrap-and-infrastructure.md)

## 5. 常见坑与实践建议

- **不要在构造器里依赖 field injection 的字段**：那一定是 `null`（这是机制决定的，不是偶然）
- **必填依赖优先用 constructor injection**：更早失败、更容易测试、也更符合不可变设计
- 当类存在多个构造器时：
  - 用 `@Autowired` 明确指定注入构造器，避免“选择规则误判”

## 6. 延伸阅读（把点连成线）

本章本质是在讲：**容器通过 BPP 让注解“生效”**。这条线能直接解释 AOP/事务为何会出现“入口必须走代理”的坑：

- AOP（代理心智模型）：`spring-core-aop/docs/01-aop-proxy-mental-model.md`
- 事务也是代理：`spring-core-tx/docs/02-transactional-proxy.md`

