# 90：常见坑清单（Web MVC）

## 400/校验相关

- DTO 上写了约束注解，但 controller 入参没加 `@Valid`：校验不会触发。
- 400 不等于校验失败：也可能是 JSON 解析失败/绑定失败（建议把两类错误响应区分开）。

## `@WebMvcTest` 相关

- `@WebMvcTest` 只加载 Web 层：如果 controller 依赖 service/repository，通常需要 `@MockBean` 或显式 `@Import`。
- `@WebMvcTest` 的“更快”来自加载范围更小：如果你把太多东西 `@Import` 进来，它就不再快了。

## 404/路由相关

- 路由拼错：确认类级 `@RequestMapping` 与方法级 `@GetMapping/@PostMapping` 的组合。
- path variable 名称不匹配：`@PathVariable("id") Long id`

## 建议的排查顺序

1. 先用测试把“现象”固化（状态码 + 响应形状）
2. 再回到 controller / handler / advice 看“为什么”
3. 需要更接近真实链路时，再用 `@SpringBootTest(webEnvironment=RANDOM_PORT)`

