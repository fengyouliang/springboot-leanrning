# Spring Core Transaction（Tx）文档索引

> 目标：把 `@Transactional` 的边界、代理机制、回滚与传播讲清楚，并能用最小测试验证。

---

## Part 00｜阅读指南
- [00-deep-dive-guide](part-00-guide/00-deep-dive-guide.md)

## Part 01｜事务基础（Boundary & Proxy）
- [01-transaction-boundary](part-01-transaction-basics/01-transaction-boundary.md)
- [02-transactional-proxy](part-01-transaction-basics/02-transactional-proxy.md)
- [03-rollback-rules](part-01-transaction-basics/03-rollback-rules.md)
- [04-propagation](part-01-transaction-basics/04-propagation.md)

## Part 02｜编程式事务与调试（Template & Debugging）
- [05-transaction-template](part-02-template-and-debugging/05-transaction-template.md)
- [06-debugging](part-02-template-and-debugging/06-debugging.md)

## Appendix｜附录
- [90-common-pitfalls](appendix/90-common-pitfalls.md)
- [99-self-check](appendix/99-self-check.md)

---

## 如何验证（建议）
- 运行本模块测试：`mvn -pl spring-core-tx test`

