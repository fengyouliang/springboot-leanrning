# 第 16 章：Web Client 主线

这一章解决的问题是：**为什么 WebClient 既能同步也能异步、过滤器链怎么工作、错误处理怎么写才不会“吞掉根因”**。

---

## 主线（按时间线顺读）

1. 构建 client：`WebClient.builder()`
2. 组装过滤器链：exchange filters（日志/鉴权/重试/指标）
3. 发起请求：request → exchange → decode
4. 错误处理：状态码分支（4xx/5xx）、body 解析失败、超时/取消
5. 常见坑：block 的位置、线程模型、超时配置、错误链路的“丢栈/丢 body”

---

## 深挖入口（模块 docs）

- 模块目录页：[`springboot-web-client/docs/README.md`](../springboot-web-client/docs/README.md)
- 模块主线时间线（含可跑入口）：[`springboot-web-client/docs/part-00-guide/03-mainline-timeline.md`](../springboot-web-client/docs/part-00-guide/03-mainline-timeline.md)

---

## 下一章怎么接

当模块越来越多，最重要的工程能力之一就是测试：怎么选 slice、怎么控制上下文、怎么写出可维护的可断言证据链。

- 下一章：[第 17 章：Testing 主线](17-testing-mainline.md)

