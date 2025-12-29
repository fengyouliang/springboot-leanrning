# 13. BeanDefinitionRegistryPostProcessor：在“注册阶段”动态加定义

这一章聚焦一个比 BFPP 更“早、更强”的扩展点：

- `BeanDefinitionRegistryPostProcessor`（简称 BDRPP）

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansRegistryPostProcessorLabTest.java`

## 1. 心智模型：先有“定义”，后有“实例”

容器启动阶段的关键流程可以粗略理解为：

1) 收集/注册 `BeanDefinition`
2) 运行 post-processors（可能改定义、加定义）
3) 实例化单例 bean（`preInstantiateSingletons`）

BDRPP 的价值在于：它可以在 **第 1 步和第 2 步之间** 动态注册新的 `BeanDefinition`。

## 2. 现象：你没有显式注册 bean，但它依然出现了

`SpringCoreBeansRegistryPostProcessorLabTest.beanDefinitionRegistryPostProcessor_canRegisterNewBeanDefinitions()` 里：

- 你只注册了一个 BDRPP
- BDRPP 在 `postProcessBeanDefinitionRegistry(...)` 里注册了 `registeredBean` 的定义
- refresh 之后，你能直接 `getBean(RegisteredBean.class)`

这说明：**BDRPP 能把“定义”塞进容器，从而让 bean 真正成为容器的一部分**。

## 3. 顺序：BDRPP 先于普通 BFPP

`SpringCoreBeansRegistryPostProcessorLabTest.bdrppRunsBeforeRegularBeanFactoryPostProcessor()` 里展示：

- BDRPP 先注册一个 `BeanDefinition`
- 之后 BFPP 再修改这个 `BeanDefinition` 的属性
- 最终实例化出的对象反映了 BFPP 的修改结果

你应该记住：

- **BDRPP 能“新增定义”**
- **BFPP 更常见的用途是“修改定义”**

## 4. 常见坑

- **坑 1：在 BDRPP/BFPP 里 `getBean()` 触发提前实例化**
  - post-processor 阶段本质是“定义层”的工作。
  - 如果你在这里强行拿实例，可能导致：
    - 某些 BPP 没机会介入
    - 生命周期顺序变得反直觉

- **坑 2：beanName 冲突**
  - BDRPP 动态注册时必须保证名称唯一，否则会覆盖或直接报错（取决于容器配置）。

## 5. 一句话自检

- 你能解释清楚：为什么 BFPP 能修改 BDRPP 注册的定义？（提示：因为 BDRPP 更早）
