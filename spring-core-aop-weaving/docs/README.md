# Spring Core AOP Weaving 文档索引

> 目标：把 **AspectJ weaving（LTW/CTW）** 的心智模型、能力边界与可复现实验（Labs/Exercises）串成“像书本一样”的结构。

---

## Part 00｜阅读指南
- [00-deep-dive-guide](part-00-guide/00-deep-dive-guide.md)

## Part 01｜心智模型（Proxy vs Weaving）
- [01-proxy-vs-weaving](part-01-mental-model/01-proxy-vs-weaving.md)

## Part 02｜LTW：Load-Time Weaving（-javaagent）
- [02-ltw-basics](part-02-ltw/02-ltw-basics.md)

## Part 03｜CTW：Compile-Time Weaving（编译期织入）
- [03-ctw-basics](part-03-ctw/03-ctw-basics.md)

## Part 04｜Join Point & Pointcut Cookbook
- [04-join-point-cookbook](part-04-join-points/04-join-point-cookbook.md)

## Appendix｜附录
- [90-common-pitfalls](appendix/90-common-pitfalls.md)
- [99-self-check](appendix/99-self-check.md)

---

## 如何验证（建议）
- 运行本模块测试：`mvn -pl spring-core-aop-weaving test`
