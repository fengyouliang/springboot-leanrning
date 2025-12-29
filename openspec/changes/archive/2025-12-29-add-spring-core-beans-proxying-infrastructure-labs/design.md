# Design: Proxying & Injection Deep-Dive Labs (spring-core-beans)

## Goals
- 用 **最小容器 + 可断言实验** 把两类“容器扩展点”知识点讲透，并能直接解释 AOP/Tx/Validation 的常见坑：
  - 注入阶段（property population / injection）发生在何时、由谁触发
  - 代理/替换阶段（auto-proxying / wrapping）如何把原始对象替换成代理对象
- 保持学习体验一致：
  - Labs 默认启用并全绿
  - Exercises 默认 `@Disabled`，按提示逐题开启
  - 每个 Lab 对应一章中文 docs：现象 → 机制 → 复现 → 断言 → Debug

## Non-Goals
- 不追求覆盖所有 Spring 内部细节（例如完整复刻 `AutowiredAnnotationBeanPostProcessor` 实现）
- 不把 `spring-core-beans` 变成 “AOP/Tx 模块的替代品”
  - AOP/Tx 的完整机制仍在各自模块讲解
  - 本变更只提供“容器视角的桥梁解释”，帮助学习者建立统一心智模型

## Approach
### 1) Injection Phase Lab
核心设计点：
- 使用 `AnnotationConfigApplicationContext` 或 `GenericApplicationContext + AnnotationConfigUtils.registerAnnotationConfigProcessors(...)`
- 引入一个自定义 `InstantiationAwareBeanPostProcessor`：
  - 在 `postProcessProperties(...)` 记录事件/顺序
  - 通过断言固定“注入发生在 init 之前”的事实（并对照 `@PostConstruct` 或 init 方法）
- 在同一个 Lab 内做 **field injection vs constructor injection** 的对照：
  - field injection：让学习者“看见”属性填充发生在 `postProcessProperties(...)` 这条路径上
  - constructor injection：使用“多构造器 + `@Autowired` 指定构造器”的方式，让学习者理解构造器选择同样依赖注解处理器参与（避免单构造器自动注入导致机制误判）
- 文档中明确映射到基础设施：
  - `@Autowired` 依赖 `AutowiredAnnotationBeanPostProcessor`
  - `@PostConstruct` 依赖 `CommonAnnotationBeanPostProcessor`

为什么选这个切入点：
- 学习者最常见的误解是“注解=语言魔法”；通过这个 Lab 可以把注解落到“容器阶段 + 处理器”的确定模型上

### 2) Proxying Phase Lab
核心设计点：
- 使用一个最小的 `BeanPostProcessor` 在 `postProcessAfterInitialization(...)` 返回 JDK 动态代理（或极轻量 wrapper）
- 通过断言复现 3 个关键结论：
  1. 容器最终暴露的 bean 可能是代理（不是原始对象）
  2. interface-based 代理会影响类型匹配（为什么按实现类 `getBean` 会失败）
  3. self-invocation 仍然绕过代理（与 AOP/Tx 同源）
- 文档中显式 cross-link：
  - `spring-core-aop` 的自调用陷阱/代理类型差异
  - `spring-core-tx` 的“事务也是代理 + 入口必须走代理”

为什么不直接引入 Spring AOP AutoProxyCreator：
- `spring-core-beans` 目标是讲容器机制；使用“最小可运行代理”更容易把注意力放在容器扩展点本身
- 真实 `AutoProxyCreator` 的细节（Advisor/Pointcut/Interceptor 链）在 AOP/Tx 模块更适合展开

## Documentation
新增 docs 章节建议（命名仅示例）：
- `30-injection-phase-and-postprocessproperties.md`
- `31-auto-proxying-as-bpp.md`

每章固定包含：
- 对应 Lab 路径
- OBSERVE（2–4 行）
- 机制解释（对应容器阶段/扩展点）
- Debug 路径（建议断点位置、如何打印 bean 类型/代理判断）
- 常见坑（与 AOP/Tx 关联点）
