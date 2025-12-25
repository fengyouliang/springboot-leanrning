# spring-core-profiles

本模块用于系统学习 **Profiles** 与 **条件装配（Conditional Bean Registration）**。

包含内容：

- 使用 `@Profile` 进行 profile 条件装配（包含 `!dev` 这类表达式）
- 使用 `@ConditionalOnProperty` 进行基于配置项的装配（Spring Boot 自动配置中很常见）
- 保证每个场景都不会注入歧义（每个场景只存在一个 `GreetingProvider`）

## 学习目标

- 理解 `@Profile("dev")` 的 Bean 在什么时候会生效
- 使用配置项开关（例如 `app.mode=fancy`）切换行为
- 在测试中验证当前到底注入了哪个 Bean

## 运行

默认（不指定 profile，也不指定额外配置）：

```bash
mvn -pl spring-core-profiles spring-boot:run
```

启用 `dev` profile：

```bash
mvn -pl spring-core-profiles spring-boot:run -Dspring-boot.run.profiles=dev
```

启用配置项开关：

```bash
mvn -pl spring-core-profiles spring-boot:run -Dspring-boot.run.arguments=--app.mode=fancy
```

运行后观察控制台输出：

- activeProfiles
- `app.mode`
- 当前生效的 `GreetingProvider` 实现类

## 测试

```bash
mvn -pl spring-core-profiles test
```

## Deep Dive（Labs / Exercises）

- Labs（默认启用）：`SpringCoreProfilesLabTest`（基于 `ApplicationContextRunner`，更快、更聚焦）
- Exercises（默认禁用）：`SpringCoreProfilesExerciseTest`（带 `@Disabled`）

启用 Exercises：打开 `*ExerciseTest`，移除/注释 `@Disabled`，按提示完成后再运行 `mvn -pl spring-core-profiles test`。

## 小练习

- 增加一个 `prod` profile 的 provider，并决定它是否应该覆盖 property toggle 的选择
- 增加第二个开关（例如 `app.language=en`），并按条件注册 provider
- （进阶）增加一个 `@ConditionalOnMissingBean` 的 fallback bean，并解释这种兜底模式

## 参考

- Spring Framework Reference：Bean Profiles
- Spring Boot Reference：Conditional auto-configuration annotations
