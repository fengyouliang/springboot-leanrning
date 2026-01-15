# 主线时间线：Spring Boot Data JPA

!!! summary
    - 这一模块关注：JPA 的实体状态与持久化上下文如何工作，以及 flush/dirty checking/fetching 等最影响真实项目的分支。
    - 读完你应该能复述：**实体状态 → Persistence Context → SQL 何时发出（flush）→ 可见性与一致性** 这一条主线。
    - 推荐顺序：先读《深挖导读》→ 本章 → Part 01 顺读 → 附录排坑。

!!! example "建议先跑的 Lab（把时间线变成证据）"

    - Lab：`BootDataJpaLabTest`

## 在 Spring 主线中的位置

- Data JPA 几乎必然与事务一起出现：很多“查不到/查到旧数据”的问题，本质是事务隔离 + flush 时机 + 持久化上下文的叠加。
- 性能问题的高发点：N+1、无意的 flush、脏检查导致的额外 SQL。

## 主线时间线（建议顺读）

1. 先把实体状态讲清楚：Transient/Managed/Detached/Removed
   - 阅读：[01. 实体状态](../part-01-data-jpa/01-entity-states.md)
2. 再把持久化上下文跑通：一级缓存与 identity
   - 阅读：[02. 持久化上下文](../part-01-data-jpa/02-persistence-context.md)
3. flush 与可见性：什么时候会发 SQL，为什么“看起来没写但查到了”
   - 阅读：[03. flush 与可见性](../part-01-data-jpa/03-flush-and-visibility.md)
4. 脏检查：为什么你没 save 也会 update
   - 阅读：[04. 脏检查](../part-01-data-jpa/04-dirty-checking.md)
5. 抓住性能分支：fetching 与 N+1
   - 阅读：[05. fetching 与 N+1](../part-01-data-jpa/05-fetching-and-n-plus-one.md)
6. 用 slice 测试把行为固定下来：@DataJpaTest
   - 阅读：[06. @DataJpaTest](../part-01-data-jpa/06-datajpatest-slice.md)
7. 学会看 SQL：把“到底执行了什么”变成可观察证据
   - 阅读：[07. SQL 调试](../part-01-data-jpa/07-debug-sql.md)

## 排坑与自检

- 常见坑：[90-common-pitfalls.md](../appendix/90-common-pitfalls.md)
- 自检：[99-self-check.md](../appendix/99-self-check.md)
