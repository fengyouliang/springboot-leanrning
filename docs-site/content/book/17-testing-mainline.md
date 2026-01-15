# 第 17 章：Testing 主线

这一章解决的问题是：**为什么 `@WebMvcTest` 更快、为什么 `@SpringBootTest` 更像集成测试、为什么上下文缓存会让你“以为自己修好了”**。

---

## 主线（按时间线顺读）

1. 选择测试粒度：
   - slice test（更快、更聚焦）
   - full context（更接近真实，但更慢）
2. 控制上下文：MockBean/测试配置/测试 profile
3. 固化断言：让机制结论可回归（而不是靠日志）
4. 运行与排障：只跑一个 test class/一个方法，快速定位失败
5. 常见坑：上下文污染、并发不稳定、网络/时间相关、测试之间隐式依赖

---

## 深挖入口（模块 docs）

- 模块目录页：[`springboot-testing/docs/README.md`](../springboot-testing/docs/README.md)
- 模块主线时间线（含可跑入口）：[`springboot-testing/docs/part-00-guide/03-mainline-timeline.md`](../springboot-testing/docs/part-00-guide/03-mainline-timeline.md)

---

## 下一章怎么接

把这些机制串成一条“真实业务链路”，是验证你是否真正掌握的最快方式。我们用 business case 模块收束整本书。

- 下一章：[第 18 章：Business Case 收束](18-business-case.md)

