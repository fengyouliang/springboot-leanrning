# 47. BeanDefinitionReader：除了注解与 XML，还有 Properties / Groovy

这一章解决一个“源码视角必须掌握，但现代项目里容易被忽略”的问题：

> **Spring 是怎么把不同输入源（注解、XML、properties、groovy）统一成 BeanDefinition 的？BeanDefinitionReader 到底干了什么？**

核心结论：

- **BeanDefinitionReader 只负责一件事：把某种输入源解析成 BeanDefinition，并注册进 BeanDefinitionRegistry。**
- 它通常不负责“实例化 bean”，实例化仍然由 BeanFactory/容器主线完成。

---

## 0. 复现入口（可运行）

入口测试：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansPropertiesBeanDefinitionReaderLabTest.java`
- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansGroovyBeanDefinitionReaderLabTest.java`

推荐运行命令：

```bash
mvn -pl spring-core-beans -Dtest=SpringCoreBeansPropertiesBeanDefinitionReaderLabTest test
mvn -pl spring-core-beans -Dtest=SpringCoreBeansGroovyBeanDefinitionReaderLabTest test
```

对应资源文件：

- `spring-core-beans/src/test/resources/part05_aot_and_real_world/reader/beans.properties`
- `spring-core-beans/src/test/resources/part05_aot_and_real_world/reader/beans.groovy`

---

## 1. 是什么：为什么要有 BeanDefinitionReader 家族？

从 beans 体系角度看，Spring 的强大来自“输入多样但输出统一”：

- 输入可以是：注解、`@Bean`、`@Import`、XML、properties、groovy DSL、甚至程序化注册……
- 但最终都会归一为：**BeanDefinition（定义层）**

BeanDefinitionReader 的价值在于：

> 让“新的输入源”以插件形式接入容器定义层，而不用改容器核心。

---

## 2. 怎么用：两种典型 reader 的最小闭环

### 2.1 PropertiesBeanDefinitionReader（遗留/轻量输入）

适用场景：

- 遗留项目（非常早期的 Spring 配置风格）
- 教学/快速 demo：用最少语法表达“定义 → 注入”

本仓库的最小示例：

- reader：`PropertiesBeanDefinitionReader`
- registry：`DefaultListableBeanFactory`
- 输入：`beans.properties`

你应该观察到：

- reader 先把 properties 解析成 BeanDefinition 并注册
- `getBean()` 时才会创建实例并完成属性填充

### 2.2 GroovyBeanDefinitionReader（DSL 输入）

适用场景：

- DSL 风格配置（历史上常见于 Spring 生态中的脚本化配置）
- 你想把“定义层输入”做成更可读的脚本

本仓库的最小示例：

- reader：`GroovyBeanDefinitionReader`
- registry：`GenericApplicationContext`
- 输入：`beans.groovy`

依赖说明：

- `GroovyBeanDefinitionReader` 位于 Spring beans 包中，但运行时需要 Groovy 运行库
- 本仓库已在 `spring-core-beans/pom.xml` 以 test scope 引入 `org.apache.groovy:groovy:4.0.21`，确保 Lab 可运行

---

## 3. 原理：Reader 把“输入”落到定义层主线的哪个位置？

你可以把 Reader 放回容器主线去理解：

1) 你选择某个输入源（properties/groovy/xml/annotations）
2) 对应的 Reader 把它解析为 **BeanDefinition** 并注册进 Registry（定义层）
3) 之后你 refresh context 或调用 getBean：
   - BeanFactory 根据定义创建实例（实例层）
   - 执行注入、回调、BPP 等（生命周期链路）

所以 Reader 解决的是“定义从哪里来”的问题，而不是“对象怎么创建/怎么被代理”的问题。

---

## 4. 怎么实现的：断点入口与观察点（从 reader 到 registry）

建议断点（两条 reader 共通的收敛点）：

- `AbstractBeanDefinitionReader#loadBeanDefinitions`（reader 抽象入口）
- `DefaultListableBeanFactory#registerBeanDefinition`（定义入库统一入口）

Properties reader 的典型断点：

- `PropertiesBeanDefinitionReader#loadBeanDefinitions`

Groovy reader 的典型断点：

- `GroovyBeanDefinitionReader#loadBeanDefinitions`

建议观察点：

- 注册了哪些 beanName（数量/名称是否符合预期）
- BeanDefinition 的 beanClassName / propertyValues / constructorArgs
- refresh/getBean 的时机：你是否把“注册定义”和“创建实例”混为一谈

---

## 5. 常见误区

1) **误区：Reader = 创建对象**
   - Reader 注册的是“配方”（BeanDefinition），对象创建发生在后续主线。
2) **误区：我写的是 Groovy/Properties，所以不属于 beans 体系**
   - 恰恰相反：这些机制说明 beans 体系的抽象能力（输入可扩展，输出统一）。

---

上一章：[46. XML namespace 扩展：NamespaceHandler / Parser / spring.handlers](46-xml-namespace-extension.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[48. 方法注入：replaced-method / MethodReplacer（实例化策略分支）](48-method-injection-replaced-method.md)
