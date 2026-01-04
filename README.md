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

- 只构建/测试某个模块（示例：`springboot-web-mvc`）：

```bash
mvn -q -pl springboot-web-mvc test
```

- 运行某个模块（示例：`springboot-basics`）：

```bash
mvn -pl springboot-basics spring-boot:run
```

## Debug 工具箱（遇到红测/异常时）

- 常用命令：
  - 全仓库：`mvn -q test`
  - 单模块：`mvn -q -pl <module> test`
  - 运行模块：`mvn -pl <module> spring-boot:run`
  - 也可以用脚本（可读、可改、便于记忆）：`scripts/test-all.sh`、`scripts/test-module.sh`、`scripts/run-module.sh`
- 常用定位套路：
  - 先看**失败断言**（测试描述通常就是“现象”），再回到对应的 `*LabTest` 代码
  - 优先用断点“看见容器/代理/事务边界”而不是只看日志
  - Boot 条件装配排查：必要时加 `--debug` 看 Condition Evaluation（或对照 `spring-core-beans` 的调试章节）

## 推荐学习路线（含预计耗时与完成标准）

### 每个模块的通用完成标准（退出条件）

- 能解释：用自己的话讲清“机制 + 典型坑 + 为什么这样设计”（不背 API）
- 能改写：完成一个 Labs/Exercise 的“改造题”，并保持模块测试全绿
- 能调试：遇到红测/异常，能用断点/日志/断言定位根因并验证修复

### 主线（先跑通业务闭环）

| 顺序 | 模块 | 建议耗时 | 你应该做到（能解释/能改写/能调试） |
| --- | --- | --- | --- |
| 1 | `springboot-basics` | 0.5–1h | 配置绑定 + Profile；新增配置项并验证；能解释配置优先级 |
| 2 | `springboot-web-mvc` | 1–2h | Controller/校验/错误处理；扩展请求字段；能定位 400 的字段错误 |
| 3 | `springboot-testing` | 1–2h | slice vs full context；补一条测试；能解释为什么 `@WebMvcTest` 更快 |
| 4 | `springboot-data-jpa` | 2–3h | persistence context/flush/脏检查；加查询；能解释“一级缓存假象” |
| 5 | `springboot-actuator` | 0.5–1h | 暴露端点 + 自定义 health；加开关；能解释 exposure 与安全边界 |
| 6 | `springboot-business-case` | 2–4h | 串联 Web/JPA/Tx/AOP/Events；改一条链路；能定位代理/事务边界问题 |

### 机制线（把底层原理补齐）

| 顺序 | 模块 | 建议耗时 | 你应该做到（能解释/能改写/能调试） |
| --- | --- | --- | --- |
| 1 | `spring-core-beans` | 4–6h | Bean 注册/注入/生命周期/扩展点；能解释 BFPP vs BPP；能用调试手段“看见容器” |
| 2 | `spring-core-profiles` | 1–2h | `@Profile`/`@ConditionalOnProperty`；避免注入歧义；能定位条件为何不生效 |
| 3 | `spring-core-validation` | 1–2h | 约束/violation/method validation；能解释“为何依赖代理”；能定位 `@Validated` 缺失 |
| 4 | `spring-core-aop` | 2–3h | 代理/切点/自调用/final 限制；能判断 JDK vs CGLIB；能解释“入口没走代理” |
| 5 | `spring-core-tx` | 2–3h | 事务边界/回滚规则/传播；能解释 checked exception；能定位“自调用导致事务不生效” |
| 6 | `spring-core-events` | 1–2h | 同步/异常传播/@Async/after-commit；能解释回滚时机；能稳定断言异步 |
| 7 | `spring-core-resources` | 1–2h | `Resource` 抽象/pattern/jar 差异；能区分 handle vs exists；能定位 classpath 路径问题 |

## Labs/Exercises 总索引（按知识点 / 难度）

> 说明：⭐=入门，⭐⭐=进阶，⭐⭐⭐=挑战/综合。Exercises 默认 `@Disabled`，建议按模块 README 的索引逐个开启。

### 配置 / Profiles / 条件装配

