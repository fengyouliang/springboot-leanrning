# 第 9 章：Cache 主线

这一章解决的问题是：**为什么加上 `@Cacheable` 就能缓存、缓存 key 怎么算、为什么同一个方法有时命中有时不命中**。核心仍然是：AOP 代理 + Cache 抽象。

---

## 主线（按时间线顺读）

1. 你声明缓存意图：`@Cacheable/@CachePut/@CacheEvict`
2. 容器为目标 Bean 创建代理（和事务类似）
3. 调用进入缓存拦截器：
   - 计算 key（key generator / SpEL）
   - 查询 Cache（命中则短路返回）
   - 不命中则调用目标方法并写回
4. 常见坑：自调用绕过缓存、key 设计不稳定、null 值策略、cache manager 配置差异

---

## 深挖入口（模块 docs）

- 模块目录页：[`springboot-cache/docs/README.md`](../springboot-cache/docs/README.md)
- 模块主线时间线（含可跑入口）：[`springboot-cache/docs/part-00-guide/03-mainline-timeline.md`](../springboot-cache/docs/part-00-guide/03-mainline-timeline.md)

---

## 下一章怎么接

缓存解决“读多写少”的成本，但很多业务还有“异步与定时任务”的需求：我们进入 Async/Scheduling 主线。

- 下一章：[第 10 章：Async/Scheduling 主线](10-async-scheduling-mainline.md)

