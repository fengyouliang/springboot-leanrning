# 00. 深挖指南：把“Bean 三层模型”落到源码与断点

如果你觉得 `docs/01` 这类“概念章”看完仍然不过瘾，通常不是因为它讲错了，而是因为你已经进入下一阶段：

> 你需要把概念映射到**时间线（refresh 流程）**、**数据结构（BeanDefinition/缓存）**、以及**关键参与者（哪些类/哪些扩展点在起作用）**。

本章不新增概念，而是给你一套“深挖路线”，让你能在 IDE 里通过断点和测试，把容器行为看成**可追踪的过程**。

> 适用版本：本仓库基于 Spring Boot 3.x（对应 Spring Framework 6.x）。类名/方法名可能在小版本中微调，但主干结构非常稳定。

---

## 1. 深挖时最容易迷路的点（以及正确抓手）

### 1.1 不要试图“背源码”，要建立 3 条主线

1) **时间线（发生顺序）**：容器从 `refresh()` 开始，按阶段推进  
2) **定义到实例的映射**：`BeanDefinition` →（合并/增强）→ 实例创建与注入  
3) **扩展点介入点**：BDRPP/BFPP/BPP 分别在“多早、改什么、会影响谁”

如果你在断点里不知道“下一步该去哪”，就回到这三条主线：你当前是在时间线的哪个阶段？你在看定义还是实例？有哪些扩展点可能在改它？

---

## 2. 一张“最小源码导航图”（建议贴在脑子里）

把 `docs/01` 的三层模型落到源码，最小可以这么映射：

### 2.1 定义层：BeanDefinition 进来、存起来、被调整

- **容器与注册表**：`BeanDefinitionRegistry`（接口语义）  
- **最常见实现**：`DefaultListableBeanFactory`（既是 `BeanFactory` 也是 Registry）
- **定义对象**：`BeanDefinition` / `RootBeanDefinition`（实际项目里你常看到的是 Root）

定义层最关键的“会动定义”的入口：

- `BeanDefinitionRegistryPostProcessor`（BDRPP）：能“新增/删除/改名/再注册”定义
- `BeanFactoryPostProcessor`（BFPP）：能“改已有定义的配方/属性”
- `ConfigurationClassPostProcessor`：把 `@Configuration/@Bean/@Import` 解析成一堆定义（属于 BFPP 阵营）

对应章节：

- [02. 注册入口](02-bean-registration.md)
- [06. PostProcessor 概览](06-post-processors.md)
- [12. 注解为什么能工作（基础设施处理器）](12-container-bootstrap-and-infrastructure.md)
- [13. BDRPP](13-bdrpp-definition-registration.md)

### 2.2 实例层：createBean → 注入 → 初始化 → 可能被代理

实例层的骨架几乎都在 `AbstractAutowireCapableBeanFactory` 一条链路上：

- `createBean(...)`：创建入口（会走各种策略/短路）
- `doCreateBean(...)`：核心主流程（实例化 → 属性填充 → 初始化）
- `populateBean(...)`：属性填充（依赖注入最“肉”的地方）
- `initializeBean(...)`：初始化（aware、before-init、init-method、after-init）

实例层最关键的“会动实例/替换实例”的入口：

- `InstantiationAwareBeanPostProcessor`：能影响实例化/属性填充（例如决定构造器、提前返回代理等）
- `BeanPostProcessor`：before/after init 可包装代理（你看到的 AOP/事务代理基本都在这里出现）

对应章节：

- [30. 注入发生在什么时候（field vs constructor）](30-injection-phase-field-vs-constructor.md)
- [15. 实例化前短路](15-pre-instantiation-short-circuit.md)
- [31. BPP 如何把 Bean 换成 Proxy](31-proxying-phase-bpp-wraps-bean.md)

### 2.3 缓存与“循环依赖能不能救”：单例的三层缓存

循环依赖/提前暴露/early reference 这条线，如果你只记“三级缓存”会很虚；建议你把它落到这几个对象上：

