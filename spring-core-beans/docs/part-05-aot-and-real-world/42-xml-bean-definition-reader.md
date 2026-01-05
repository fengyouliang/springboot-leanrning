# 42. XML → BeanDefinitionReader：定义层解析与错误分型

这一章解决一个“你不一定天天写，但你一定会遇到”的问题：

> **当你看到 `BeanDefinitionStoreException`、`BeanDefinitionParsingException`、或者某个 bean “定义层”就读不进来时，应该从哪里下手？**

Spring 的 IoC 容器把所有配置来源（注解、`@Bean`、`@Import`、XML、程序化注册……）最终都归一到：

> **BeanDefinition（定义层）**

XML 只是其中一种输入形式。理解它的价值在于：它能让你更清晰地区分“定义层失败”与“实例层失败”。

---

## 1. 结论先行：XML 的价值不在“写法”，而在“链路”

XML 这条链路的核心是：

- `XmlBeanDefinitionReader#loadBeanDefinitions`：把 XML 读成 BeanDefinition，并注册到 BeanFactory
- 注册成功之后，后续仍走统一主线：refresh → instantiate → populate → initialize

因此你遇到 XML 相关异常时，第一件事就是分型：

- **定义层异常**：读/解析/注册阶段失败（refresh 前半段）
- **实例层异常**：创建/注入/初始化阶段失败（refresh 后半段或 getBean 时）

---

## 2. 复现入口（可运行）

本模块提供最小 XML 示例：

- 正常 XML：成功注册 BeanDefinition，并能读取 definition 元信息
- 非法 XML：抛出 `BeanDefinitionStoreException`（用于你建立“错误分型”直觉）

入口测试：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansXmlBeanDefinitionReaderLabTest.java`

推荐运行命令：

```bash
mvn -pl spring-core-beans -Dtest=SpringCoreBeansXmlBeanDefinitionReaderLabTest test
```

---

## 3. Debug / 断点建议

把 XML 问题迅速收敛到 2 个入口：

- `XmlBeanDefinitionReader#loadBeanDefinitions`（读/解析/注册主入口）
- `DefaultListableBeanFactory#registerBeanDefinition`（定义注册入口：冲突/覆盖/合法性检查）

当你需要把错误放回 refresh 主线理解时：

- `AbstractApplicationContext#refresh`
- `PostProcessorRegistrationDelegate#invokeBeanFactoryPostProcessors`

---

## 4. 常见误区

1) **误区：XML 问题只能靠“看 XML”解决**
   - 更有效：先分型（定义层 vs 实例层），再锁定断点入口。
2) **误区：XML = 过时，不用学**
   - 在真实项目里，遗留配置/三方组件/某些 starter 仍可能引入 XML 资源；排障时你必须认识链路。

---

## 5. 小结与下一章预告

这一章你应该带走的能力是：

- 能把 XML 输入归一到 BeanDefinition 视角
- 能用 `BeanDefinitionStoreException` 快速判断“定义层失败”

下一章进入真实项目更常见的另一个坑：

- 容器外对象（不是 Spring 创建的）怎么做注入与生命周期托管？

---

上一章：[41. RuntimeHints 入门：把构建期契约跑通](41-runtimehints-basics.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[43. 容器外对象注入：AutowireCapableBeanFactory](43-autowirecapablebeanfactory-external-objects.md)

