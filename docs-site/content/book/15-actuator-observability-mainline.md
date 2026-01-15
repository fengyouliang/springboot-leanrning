# 第 15 章：Actuator/Observability 主线

这一章解决的问题是：**应用怎么暴露健康检查、指标、信息端点；为什么 exposure 配置与安全边界很关键；如何把“看不见的运行状态”变成可观测信号**。

---

## 主线（按时间线顺读）

1. Actuator 端点注册：health/info/metrics 等
2. exposure 决定哪些端点对外可见（运维需要 vs 安全边界）
3. 自定义 health/indicator：把关键依赖状态可视化
4. metrics 采集：把“请求量/耗时/错误”等固化成指标
5. 常见坑：端点暴露过多、生产环境未做鉴权、误把 actuator 当业务 API

---

## 深挖入口（模块 docs）

- 模块目录页：[`springboot-actuator/docs/README.md`](../springboot-actuator/docs/README.md)
- 模块主线时间线（含可跑入口）：[`springboot-actuator/docs/part-00-guide/03-mainline-timeline.md`](../springboot-actuator/docs/part-00-guide/03-mainline-timeline.md)

---

## 下一章怎么接

当你需要向外部服务发请求时，WebClient 是现代 Spring 体系里的核心客户端。我们把“客户端主线”串一遍。

- 下一章：[第 16 章：Web Client 主线](16-web-client-mainline.md)

