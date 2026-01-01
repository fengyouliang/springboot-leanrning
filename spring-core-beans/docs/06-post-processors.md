# 06. 容器扩展点：BFPP vs BPP（以及它们能/不能做什么）

这一章是理解 Spring “高级玩法”的关键。很多你觉得像“魔法”的特性，本质都是某个 post-processor 在某个阶段做了事。

先记住一句话：

- **BFPP 改定义**（`BeanDefinition`）
- **BPP 改实例**（bean object / proxy）

## 1. BFPP：`BeanFactoryPostProcessor`

### 1.1 它在什么时候运行？

在容器已经收集完 `BeanDefinition` 之后、创建大部分 bean 之前运行。

因此它的典型能力是：

- 修改已有 `BeanDefinition`（属性、scope、依赖、lazy 等）
- （通过更底层的接口）注册额外的 `BeanDefinition`

### 1.2 本模块的实验：BFPP 修改定义再生效

对应测试：

- `SpringCoreBeansContainerLabTest.beanFactoryPostProcessorCanModifyBeanDefinitionBeforeInstantiation()`

实验做的事情是：

- 先注册 `ExampleBean` 的定义
- BFPP 在实例化前把 `value` 属性写进定义里
- 最终创建的实例读到了被修改的值

你需要体会的是：**BFPP 并没有直接“改对象”，而是改了“怎么创建对象的配方”。**

### 1.3 常见 BFPP（了解它们存在很重要）

你未来会经常遇到：

- 占位符/属性解析相关（把 `${...}` 换成真实值）
- 配置类处理（把 `@Configuration` / `@Bean` / `@Import` 解析成 BeanDefinition）

也就是说：很多“注解配置能工作”，背后本身就依赖 BFPP/registry post-processor。

## 2. BPP：`BeanPostProcessor`

### 2.1 它在什么时候运行？

在每个 bean 初始化前后都会被调用（更准确地说：在 bean 创建流程的某些钩子点）。

它的典型能力是：

- 修改 bean 实例的属性
- 用代理包装 bean（AOP 的基础）

### 2.2 本模块的实验：BPP 修改实例

对应测试：

- `SpringCoreBeansContainerLabTest.beanPostProcessorCanModifyBeanInstanceAfterInitialization()`

实验做的事情是：

- 工厂方法先创建一个 `ExampleBean`
- BPP 在初始化后把它的 `value` 改成新值
- 你从容器拿到的最终对象反映出修改

### 2.3 BPP 与“你以为的对象”之间的差距

这也是为什么很多时候你 debug 会发现：

- 你注入的类型看起来是 `MyService`
- 但运行时对象可能是 `MyService$$SpringCGLIB$$...` 或 JDK proxy

因为 BPP 有机会把实例替换成代理。

在真实项目里，这个“代理/增强”的典型实现就是 AutoProxyCreator（AOP/事务/缓存/安全等最终都会走到“BPP 替换 bean”这一层）。  
对应完整版本的容器主线与断点导航：见 `spring-core-aop/docs/07-autoproxy-creator-mainline.md`。

## 3. 顺序（Ordering）：为什么同一个扩展点里顺序也很重要

多个 BFPP/BPP 同时存在时，顺序会决定最终效果。

Spring 通常用这些规则决定顺序：

- `PriorityOrdered`（最优先）
- `Ordered`
- 没有顺序接口（最后）

学习阶段你不需要背接口继承树，但要知道：

- 顺序是可控的
- 顺序问题会导致“某些增强没生效 / 生效得很奇怪”

## 3.1 你必须补齐的第三类：`BeanDefinitionRegistryPostProcessor`（BDRPP）

很多人只分 BFPP 与 BPP，但真正做源码级排障时，你需要补齐第三类：

- **BDRPP：改的是“注册表”（registry）**
  - 能新增/删除/修改 `BeanDefinition`
  - 发生得更早：在 BFPP 之前（因此影响面更大）
  - 典型代表：`ConfigurationClassPostProcessor`（它让 `@Configuration/@Bean/@ComponentScan` 等能工作）

一旦你能分清这三类，你就能回答一类非常常见的问题：

> “这个 bean 到底是在什么时候、被谁注册进来的？”

## 3.2 源码级时间线：refresh 里它们到底在哪发生？

你可以把它们粗略放进 `AbstractApplicationContext#refresh` 的时间线（只记住关键点即可）：

1. **invoke BFPP/BDRPP**：先让“定义”稳定下来（能注册/改 BeanDefinition）
2. **register BPP**：把所有 BPP 注册进容器（后面创建 bean 时会用到）
3. **finishBeanFactoryInitialization**：开始创建非 lazy 的 singleton（此时 BPP 会大量介入）

这也是为什么：

- BFPP/BDRPP 更像“编译期改元数据”
- BPP 更像“运行期改对象/换代理”

## 3.3 断点闭环（用本仓库 Lab/Test 跑一遍）

建议用这些测试把“时机”变成手感（每个都对应非常典型的真实问题）：

- BFPP 影响定义，再影响实例：
  - `SpringCoreBeansContainerLabTest#beanFactoryPostProcessorCanModifyBeanDefinitionBeforeInstantiation`
- BPP 影响实例（甚至换成代理）：
  - `SpringCoreBeansContainerLabTest#beanPostProcessorCanModifyBeanInstanceAfterInitialization`
- 顺序规则（PriorityOrdered/Ordered/无序）：
  - `SpringCoreBeansPostProcessorOrderingLabTest`
- BDRPP 能在注册阶段加定义：
  - `SpringCoreBeansRegistryPostProcessorLabTest`
- 手工注册 BPP 的顺序陷阱：
  - `SpringCoreBeansProgrammaticBeanPostProcessorLabTest`

### 3.4 推荐断点（够用版）

- 入口时间线：
  - `AbstractApplicationContext#refresh`
  - `PostProcessorRegistrationDelegate#invokeBeanFactoryPostProcessors`
  - `PostProcessorRegistrationDelegate#registerBeanPostProcessors`
- 创建单个 bean 的主线（看 BPP 介入位置）：
  - `AbstractAutowireCapableBeanFactory#doCreateBean`
  - `AbstractAutowireCapableBeanFactory#initializeBean`

## 4. 典型误用与坑

### 4.1 在 BFPP 里 `getBean()` 触发提前实例化

BFPP 本该在“定义层”工作，如果你在里面直接拿 bean（实例层），可能会触发一些 bean 提前创建，导致：

- 后续的 BPP 没机会介入
- 生命周期回调顺序变得反直觉

### 4.2 BPP 写成“全局修改器”导致不可预测

如果你在 BPP 里对很多 bean 做复杂逻辑，会让系统变得：

- 难以推理
- 难以测试
- 难以 debug

学习阶段建议把 BPP 当作“理解容器机制”的窗口，而不是“解决业务问题的日常手段”。

下一章我们看一个特别常见、也特别容易误解的点：`@Configuration(proxyBeanMethods=...)`。
对应 Lab/Test：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansContainerLabTest.java`
推荐断点：`PostProcessorRegistrationDelegate#invokeBeanFactoryPostProcessors`、`PostProcessorRegistrationDelegate#registerBeanPostProcessors`、`AbstractAutowireCapableBeanFactory#applyBeanPostProcessorsAfterInitialization`
