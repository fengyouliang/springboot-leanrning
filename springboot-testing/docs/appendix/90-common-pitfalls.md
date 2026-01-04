# 90 - Common Pitfalls（springboot-testing）

## 常见坑
1. 误把 slice 当成全量上下文：缺失的 bean/auto-config 导致误判
2. `@MockBean` 过度使用：测试变成“模拟驱动”，与真实行为脱节
3. 测试不稳定：依赖随机端口/时间/并发时机但没有隔离策略