- `DefaultSingletonBeanRegistry`：单例缓存与 early reference 的核心所在
- 关键动作：`getSingleton(...)`、提前暴露（singletonFactory）、early reference 生成

对应章节：

- [09. 循环依赖概览](09-circular-dependencies.md)
- [16. early reference 与循环依赖：getEarlyBeanReference](16-early-reference-and-circular.md)

---

## 3. 断点清单：你想“看见什么”，就打哪一类断点

本仓库已经把很多点做成了可运行的 Labs；建议你用“测试 + 断点”方式学习（比跑 Boot 全量启动更聚焦）。

### 3.1 看清“启动时间线”：从 refresh 开始

建议断点（看整体阶段划分，不建议一步步单步到天荒地老）：

- `AbstractApplicationContext#refresh`
- `PostProcessorRegistrationDelegate#invokeBeanFactoryPostProcessors`
- `PostProcessorRegistrationDelegate#registerBeanPostProcessors`
- `DefaultListableBeanFactory#preInstantiateSingletons`

你会建立一个非常关键的直觉：

- “**先把 PostProcessor 装好**，再批量创建单例”
- 很多“魔法”其实都发生在“创建任何业务 bean 之前”

### 3.2 看清“一个 Bean 的诞生”：从 doCreateBean 切入

建议断点：

- `AbstractAutowireCapableBeanFactory#doCreateBean`
- `AbstractAutowireCapableBeanFactory#populateBean`
- `AbstractAutowireCapableBeanFactory#initializeBean`

观察重点：

- 什么时候创建原始对象
- 什么时候开始做依赖注入
- 什么时候触发 `@PostConstruct` / `InitializingBean`
- 什么时候 BPP 可能把实例换成代理

### 3.3 看清“DI 为什么选它”：从 resolveDependency 切入

建议断点：

- `DefaultListableBeanFactory#doResolveDependency`
- `AutowiredAnnotationBeanPostProcessor#postProcessProperties`

观察重点：

- `DependencyDescriptor` 描述了“注入点是什么”（字段/参数/泛型信息）
- 候选集合是怎么来的（按类型查、再按 qualifier/primary 等规则收敛）

对应章节：

- [03. 依赖注入解析](03-dependency-injection-resolution.md)
- [33. 候选选择与顺序](33-autowire-candidate-selection-primary-priority-order.md)

---

## 4. 推荐的“深挖练习”（每个练习都能在 30 分钟内闭环）

### 练习 A：从 BeanDefinition 到实例（最适合刚开始深挖）

1) 运行 `spring-core-beans` 的测试（只跑一个类也行）
2) 在 `SpringCoreBeansContainerLabTest.beanDefinitionIsNotTheBeanInstance()` 断点  
3) 顺着 `getBean(...)` 看一次 `createBean → doCreateBean`

目标：你要能用自己的话把“定义层”与“实例层”串起来。

### 练习 B：让注入阶段“可见”（最适合理清阶段感）

直接按 [30 章](30-injection-phase-field-vs-constructor.md) 给的断点走一遍。

目标：建立“构造器阶段 vs 属性填充阶段”的手感，不再把 `@Autowired` 当成“构造时就有”。

### 练习 C：看一次 early reference（最适合理清循环依赖到底怎么救）

按 [16 章](16-early-reference-and-circular.md) 的思路，在 `DefaultSingletonBeanRegistry#getSingleton(...)` 观察 early reference 的生成与使用。

目标：能解释“为什么 setter 循环有时能成、构造器循环必死”背后的缓存与时机。

---

## 5. 读完本章你应该获得什么

如果本章有效，你应该能做到：

- 遇到“为什么它被代理/为什么注入的是它/为什么它没注册”，不再只能靠猜
- 能把问题定位到：定义层（注册/条件/顺序）还是实例层（注入/代理/回调）
- 能用断点验证自己的推理，而不是靠日志碰运气

回到概念章继续读也不会“太简单”了：因为你已经知道每个概念在源码里对应哪里、能怎么证明。 

