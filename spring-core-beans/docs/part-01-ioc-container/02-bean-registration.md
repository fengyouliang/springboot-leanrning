# 02. Bean 注册入口：扫描、@Bean、@Import、registrar

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**02. Bean 注册入口：扫描、@Bean、@Import、registrar**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

这一章解决的问题是：**一个 Bean 是怎么“进入容器”的？**  
你会看到：Spring 的“注册入口”不止 `@Component`。理解这些入口，是理解 Spring Boot 自动装配、以及各种框架“魔法”的前提。

## 1. 先把“注册”说清楚

“注册 Bean”在 Spring 语境下，通常意味着：

- 向容器注册一个 `BeanDefinition`（定义层）
- 或者告诉容器“将来需要创建这种 bean”（最终仍会落到定义层/工厂方法）

反过来说：**只要能产生 BeanDefinition，理论上就能注册 Bean**。这也是 Spring 扩展能力强的根本原因。

## 2. 最常见入口：组件扫描（`@ComponentScan` / stereotype）

你在本模块里已经用到了：

- `@Component`：`BeansDemoRunner`、`DirectPrototypeConsumer`、`ProviderPrototypeConsumer`、`LifecycleLogger`
- `@Service`：`FormattingService`
- `@Component("beanName")`：`UpperCaseTextFormatter` / `LowerCaseTextFormatter`

组件扫描的核心思想是：

- 扫描 classpath
- 找到符合条件的类
- 为每个候选类创建一个 `BeanDefinition`
- 注册进容器

1) **扫描范围**（base package）决定了“你以为存在的 bean”是否真的存在  
2) 扫描产生的 beanName 有默认规则（通常是类名首字母小写），你也可以显式指定

### 2.1 include/exclude filters：把“扫描”从黑盒变成可控工具

很多项目遇到“为什么这个类被扫进来了/为什么没扫进来”，本质都在这三件事上：

- basePackages 是否覆盖到目标类
- 默认过滤器（stereotype 注解）是否启用
- include/exclude filters 是否额外收窄/扩展了候选

- stereotype（`@Component/@Service`）如何变成候选
- `@Component("explicitName")` 如何影响 beanName
- `excludeFilters` 能如何让“明明标了 @Component 的类”不进入容器

## 3. 另一条大路：`@Configuration` + `@Bean`

`@Bean` 方法也是注册入口：

- `@Bean` 方法并不是“立即执行创建对象”
- 它首先被解析成定义（例如：beanName 默认是方法名）
- 在后续实例化阶段才会调用工厂方法创建实例

一个重要的工程实践是：

- 在 `@Bean` 方法里通过“方法参数”声明依赖（推荐）
- 避免在方法体里直接调用另一个 `@Bean` 方法（除非你真的理解 `proxyBeanMethods` 的语义）

这一点会在 [07 章](07-configuration-enhancement.md) 展开。

## 4. `@Import`：把“注册入口”组合起来

`@Import` 可以把另一个配置（或一组配置）引入当前配置。它是很多 `@EnableXxx` 的底层实现方式之一。

`@Import` 常见三种用法（理解概念即可）：

### 4.1 直接 import 配置类（最直观）

```java
@Configuration
@Import(OtherConfig.class)
class AppConfig {}
```

这就像把 `OtherConfig` 也当作配置来源参与解析与注册。

### 4.2 import `ImportSelector`（用代码决定“导入哪些配置”）

`ImportSelector` 的任务是：**在配置类解析阶段**返回一组要导入的“配置类全限定名”，让 Spring 把这些配置类也纳入同一条解析/注册主线。

#### 4.2.1 为什么很多初学者看完还是“不知道怎么用/也不知道它在干什么”

站在初学者视角，`ImportSelector` 容易“读懂一句话，但仍不会用”，通常是因为下面这些认知断层：

1) **你以为它“注册 Bean”，但它真正返回的是“配置类名”**  
   它不直接往容器里塞一个 bean；它返回“下一步要解析的配置来源”。  
   后面真正产出 `BeanDefinition` 的，仍然是配置类解析器（把返回的配置类继续解析）。

3) **真实项目里它常常被 `@EnableXxx`/starter 包起来，你根本看不到它**  
   你写的是 `@EnableSomething`，但真正决定导入列表的是它背后的 selector（Boot 自动装配就是一个大号版本：DeferredImportSelector）。

最小闭环通常由 4 个部件组成：

#### 4.2.3 原理：把现象放回容器主线（它发生在哪个阶段？产物是什么？）

把它放回 refresh 主线，你会更容易把“魔法入口”还原成确定步骤：

