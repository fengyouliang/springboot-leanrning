# 主线时间线：Spring Core Tx（事务）

!!! summary
    - 这一模块关注：@Transactional 如何通过 AOP 代理把“事务边界”织入方法调用，以及传播/回滚规则如何生效。
    - 读完你应该能复述：**方法调用 → 事务拦截器 → 事务管理器 → 提交/回滚** 这一条主线。
    - 推荐顺序：先读《深挖导读》→ 本章 → Part 01（事务基础）→ Part 02（模板与调试）→ 附录排坑。

!!! example "建议先跑的 Lab（把时间线变成证据）"

    - Lab：`SpringCoreTxLabTest`

## 在 Spring 主线中的位置

- 事务依赖 AOP：没有代理就没有“拦截器包裹方法调用”的事务边界。
- 事务的“看起来不对”通常来自三类分支：**没代理上**、**传播/回滚规则与预期不同**、**资源/管理器配置不一致**。

## 主线时间线（建议顺读）

1. 先把“事务边界”这件事讲清楚：哪里开始、哪里结束、谁决定提交/回滚
   - 阅读：[01. 事务边界](../part-01-transaction-basics/01-transaction-boundary.md)
2. 再把“@Transactional 为何生效”跑通：代理与拦截器
   - 阅读：[02. @Transactional 代理](../part-01-transaction-basics/02-transactional-proxy.md)
3. 回滚规则：哪些异常会回滚、哪些不会（以及怎么验证）
   - 阅读：[03. 回滚规则](../part-01-transaction-basics/03-rollback-rules.md)
4. 传播行为：嵌套调用如何决定复用/新建事务
   - 阅读：[04. 传播行为](../part-01-transaction-basics/04-propagation.md)
5. 当你不想要注解：TransactionTemplate 的“显式边界”
   - 阅读：[05. TransactionTemplate](../part-02-template-and-debugging/05-transaction-template.md)
6. 最后学会调试：先能把“有没有进拦截器、拿到的是什么事务”看见
   - 阅读：[06. 调试](../part-02-template-and-debugging/06-debugging.md)

## 排坑与自检

- 常见坑：[90-common-pitfalls.md](../appendix/90-common-pitfalls.md)
- 自检：[99-self-check.md](../appendix/99-self-check.md)
