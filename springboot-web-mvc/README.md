# springboot-web-mvc

本模块用于学习 Spring MVC 的常见入门点：**REST Controller**、**参数校验（Validation）**、**统一错误处理（ControllerAdvice）**。

## 你将学到什么

- 用 `@RestController` 编写 JSON API
- 用 `@Valid` + `jakarta.validation` 做请求参数校验
- 用 `@RestControllerAdvice` 统一返回错误响应
- 对比 `@WebMvcTest`（切片）与 `@SpringBootTest`（全量上下文）的测试体验

## 前置知识

- 建议先完成 `springboot-basics`（至少理解配置加载与启动过程）
- 了解 HTTP/JSON 的基本概念（状态码、请求体、响应体）
- （可选）了解 Bean Validation 的基本注解（`@NotBlank`、`@Email`）

## 关键命令

### 运行

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

### 测试

```bash
mvn -pl springboot-web-mvc test
```

## 推荐 docs 阅读顺序

建议按 “入口 → 校验与错误形状 → 异常处理 → 绑定扩展 → 入口增强（拦截器/过滤器）” 的顺序学习：

1. [校验与错误响应形状](docs/01-validation-and-error-shaping.md)
2. [统一异常处理与坏输入](docs/02-exception-handling.md)
3. [请求绑定与 Converter/Formatter](docs/03-binding-and-converters.md)
4. [Interceptor vs Filter：入口与顺序](docs/04-interceptor-and-filter-ordering.md)
5. [常见坑清单](docs/90-common-pitfalls.md)

对应的可运行实验（先跑后读）：
- `src/test/java/com/learning/springboot/bootwebmvc/BootWebMvcLabTest.java`（`@WebMvcTest` 切片）
- `src/test/java/com/learning/springboot/bootwebmvc/BootWebMvcSpringBootLabTest.java`（`@SpringBootTest` 全量）
    
## 概念 → 在本模块哪里能“看见”

| 你要理解的概念 | 去读哪一章 | 去看哪个测试/代码 | 你应该能解释清楚 |
| --- | --- | --- | --- |
| 校验在边界触发 | [docs/01](docs/01-validation-and-error-shaping.md) | `BootWebMvcLabTest#returnsValidationErrorWhenRequestIsInvalid` + `CreateUserRequest` | 为什么需要 `@Valid`，失败时异常从哪来 |
| 统一错误响应形状 | [docs/01](docs/01-validation-and-error-shaping.md) | `GlobalExceptionHandler` + `ApiError` | 为什么要自定义错误结构，结构由谁决定 |
| malformed JSON vs 校验失败 | [docs/02](docs/02-exception-handling.md) | `BootWebMvcLabTest#returnsBadRequestWhenJsonIsMalformed` + `BootWebMvcExerciseTest#exercise_handleMalformedJson` | 两类 400 的根因差异 |
| Converter/Formatter 扩展绑定 | [docs/03](docs/03-binding-and-converters.md) | `BootWebMvcExerciseTest#exercise_converterFormatter` | String 如何变成自定义类型 |
| Interceptor 生效范围与顺序 | [docs/04](docs/04-interceptor-and-filter-ordering.md) | `BootWebMvcExerciseTest#exercise_interceptor` | 为什么它只对 `/api/**` 生效 |

> 想从机制层理解“校验为什么有时不生效”，可进一步阅读 `spring-core-validation/docs/03-method-validation-proxy.md`（方法参数校验与代理）。

## Labs / Exercises 索引（按知识点 / 难度）

> 说明：⭐=入门，⭐⭐=进阶。Exercises 默认 `@Disabled`，建议逐个开启。

| 类型 | 入口 | 知识点 | 难度 | 下一步 |
| --- | --- | --- | --- | --- |
| Lab | `src/test/java/com/learning/springboot/bootwebmvc/BootWebMvcLabTest.java` | `@WebMvcTest` 切片：Controller/校验/错误结构 | ⭐ | 看 `GlobalExceptionHandler` 的错误结构与字段 |
| Lab | `src/test/java/com/learning/springboot/bootwebmvc/BootWebMvcSpringBootLabTest.java` | `@SpringBootTest`：RANDOM_PORT 下的端到端行为 | ⭐ | 对比切片与全量上下文加载范围 |
| Exercise | `src/test/java/com/learning/springboot/bootwebmvc/BootWebMvcExerciseTest.java` | 按提示扩展字段/错误响应/测试断言 | ⭐–⭐⭐ | 从“新增字段 + 校验”开始 |

## 常见 Debug 路径

- `400 Bad Request`：先看响应体里 `fieldErrors`，再定位到对应 DTO 的校验注解
- 校验没触发：确认 controller 入参是否带 `@Valid`、是否走到 `GlobalExceptionHandler`
- JSON 解析失败：优先检查请求体是否是合法 JSON（以及字段名是否匹配）
- 404：确认路由是否正确（`/api/...`）、是否加了类级别 `@RequestMapping`

## 扩展练习（可选）

- 给 `CreateUserRequest` 增加一个字段 `age`，要求 `>= 18`
- 把错误响应结构扩展为：包含 `timestamp`、`path` 等信息

## 参考

- Spring MVC
- Bean Validation (Jakarta Validation)
