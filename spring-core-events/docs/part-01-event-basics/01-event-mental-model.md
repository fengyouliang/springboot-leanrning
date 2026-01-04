# 01. 事件心智模型：发布（publish）与订阅（listen）到底在解耦什么？

Spring 的 Application Events 解决的是一个非常具体的问题：

> 让“发生了什么”（事件）与“需要做什么”（监听器）解耦。

你不需要一开始就把它理解成“消息队列”。在本模块里，把它当成**进程内的回调机制**更合适。

## 本模块的最小闭环

- 发布方：`UserRegistrationService`
  - 在 `register(username)` 里发布 `UserRegisteredEvent`
- 监听方：`UserRegisteredListener`
  - `@EventListener` 接收事件，并写入 `InMemoryAuditLog`

对应测试：`SpringCoreEventsLabTest#listenerReceivesPublishedEvent`

## 你需要记住的 3 件事

1) **事件默认是同步的**

- `publishEvent(...)` 会在当前线程里依次调用监听器
- 监听器执行完毕，发布方法才会返回

验证入口：`SpringCoreEventsLabTest#eventsAreSynchronousByDefault`

2) **事件类型匹配，决定谁会被调用**

- 监听方法的参数类型决定它能接收什么事件
- 你可以发布任何对象（不仅仅是 `ApplicationEvent` 子类）

验证入口：`SpringCoreEventsLabTest#publishingPlainObjectsAlsoWorks_asPayloadEvents`

3) **事件对象建议做成“不可变”**

- 学习阶段特别建议把事件建模为不可变（例如 record）
- 否则多个监听器共享同一个事件对象时，很容易出现“互相污染”的副作用

本模块的 `UserRegisteredEvent` 就是 `record`，非常适合学习。

## 一句话总结

事件不是为了“炫技”，而是为了让你的核心流程更清晰：

- 核心流程：只负责发布“发生了什么”
- 扩展动作：由监听器决定“要做什么”

