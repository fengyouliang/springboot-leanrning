# spring-core-beans

本模块用“可运行的最小示例 + 可验证的测试实验（Labs/Exercises）”讲透 Spring Framework 的 **IoC 容器与 Bean**：

- Bean 的心智模型：`BeanDefinition`（定义） vs Bean instance（实例）
- Bean 如何被“注册”进容器：`@ComponentScan` / `@Bean` / `@Import` / registrar
- 依赖注入（DI）如何解析：类型、名称、`@Qualifier`、`@Primary`
- Scope 的真实语义：`singleton`、`prototype`，以及“prototype 注入 singleton”的坑
- 生命周期：创建、初始化、销毁；你到底能在什么时候做什么
- 容器扩展点：`BeanFactoryPostProcessor` vs `BeanPostProcessor`
- `@Configuration(proxyBeanMethods=...)` 对 `@Bean` 语义的影响
- `FactoryBean`：product vs factory，`&` 前缀的常见误解
- 循环依赖：为什么构造器循环会失败，setter 有时能成功
- Spring Boot 自动装配如何影响最终的 Bean 图（bean graph）

这份 `README.md` 只做索引与导航；更深入的解释请按章节阅读：见 [docs/](docs/)。

## 快速开始

运行应用（看控制台输出）：

```bash
mvn -pl spring-core-beans spring-boot:run
```

运行测试（Labs 默认启用，Exercises 默认禁用）：

```bash
mvn -pl spring-core-beans test
```

启用 Exercises：打开 `*ExerciseTest`，移除/注释 `@Disabled`，按提示完成后再运行 `mvn -pl spring-core-beans test`。

## 推荐阅读顺序（从“能解释清楚”到“理解机制”）

1. [Bean 心智模型：BeanDefinition vs 实例](docs/01-bean-mental-model.md)
2. [Bean 注册入口：扫描、@Bean、@Import、registrar](docs/02-bean-registration.md)
3. [依赖注入解析：类型/名称/@Qualifier/@Primary](docs/03-dependency-injection-resolution.md)
4. [Scope 与 prototype 注入陷阱](docs/04-scope-and-prototype.md)
5. [生命周期：初始化、销毁与回调](docs/05-lifecycle-and-callbacks.md)
6. [容器扩展点：BFPP vs BPP](docs/06-post-processors.md)
7. [`@Configuration` 增强与 `@Bean` 语义](docs/07-configuration-enhancement.md)
8. [`FactoryBean`：产品 vs 工厂](docs/08-factorybean.md)
9. [循环依赖：现象、原因与规避](docs/09-circular-dependencies.md)
10. [Spring Boot 自动装配如何影响 Bean](docs/10-spring-boot-auto-configuration.md)
11. [调试与自检：如何“看见”容器正在做什么](docs/11-debugging-and-observability.md)
12. [常见坑清单（建议反复对照）](docs/90-common-pitfalls.md)
13. [自测题：你是否真的理解了？](docs/99-self-check.md)

## 概念 → 在本模块哪里能“看见”