- ⭐ `springboot-basics/src/test/java/com/learning/springboot/bootbasics/BootBasicsDefaultLabTest.java`：配置绑定 + 默认 profile
- ⭐ `springboot-basics/src/test/java/com/learning/springboot/bootbasics/BootBasicsDevLabTest.java`：dev profile 覆盖与 Bean 切换
- ⭐⭐ `springboot-basics/src/test/java/com/learning/springboot/bootbasics/BootBasicsOverrideLabTest.java`：测试级 property override 优先级
- ⭐⭐ `spring-core-profiles/src/test/java/com/learning/springboot/springcoreprofiles/SpringCoreProfilesLabTest.java`：`@Profile`/`@ConditionalOnProperty` + `ApplicationContextRunner`
- （练习）`springboot-basics/src/test/java/com/learning/springboot/bootbasics/BootBasicsExerciseTest.java`
- （练习）`spring-core-profiles/src/test/java/com/learning/springboot/springcoreprofiles/SpringCoreProfilesExerciseTest.java`

### Web MVC / 错误处理

- ⭐ `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/BootWebMvcLabTest.java`：`@WebMvcTest` 切片（更快、更聚焦）
- ⭐ `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/BootWebMvcSpringBootLabTest.java`：`@SpringBootTest` 全量上下文（更接近集成）
- ⭐⭐⭐ `springboot-business-case/src/test/java/com/learning/springboot/bootbusinesscase/BootBusinessCaseLabTest.java`：综合链路（含 Validation/JPA/Tx/Events/AOP）
- （练习）`springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/BootWebMvcExerciseTest.java`
- （练习）`springboot-business-case/src/test/java/com/learning/springboot/bootbusinesscase/BootBusinessCaseExerciseTest.java`

### 测试切片（Testing）

- ⭐ `springboot-testing/src/test/java/com/learning/springboot/boottesting/GreetingControllerWebMvcLabTest.java`：`@WebMvcTest` + `@MockBean`
- ⭐ `springboot-testing/src/test/java/com/learning/springboot/boottesting/GreetingControllerSpringBootLabTest.java`：`@SpringBootTest(webEnvironment=RANDOM_PORT)`
- ⭐⭐ `springboot-testing/src/test/java/com/learning/springboot/boottesting/BootTestingMockBeanLabTest.java`：full context 里用 `@MockBean` 覆盖真实 Bean
- （练习）`springboot-testing/src/test/java/com/learning/springboot/boottesting/BootTestingExerciseTest.java`

### JPA（Spring Data JPA）

- ⭐⭐ `springboot-data-jpa/src/test/java/com/learning/springboot/bootdatajpa/BootDataJpaLabTest.java`：persistence context / flush / dirty checking
- （练习）`springboot-data-jpa/src/test/java/com/learning/springboot/bootdatajpa/BootDataJpaExerciseTest.java`

### Bean / IoC 容器

- ⭐⭐⭐ `spring-core-beans/README.md`：IoC 容器与 Bean 机制总入口（含学习路线、Start Here、完整 Labs/Exercises 与 container internals 深潜）
- ⭐⭐ `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansLabTest.java`：Start Here（最小闭环，建议命令：`mvn -pl spring-core-beans -Dtest=SpringCoreBeansLabTest test`）
- ⭐⭐ `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansContainerLabTest.java`：容器机制闭环（定义层/实例层/BFPP/BPP/循环依赖，建议命令：`mvn -pl spring-core-beans -Dtest=SpringCoreBeansContainerLabTest test`）
- ⭐⭐ `spring-core-beans/docs/00-deep-dive-guide.md`：断点地图与深挖练习（从一个入口测试走完整主线）
- ⭐⭐ `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansAutoConfigurationImportOrderingLabTest.java`：Boot 自动装配导入/排序主线（after/before 顺序 + 条件可见性）
- ⭐⭐ `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansAutoConfigurationOverrideMatrixLabTest.java`：覆盖/back-off 场景矩阵（NoUnique → 两类修复路径）
- ⭐ `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansBeanDefinitionOriginLabTest.java`：定位 Bean 来源（谁注册的/从哪来/工厂方法 vs 直接类）

### AOP / 代理

- ⭐⭐ `spring-core-aop/src/test/java/com/learning/springboot/springcoreaop/SpringCoreAopLabTest.java`：最小 advice 闭环 + 自调用陷阱
- ⭐⭐⭐ `spring-core-aop/src/test/java/com/learning/springboot/springcoreaop/SpringCoreAopProxyMechanicsLabTest.java`：JDK vs CGLIB、final 限制、`@Order`
- （练习）`spring-core-aop/src/test/java/com/learning/springboot/springcoreaop/SpringCoreAopExerciseTest.java`

