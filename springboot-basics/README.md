# springboot-basics

本模块用于学习 Spring Boot 的“最小闭环”：**应用启动**、**配置属性绑定（`@ConfigurationProperties`）**、**Profile（`dev`）切换**。

## 学习目标

- 理解一个最小的 Spring Boot 应用如何启动
- 学会用 `@ConfigurationProperties` 读取 `application.properties` 配置
- 学会用 Profile（例如 `dev`）切换配置与 Bean

## 运行

- 默认配置（不指定 profile）：

```bash
mvn -pl springboot-basics spring-boot:run
```

- 启用 `dev` profile：

```bash
mvn -pl springboot-basics spring-boot:run -Dspring-boot.run.profiles=dev
```

运行后观察控制台输出：

- `activeProfiles` 是否变化
- `app.greeting` 是否来自 `application.properties` / `application-dev.properties`
- `greetingProvider` 是否从 `DefaultGreetingProvider` 切换到 `DevGreetingProvider`

## 测试

```bash
mvn -pl springboot-basics test
```

## Deep Dive（Labs / Exercises）

本模块的“深入学习”以测试为主：

- Labs（默认启用）：
  - `BootBasicsDefaultLabTest`：默认 profile 的配置绑定与 Bean 选择
  - `BootBasicsDevLabTest`：`dev` profile 的配置覆盖与 Bean 切换
  - `BootBasicsOverrideLabTest`：测试级 property override 的优先级
- Exercises（默认禁用）：`BootBasicsExerciseTest`（带 `@Disabled`）

启用 Exercises：打开 `*ExerciseTest`，移除/注释 `@Disabled`，按提示完成后再运行 `mvn -pl springboot-basics test`。

## 小练习

- 新增一个配置项 `app.color`，并在启动输出里打印出来
- 增加一个新的 profile（例如 `prod`），让它输出不同的 greeting

## 参考

- Spring Boot Reference: Configuration Properties