| 你要理解的概念 | 去读哪一章 | 去看哪个测试/代码 | 你应该能解释清楚 |
| --- | --- | --- | --- |
| `@Qualifier` 解决多实现注入 | [docs/03](docs/03-dependency-injection-resolution.md) | `src/main/java/.../FormattingService.java`、`src/main/java/.../*TextFormatter.java`、`src/test/java/.../SpringCoreBeansLabTest.java` | 为什么会歧义、如何指定注入目标、如何验证注入结果 |
| prototype 注入 singleton 的“看起来像单例” | [docs/04](docs/04-scope-and-prototype.md) | `src/main/java/.../DirectPrototypeConsumer.java`、`src/main/java/.../ProviderPrototypeConsumer.java`、`src/main/java/.../PrototypeIdGenerator.java` | prototype 的语义是“每次向容器要都是新的”，而不是“每次方法调用都是新的” |
| `@PostConstruct` 何时运行 | [docs/05](docs/05-lifecycle-and-callbacks.md) | `src/main/java/.../LifecycleLogger.java`、`src/test/java/.../SpringCoreBeansLabTest.java` | 容器启动阶段发生了什么、回调在什么时机触发 |
| `@Import` / `ImportSelector` / registrar（高级注册入口） | [docs/02](docs/02-bean-registration.md) | `src/test/java/.../SpringCoreBeansImportLabTest.java` | 配置类解析阶段到底导入了什么、ImportSelector 如何决定导入列表、registrar 如何直接注册 BeanDefinition |
| `BeanDefinition` vs Bean 实例 | [docs/01](docs/01-bean-mental-model.md) | `src/test/java/.../SpringCoreBeansContainerLabTest.java` | “定义”是元数据，“实例”是对象；扩展点通常围绕两者分别工作 |
| BFPP 能改定义、BPP 能包/改实例 | [docs/06](docs/06-post-processors.md) | `src/test/java/.../SpringCoreBeansContainerLabTest.java` | 为什么 BFPP 更早、为什么 BPP 常导致代理/增强、它们各自的边界是什么 |
| `@Configuration` 增强与 `proxyBeanMethods` | [docs/07](docs/07-configuration-enhancement.md) | `src/test/java/.../SpringCoreBeansContainerLabTest.java` | 为什么 “在 `@Bean` 方法里直接调用另一个 `@Bean` 方法” 会改变实例语义 |
| `FactoryBean` 的 `&` 前缀 | [docs/08](docs/08-factorybean.md) | `src/test/java/.../SpringCoreBeansContainerLabTest.java` | 为什么 `getBean("name")` 拿到的是产品而不是工厂本身 |
| 循环依赖：构造器 vs setter | [docs/09](docs/09-circular-dependencies.md) | `src/test/java/.../SpringCoreBeansContainerLabTest.java` | 为什么构造器循环会失败、setter 为什么有时能靠“提前暴露”成功 |
| Boot 自动装配带来的“你没写但它存在的 Bean” | [docs/10](docs/10-spring-boot-auto-configuration.md) | `src/test/java/.../SpringCoreBeansAutoConfigurationLabTest.java`（基于 `ApplicationContextRunner`） + [docs/11](docs/11-debugging-and-observability.md)（调试方式） | 自动装配是如何被导入/生效/失效的，以及你如何覆盖/禁用它 |

## Labs / Exercises（怎么学效果最好）

- Labs（默认启用，保持全绿）：
  - `SpringCoreBeansLabTest`：基于 Spring Boot 上下文的“外部行为”验证（Qualifier/Scope/生命周期）
  - `SpringCoreBeansContainerLabTest`：容器内部机制实验（BFPP/BPP、`@Configuration` 代理、`FactoryBean`、`@Lookup`、循环依赖）
  - `SpringCoreBeansImportLabTest`：高级注册入口实验（`@Import` / `ImportSelector` / `ImportBeanDefinitionRegistrar`）
  - `SpringCoreBeansAutoConfigurationLabTest`：Boot 自动装配实验（条件生效/失效、`@ConditionalOnMissingBean` 覆盖策略）
- Exercises（默认禁用，带 `@Disabled`，建议逐个开启）：
  - `SpringCoreBeansExerciseTest`
  - `SpringCoreBeansImportExerciseTest`
  - `SpringCoreBeansAutoConfigurationExerciseTest`

## 下一步（学完这里去哪里）

- 想理解代理与切面：`spring-core-aop`
- 想理解事件与监听器：`spring-core-events`
- 想理解事务与传播/回滚：`spring-core-tx`
- 想理解条件装配/环境：`spring-core-profiles`

## 参考

- Spring Framework Reference：Core Technologies（IoC Container / Beans / Context）
- Spring Boot Reference：Auto-configuration / Condition Evaluation（理解 Boot 如何“导入配置并注册 Bean”）
