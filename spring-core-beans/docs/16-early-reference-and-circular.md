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

如果你只关注“循环依赖能不能启动”，你会以为 early reference 只是“救活 setter 循环”的技巧。

但对读者 C 来说，真正关键的是这句话：

> **getEarlyBeanReference 解决的不是“引用能不能拿到”，而是“拿到的引用是否已经是最终形态（proxy/wrapper）”。**

为什么这很重要？

- 很多框架能力（AOP/事务/异步/缓存/安全）都会在 BPP 阶段把 bean 包装成 proxy（见 docs/31）。
- 循环依赖场景下，A 在创建中需要注入 B，B 也在创建中需要注入 A。
- 为了“救活”，容器会把 A 的一个引用提前暴露给 B（early exposure）。

问题来了：如果你提前暴露的是 **原始对象**，但最终对外暴露的是 **proxy**，那么：

- B 持有的是原始对象引用（绕过 proxy）
- 其他地方拿到的是 proxy
- 同一个 bean 在系统里出现两种形态 → 行为不一致、排障困难

`getEarlyBeanReference` 就是为了解决这个“early 与 final 不一致”的根源问题：让框架能在“提前暴露”时就给出代理版引用，从而让依赖方拿到的就是最终形态。

### 2.1 你应该把它与哪几个点一起记？

- `SmartInstantiationAwareBeanPostProcessor#getEarlyBeanReference`：给出 early proxy 的扩展点
- `BeanPostProcessor#postProcessAfterInitialization`：给出 final proxy 的常见扩展点
- 三层缓存：`singletonFactories`/`earlySingletonObjects`/`singletonObjects`（见 docs/09）

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

## 源码最短路径（call chain）

> 目标：在循环依赖场景下，把“三级缓存（singleton/early/factory）”与“raw vs wrapped 检查点”放回同一条最短调用链。

一条最常见、最有价值的最短栈（以 setter 循环依赖为例）：

- `AbstractAutowireCapableBeanFactory#doCreateBean("alpha", ...)`
  - `DefaultSingletonBeanRegistry#addSingletonFactory("alpha", ...)`  
    - **这里把 `singletonFactory` 放进三级缓存（为 early reference 做准备）**
  - `populateBean(...)`（开始属性填充，触发对 `beta` 的依赖解析与创建）
    - `doResolveDependency(...)` / `getBean("beta")`
      - `doCreateBean("beta", ...)`
        - `populateBean(...)`（beta 需要注入 alpha）
          - `DefaultSingletonBeanRegistry#getSingleton("alpha", ...)`  
            - **这里命中 early reference 分支（从三级缓存拿 early 引用）**
            - `AbstractAutowireCapableBeanFactory#getEarlyBeanReference(...)`（如果有 `SmartInstantiationAwareBeanPostProcessor`，会走到这里）
- `initializeBean(...)`（BPP after-init 可能会把 bean 替换成 proxy/wrapper）
- `doCreateBean(...)` 尾部的“raw vs wrapped”一致性检查  
  - **如果 early 引用是 raw，但最终暴露对象是 wrapped/proxy，容器可能会失败（fail fast）**

你只要把这条链路走通一次，就能把“三级缓存到底解决什么”与“为什么会有 raw vs wrapped 不一致”串成一条线。

## 固定观察点（watch list）

> 目标：在 `getSingleton` 与 `doCreateBean` 里，只看这些结构/变量，就能判断当前处于哪一层缓存、以及是否发生 raw vs wrapped 不一致。

建议在 `DefaultSingletonBeanRegistry#getSingleton(...)` 里 watch/evaluate：

- `singletonObjects`：一级缓存（完全初始化后的单例）
- `earlySingletonObjects`：二级缓存（提前暴露的 early singleton reference）
- `singletonFactories`：三级缓存（`ObjectFactory`，用于按需创建 early reference）
- `isSingletonCurrentlyInCreation(beanName)`：是否处于创建中（决定 early 分支是否可能发生）

建议在 `AbstractAutowireCapableBeanFactory#doCreateBean(...)` 尾部 watch/evaluate：

- `earlySingletonReference`：early 引用（如果发生了循环依赖/提前暴露，这里通常不为 null）
- `exposedObject`：最终暴露对象（可能已经被 after-init BPP 替换成 proxy）
- `hasDependentBean(beanName)` + `getDependentBeans(beanName)`：是否已有其他 bean 拿到过 early/raw 引用（决定是否触发 fail-fast）

> 小技巧：当你看到异常提示里出现 “raw version / wrapped” 关键词时，几乎可以直接定位到这个尾部检查点。

## 反例（counterexample）

**反例：我按“实现类”注入，但最终容器暴露的是 JDK proxy（wrapped），类型直接对不上。**

最小复现入口（必现，且错误信息直给“expected type vs actual proxy type”）：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansEarlyReferenceLabTest.java`
  - `injectingConcreteTypeFailsWhenFinalBeanIsJdkProxy_duringCircularDependency()`

你在断点里应该看到什么（用于纠错）：

- 你的注入点是 `ConcreteAlphaImpl`（实现类）
- 但容器最终暴露的 bean 可能是 JDK proxy（例如 `$Proxy...`，只实现接口）
- 因此注入阶段会直接失败：`BeanNotOfRequiredTypeException`（通常被 `UnsatisfiedDependencyException` 包一层）

正确做法（本章实验的成功路径）：

- 优先按接口注入（让 proxy 仍然满足类型约束），并把“调用链必须走代理”的心智模型打牢（见 [31](31-proxying-phase-bpp-wraps-bean.md)）
- 如果你确实必须按实现类注入：你需要 class-based proxy（或避免用会改变暴露类型的代理策略）
- 如果你在循环依赖场景还希望 early 与 final 形态一致：实现 `SmartInstantiationAwareBeanPostProcessor#getEarlyBeanReference(...)` 并保证 after-init 返回同一个 proxy  
  ⇒ 参见 `getEarlyBeanReference_canProvideEarlyProxyDuringCircularDependencyResolution()`

## 5. 一句话自检

- 你能解释清楚：为什么循环依赖场景下，容器需要一个“提前暴露的引用”？
- 你能解释清楚：`getEarlyBeanReference` 为什么必须跟“代理/包装”一起讲？
对应 Lab/Test：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansEarlyReferenceLabTest.java`
推荐断点：`DefaultSingletonBeanRegistry#getSingleton`、`AbstractAutowireCapableBeanFactory#getEarlyBeanReference`、`SmartInstantiationAwareBeanPostProcessor#getEarlyBeanReference`
