# 12. 容器启动与基础设施处理器：为什么注解能工作？

这一章回答一个很容易被忽略的问题：

> 你写的 `@Configuration` / `@Bean` / `@Autowired` / `@PostConstruct` 之所以“能工作”，不是因为注解本身有魔法，而是因为 **容器在启动时注册并运行了一组基础设施 BFPP/BPP**。

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansBootstrapInternalsLabTest.java`

## 1. 现象：同样是 Spring 容器，不同启动方式结果不一样

### 1.1 `GenericApplicationContext` 默认不处理注解

如果你直接用 `GenericApplicationContext` 注册 bean：

- `@Autowired` 不会发生（字段仍然是 `null`）
- `@PostConstruct` 不会运行（回调不会被触发）

这不是 bug，而是：你没有把“注解解析与回调”的那套基础设施装进去。

对应测试：

- `SpringCoreBeansBootstrapInternalsLabTest.withoutAnnotationConfigProcessors_autowiredAndPostConstructAreNotApplied()`

### 1.2 注册 annotation processors 后，注解才会被处理

当你调用：

- `AnnotationConfigUtils.registerAnnotationConfigProcessors(context)`

容器会注册一组核心处理器（简化理解）：

- `AutowiredAnnotationBeanPostProcessor`：处理 `@Autowired` / `@Value`
- `CommonAnnotationBeanPostProcessor`：处理 `@PostConstruct` / `@PreDestroy`
- `ConfigurationClassPostProcessor`：解析 `@Configuration` / `@Bean` / `@Import` 等

对应测试：

- `SpringCoreBeansBootstrapInternalsLabTest.registerAnnotationConfigProcessors_enablesAutowiredAndPostConstruct()`

## 2. `@Bean` 为什么能“变成 BeanDefinition”？

很多人以为：

- 写了 `@Configuration` + `@Bean`，容器就自然知道要注册这些 bean

但实际上：

- 如果没有 `ConfigurationClassPostProcessor`（一个 BFPP），`@Bean` 方法根本不会被解析成额外的 `BeanDefinition`

对应测试（同一个 config class，两种容器启动方式得到不同结果）：

- `SpringCoreBeansBootstrapInternalsLabTest.configurationClassIsNotParsedWithoutConfigurationClassPostProcessor()`

## 3. 常见坑

- **误解 1：注解是语言特性**
  - 注解只是元数据；让它“生效”的是容器启动阶段注册的处理器。

- **误解 2：以为任何 ApplicationContext 都等价**
  - `AnnotationConfigApplicationContext` 默认就带“注解能力”，而 `GenericApplicationContext` 默认不带。

- **误解 3：把“容器没装处理器”当成业务 bug**
  - 学机制时请优先问：当前容器有没有注册对应的 BFPP/BPP？

## 4. 一句话自检

- 你能解释清楚：`@Autowired`/`@PostConstruct`/`@Bean` 分别依赖哪些处理器让它们生效吗？
