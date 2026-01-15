# 第 12 章：Resources 主线

这一章解决的问题是：**为什么 `classpath:` 在 IDE 里能读到、打成 jar 后就读不到，为什么 pattern 扫描会漏/多，`exists()` 和 `getFile()` 有什么陷阱**。

---

## 主线（按时间线顺读）

1. 统一抽象：`Resource`（file/classpath/url/byte array 等）
2. 加载入口：`ResourceLoader` / `ApplicationContext` 提供统一加载能力
3. pattern 扫描：`PathMatchingResourcePatternResolver` 支持 `classpath*:` 等语法
4. jar 语义差异：能 `getInputStream()` 不代表能 `getFile()`
5. 常见坑：路径前缀、相对路径基准、jar 场景下 file 语义失效

---

## 深挖入口（模块 docs）

- 模块目录页：[`spring-core-resources/docs/README.md`](../spring-core-resources/docs/README.md)
- 模块主线时间线（含可跑入口）：[`spring-core-resources/docs/part-00-guide/03-mainline-timeline.md`](../spring-core-resources/docs/part-00-guide/03-mainline-timeline.md)

---

## 下一章怎么接

配置与资源加载之后，最容易被忽略但极其常见的“开关”是 Profile：它同时影响配置与 Bean 注册。我们单独把它串一遍。

- 下一章：[第 13 章：Profiles 主线](13-profiles-mainline.md)

