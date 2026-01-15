# Spring Core AOP：目录

> 这一模块建议“从代理主线顺读”：先把代理心智模型与边界打牢，再进入 AutoProxyCreator 的主线，最后处理真实世界的多层代理叠加与排障。

## 从这里开始（建议顺序）

1. [主线时间线](part-00-guide/03-mainline-timeline.md)
2. [深挖导读](part-00-guide/00-deep-dive-guide.md)

## 顺读主线

- [代理心智模型](part-01-proxy-fundamentals/01-aop-proxy-mental-model.md)
- [JDK vs CGLIB](part-01-proxy-fundamentals/02-jdk-vs-cglib.md)
- [self-invocation](part-01-proxy-fundamentals/03-self-invocation.md)
- [代理限制（final 等）](part-01-proxy-fundamentals/04-final-and-proxy-limits.md)
- [exposeProxy](part-01-proxy-fundamentals/05-expose-proxy.md)
- [代理调试](part-01-proxy-fundamentals/06-debugging.md)
- [AutoProxyCreator 主线](part-02-autoproxy-and-pointcuts/07-autoproxy-creator-mainline.md)
- [切点表达式系统](part-02-autoproxy-and-pointcuts/08-pointcut-expression-system.md)
- [多层代理叠加](part-03-proxy-stacking/09-multi-proxy-stacking.md)
- [叠加排障手册](part-03-proxy-stacking/10-real-world-stacking-playbook.md)

## 排坑与自检

- [常见坑](appendix/90-common-pitfalls.md)
- [自检](appendix/99-self-check.md)

