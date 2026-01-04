# Spring Core Resources 文档索引

> 目标：把 Resource 抽象、classpath 解析规则与常见坑做成可复现的“书本结构”。

---

## Part 00｜阅读指南
- [00-deep-dive-guide](part-00-guide/00-deep-dive-guide.md)

## Part 01｜资源抽象与定位（Resource Abstraction）
- [01-resource-abstraction](part-01-resource-abstraction/01-resource-abstraction.md)
- [02-classpath-locations](part-01-resource-abstraction/02-classpath-locations.md)
- [03-classpath-star-and-pattern](part-01-resource-abstraction/03-classpath-star-and-pattern.md)
- [04-exists-and-handles](part-01-resource-abstraction/04-exists-and-handles.md)
- [05-reading-and-encoding](part-01-resource-abstraction/05-reading-and-encoding.md)
- [06-jar-vs-filesystem](part-01-resource-abstraction/06-jar-vs-filesystem.md)

## Appendix｜附录
- [90-common-pitfalls](appendix/90-common-pitfalls.md)
- [99-self-check](appendix/99-self-check.md)

---

## 如何验证（建议）
- 运行本模块测试：`mvn -pl spring-core-resources test`

