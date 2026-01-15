# 第 1 章：Boot 启动与配置主线

这一章解决的问题很朴素：**一个 Spring Boot 应用启动时，“配置”到底从哪里来、最终值是什么、它怎么影响后续的 Bean 装配与运行期行为**。

你不需要先背配置项；你需要先能画出一条可验证的链路：**配置来源 → Environment → 绑定 → 影响条件装配/业务行为**。

---

## 主线（按时间线顺读）

把配置当成“事实来源”，把 `Environment` 当成“最终事实数据库”：

1. 多来源配置进入 `Environment`（多份 `PropertySource`）
2. Profile 参与分流与覆盖（既影响“配置文件参与”，也影响“Bean 是否注册”）
3. `@ConfigurationProperties` 把字符串配置绑定成结构化对象（并暴露绑定失败/默认值/覆盖结果）
4. 业务代码读取绑定对象/Environment，行为由最终值决定

---

## 深挖入口（模块 docs）

这章在书里给你“主线”，细节与证据链建议下沉到模块文档：

- 模块目录页（建议从这里顺读）：[`springboot-basics/docs/README.md`](../springboot-basics/docs/README.md)

如果你想把“配置主线”进一步拆细成可回归的阅读顺序（推荐顺读）：

1. 配置从哪里来、谁覆盖谁：[`配置源与 Profiles`](../springboot-basics/docs/part-01-boot-basics/01-property-sources-and-profiles.md)
2. 配置如何绑定成对象：[`配置绑定（@ConfigurationProperties）`](../springboot-basics/docs/part-01-boot-basics/02-configuration-properties-binding.md)
3. 最常见的坑一次性清掉：[`常见坑`](../springboot-basics/docs/appendix/90-common-pitfalls.md) / [`自检`](../springboot-basics/docs/appendix/99-self-check.md)

如果你只跑一个最小闭环，优先从 Lab 入手：

- `BootBasicsOverrideLabTest`（建议先跑，能最快把“覆盖优先级”变成断言）

---

## 下一章怎么接

配置的最终值会进入容器与自动配置判断，所以下一章我们把视角切到 **IoC 容器本身**：

- 下一章：[第 2 章：IoC 容器主线（Beans）](02-ioc-container-mainline.md)
