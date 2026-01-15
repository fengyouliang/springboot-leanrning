# 第 7 章：Security 主线

这一章解决的问题是：**你没写安全框架代码，为什么请求就会被拦住、为什么会出现 401/403、为什么 CSRF 会影响表单提交**。

---

## 主线（按时间线顺读）

把 Security 当成“在 Web 请求前后加一串过滤器”：

1. 请求进入 Security Filter Chain（Filter）
2. 认证（Authentication）：是谁（identity）？
3. 授权（Authorization）：能做什么（authority）？
4. 异常处理与重定向：401/403、登录页、错误页
5. 常见坑：Filter 顺序、匿名用户、Session/RememberMe、CSRF 与非幂等请求

---

## 深挖入口（模块 docs）

- 模块目录页：[`springboot-security/docs/README.md`](../springboot-security/docs/README.md)
- 模块主线时间线（含可跑入口）：[`springboot-security/docs/part-00-guide/03-mainline-timeline.md`](../springboot-security/docs/part-00-guide/03-mainline-timeline.md)

---

## 下一章怎么接

请求通过安全边界后，最常见的落点是“读写数据”：我们进入 Data JPA 主线。

- 下一章：[第 8 章：Data JPA 主线](08-data-jpa-mainline.md)

