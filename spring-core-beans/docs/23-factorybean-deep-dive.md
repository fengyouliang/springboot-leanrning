# 23. FactoryBean 深潜：product vs factory、类型匹配、以及 isSingleton 缓存语义

`FactoryBean` 是 Spring 里非常“容器味”的机制：

- 这个 bean 本身是工厂
- 容器对它有特殊对待

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansFactoryBeanDeepDiveLabTest.java`
- （基础版）`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansContainerLabTest.java`（`factoryBeanByNameReturnsProductAndAmpersandReturnsFactory`）

## 1. 最重要的规则：`&` 前缀

给定一个 FactoryBean 的 beanName（例如 `valueFactory`）：

- `getBean("valueFactory")` 拿到的是 **product**（`getObject()` 的返回值）
- `getBean("&valueFactory")` 拿到的是 **factory**（FactoryBean 自身）

对应测试：

- `SpringCoreBeansFactoryBeanDeepDiveLabTest.factoryBeanProductParticipatesInTypeMatching_andIsRetrievedByProductType()`

## 2. product 也参与“按类型查找”

因为 FactoryBean 会声明：

- `getObjectType()`：它生产的对象类型

所以你可以：

- `getBean(Value.class)` 拿到 product（即使容器里没有直接注册 `Value` 的 BeanDefinition）

这也是为什么 `FactoryBean` 经常被用在：

- 把“复杂构建逻辑”封装成一个容器可管理的工厂

## 3. isSingleton 的语义：容器是否缓存“product”

对应测试：

- `SpringCoreBeansFactoryBeanDeepDiveLabTest.singletonFactoryBeanProduct_isCached_byTheContainer()`
- `SpringCoreBeansFactoryBeanDeepDiveLabTest.nonSingletonFactoryBeanProduct_isNotCached_byTheContainer()`

你应该观察到：

- 当 `isSingleton() == true`：多次 `getBean(Value.class)` 返回同一个 product 实例
- 当 `isSingleton() == false`：每次 `getBean(Value.class)` 都会重新调用 `getObject()` 产生新实例

学习重点：

- **isSingleton 控制的是 product 的缓存语义**
- factory bean 自己通常仍然是容器管理的 singleton（除非你显式把它定义成 prototype）

## 4. 常见坑

- **坑 1：`getObjectType()` 返回 null 或者返回不准**
  - 会影响按类型匹配与某些条件判断。

- **坑 2：`isSingleton()` 返回与真实行为不一致**
  - 容器会按你声明的语义缓存/不缓存；声明错了很容易造成“看起来像缓存 bug”。

## 源码锚点（建议从这里下断点）

- `AbstractBeanFactory#getObjectForBeanInstance`：处理 “FactoryBean 的 product vs factory” 分流（`&` 前缀的核心路径）
- `BeanFactoryUtils#isFactoryDereference`：判断 beanName 是否带 `&`（理解为什么 `&name` 拿到的是工厂）
- `FactoryBeanRegistrySupport#getObjectFromFactoryBean`：调用 `FactoryBean#getObject()` 并决定是否缓存 product
- `FactoryBeanRegistrySupport#getCachedObjectForFactoryBean`：product 的缓存入口（与 `isSingleton()` 语义直接相关）
- `FactoryBean#getObjectType`：product 的类型声明入口（影响 type matching 与条件判断）

## 断点闭环（用本仓库 Lab/Test 跑一遍）

入口：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansFactoryBeanDeepDiveLabTest.java`
- （基础版）`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansContainerLabTest.java`（`factoryBeanByNameReturnsProductAndAmpersandReturnsFactory`）

建议断点：

1) 你在 Lab 里的 `FactoryBean#getObject()` / `getObjectType()` / `isSingleton()`：观察 product 创建次数与类型声明
2) `AbstractBeanFactory#getObjectForBeanInstance`：观察 `getBean("name")` 与 `getBean("&name")` 在这里分叉
3) `FactoryBeanRegistrySupport#getObjectFromFactoryBean`：观察容器何时调用 `getObject()`，以及返回值如何被处理
4) `FactoryBeanRegistrySupport#getCachedObjectForFactoryBean`：对照 `isSingleton()` 为 true/false 时缓存是否命中

## 排障分流：这是定义层问题还是实例层问题？

- “我 `getBean("name")` 拿到的不是工厂而是产品” → **实例层（FactoryBean 语义）**：这是 Spring 的特殊规则；要拿工厂请用 `&name`（本章第 1 节）
- “按类型发现/条件装配行为很怪” → **定义层（类型元数据）**：检查 `getObjectType()` 是否可靠（见 [29](29-factorybean-edge-cases.md)）
- “product 缓存像是坏了/每次 get 都创建新对象” → **实例层（缓存语义）**：检查 `isSingleton()` 返回值是否与你期望一致（本章第 3 节）
- “以为 factory 的 scope 就等于 product 的 scope” → **实例层概念澄清**：`isSingleton()` 控制的是 product 缓存，不是 factory 自己的 scope（本章第 3 节）

## 5. 一句话自检

- 你能解释清楚：为什么 `&beanName` 可以拿到 factory 自己吗？
- 你能解释清楚：`isSingleton()` 控制的是“product 是否缓存”而不是“factory 是否单例”吗？
