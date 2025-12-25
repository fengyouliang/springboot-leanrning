# springboot-testing

本模块用于学习 Spring Boot 的测试入门：

- `@WebMvcTest`：只加载 Web 层（Controller），更快、更聚焦
- `@SpringBootTest`：加载完整应用上下文，更接近集成测试

## 学习目标

- 理解“测试切片（slice test）”的意义
- 会写一个 `@WebMvcTest` + `@MockBean` 的 Controller 测试
- 会写一个 `@SpringBootTest(webEnvironment=RANDOM_PORT)` 的端到端测试

## 运行

```bash
mvn -pl springboot-testing spring-boot:run
```

默认端口：`8083`

### 快速验证

```bash
curl 'http://localhost:8083/api/greeting?name=Bob'
```

## 测试

```bash
mvn -pl springboot-testing test
```

## Deep Dive（Labs / Exercises）

- Labs（默认启用）：
  - `GreetingControllerWebMvcLabTest`：`@WebMvcTest` + `@MockBean`
  - `GreetingControllerSpringBootLabTest`：`@SpringBootTest(webEnvironment=RANDOM_PORT)`
  - `BootTestingMockBeanLabTest`：在 full context 里用 `@MockBean` 覆盖真实 Bean
- Exercises（默认禁用）：`BootTestingExerciseTest`（带 `@Disabled`）

启用 Exercises：打开 `*ExerciseTest`，移除/注释 `@Disabled`，按提示完成后再运行 `mvn -pl springboot-testing test`。

## 小练习

- 为 `GreetingService` 增加一个“敏感词过滤”逻辑，并补充相应测试
- 增加一个 `@JsonTest`（或类似切片）来学习 JSON 序列化测试

## 参考

- Spring Boot Testing
