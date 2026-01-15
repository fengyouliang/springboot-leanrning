# 主线时间线：Spring Boot Cache

!!! summary
    - 这一模块关注：缓存注解如何通过代理织入方法调用，以及 key/condition/unless/并发击穿等关键边界。
    - 读完你应该能复述：**方法调用 → 缓存拦截器 → key 计算 → 命中/回源 → 回写/失效** 这一条主线。
    - 推荐顺序：先读《深挖导读》→ 本章 → Part 01 顺读 → 附录排坑。

!!! example "建议先跑的 Lab（把时间线变成证据）"

    - Lab：`BootCacheLabTest`

## 在 Spring 主线中的位置

- Cache 依赖 AOP：很多行为差异来自代理边界、key 计算、条件表达式与并发语义。
- 缓存最终是“读写一致性”问题：你需要明确缓存层与数据层的边界。

## 主线时间线（建议顺读）

1. 先把 @Cacheable 的基本语义跑通（命中/回源/回写）
   - 阅读：[01. @Cacheable 基础](../part-01-cache/01-cacheable-basics.md)
2. 写路径：@CachePut / @CacheEvict 如何影响一致性
   - 阅读：[02. @CachePut/@CacheEvict](../part-01-cache/02-cacheput-and-evict.md)
3. key/condition/unless：表达式与行为差异的来源
   - 阅读：[03. key/condition/unless](../part-01-cache/03-key-condition-unless.md)
4. 并发击穿：sync 与 stampede 的真实语义
   - 阅读：[04. sync 与击穿](../part-01-cache/04-sync-stampede.md)
5. 过期与时间：如何验证“到底什么时候失效”
   - 阅读：[05. 过期语义](../part-01-cache/05-expiry-with-ticker.md)

## 排坑与自检

- 常见坑：[90-common-pitfalls.md](../appendix/90-common-pitfalls.md)
- 自检：[99-self-check.md](../appendix/99-self-check.md)
