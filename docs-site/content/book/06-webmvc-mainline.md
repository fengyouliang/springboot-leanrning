# 第 6 章：Web MVC 请求主线

这一章解决的问题是：**一个 HTTP 请求进入 Spring Boot 后，是怎么被路由到你的 Controller、怎么完成参数绑定/校验、怎么写回响应、出错时怎么被统一处理**。

---

## 主线（按时间线顺读）

把 Web MVC 看成一条“请求流水线”：

1. 请求进入 `DispatcherServlet`
2. `HandlerMapping` 找到 handler（Controller 方法）
3. `HandlerAdapter` 调用 handler：
   - ArgumentResolver 解析参数（`@RequestParam/@PathVariable/@RequestBody/@ModelAttribute`）
   - Validator/BindingResult 参与校验与错误收集
4. 写回响应：
   - View 渲染（HTML）
   - 或 MessageConverter 序列化（JSON）
5. 出错时进入异常解析链：ExceptionResolvers（400/404/415/500 等）
6. 常见边界：媒体类型协商（406/415）、绑定失败分支（BindException vs MethodArgumentNotValid）、Filter/Interceptor 顺序与 async 生命周期

---

## 深挖入口（模块 docs）

- 模块目录页：[`springboot-web-mvc/docs/README.md`](../springboot-web-mvc/docs/README.md)
- 模块主线时间线（含可跑入口）：[`springboot-web-mvc/docs/part-00-guide/03-mainline-timeline.md`](../springboot-web-mvc/docs/part-00-guide/03-mainline-timeline.md)

建议先跑的最小闭环：

- `BootWebMvcLabTest`（`@WebMvcTest` 切片）

---

## 下一章怎么接

Web MVC 把“请求处理”跑通之后，下一层经常就会碰到“认证/授权”：我们进入 Security 主线。

- 下一章：[第 7 章：Security 主线](07-security-mainline.md)