### 事务（Tx）

- ⭐⭐ `spring-core-tx/src/test/java/com/learning/springboot/springcoretx/SpringCoreTxLabTest.java`：边界/回滚/传播/模板
- ⭐⭐ `spring-core-tx/src/test/java/com/learning/springboot/springcoretx/SpringCoreTxSelfInvocationPitfallLabTest.java`：自调用绕过事务最小复现 + 修复对比
- （练习）`spring-core-tx/src/test/java/com/learning/springboot/springcoretx/SpringCoreTxExerciseTest.java`

### 事件（Events）

- ⭐⭐ `spring-core-events/src/test/java/com/learning/springboot/springcoreevents/SpringCoreEventsLabTest.java`：多监听器/顺序/condition/payload
- ⭐⭐ `spring-core-events/src/test/java/com/learning/springboot/springcoreevents/SpringCoreEventsMechanicsLabTest.java`：异常传播 + `@Async`
- （练习）`spring-core-events/src/test/java/com/learning/springboot/springcoreevents/SpringCoreEventsExerciseTest.java`

### Validation（校验）

- ⭐⭐ `spring-core-validation/src/test/java/com/learning/springboot/springcorevalidation/SpringCoreValidationLabTest.java`：程序化校验 + Spring 集成
- ⭐⭐ `spring-core-validation/src/test/java/com/learning/springboot/springcorevalidation/SpringCoreValidationMechanicsLabTest.java`：代理差异 + groups + 自定义约束
- （练习）`spring-core-validation/src/test/java/com/learning/springboot/springcorevalidation/SpringCoreValidationExerciseTest.java`

### Resources（资源）

- ⭐⭐ `spring-core-resources/src/test/java/com/learning/springboot/springcoreresources/SpringCoreResourcesLabTest.java`：读取/模式扫描
- ⭐⭐ `spring-core-resources/src/test/java/com/learning/springboot/springcoreresources/SpringCoreResourcesMechanicsLabTest.java`：handle/exists/description
- （练习）`spring-core-resources/src/test/java/com/learning/springboot/springcoreresources/SpringCoreResourcesExerciseTest.java`

### Actuator（可观测性）

- ⭐ `springboot-actuator/src/test/java/com/learning/springboot/bootactuator/BootActuatorLabTest.java`：health/info + 自定义健康检查
- ⭐⭐ `springboot-actuator/src/test/java/com/learning/springboot/bootactuator/BootActuatorExposureOverrideLabTest.java`：端点暴露配置与验证
- （练习）`springboot-actuator/src/test/java/com/learning/springboot/bootactuator/BootActuatorExerciseTest.java`

## 模块目录（Catalog）

| 模块 | 主题 | 入口说明 |
|---|---|---|
| `springboot-basics` | 启动、配置属性、Profiles | [README](springboot-basics/README.md) |
| `springboot-web-mvc` | REST Controller、Validation、错误处理 | [README](springboot-web-mvc/README.md) |
| `springboot-data-jpa` | Spring Data JPA + H2、Entity、Repository、CRUD | [README](springboot-data-jpa/README.md) |
| `springboot-actuator` | Actuator 端点 + 自定义健康检查 | [README](springboot-actuator/README.md) |
| `springboot-testing` | 测试基础：`@SpringBootTest`、`@WebMvcTest` 等 | [README](springboot-testing/README.md) |
| `springboot-business-case` | Capstone：MVC + Validation + JPA + Tx + Events + AOP | [README](springboot-business-case/README.md) |
| `springboot-security` | Security：认证/授权/CSRF/method security/JWT | [README](springboot-security/README.md) |
| `springboot-web-client` | Web Client：RestClient vs WebClient、超时/重试/错误处理 | [README](springboot-web-client/README.md) |
| `springboot-async-scheduling` | 异步与调度：`@Async`、线程池、`@Scheduled` | [README](springboot-async-scheduling/README.md) |
| `springboot-cache` | 缓存：Spring Cache + Caffeine（key/evict/过期） | [README](springboot-cache/README.md) |
| `spring-core-beans` | Spring Core：Bean、DI、`@Qualifier`、Scope、生命周期 | [README](spring-core-beans/README.md) |
| `spring-core-aop` | Spring AOP：代理、Advice、Pointcut、自调用陷阱 | [README](spring-core-aop/README.md) |
| `spring-core-events` | Spring 事件：发布事件、`@EventListener`、默认同步 | [README](spring-core-events/README.md) |
| `spring-core-validation` | 校验：Bean Validation + Spring 集成 | [README](spring-core-validation/README.md) |
| `spring-core-resources` | 资源：`Resource` 抽象 + classpath pattern | [README](spring-core-resources/README.md) |
| `spring-core-tx` | 事务：`@Transactional` 提交/回滚（JDBC + H2） | [README](spring-core-tx/README.md) |
| `spring-core-profiles` | Profiles/条件装配：`@Profile` + `@ConditionalOnProperty` | [README](spring-core-profiles/README.md) |

