# 04. Scope 与 prototype 注入陷阱（ObjectProvider / @Lookup / scoped proxy）

这一章的主题是：**scope 不是“对象的特性”，而是“容器如何管理对象的策略”。**

尤其要吃透一句话：

> prototype 的语义是“每次向容器要都会新建”，不是“每次方法调用都会新建”。

## 1. singleton vs prototype：到底“一”指什么？

- `singleton`：**同一个容器**里，这个 beanName 对应的实例只有一个
- `prototype`：容器**每次创建/获取**都会创建一个新实例；容器通常不缓存它（也不负责销毁回调）

注意关键限定词：同一个容器。不同 `ApplicationContext` 里当然会有不同实例。

## 2. 本模块里你能直接观察到的现象

代码对应：

- prototype bean：`PrototypeIdGenerator`（`@Scope("prototype")`）
- 直接注入：`DirectPrototypeConsumer`
- Provider 延迟获取：`ProviderPrototypeConsumer`

运行测试你会看到：

- `DirectPrototypeConsumer.currentId()` 连续两次拿到同一个 UUID
- `ProviderPrototypeConsumer.newId()` 连续两次拿到不同 UUID

对应验证：

- `SpringCoreBeansLabTest.demonstratesPrototypeScopeBehavior()`

## 3. 为什么“prototype 注入 singleton”会看起来像单例？

容器创建 singleton 的时候，会把它的依赖也解析出来并注入进去。

如果你把 prototype 当作一个普通依赖注入到 singleton 里，发生的是：

1) 创建 singleton A
2) 解析到它需要 prototype P
3) **创建一个 P 并注入到 A**
4) A 从此持有这个 P 的引用（A 自己是单例）

之后你再调用 A 的方法，当然一直是同一个 P 引用 —— 这不是 prototype “失效”，而是你**只向容器要过一次 P**。

## 4. 解决方案 1：`ObjectProvider`（推荐，简单有效）

`ObjectProvider<T>` 让你把“获取对象的动作”推迟到方法调用时：

- 注入的是 provider（可以理解为“容器句柄”）
- 每次 `getObject()` 才真正向容器要一个实例

本模块的 `ProviderPrototypeConsumer` 就是这样做的。

适用场景：

- prototype 注入 singleton
- 可选依赖（没注册也可以）
- 想延迟创建（避免启动期就创建）

## 5. 解决方案 2：`@Lookup`（方法注入，适合“每次调用都要新的”）

`@Lookup` 的效果可以理解为：

- Spring 生成一个子类/代理
- 在方法调用时，由容器动态返回一个 bean

本模块的容器实验覆盖了它：

- `SpringCoreBeansContainerLabTest.lookupMethodCanObtainFreshPrototypeEachCall()`

适用场景：

- 你希望调用 `consumer.next()` 时每次都要一个新 prototype
- 你不想显式注入 `ObjectProvider`

注意：`@Lookup` 依赖运行时的增强/代理机制，阅读成本更高；学习阶段建议先掌握 `ObjectProvider`。

## 6. 解决方案 3：scoped proxy（谨慎使用）

你可以把某个 scope 的 bean 包装成代理，然后把代理注入到 singleton：

- singleton 持有的是“代理”
- 代理在每次方法调用时去当前 scope 找真实对象

优点：调用方代码很干净  
缺点：引入代理语义，debug 成本上升；某些情况下会误以为自己拿到的是“真实对象”

学习阶段建议把它当作“了解存在即可”的方案。

## 7. 一句话自检

读完这一章你应该能回答：

1) “prototype 的语义到底是什么？”
2) “为什么直接注入 prototype 到 singleton 会得到同一个实例？”
3) “`ObjectProvider` 和 `@Lookup` 的差别是什么？”

下一章我们把 scope 与生命周期合起来讲：什么时候创建、什么时候初始化、什么时候销毁。
对应 Lab/Test：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part00_guide/SpringCoreBeansLabTest.java`
推荐断点：`AbstractBeanFactory#doGetBean`、`DefaultSingletonBeanRegistry#getSingleton`、`DefaultListableBeanFactory#doResolveDependency`

## 面试常问（prototype 注入陷阱）

- 常问：`prototype` 的真实语义是什么？为什么“prototype 注入 singleton”会像单例？
  - 答题要点：prototype 的语义是“每次向容器要都是新的”；但注入发生在 singleton 创建时，只解析一次导致实例被“冻结”。
- 常见追问：怎么修复？`ObjectProvider` / `@Lookup` / scoped proxy 什么时候用？
  - 答题要点：需要“每次用都新”→ provider/lookup；需要“按上下文动态解析”→ scoped proxy；关键是让解析发生在“使用时”，不是“创建 singleton 时”。
