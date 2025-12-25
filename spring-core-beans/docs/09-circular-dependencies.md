# 09. 循环依赖：现象、原因与规避（constructor vs setter）

循环依赖是 Spring 学习路上绕不开的一关。它既是“容器能力的体现”，也是“架构设计的警报”。

这一章回答：

1) 为什么构造器循环依赖会失败？
2) 为什么 setter 循环依赖有时会成功？
3) 在工程里你应该怎么处理？

## 1. 两个最经典的环

### 1.1 构造器循环（通常失败）

本模块实验：

- `SpringCoreBeansContainerLabTest.circularDependencyWithConstructorsFailsFast()`

原因直观到一句话就够：

> 构造器注入要求依赖在“创建对象之前”就必须准备好，因此环上任何一环都无法先完成实例化。

### 1.2 setter 循环（有时能成功）

本模块实验：

- `SpringCoreBeansContainerLabTest.circularDependencyWithSettersMaySucceedViaEarlySingletonExposure()`

它能成功的关键在于 Spring 对 singleton 的一个机制：**提前暴露（early singleton exposure）**。

你可以把它理解为：

1) 容器创建 A（先 new 出来）
2) 发现 A 需要 B，于是去创建 B
3) 创建 B 时发现它需要 A
4) 如果容器允许，它可以把“一个尚未完全初始化的 A 引用（或一个工厂）”提前暴露给 B
5) B 创建完成后再回头把 B 注入 A

这是一种“让环先跑起来”的机制，但它也带来风险：你可能拿到半初始化对象，或者代理/增强顺序更复杂。

## 2. Spring Framework vs Spring Boot：一个重要差异

在纯 Spring Framework 容器里，setter 的单例循环依赖通常默认允许（如本模块实验所示）。

但在 Spring Boot 里，循环依赖在较新的版本中往往默认更严格（常见做法是默认禁止），并提供开关允许：

- `spring.main.allow-circular-references`

这也是为什么你会遇到：

- 同样的代码，单测用 `AnnotationConfigApplicationContext` 能过
- 放到 Boot 应用里就启动失败

学习时建议你把它当作“工具差异”，更重要的是理解机制与规避策略。

## 3. 工程上怎么处理（强烈建议按优先级）

### 3.1 首选：重构消除环（正确方向）

常见做法：

- 抽取一个更小的职责接口
- 把共享逻辑下沉到第三个组件
- 用事件/回调解耦（见 `spring-core-events`）

### 3.2 次选：用延迟依赖打断环（了解，谨慎）

例如：

- `ObjectProvider<T>`
- `@Lazy`（让某个依赖延迟初始化）

它们的本质都是：不要在“创建对象时”就强行拿到完整依赖，推迟到使用时再获取。

### 3.3 不推荐：为了让它“能启动”而改成 setter 注入

setter 注入在某些情况下能让环跑起来，但会：

- 降低不可变性
- 增加半初始化风险
- 让 bug 更隐蔽

## 4. 一句话自检

你应该能回答：

1) “构造器循环为什么必然失败？”
2) “setter 循环为什么有时能成功？early exposure 是什么？”
3) “为什么循环依赖在架构上通常是坏味道？”

下一章我们把这些概念和 Spring Boot 联系起来：自动装配如何“加入更多 bean”，从而让依赖图变复杂。

