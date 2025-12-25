# 08. `FactoryBean`：产品 vs 工厂（以及 `&` 前缀）

`FactoryBean` 是 Spring 里一个非常“老牌但重要”的扩展点，常见于各种框架集成（ORM、RPC、代理生成等）。

这一章解决的问题是：

> 为什么 `getBean("xxx")` 拿到的不是 `xxx` 这个类型本身，而是“它生产的对象”？

## 1. `FactoryBean` 的核心语义

当某个 bean 实现了 `FactoryBean<T>`：

- 容器默认把它当作“工厂”
- **按 beanName 获取时返回的是 `T`（产品）**
- 如果你想拿到工厂本身，需要在 beanName 前加 `&`

这就是很多人第一次碰到 `FactoryBean` 时的迷惑点。

## 2. 本模块的实验：用 `&sequence` 拿到工厂

对应测试：

- `SpringCoreBeansContainerLabTest.factoryBeanByNameReturnsProductAndAmpersandReturnsFactory()`

实验里定义了一个 `SequenceFactoryBean implements FactoryBean<Long>`：

- `getBean("sequence", Long.class)` 返回的是 Long（产品），并且每次调用递增
- `getBean("&sequence")` 返回的是 `SequenceFactoryBean`（工厂本身）

你需要记住的就是：

- `"name"` → product
- `"&name"` → factory

## 3. `FactoryBean` 常见用途（理解即可）

- 复杂对象的创建（需要大量配置、或创建过程昂贵）
- 与外部系统集成时，把“连接/代理对象的创建”封装成 bean
- 生成代理对象（你以为注入的是接口实现，其实是代理）

## 4. 常见坑

1) 你以为注册的是 `MyFactoryBean`，结果注入点按类型找不到  
   - 因为容器对外暴露的类型是它生产的 `T`
2) 你以为 `@Autowired MyFactoryBean` 能注入工厂  
   - 需要按 `&name` 或按工厂类型显式获取/注入（并不常见）
3) 你以为 `FactoryBean` 的 `isSingleton()` 决定工厂是不是单例  
   - 它影响的是“产品是否单例”，不是“工厂本身是否单例”（工厂通常也是单例 bean）

下一章我们讲一个更偏“容器内部”的现象：循环依赖。

