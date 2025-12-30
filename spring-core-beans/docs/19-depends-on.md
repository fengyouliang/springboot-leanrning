# 19. dependsOn：强制初始化顺序（即使没有显式依赖）

`dependsOn` 是容器提供的一个“强行排序”能力：

- 它解决的是**初始化顺序**问题
- 不是依赖注入（DI）问题

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansDependsOnLabTest.java`

## 1. 现象：两个互不依赖的 bean，也可以有固定初始化顺序

对应测试：

- `SpringCoreBeansDependsOnLabTest.dependsOn_forcesInitializationOrder_evenWithoutDirectDependencies()`

实验里：

- `Second` 并不注入 `First`
- 但 `Second` 的 bean definition 声明了 `dependsOn("first")`

因此容器会：

- 先初始化 `first`
- 再初始化 `second`

## 2. 常见用法（了解即可，别滥用）

你可能会在一些“基础设施”里看到它：

- 需要确保某个初始化逻辑先跑（例如注册某些全局资源）

但一般业务代码不推荐依赖它，因为它会让依赖关系“隐形”。

## 3. 常见坑

- **坑 1：把 dependsOn 当成 DI 手段**
  - dependsOn 不会把 `first` 注入到 `second` 里。

- **坑 2：过度使用导致容器拓扑不透明**
  - 学习阶段可以用它做实验；工程里请谨慎。

## 源码锚点（建议从这里下断点）

- `RootBeanDefinition#getDependsOn`：`dependsOn` 元数据来源（最终挂在 BeanDefinition 上）
- `AbstractBeanFactory#doGetBean`：创建 bean 之前会先处理 `dependsOn`（先 `getBean(dep)` 再创建当前 bean）
- `DefaultSingletonBeanRegistry#registerDependentBean`：记录依赖关系（影响销毁顺序、依赖图可观测性）
- `DefaultListableBeanFactory#preInstantiateSingletons`：非 lazy 单例批量创建期间也会触发 `dependsOn` 的顺序保证
- `DefaultSingletonBeanRegistry#isDependent`：容器用于判断依赖关系/避免重复依赖处理的辅助入口

## 断点闭环（用本仓库 Lab/Test 跑一遍）

入口：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansDependsOnLabTest.java`
  - `dependsOn_forcesInitializationOrder_evenWithoutDirectDependencies()`

建议断点：

1) `Second` / `First` 的构造器或 init 回调：观察最终的创建/初始化顺序
2) `RootBeanDefinition#getDependsOn`：确认 `second` 的定义上确实声明了 dependsOn
3) `AbstractBeanFactory#doGetBean`：观察创建 `second` 前会先触发 `getBean("first")`
4) `DefaultSingletonBeanRegistry#registerDependentBean`：观察容器把这条“隐式依赖”记录进依赖关系表

## 排障分流：这是定义层问题还是实例层问题？

- “我设置了 dependsOn，但顺序没变” → **优先定义层**：`dependsOn` 是否真的写进 `BeanDefinition`？beanName 是否写对？（看 `getDependsOn`）
- “我用 dependsOn 想让 `first` 自动注入到 `second`” → **不是注入问题，是概念误用**：dependsOn 只管顺序，不管 DI（回看本章开头）
- “启动/关闭顺序很怪，像是有隐式依赖” → **定义层 + 依赖关系问题**：排查 `dependsOn`/工厂内部注册的依赖（结合 [11](11-debugging-and-observability.md) 观察 bean 图）
- “出现依赖环（dependsOn A → B → A）” → **定义层问题**：这属于人为引入的拓扑环，建议回避而不是依赖容器“救场”

## 4. 一句话自检

- 你能解释清楚：dependsOn 解决的是什么问题？（初始化顺序，不是注入）
