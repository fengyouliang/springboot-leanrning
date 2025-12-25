# spring-core-beans

本模块用于学习 Spring Framework 的基础能力（Spring Boot 也是构建在这些能力之上）：

- 通过组件扫描注册 Bean（`@Component`、`@Service`）
- 构造器注入（DI）
- 多实现时用 `@Qualifier` 选择 Bean
- Bean Scope（`singleton` vs `prototype`）
- 基础生命周期回调（`@PostConstruct`、`@PreDestroy`）

## 学习目标

- 理解什么是 Spring Bean，以及它是如何被创建与管理的
- 学会使用“构造器注入”作为默认 DI 风格
- 当存在多个候选 Bean 时，学会用 `@Qualifier` 消除歧义
- 直观看到 Scope 的实际行为（以及为什么“`prototype` 注入到 `singleton`”会让人困惑）
- 理解生命周期回调在容器生命周期中的位置

## 运行

```bash
mvn -pl spring-core-beans spring-boot:run
```

运行后观察控制台输出：

- `@Qualifier` 最终注入的是哪个 formatter bean
- 为什么“直接注入到单例里的 `prototype` bean”表现得像单例
- 如何使用 `ObjectProvider` 获取“新的” `prototype` bean 实例

## 测试

```bash
mvn -pl spring-core-beans test
```

## Deep Dive（Labs / Exercises）

- Labs（默认启用）：
  - `SpringCoreBeansLabTest`：基于 Spring Boot 上下文的 Bean 行为验证（Qualifier/Scope/生命周期）
  - `SpringCoreBeansContainerLabTest`：容器内部机制实验（BFPP/BPP、`@Configuration` 代理、`FactoryBean`、`@Lookup`、循环依赖）
- Exercises（默认禁用）：`SpringCoreBeansExerciseTest`（带 `@Disabled`）

启用 Exercises：打开 `*ExerciseTest`，移除/注释 `@Disabled`，按提示完成后再运行 `mvn -pl spring-core-beans test`。

## 小练习

- 新增一个 `TextFormatter` 实现，并用 `@Qualifier` 切换注入目标
- 把 `PrototypeIdGenerator` 改成 `singleton`，并更新测试断言
- 在 `@Configuration` 里实现一个 `@Bean(initMethod=..., destroyMethod=...)`，对比它与 `@PostConstruct` / `@PreDestroy` 的差异

## 参考

- Spring Framework Reference：Core Technologies（IoC Container / Beans）
- Spring Boot Reference：Dependency Injection & Auto-configuration（Boot 如何帮你装配 Bean）
