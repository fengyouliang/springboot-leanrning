# 20. registerResolvableDependency：能注入，但它不是 Bean

有些东西你可以直接注入到 bean 里：

- `ApplicationContext`
- `BeanFactory`
- `Environment`

很多初学者会误以为：

- “那它们一定也是普通 Bean 吧？”

这一章用一个可运行实验告诉你：

- 有些依赖参与 autowiring，但它不是通过 BeanDefinition 注册出来的

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansResolvableDependencyLabTest.java`

## 1. 现象：能注入，但 `getBean(该类型)` 失败

对应测试：

- `SpringCoreBeansResolvableDependencyLabTest.registerResolvableDependency_enablesAutowiringWithoutRegisteringABean()`

实验里我们做了三件事：

1) `registerResolvableDependency(NotABeanDependency.class, instance)`
2) 注册一个 `NeedsDependency`，构造器参数是 `NotABeanDependency`
3) refresh 后 `NeedsDependency` 能拿到我们注册的 instance

但同时：

- `context.getBean(NotABeanDependency.class)` 会报 `NoSuchBeanDefinitionException`

学习重点：

- **ResolvableDependency 参与“注入解析”**
- **但不参与“Bean 查找”**（它不是普通 bean）

## 2. 机制：它是“特殊依赖表”，不是 BeanDefinition

你可以把它理解为：

- 容器里有一张“特殊依赖表”
- 当容器解析构造器/字段依赖时，会先看这张表

所以它非常适合给框架提供“容器级依赖”。

### 2.1 这张“特殊依赖表”在源码里是什么？

在 `DefaultListableBeanFactory` 里，它通常就是一个按类型索引的 Map（概念上可以理解为）：  

- `Map<Class<?>, Object> resolvableDependencies`

它的 key 是“你想让容器能注入的类型”，value 是“注入时返回的值”。

注意两个细节：

1) value 不一定只是一个“固定实例”  
   - 也可以是一个 `ObjectFactory<?>`（让容器在注入时再去取，达到 lazy 的效果）
2) 这张表的语义是 **“参与依赖解析（autowiring）”**  
   - 它不是 `BeanDefinition`，不会进入正常的 bean 生命周期

### 2.2 它在依赖解析链路的哪个位置命中？（注入路径）

把“依赖注入”看成一条链路会更清晰：

1) 需要解析一个注入点（构造器参数/字段/方法参数）  
2) 容器把注入点封装成 `DependencyDescriptor`  
3) 进入 `DefaultListableBeanFactory#doResolveDependency(...)`  
4) **优先检查** `resolvableDependencies` 能否命中（命中就直接返回 value）  
5) 命不中，才进入“按 bean 候选集”路线：`findAutowireCandidates(...)` + 规则收敛（`@Primary/@Qualifier/@Priority` 等）

你用断点验证时，一般不需要把整条链路单步到底；只要在 `doResolveDependency` 看清：

- `descriptor.getDependencyType()`（注入点要什么）
- `resolvableDependencies` 是否有这个 key
- 没命中时是否继续走 `findAutowireCandidates(...)`

### 2.3 为什么 `getBean(type)` 查不到？（查找路径完全不同）

`context.getBean(SomeType.class)` 走的是 **Bean 查找** 路径：

- 典型入口：`AbstractBeanFactory#doGetBean(...)`
- 它依赖的是：
  - `BeanDefinition` 注册表
  - 单例缓存（`singletonObjects`）
  - `FactoryBean` 等“bean 语义”

而 `ResolvableDependency` 的 key/value **不在**这些结构里，因此：

- 它可以被 `doResolveDependency` 命中（注入成功）
- 但不会被 `doGetBean` 命中（查找失败）

> 一句话总结：**注入（resolveDependency）** 和 **查找（getBean）** 是两条不同的管道。

### 2.4 容器默认会注册哪些 ResolvableDependency？（以及怎么确认）

在真实的 `ApplicationContext` 里，你能注入很多“容器对象”，通常并不是因为它们是普通 bean，而是因为 context 在 refresh 过程中做了准备工作。

