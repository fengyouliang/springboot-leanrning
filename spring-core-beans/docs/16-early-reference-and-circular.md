# 16. early reference 与循环依赖：getEarlyBeanReference 到底解决什么？

循环依赖是学习容器机制时绕不开的一块。

这一章聚焦一个非常关键但经常被忽略的入口：

- `SmartInstantiationAwareBeanPostProcessor#getEarlyBeanReference`

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansEarlyReferenceLabTest.java`

## 1. 现象：setter 循环依赖有时能成功

在 `SpringCoreBeansContainerLabTest` 里你已经见过：

- 构造器循环依赖通常会失败（无法创建任何一方）
- setter 循环依赖有时能成功

成功的关键在于：容器允许在“对象还没完全初始化完成”时，先暴露一个 **early singleton reference**。

## 2. getEarlyBeanReference：为什么需要它？

如果没有 getEarlyBeanReference，setter 循环依赖通常会用“原始对象引用”去填充依赖。

但真实系统里经常存在“包装/代理”需求（典型就是 AOP）：

- 你希望注入到别人那里的是“代理对象”
- 而不是“半成品的原始对象”

`getEarlyBeanReference` 的设计目的就是：

- 在循环依赖需要 early reference 的时候
- 也能返回“该 bean 最终应该暴露的形态”（例如 proxy）

## 3. 本模块的实验：让 early reference 直接变成 proxy

对应测试：

- `SpringCoreBeansEarlyReferenceLabTest.getEarlyBeanReference_canProvideEarlyProxyDuringCircularDependencyResolution()`

实验做的事：

- `Alpha` 与 `Beta` 用 setter 互相依赖
- 我们实现一个 `SmartInstantiationAwareBeanPostProcessor`
  - 在 `getEarlyBeanReference` 阶段为 `alpha` 创建 JDK proxy
  - 并在 `postProcessAfterInitialization` 阶段返回同一个 proxy，保证“最终形态一致”

你应该观察到：

- 循环依赖能够完成
- `alpha` 在容器里拿到的是 proxy
- `beta` 注入到的 `alpha` 也是同一个 proxy

## 4. 最容易踩的坑：early 和 final 不一致

如果你：

- early 阶段返回了原始对象
- final 阶段又返回了代理对象

容器可能会报类似错误（含义是）：

- 有别的 bean 已经拿到“原始对象”
- 但最终这个 bean 又被包装成了“代理对象”
- 系统出现“同一个 bean 两种形态并存”，容器默认会阻止这种不一致

学习阶段建议：

- 要么 early 与 final 都不包装
- 要么像本实验一样：**early 与 final 返回同一个 wrapper/proxy**

## 源码锚点（建议从这里下断点）

- `DefaultSingletonBeanRegistry#getSingleton`：单例获取入口（循环依赖时会出现 early reference 分支）
- `DefaultSingletonBeanRegistry#addSingletonFactory`：提前暴露“singletonFactory”的地方（为 early reference 做准备）
- `AbstractAutowireCapableBeanFactory#getEarlyBeanReference`：容器向 BPP 请求 early reference 的桥接点
- `SmartInstantiationAwareBeanPostProcessor#getEarlyBeanReference`：扩展点入口（让 early reference 也能是 proxy/wrapper）
- `AbstractAutowireCapableBeanFactory#doCreateBean`：创建主流程（在合适时机触发提前暴露与属性填充）

## 断点闭环（用本仓库 Lab/Test 跑一遍）

入口：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansEarlyReferenceLabTest.java`
  - `getEarlyBeanReference_canProvideEarlyProxyDuringCircularDependencyResolution()`

建议断点：

1) 你在 Lab 里实现的 `getEarlyBeanReference(...)`：观察 early 阶段返回的对象形态（proxy）
2) `AbstractAutowireCapableBeanFactory#getEarlyBeanReference`：观察容器在什么时候向 BPP 请求 early reference
3) `DefaultSingletonBeanRegistry#getSingleton`：观察循环依赖时“从三级缓存取 early reference”的分支
4) `BeanPostProcessor#postProcessAfterInitialization`（你在 Lab 里的实现）：确认 final 阶段返回的对象与 early 阶段一致

你应该看到：

- `beta` 注入到的 `alpha` 与容器最终暴露的 `alpha` 是同一个 proxy（same reference）

## 排障分流：这是定义层问题还是实例层问题？

- “构造器循环依赖失败” → **实例层（创建时机）**：构造器依赖发生在实例化之前，容器没机会提前暴露引用（回看 [09](09-circular-dependencies.md)）
- “setter 循环依赖也失败/报 raw vs wrapped 不一致” → **实例层（early vs final 形态不一致）**：检查 early 与 afterInit 是否返回同一个 proxy（本章第 4 节）
- “循环依赖解决了但拿到的类型变了（proxy）” → **实例层（代理语义）**：这是为了保证“最终暴露形态一致”，与 AOP/事务心智模型一致（见 [31](31-proxying-phase-bpp-wraps-bean.md)）
- “以为这只和循环依赖有关” → **实例层通用机制**：early reference 是为了解决“创建中暴露引用”，但核心仍是 BPP 能改变 bean 形态（见 [00](00-deep-dive-guide.md)）

## 5. 一句话自检

- 你能解释清楚：为什么循环依赖场景下，容器需要一个“提前暴露的引用”？
- 你能解释清楚：`getEarlyBeanReference` 为什么必须跟“代理/包装”一起讲？
