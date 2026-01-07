# 42. XML → BeanDefinitionReader：定义层解析与错误分型

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**42. XML → BeanDefinitionReader：定义层解析与错误分型**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

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

本模块提供最小 XML 示例：

- 正常 XML：成功注册 BeanDefinition，并能读取 definition 元信息
- 非法 XML：抛出 `BeanDefinitionStoreException`（用于你建立“错误分型”直觉）

入口测试：

---

把 XML 问题迅速收敛到 3 个层次（入口 → 解析 → 入库）：

1) 入口：`XmlBeanDefinitionReader#loadBeanDefinitions`（读资源 + 进入 XML 解析）
2) 解析：`DefaultBeanDefinitionDocumentReader#registerBeanDefinitions`（把 Document 变成一组 BeanDefinition）
   - 进一步深挖：`BeanDefinitionParserDelegate#parseBeanDefinitionElement`
3) 入库：`DefaultListableBeanFactory#registerBeanDefinition`（定义注册入口：冲突/覆盖/合法性检查）

当你需要把错误放回 refresh 主线理解时：

- `AbstractApplicationContext#refresh`
- `PostProcessorRegistrationDelegate#invokeBeanFactoryPostProcessors`

- `Resource` / `resourceDescription`：到底读的是哪一个 XML（路径/类路径资源/文件资源）
- `beanName` / `beanClassName`：解析到的定义是否符合预期
- `BeanDefinition` 的关键信息：scope、propertyValues、constructorArgumentValues
- 异常分型：是“XML 语法/命名空间解析失败”，还是“注册阶段合法性检查失败”

---

---

这一章你应该带走的能力是：

- 能把 XML 输入归一到 BeanDefinition 视角
- 能用 `BeanDefinitionStoreException` 快速判断“定义层失败”

- 容器外对象（不是 Spring 创建的）怎么做注入与生命周期托管？

---

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreBeansXmlBeanDefinitionReaderLabTest`
- 建议命令：`mvn -pl spring-core-beans test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 2. 复现入口（可运行）

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansXmlBeanDefinitionReaderLabTest.java`

推荐运行命令：

```bash
mvn -pl spring-core-beans -Dtest=SpringCoreBeansXmlBeanDefinitionReaderLabTest test
```

## 3. 源码 / 断点建议（把“看 XML”变成“走链路”）

建议观察点（下断点时优先盯这些变量）：

1) **误区：XML 问题只能靠“看 XML”解决**
   - 更有效：先分型（定义层 vs 实例层），再锁定断点入口。
2) **误区：XML = 过时，不用学**
   - 在真实项目里，遗留配置/三方组件/某些 starter 仍可能引入 XML 资源；排障时你必须认识链路。

## F. 常见坑与边界

## 4. 常见误区

下一章进入真实项目更常见的另一个坑：

## G. 小结与下一章

## 5. 小结与下一章预告

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreBeansXmlBeanDefinitionReaderLabTest`
- Test file：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansXmlBeanDefinitionReaderLabTest.java`

上一章：[41. RuntimeHints 入门：把构建期契约跑通](41-runtimehints-basics.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[43. 容器外对象注入：AutowireCapableBeanFactory](43-autowirecapablebeanfactory-external-objects.md)

<!-- BOOKIFY:END -->