你会发现：`ImportSelector` 的“产物”不是 bean，而是**“更多配置输入”**。它改变的是“定义层的输入集合”，而不是“实例层的行为”。

- `ConfigurationClassPostProcessor#processConfigBeanDefinitions`（配置解析总入口）
- `ConfigurationClassParser#processImports`（处理 `@Import` 的主分支）
- 你的 `ImportSelector#selectImports`（观察返回的 class names）
- `ConfigurationClassBeanDefinitionReader#loadBeanDefinitionsForConfigurationClass`（把解析模型落到 BeanDefinitionRegistry）
- `DefaultListableBeanFactory#registerBeanDefinition`（最终入库）

- `importingClassMetadata.getClassName()`：是谁触发了 import（哪个 `@EnableXxx`）
- `importingClassMetadata.getAnnotationAttributes(...)`：注解属性是否读取正确
- `environment.getProperty(...)`：条件输入是否符合预期（missing/false/true 的三态尤其重要）
- `selectImports(...)` 的返回数组：导入列表是否命中你预期的分支
- 最终容器里是否出现目标 bean：`context.containsBean("...")` / `getBean(...)`

### 4.3 import `ImportBeanDefinitionRegistrar`（最强，也最容易滥用）

`ImportBeanDefinitionRegistrar` 允许你直接对 `BeanDefinitionRegistry` 操作：

- 你可以用代码注册任意数量、任意形态的 `BeanDefinition`
- 也可以读取 `@EnableXxx` 自己的注解属性，然后据此注册 bean

这就是“很多框架看起来像魔法”的来源：它们把配置转成 BeanDefinition 并注册。

常见风险：

## 5. registrar / post-processor：到底谁更“底层”？

你会在资料里看到：

- `ImportBeanDefinitionRegistrar`
- `BeanDefinitionRegistryPostProcessor`
- `BeanFactoryPostProcessor`

可以这样理解优先级（从“更早、更偏定义层”到“更晚、开始接触实例”）：

1) **配置类解析阶段的 import/registrar**：用于“导入配置/注册定义”
2) `BeanDefinitionRegistryPostProcessor`：也能注册定义，通常在 refresh 很早期执行
3) `BeanFactoryPostProcessor`（BFPP）：主要用于“修改已有定义”
4) `BeanPostProcessor`（BPP）：开始触达“实例层”

## 6. Spring Boot 自动装配：本质上是“批量 @Import”（但更复杂）

理解 `@Import` 后，Boot 自动装配就不会那么“玄学”了：

- `@SpringBootApplication` 里包含了 `@EnableAutoConfiguration`
- `@EnableAutoConfiguration` 的核心实现是通过（Deferred）ImportSelector 导入一组“自动配置类”
- 这些自动配置类本身也是配置来源，会注册大量 BeanDefinition（通常带各种 `@Conditional...`）

更详细内容见：

- [10. Spring Boot 自动装配如何影响 Bean](../part-02-boot-autoconfig/10-spring-boot-auto-configuration.md)

## 8. 你应该能做到的“迁移练习”（强烈推荐）

1) 用 `@Import(SomeConfig.class)` 引入一个额外 `@Bean`
2) 写一个最小 `ImportSelector`，根据某个系统属性决定导入 `UpperCaseTextFormatter` 还是 `LowerCaseTextFormatter`

如果你不确定“练习题该怎么写才算闭环”，可以先对照本仓库的 Solution：

## 9. 源码解析：这些“注册入口”最终如何落到 BeanDefinitionRegistry

这一节把“入口名字”翻译成“Spring 源码主线”：

- 你写下的扫描 / `@Bean` / `@Import` / registrar，最终都会在**定义层**变成 `BeanDefinition`，并通过 `BeanDefinitionRegistry` 写入容器
- 在 `AnnotationConfigApplicationContext` 这类典型容器里，定义层的核心推进者是：`ConfigurationClassPostProcessor`（它本质是一个 BDRPP）

> 说明：这里的“源码解析”以 Spring Framework 的稳定主线为准，不对某个小版本的内部细节做强绑定。

### 9.1 总主线（从 refresh 到“定义入库”）

在容器启动时，配置解析与定义注册发生在 refresh 的早期阶段（定义层）：

1) `AbstractApplicationContext#refresh`
2) `PostProcessorRegistrationDelegate#invokeBeanFactoryPostProcessors`
3) `ConfigurationClassPostProcessor#postProcessBeanDefinitionRegistry`
4) `ConfigurationClassPostProcessor#processConfigBeanDefinitions`

你只要抓住一个事实就够了：**`ConfigurationClassPostProcessor` 会把“各种 inputs”解析成 BeanDefinition 并注册。**

