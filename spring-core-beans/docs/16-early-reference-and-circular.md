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

## 5. 一句话自检

- 你能解释清楚：为什么循环依赖场景下，容器需要一个“提前暴露的引用”？
- 你能解释清楚：`getEarlyBeanReference` 为什么必须跟“代理/包装”一起讲？
