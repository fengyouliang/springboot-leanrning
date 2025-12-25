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

## 3. 顺序（Ordering）：为什么同一个扩展点里顺序也很重要

多个 BFPP/BPP 同时存在时，顺序会决定最终效果。

Spring 通常用这些规则决定顺序：

- `PriorityOrdered`（最优先）
- `Ordered`
- 没有顺序接口（最后）

学习阶段你不需要背接口继承树，但要知道：

- 顺序是可控的
- 顺序问题会导致“某些增强没生效 / 生效得很奇怪”

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