最有价值的源码入口是：

- `AbstractApplicationContext#prepareBeanFactory`

你可以在这里打断点，然后在 debugger 里展开 `beanFactory`，观察 `resolvableDependencies` 里有哪些默认条目（不同 Spring 小版本可能略有调整）。

建议你至少确认下面这类类型是否出现（只记“方向”，不强记列表）：

- `BeanFactory` / `ApplicationContext`（容器本体）
- `ResourceLoader` / `ApplicationEventPublisher`（容器对外的基础能力接口）

然后你再回到本章的结论，会更“实”：  
**这些东西能注入，不代表它们是 bean。**

### 2.5 高级用法：用 `ObjectFactory` 做“按需提供”

如果你把 value 注册成 `ObjectFactory<?>`，你就能把“注入值”变成“按需计算/按需获取”。

典型用途（学习阶段知道即可）：

- 延迟访问某个对象（避免过早初始化）
- 注入一个“代理式入口”，内部再决定返回什么

但需要强调：这属于容器/框架内部手段。  
业务对象不要用它替代正常的 bean 注册，否则排障成本会非常高。

### 2.6 它和 `*Aware` 是什么关系？（两种“把容器对象交给 bean”的方式）

初学者常见困惑是：

- “我既可以 `@Autowired ApplicationContext`，也可以实现 `ApplicationContextAware`，它们是不是一回事？”

它们最终效果相似，但机制不同：

1) **ResolvableDependency（本章）**  
   - 发生在依赖解析阶段（`doResolveDependency`）  
   - 注入点是构造器参数/字段/方法参数  
2) **Aware 回调（BPP 机制）**  
   - 发生在初始化阶段（`initializeBean` 附近，由基础设施 BPP 触发）  
   - 容器把自己“回调”给 bean（例如调用 `setApplicationContext(...)`）

如果你在 debug 时把两者混在一起看，很容易误判“为什么这个注入能生效/为什么另一个不生效”。  
建议和 [12](12-container-bootstrap-and-infrastructure.md) 一起对照理解。

## 3. 常见坑

- **坑 1：以为它会出现在 beans 列表里**
  - 不会。它不是 bean。

- **坑 2：以为它有 scope/lifecycle**
  - 它不是 bean，自然也没有完整的 bean 生命周期语义。

- **坑 3：以为它会出现在依赖图里**
  - 依赖图是按 beanName 记录的；ResolvableDependency 没有 beanName，所以你用 `getDependenciesForBean(...)` 不会看到它。

- **坑 4：把业务对象塞进 ResolvableDependency**
  - 这会绕开 BeanDefinition 与生命周期语义，让“为什么它被注入/为什么它被代理/为什么它没销毁”变得非常难解释。

## 源码锚点（建议从这里下断点）

- `AbstractApplicationContext#prepareBeanFactory`：context 在 refresh 中准备 beanFactory（会注册一批默认 resolvable dependencies）
- `DefaultListableBeanFactory#registerResolvableDependency`：把“可解析但非 bean”的依赖放进特殊依赖表
- `DefaultListableBeanFactory#resolveDependency` / `DefaultListableBeanFactory#doResolveDependency`：依赖解析主流程（会优先检查 resolvableDependencies）
- `DependencyDescriptor#getDependencyType`：注入点抽象（字段/参数的类型信息从这里进入解析流程）
- `DefaultListableBeanFactory#findAutowireCandidates`：当 resolvableDependencies 未命中时，才会走“按 bean 候选集”找候选
- `AbstractBeanFactory#doGetBean`：`getBean(type)` 走的是 bean 查找链路，不会命中 resolvableDependencies（因此会失败）

## 断点闭环（用本仓库 Lab/Test 跑一遍）