> 端口说明：`springboot-web-mvc` 默认 `8081`，`springboot-actuator` 默认 `8082`，`springboot-testing` 默认 `8083`，`springboot-business-case` 默认 `8084`，`springboot-security` 默认 `8085`。非 Web 模块不监听端口。

## 学习建议

- 先从 `springboot-basics` 开始：理解应用启动、配置加载、Profile 切换。
- 每个模块都尽量保持“可运行、可观察、有测试”，按模块 README 的步骤操作即可。

## 跨模块概念地图（把点连成网）

下面这些“连接线”往往比单个知识点更重要：它们能解释为什么你在不同模块里会遇到同一类现象。

- **代理（Proxy）是共同底座**：AOP、事务（`@Transactional`）、方法参数校验（method validation）都依赖代理机制  
  - 从机制角度建议先读：[AOP 心智模型](spring-core-aop/docs/part-01-proxy-fundamentals/01-aop-proxy-mental-model.md)、[`@Transactional` 也是代理](spring-core-tx/docs/part-01-transaction-basics/02-transactional-proxy.md)、[方法参数校验也需要代理](spring-core-validation/docs/part-01-validation-core/03-method-validation-proxy.md)
- **自调用（self-invocation）是代理世界第一大坑**：同一个类里用 `this.xxx()` 调用会绕过代理，因此 AOP/Tx 都可能“不生效”  
  - 对照：[AOP 自调用陷阱](spring-core-aop/docs/part-01-proxy-fundamentals/03-self-invocation.md)、[Tx 常见坑清单](spring-core-tx/docs/appendix/90-common-pitfalls.md)
- **事务边界决定持久化行为**：JPA 的 flush / dirty checking 不是“魔法”，它强依赖事务与 persistence context  
  - 对照：[JPA Persistence Context](springboot-data-jpa/docs/02-persistence-context.md)、[事务边界](spring-core-tx/docs/part-01-transaction-basics/01-transaction-boundary.md)
- **事件（Events）与事务（Tx）的时机关系**：同步事件 vs after-commit 事件（`@TransactionalEventListener`）能解释“回滚了但监听器为什么执行了/没执行”  
  - 从现象入手：[spring-core-events](spring-core-events/README.md)、[`@TransactionalEventListener`（after-commit）](spring-core-events/docs/part-02-async-and-transactional/07-transactional-event-listener.md)、[springboot-business-case](springboot-business-case/README.md)
- **资源（Resources）是很多能力的地基**：配置文件、classpath 扫描、jar/本地差异，最终都会回到 `Resource` 抽象  
  - 对照：[Resource 抽象](spring-core-resources/docs/part-01-resource-abstraction/01-resource-abstraction.md)、[jar vs filesystem](spring-core-resources/docs/part-01-resource-abstraction/06-jar-vs-filesystem.md)
- **测试切片 vs 全量上下文**：`@DataJpaTest` / `@WebMvcTest` 用来快速验证机制，`@SpringBootTest` 更接近集成链路  
  - 对照：[springboot-testing](springboot-testing/README.md)、[`@DataJpaTest` 切片](springboot-data-jpa/docs/06-datajpatest-slice.md)

## 常见问题

- `mvn` 不存在：确认已安装 Maven，并确保 `mvn -v` 可用
- 端口占用：修改模块的 `application.properties` 里的 `server.port`，或运行时追加 `--server.port=9090`
- JDK 版本不对：确认 `java -version` 为 17（或更高）