### 9.2 扫描（`@ComponentScan` / stereotype）到底是谁在扫

扫描并不是“Spring 启动时自动扫一遍 classpath”，而是：

- 配置类解析阶段发现了 `@ComponentScan`（或隐式的扫描配置）
- 然后调用扫描器把候选类转成 `BeanDefinition` 并注册

- `ComponentScanAnnotationParser`（解析 `@ComponentScan` 元信息）
- `ClassPathBeanDefinitionScanner#doScan`（真正执行扫描）
- `ClassPathScanningCandidateComponentProvider`（找到候选）
- `BeanNameGenerator`（决定默认 beanName）

仓库中的扫描示例（`src/main/java`，最小片段）：

```java
@Component("upperFormatter")
public class UpperCaseTextFormatter implements TextFormatter { ... }
```

它最终会变成一个“基于 class 的 BeanDefinition”（一般能在 definition 中看到 beanClassName，以及 resource/source 的元信息）。

### 9.3 `@Configuration` + `@Bean`：为什么说“@Bean 先变成定义，后执行工厂方法”

`@Bean` 方法本质上是“一个工厂方法定义”。在定义层它会被记录为：

- beanName（默认是方法名）
- factoryBeanName（哪个配置类提供）
- factoryMethodName（哪个方法创建）

关键参与者：

- `ConfigurationClassParser`：把配置输入解析成配置模型
- `ConfigurationClassBeanDefinitionReader`：把模型“落到 BeanDefinitionRegistry”

```java
@Configuration
static class ImportedConfiguration {
    @Bean
    ImportedMarker importedMarker() { ... }
}
```

你在 `BeanDefinition` 上看到 `factoryMethodName=importedMarker` 时，就应该立刻联想到：**这是“工厂方法定义”，并不是“扫描出来的类定义”。**

### 9.4 `@Import` / ImportSelector / Registrar：为什么它们像“框架魔法入口”

`@Import` 发生在配置类解析阶段，它会把“额外配置来源”拼进同一条定义注册主线里。

你只需要掌握三种模式的本质差异：

1) **import 配置类**：把另一个配置类当作输入（最终它的 `@Bean` 也会变成 BeanDefinition）
2) **import selector**：在解析阶段返回“要导入的配置类列表”（Boot 自动装配是它的加强版：DeferredImportSelector）
3) **import registrar**：直接拿到 `BeanDefinitionRegistry`，用代码注册任意定义（最强也最容易滥用）

```java
static class RegisteredMessageRegistrar implements ImportBeanDefinitionRegistrar {
    @Override
    public void registerBeanDefinitions(AnnotationMetadata meta, BeanDefinitionRegistry registry) { ... }
}
```

你可以把 registrar 记成一句话：**它跳过“注解到定义”的自动推导过程，直接把定义写进容器。**

### 9.5 真实排障：如何从 BeanDefinition 反推“注册入口”

当你问“这个 bean 到底是谁注册的？”时，优先从 `BeanDefinition` 这几项入手：

- `beanClassName`：更像扫描/直接类定义
- `factoryBeanName + factoryMethodName`：几乎可以肯定来自 `@Bean` 工厂方法
- `resourceDescription`：很多情况下能提示来自哪个配置资源
- `source`：可能是注解元数据/方法元数据（用于进一步追根）

本模块已有可复用的小工具（测试辅助类）可以 dump 这些信息：

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`SpringCoreBeansComponentScanLabTest` / `SpringCoreBeansImportLabTest`
- 建议命令：`mvn -pl spring-core-beans test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 0. 复现入口（可运行）

- 入口测试（推荐先跑通再下断点）：
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansComponentScanLabTest.java`
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansImportLabTest.java`
- 推荐运行命令：
  - `mvn -pl spring-core-beans -Dtest=SpringCoreBeansComponentScanLabTest test`

最小可复现实验（推荐先跑再下断点）：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansComponentScanLabTest.java`

你在这个 Lab 里应该能断言并复述：

它的本质不是“运行时动态装配”，而是**配置类解析阶段**的一部分（仍然属于“定义层”）。

2) **你以为它是运行时机制，但它发生在“定义层（解析阶段）”**  
   `ImportSelector` 的执行时机很早，早到还没有进入“实例化 Bean”的主线。  
   所以你用它的时候，心智模型应该是：**它改变的是“未来将有哪些 BeanDefinition”，不是“现有 Bean 的行为”**。

4) **缺少一个“最小闭环”会让人完全抓不住**  
   对初学者来说，重要的不是“接口名”，而是：放在哪、怎么触发、返回什么、跑完看到什么现象、怎么下断点证明。

