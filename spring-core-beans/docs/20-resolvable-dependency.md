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

## 3. 常见坑

- **坑 1：以为它会出现在 beans 列表里**
  - 不会。它不是 bean。

- **坑 2：以为它有 scope/lifecycle**
  - 它不是 bean，自然也没有完整的 bean 生命周期语义。

## 源码锚点（建议从这里下断点）

- `DefaultListableBeanFactory#registerResolvableDependency`：把“可解析但非 bean”的依赖放进特殊依赖表
- `DefaultListableBeanFactory#doResolveDependency`：依赖解析主流程（会优先检查 resolvableDependencies）
- `DependencyDescriptor#getDependencyType`：注入点抽象（字段/参数的类型信息从这里进入解析流程）
- `DefaultListableBeanFactory#findAutowireCandidates`：当 resolvableDependencies 未命中时，才会走“按 bean 候选集”找候选
- `AbstractBeanFactory#doGetBean`：`getBean(type)` 走的是 bean 查找链路，不会命中 resolvableDependencies（因此会失败）

## 断点闭环（用本仓库 Lab/Test 跑一遍）

入口：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansResolvableDependencyLabTest.java`
  - `registerResolvableDependency_enablesAutowiringWithoutRegisteringABean()`

建议断点：

1) `DefaultListableBeanFactory#registerResolvableDependency`：观察 NotABeanDependency 被放入哪张表（它不会变成 BeanDefinition）
2) `DefaultListableBeanFactory#doResolveDependency`：观察构造器参数解析时直接命中 resolvableDependencies 并返回 instance
3) `AbstractBeanFactory#doGetBean`（或测试里 `context.getBean(NotABeanDependency.class)` 那一行）：观察为什么它会抛 `NoSuchBeanDefinitionException`

## 排障分流：这是定义层问题还是实例层问题？

- “某个类型能注入，但 `getBean(type)` 拿不到” → **优先实例层（解析路径差异）**：它可能是 ResolvableDependency，而不是普通 bean（本章 Lab）
- “我想让它也出现在 beans 列表/支持 scope/lifecycle” → **定义层需求**：你需要注册 BeanDefinition（而不是 ResolvableDependency）（回看 [02](02-bean-registration.md)）
- “把业务对象塞进 ResolvableDependency 里导致难 debug” → **设计/使用问题**：ResolvableDependency 更适合容器级依赖（framework internal），业务对象更适合普通 bean（对照本章第 2 节）
- “依赖解析选错候选/歧义” → **实例层（候选解析）**：ResolvableDependency 只是其中一种来源，回到 [03](03-dependency-injection-resolution.md)/[33](33-autowire-candidate-selection-primary-priority-order.md)

## 4. 一句话自检

- 你能解释清楚：为什么它能被注入，但不能被 `getBean(type)` 拿到吗？
