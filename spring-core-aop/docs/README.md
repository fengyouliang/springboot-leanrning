# Spring Core AOP 文档索引

> 目标：把 AOP 的概念、主线调用链、源码关键点与可复现实验（Labs/Exercises）串成“像书本一样”的结构。

---

## Part 00｜阅读指南
- [00-deep-dive-guide](part-00-guide/00-deep-dive-guide.md)

## Part 01｜代理基础与心智模型（Proxy Fundamentals）
- [01-aop-proxy-mental-model](part-01-proxy-fundamentals/01-aop-proxy-mental-model.md)
- [02-jdk-vs-cglib](part-01-proxy-fundamentals/02-jdk-vs-cglib.md)
- [03-self-invocation](part-01-proxy-fundamentals/03-self-invocation.md)
- [04-final-and-proxy-limits](part-01-proxy-fundamentals/04-final-and-proxy-limits.md)
- [05-expose-proxy](part-01-proxy-fundamentals/05-expose-proxy.md)
- [06-debugging](part-01-proxy-fundamentals/06-debugging.md)

## Part 02｜自动代理与切点系统（AutoProxy & Pointcut）
- [07-autoproxy-creator-mainline](part-02-autoproxy-and-pointcuts/07-autoproxy-creator-mainline.md)
- [08-pointcut-expression-system](part-02-autoproxy-and-pointcuts/08-pointcut-expression-system.md)

## Part 03｜多层代理与真实世界叠加（Stacking）
- [09-multi-proxy-stacking](part-03-proxy-stacking/09-multi-proxy-stacking.md)
- [10-real-world-stacking-playbook](part-03-proxy-stacking/10-real-world-stacking-playbook.md)

## Appendix｜附录
- [90-common-pitfalls](appendix/90-common-pitfalls.md)
- [99-self-check](appendix/99-self-check.md)

---

## 如何验证（建议）
- 运行本模块测试：`mvn -pl spring-core-aop test`

