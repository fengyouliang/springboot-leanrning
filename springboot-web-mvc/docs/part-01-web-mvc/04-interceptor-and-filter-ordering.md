# 04：Interceptor 与 Filter：入口在哪里、顺序怎么理解

本章的目标不是把 Filter/Interceptor 全部讲完，而是建立一个“入口与顺序”的最小心智模型：你知道它们分别在链路的哪里、什么时候该用哪个。

## 实验入口

- 练习：增加一个 `HandlerInterceptor` 并证明它只对 `/api/**` 生效：
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part00_guide/BootWebMvcExerciseTest.java`
    - `exercise_interceptor`

## 你应该观察到什么

- Interceptor 是 MVC 层能力：更贴近 handler 调用（controller 前后）
- Filter 更贴近 Servlet 容器：更接近“请求最外层”

## 机制解释（Why）

- **Filter**：发生在 Servlet 容器层，通常对所有请求都可能生效（除非你按 URL pattern 配置）
- **Interceptor**：发生在 Spring MVC handler 执行链内，便于针对某一类 handler 路由做增强

如果你是“想对 /api/** 生效”，并且增强逻辑与 handler 相关（比如给 response 增 header、记录耗时），Interceptor 往往更直观。

## Debug 建议

- 写测试优先选 `MockMvc`：它能稳定复现 handler 链路并断言结果（比手工 curl 更可控）。

