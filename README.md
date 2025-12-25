# Spring Boot 学习项目（多模块）

这个仓库是一个面向初学者的 Spring Boot 学习工作区：**一个模块对应一个主题**，每个模块都可以单独运行与测试。

## 环境要求

- JDK：`17`
- Maven：建议 `3.8+`

> 本仓库不提供 Maven Wrapper（`mvnw`），请直接使用系统的 `mvn`。

## 快速开始

- 构建并运行所有模块测试：

```bash
mvn -q test
```

- 启用“Deep Dive”学习模式：

本仓库从现在开始把每个模块的测试分为两类：

- **Labs**：`src/test/java/.../*LabTest.java`（默认启用，`mvn -q test` 必须全绿）
- **Exercises**：`src/test/java/.../*ExerciseTest.java`（默认 `@Disabled`，学习者手动开启）

开启练习的方法：打开对应的 `*ExerciseTest`，移除/注释 `@Disabled`，根据测试提示完成实现（或改造），再运行模块测试验证。

- 只构建/测试某个模块（示例：`boot-web-mvc`）：

```bash
mvn -q -pl boot-web-mvc test
```

- 运行某个模块（示例：`boot-basics`）：

```bash
mvn -pl boot-basics spring-boot:run
```

## 模块目录（Catalog）

| 模块 | 主题 | 入口说明 |
|---|---|---|
| `boot-basics` | 启动、配置属性、Profiles | [README](boot-basics/README.md) |
| `boot-web-mvc` | REST Controller、Validation、错误处理 | [README](boot-web-mvc/README.md) |
| `boot-data-jpa` | Spring Data JPA + H2、Entity、Repository、CRUD | [README](boot-data-jpa/README.md) |
| `boot-actuator` | Actuator 端点 + 自定义健康检查 | [README](boot-actuator/README.md) |
| `boot-testing` | 测试基础：`@SpringBootTest`、`@WebMvcTest` 等 | [README](boot-testing/README.md) |
| `boot-business-case` | Capstone：MVC + Validation + JPA + Tx + Events + AOP | [README](boot-business-case/README.md) |
| `spring-core-beans` | Spring Core：Bean、DI、`@Qualifier`、Scope、生命周期 | [README](spring-core-beans/README.md) |
| `spring-core-aop` | Spring AOP：代理、Advice、Pointcut、自调用陷阱 | [README](spring-core-aop/README.md) |
| `spring-core-events` | Spring 事件：发布事件、`@EventListener`、默认同步 | [README](spring-core-events/README.md) |
| `spring-core-validation` | 校验：Bean Validation + Spring 集成 | [README](spring-core-validation/README.md) |
| `spring-core-resources` | 资源：`Resource` 抽象 + classpath pattern | [README](spring-core-resources/README.md) |
| `spring-core-tx` | 事务：`@Transactional` 提交/回滚（JDBC + H2） | [README](spring-core-tx/README.md) |
| `spring-core-profiles` | Profiles/条件装配：`@Profile` + `@ConditionalOnProperty` | [README](spring-core-profiles/README.md) |

> 端口说明：`boot-web-mvc` 默认 `8081`，`boot-actuator` 默认 `8082`，`boot-testing` 默认 `8083`，`boot-business-case` 默认 `8084`。非 Web 模块不监听端口。

## 学习建议

- 先从 `boot-basics` 开始：理解应用启动、配置加载、Profile 切换。
- 每个模块都尽量保持“可运行、可观察、有测试”，按模块 README 的步骤操作即可。

## 常见问题

- `mvn` 不存在：确认已安装 Maven，并确保 `mvn -v` 可用
- 端口占用：修改模块的 `application.properties` 里的 `server.port`，或运行时追加 `--server.port=9090`
- JDK 版本不对：确认 `java -version` 为 17（或更高）
