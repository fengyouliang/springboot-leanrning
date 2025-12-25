# springboot-web-mvc

本模块用于学习 Spring MVC 的常见入门点：**REST Controller**、**参数校验（Validation）**、**统一错误处理（ControllerAdvice）**。

## 学习目标

- 用 `@RestController` 编写 JSON API
- 用 `@Valid` + `jakarta.validation` 做请求参数校验
- 用 `@RestControllerAdvice` 统一返回错误响应

## 运行

```bash
mvn -pl springboot-web-mvc spring-boot:run
```

默认端口：`8081`

### 快速验证

- Ping：

```bash
curl http://localhost:8081/api/ping
```

- 创建用户（正常）：

```bash
curl -X POST http://localhost:8081/api/users \
  -H 'Content-Type: application/json' \
  -d '{"name":"Alice","email":"alice@example.com"}'
```

- 创建用户（触发校验失败）：

```bash
curl -X POST http://localhost:8081/api/users \
  -H 'Content-Type: application/json' \
  -d '{"name":"","email":"not-an-email"}'
```

## 测试

```bash
mvn -pl springboot-web-mvc test
```

## Deep Dive（Labs / Exercises）

本模块的“深入学习”以测试为主：

- Labs（默认启用）：
  - `BootWebMvcLabTest`：`@WebMvcTest` 切片测试（更快、更聚焦）
  - `BootWebMvcSpringBootLabTest`：`@SpringBootTest` 端到端行为验证
- Exercises（默认禁用）：`BootWebMvcExerciseTest`（带 `@Disabled`）

启用 Exercises：打开 `*ExerciseTest`，移除/注释 `@Disabled`，按提示完成后再运行 `mvn -pl springboot-web-mvc test`。

## 小练习

- 给 `CreateUserRequest` 增加一个字段 `age`，要求 `>= 18`
- 把错误响应结构扩展为：包含 `timestamp`、`path` 等信息

## 参考

- Spring MVC
- Bean Validation (Jakarta Validation)
