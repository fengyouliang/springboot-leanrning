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

## 4. 一句话自检

- 你能解释清楚：为什么它能被注入，但不能被 `getBean(type)` 拿到吗？
