# Spring Boot Data JPA：目录

> 建议顺读 7 章把实体状态、持久化上下文、flush/脏检查与 N+1 的主线跑通；很多问题需要与事务（Tx）一起看。

## 从这里开始（建议顺序）

1. [主线时间线](part-00-guide/03-mainline-timeline.md)
2. [深挖导读](part-00-guide/00-deep-dive-guide.md)

## 顺读主线

- [实体状态](part-01-data-jpa/01-entity-states.md)
- [持久化上下文](part-01-data-jpa/02-persistence-context.md)
- [flush 与可见性](part-01-data-jpa/03-flush-and-visibility.md)
- [脏检查](part-01-data-jpa/04-dirty-checking.md)
- [fetching 与 N+1](part-01-data-jpa/05-fetching-and-n-plus-one.md)
- [@DataJpaTest](part-01-data-jpa/06-datajpatest-slice.md)
- [SQL 调试](part-01-data-jpa/07-debug-sql.md)

## 关联模块（按需串联）

- 事务边界与一致性：`spring-core-tx`

## 排坑与自检

- [常见坑](appendix/90-common-pitfalls.md)
- [自检](appendix/99-self-check.md)

