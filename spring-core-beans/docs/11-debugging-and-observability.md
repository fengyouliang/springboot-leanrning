# 11. 调试与自检：如何“看见”容器正在做什么

理解 Spring 容器的最快方式，是让“不可见的机制”变得可观察。

这一章给你一个实用的调试工具箱，目标是：当你遇到“为什么注入的是它？”“为什么它没注册？”“为什么它是代理？”时，知道从哪里下手。

## 1. 最简单也最有效：查容器里到底有哪些 Bean

本模块的 lab 已经用过：

- `applicationContext.getBeansOfType(TextFormatter.class)`

对应测试：

- `SpringCoreBeansLabTest.containerCanProvideAllFormatterBeansByType()`

你可以把它升级为自己的调试习惯：

- 先确认“容器里有没有你以为的 bean”
- 再确认“候选有几个”
- 再回到注入点看 `@Qualifier/@Primary` 等规则

## 2. 进一步：看 BeanDefinition（定义层）

当你怀疑“注册阶段出了问题”（扫描范围不对、`@Import` 没生效、条件没满足）时，光看实例不够。

你需要去看：

- beanName 是否存在对应的 `BeanDefinition`
- scope、lazy、dependsOn 等元数据是什么

在本模块的容器实验里你已经看过：

- `context.getBeanFactory().getBeanDefinition("exampleBean")`

对应测试：

- `SpringCoreBeansContainerLabTest.beanDefinitionIsNotTheBeanInstance()`

## 3. Spring Boot 的“条件报告”：把自动装配的生效/失效原因打印出来

当你怀疑“自动配置没生效”或“多了我不认识的 bean”时，建议开启条件评估报告：

- 在运行参数里加 `--debug`
- 或在配置里开启 `debug=true`

它会告诉你：

- 哪些自动配置生效
- 哪些没生效
- 没生效的原因（哪个条件失败）

学习阶段你不需要记住每条报告格式，但要知道它存在，并且能回答“为什么”。

## 4. 日志：把容器行为“吵”出来

当你需要更细粒度地看依赖注入/bean 创建细节时，可以临时提高日志级别（建议只在学习/调试时使用）：

- `org.springframework.beans`
- `org.springframework.context`
- `org.springframework.boot.autoconfigure`

你会看到：

- bean 创建顺序
- 自动装配导入/条件判断的部分信息

## 5. 一个实用的自检流程（遇到 DI 问题就按这个来）

1) 看异常：是“没有候选”还是“候选太多”？
2) 用 `getBeansOfType()` 确认候选集合
3) 回到注入点检查：`@Qualifier/@Primary` 是否明确
4) 如果是自动装配相关：打开 `--debug` 看条件报告
5) 如果怀疑注册阶段：查 `BeanDefinition` 是否存在、scope/名称是否符合预期

## 6. 与本模块运行输出对齐

运行本模块：

```bash
mvn -pl spring-core-beans spring-boot:run
```

你会在输出中看到这些线索：

- `qualifier.formatterImplementation=...`
- `prototype.direct.sameId=...`
- `prototype.provider.differentId=...`
- `lifecycle.initialized=...`

如果这些输出与你的理解不一致，优先回到：

- [03. 依赖注入解析](03-dependency-injection-resolution.md)
- [04. Scope 与 prototype 注入陷阱](04-scope-and-prototype.md)
- [05. 生命周期](05-lifecycle-and-callbacks.md)