入口：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansResolvableDependencyLabTest.java`
  - `registerResolvableDependency_enablesAutowiringWithoutRegisteringABean()`

建议断点：

0) （可选但很推荐）`AbstractApplicationContext#prepareBeanFactory`：观察默认注册了哪些 resolvable dependencies（理解“为什么能注入容器对象”）
1) `DefaultListableBeanFactory#registerResolvableDependency`：观察 NotABeanDependency 被放入哪张表（它不会变成 BeanDefinition）
2) `DefaultListableBeanFactory#doResolveDependency`：观察构造器参数解析时直接命中 resolvableDependencies 并返回 instance
3) `AbstractBeanFactory#doGetBean`（或测试里 `context.getBean(NotABeanDependency.class)` 那一行）：观察为什么它会抛 `NoSuchBeanDefinitionException`

## 排障分流：这是定义层问题还是实例层问题？

- “某个类型能注入，但 `getBean(type)` 拿不到” → **优先实例层（解析路径差异）**：它可能是 ResolvableDependency，而不是普通 bean（本章 Lab）
- “我想让它也出现在 beans 列表/支持 scope/lifecycle” → **定义层需求**：你需要注册 BeanDefinition（而不是 ResolvableDependency）（回看 [02](02-bean-registration.md)）
- “把业务对象塞进 ResolvableDependency 里导致难 debug” → **设计/使用问题**：ResolvableDependency 更适合容器级依赖（framework internal），业务对象更适合普通 bean（对照本章第 2 节）
- “依赖解析选错候选/歧义” → **实例层（候选解析）**：ResolvableDependency 只是其中一种来源，回到 [03](03-dependency-injection-resolution.md)/[33](33-autowire-candidate-selection-primary-priority-order.md)

## 源码最短路径（call chain）

> 目标：把“注入能命中、getBean 命不中”的两条管道用最短路径摆在一起，避免在断点里迷路。

注入管道（命中 ResolvableDependency）：

- `DefaultListableBeanFactory#doResolveDependency(descriptor, ...)`
  - `descriptor.getDependencyType()`（注入点要什么类型）
  - `this.resolvableDependencies` 命中  
    - value 如果是 instance：直接返回  
    - value 如果是 `ObjectFactory`：调用 `getObject()` 再返回

查找管道（`getBean(type)` 不会命中 ResolvableDependency）：

- `AbstractBeanFactory#doGetBean(...)`
  - 走 `BeanDefinition` 注册表 + singleton 缓存 + FactoryBean 语义  
  - **不会**查询 `resolvableDependencies`  
  ⇒ 所以 `getBean(NotABeanDependency.class)` 失败是“机制决定”，不是偶然

## 固定观察点（watch list）

在 `doResolveDependency(...)` 里建议 watch/evaluate：

- `descriptor.getDependencyType()`：决定是否能命中 `resolvableDependencies`
- `this.resolvableDependencies`：是否包含该类型 key（命中则不会再走候选集合收敛）
- `matchingBeans` / `findAutowireCandidates(...)`（如果没命中 ResolvableDependency）：说明你已经切换到“按 bean 候选集”路线（转 [03](03-dependency-injection-resolution.md)）

在 `doGetBean(...)` 里建议 watch/evaluate：

- `containsBeanDefinition(beanName)` / `beanDefinitionMap`（概念上）：它查的是“定义层”，不是 `resolvableDependencies`
- `singletonObjects`：它查的是“实例缓存”，不是 `resolvableDependencies`

## 反例（counterexample）

**反例：我看到某个类型能注入，就以为它一定是 Bean；结果 `getBean(type)` 失败。**

最小复现入口：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansResolvableDependencyLabTest.java`
  - `registerResolvableDependency_enablesAutowiringWithoutRegisteringABean()`

你在断点里应该看到什么（用于纠错）：

- `doResolveDependency` 直接命中 `resolvableDependencies`（注入成功）
- `doGetBean` 根本不会查 `resolvableDependencies`（查找失败，抛 `NoSuchBeanDefinitionException`）

## 4. 一句话自检

- 你能解释清楚：为什么它能被注入，但不能被 `getBean(type)` 拿到吗？
对应 Lab/Test：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansResolvableDependencyLabTest.java`
推荐断点：`AbstractApplicationContext#prepareBeanFactory`、`DefaultListableBeanFactory#doResolveDependency`、`AbstractBeanFactory#doGetBean`