#### 4.2.2 最小可运行写法（你可以把它当成“可控版自动装配”）

- 一个 `@EnableXxx` 注解（用 `@Import(YourSelector.class)` 把 selector 挂上去）
- 一个 `ImportSelector`（读取注解属性/环境属性，返回配置类名数组）
- 两个（或多个）候选配置类（分别提供不同 Bean）
- 一个可运行入口（Lab/Test）

本仓库已经把这 4 件套做成了可运行的 Lab：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansImportLabTest.java`
  - `importSelectorChoosesConfigurationBasedOnEnvironmentProperty()`

你可以先把它当成“读得懂的答案”，再回过头写 Exercise（见本章第 8 节）。

1) `ConfigurationClassPostProcessor`（本质是一个 BDRPP）在 refresh 早期运行  
2) 它驱动 `ConfigurationClassParser` 解析配置类  
3) 解析到 `@Import` 时，会进入 import 处理分支  
4) 如果 import 的是 `ImportSelector`：  
   - Spring 实例化 selector（并回填 `Environment`/`ResourceLoader` 等 *Aware* 依赖）  
   - 调用 `selectImports(...)` 得到“要导入的配置类名列表”  
5) 返回的配置类会被继续解析，最终把它们的 `@Bean`/`@Import` 等注册为 `BeanDefinition`

#### 4.2.4 怎么实现的：源码主线 + 断点入口 + 观察点（建议从这里下手）

建议断点（从入口到闭环）：

建议观察点（你下断点时应该盯住这些变量）：

- 过度动态化导致可读性下降（IDE/搜索难追踪）
- 注册时机/条件不清晰导致难调试

本模块的实验里已经覆盖 BFPP/BPP 的差异，见 [06 章](06-post-processors.md)。

## 7. 在本模块里如何“跑起来验证”

本模块已经提供了可运行的实验（Labs），专门把 `@Import` / `ImportSelector` / `ImportBeanDefinitionRegistrar` 做成“能跑、能断言、能观察输出”的案例：

- 对应测试：`src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansImportLabTest.java`
  - `importAnnotationBringsInAdditionalConfiguration()`：验证 `@Import` 确实把额外配置引入容器
  - `importSelectorChoosesConfigurationBasedOnEnvironmentProperty()`：用环境属性驱动 `ImportSelector` 选择不同配置
  - `importBeanDefinitionRegistrarCanRegisterBeanDefinitionProgrammatically()`：用 registrar 直接注册 `BeanDefinition` 并断言构造参数

本章对应的 Exercise / Solution（可对照练习与答案）：

- Exercise（默认 `@Disabled`）：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansImportExerciseTest.java`
- Solution（默认参与回归）：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansImportExerciseSolutionTest.java`

运行方式：

```bash
mvn -pl spring-core-beans test
```

运行时你会在测试输出里看到以 `OBSERVE:` 开头的少量提示行，用来解释“哪个分支生效、最终注册了哪个 Bean”。

为了真正吃透注册入口，建议你自己做两个小实验（可以写在 `@Disabled` 的 exercise 里）：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansImportExerciseSolutionTest.java`

你会直观感受到：“注册入口决定了最终有哪些 BeanDefinition”，而不是“运行时魔法注入”。
对应 Lab/Test：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansImportLabTest.java`
推荐断点：`ConfigurationClassPostProcessor#processConfigBeanDefinitions`、`ClassPathBeanDefinitionScanner#doScan`、`DefaultListableBeanFactory#registerBeanDefinition`

关键参与者（记住名字用于搜索/断点即可）：

仓库中的 `@Bean` 示例（`src/test/java`，最小片段）：

仓库中的 registrar 示例（`src/test/java`，最小片段）：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/testsupport/BeanDefinitionOriginDumper.java`

## F. 常见坑与边界

你要记住两个常见“坑源”：

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`SpringCoreBeansComponentScanLabTest` / `SpringCoreBeansImportLabTest`
- Exercise：`SpringCoreBeansImportExerciseTest`
- Solution：`SpringCoreBeansImportExerciseSolutionTest`
- Test file：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansComponentScanLabTest.java` / `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansImportLabTest.java` / `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansImportExerciseTest.java` / `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansImportExerciseSolutionTest.java` / `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/testsupport/BeanDefinitionOriginDumper.java`

上一章：[01. Bean 心智模型：BeanDefinition vs Bean 实例](01-bean-mental-model.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[03. 依赖注入解析：类型/名称/@Qualifier/@Primary](03-dependency-injection-resolution.md)

<!-- BOOKIFY:END -->
