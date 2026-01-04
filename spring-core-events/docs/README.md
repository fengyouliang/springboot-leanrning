# Spring Core Events 文档索引

> 目标：用“概念 → 主线机制 → 源码关键点 → 最小可复现”把 Spring 事件系统串起来。

---

## Part 00｜阅读指南
- [00-deep-dive-guide](part-00-guide/00-deep-dive-guide.md)

## Part 01｜事件基础（Event Basics）
- [01-event-mental-model](part-01-event-basics/01-event-mental-model.md)
- [02-multiple-listeners-and-order](part-01-event-basics/02-multiple-listeners-and-order.md)
- [03-condition-and-payload](part-01-event-basics/03-condition-and-payload.md)
- [04-sync-and-exceptions](part-01-event-basics/04-sync-and-exceptions.md)

## Part 02｜异步与事务（Async & Transactional）
- [05-async-listener](part-02-async-and-transactional/05-async-listener.md)
- [06-async-multicaster](part-02-async-and-transactional/06-async-multicaster.md)
- [07-transactional-event-listener](part-02-async-and-transactional/07-transactional-event-listener.md)

## Appendix｜附录
- [90-common-pitfalls](appendix/90-common-pitfalls.md)
- [99-self-check](appendix/99-self-check.md)

---

## 如何验证（建议）
- 运行本模块测试：`mvn -pl spring-core-events test`

