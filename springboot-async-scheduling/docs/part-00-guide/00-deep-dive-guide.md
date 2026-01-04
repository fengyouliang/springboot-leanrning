# 00 - Deep Dive Guide（springboot-async-scheduling）

## 推荐学习目标
1. 能解释 `@Async` 为什么依赖代理（以及它和 AOP 的共性）
2. 能把“线程在哪里切换”的证据写进测试或日志
3. 能解释自调用为何会绕过 `@Async`
4. 能理解 `@Scheduled` 的基本触发语义与边界

## 如何跑实验
- 运行本模块测试：`mvn -pl springboot-async-scheduling test`

