# 01：配置来源（PropertySources）与 Profile 覆盖

本章把 `springboot-basics` 里“配置从哪里来、谁覆盖谁”讲清楚，并对应到可运行的实验测试。

## 实验入口（先跑再看）

- 默认配置（无 dev profile）：
  - `springboot-basics/src/test/java/com/learning/springboot/bootbasics/part01_boot_basics/BootBasicsDefaultLabTest.java`
- 启用 dev profile（覆盖配置 + Bean 切换）：
  - `springboot-basics/src/test/java/com/learning/springboot/bootbasics/part01_boot_basics/BootBasicsDevLabTest.java`
- 测试级覆盖（properties precedence）：
  - `springboot-basics/src/test/java/com/learning/springboot/bootbasics/part01_boot_basics/BootBasicsOverrideLabTest.java`

## 你应该观察到什么（What to observe）

1. **默认情况下**，`Environment#getActiveProfiles()` 不包含 `dev`，并且会存在 `default` profile。
2. **当启用 `dev` profile**：
   - `application-dev.properties` 覆盖 `application.properties` 的同名 key（例如 `app.greeting`）
   - 同一注入点的 Bean 也会被 profile 条件影响（例如 `GreetingProvider` 的实现切换）
3. **当测试通过 `@SpringBootTest(properties = {...})` 提供覆盖配置**：
   - 即使 `application.properties` 里有默认值，也会被测试注入的值覆盖（`BootBasicsOverrideLabTest`）

## 机制解释（Why）

你可以把 Spring Boot 的配置加载理解成两件事：

1) **把多个来源的配置聚合成一个 Environment**
- 配置来源（PropertySource）可能来自：
  - `application.properties` / `application-<profile>.properties`
  - 测试注入的 properties（`@SpringBootTest(properties = ...)`）
  - system properties / 环境变量 / 命令行参数（本模块练习会引导你补齐）

2) **根据 Profile 决定哪些配置文件与哪些 Bean 生效**
- `@ActiveProfiles("dev")` 会在测试中激活 dev profile。
- `application-dev.properties` 只在 `dev` 激活时参与。
- Bean 切换通常来自 `@Profile` 或条件装配（本模块用“不同实现类 + profile”的方式让现象更直观）。

## Debug 建议

- 配置到底有没有进来：优先用 `Environment#getProperty("app.xxx")` + 断言，不要只看日志。
- Profile 是否真的生效：打断点看 `environment.getActiveProfiles()`。
- 想继续深挖条件装配与 profile：去看 `spring-core-profiles` 模块（更偏机制与条件评估）。

## 常见坑

- 把“Profile 覆盖”误当成“Bean 一定会切换”：配置覆盖和 Bean 注册是两条线，Bean 是否存在取决于条件注解是否匹配。
- 误判优先级：同一个 key 可能来自多个来源，建议用测试固化“谁覆盖谁”的结论。

