# 02. Bean 注册入口：扫描、@Bean、@Import、registrar

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

你要记住两个常见“坑源”：

1) **扫描范围**（base package）决定了“你以为存在的 bean”是否真的存在  
2) 扫描产生的 beanName 有默认规则（通常是类名首字母小写），你也可以显式指定

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

它的本质不是“运行时动态装配”，而是**配置类解析阶段**的一部分（仍然属于“定义层”）。

`@Import` 常见三种用法（理解概念即可）：

### 4.1 直接 import 配置类（最直观）

```java
@Configuration
@Import(OtherConfig.class)
class AppConfig {}
```

这就像把 `OtherConfig` 也当作配置来源参与解析与注册。

### 4.2 import `ImportSelector`（用代码决定“导入哪些配置”）

`ImportSelector` 的任务是：返回一组要导入的“配置类全限定名”。

典型用途：

- 做 feature toggle（根据条件导入不同实现）
- 做“按需装配”的基础设施（框架、starter 常见）

> 你不需要记接口方法签名，只要记住：它发生在配置解析阶段，用来“决定导入列表”。

### 4.3 import `ImportBeanDefinitionRegistrar`（最强，也最容易滥用）

`ImportBeanDefinitionRegistrar` 允许你直接对 `BeanDefinitionRegistry` 操作：

- 你可以用代码注册任意数量、任意形态的 `BeanDefinition`
- 也可以读取 `@EnableXxx` 自己的注解属性，然后据此注册 bean

这就是“很多框架看起来像魔法”的来源：它们把配置转成 BeanDefinition 并注册。

常见风险：

- 过度动态化导致可读性下降（IDE/搜索难追踪）
- 注册时机/条件不清晰导致难调试

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

本模块的实验里已经覆盖 BFPP/BPP 的差异，见 [06 章](06-post-processors.md)。

## 6. Spring Boot 自动装配：本质上是“批量 @Import”（但更复杂）

理解 `@Import` 后，Boot 自动装配就不会那么“玄学”了：

- `@SpringBootApplication` 里包含了 `@EnableAutoConfiguration`
- `@EnableAutoConfiguration` 的核心实现是通过（Deferred）ImportSelector 导入一组“自动配置类”
- 这些自动配置类本身也是配置来源，会注册大量 BeanDefinition（通常带各种 `@Conditional...`）

更详细内容见：

- [10. Spring Boot 自动装配如何影响 Bean](10-spring-boot-auto-configuration.md)

## 7. 在本模块里如何“跑起来验证”

本模块已经提供了可运行的实验（Labs），专门把 `@Import` / `ImportSelector` / `ImportBeanDefinitionRegistrar` 做成“能跑、能断言、能观察输出”的案例：

- 对应测试：`src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansImportLabTest.java`
  - `importAnnotationBringsInAdditionalConfiguration()`：验证 `@Import` 确实把额外配置引入容器
  - `importSelectorChoosesConfigurationBasedOnEnvironmentProperty()`：用环境属性驱动 `ImportSelector` 选择不同配置
  - `importBeanDefinitionRegistrarCanRegisterBeanDefinitionProgrammatically()`：用 registrar 直接注册 `BeanDefinition` 并断言构造参数

运行方式：

```bash
mvn -pl spring-core-beans test
```

运行时你会在测试输出里看到以 `OBSERVE:` 开头的少量提示行，用来解释“哪个分支生效、最终注册了哪个 Bean”。

## 8. 你应该能做到的“迁移练习”（强烈推荐）

为了真正吃透注册入口，建议你自己做两个小实验（可以写在 `@Disabled` 的 exercise 里）：

1) 用 `@Import(SomeConfig.class)` 引入一个额外 `@Bean`
2) 写一个最小 `ImportSelector`，根据某个系统属性决定导入 `UpperCaseTextFormatter` 还是 `LowerCaseTextFormatter`

你会直观感受到：“注册入口决定了最终有哪些 BeanDefinition”，而不是“运行时魔法注入”。
对应 Lab/Test：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part01_ioc_container/SpringCoreBeansImportLabTest.java`
推荐断点：`ConfigurationClassPostProcessor#processConfigBeanDefinitions`、`ClassPathBeanDefinitionScanner#doScan`、`DefaultListableBeanFactory#registerBeanDefinition`

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

关键参与者（记住名字用于搜索/断点即可）：

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

仓库中的 `@Bean` 示例（`src/test/java`，最小片段）：

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

仓库中的 registrar 示例（`src/test/java`，最小片段）：

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

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/testsupport/BeanDefinitionOriginDumper.java`
