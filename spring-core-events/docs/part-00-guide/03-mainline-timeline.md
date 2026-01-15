# 主线时间线：Spring Events

!!! summary
    - 这一模块关注：事件发布/监听在 Spring 中如何工作，以及同步/异步/事务事件的边界与落地方式。
    - 读完你应该能复述：**发布事件 → Multicaster 分发 → Listener 执行（同步/异步/事务）** 这一条主线。
    - 推荐顺序：先读《深挖导读》→ 本章 → Part 01（事件基础）→ Part 02（异步与事务）→ 附录排坑。

!!! example "建议先跑的 Lab（把时间线变成证据）"

    - Lab：`SpringCoreEventsLabTest`

## 在 Spring 主线中的位置

- 事件是“解耦工具”：它把调用关系从“直接调用”变成“发布/订阅”，但也会带来时序与可见性问题。
- 当事件变成异步或与事务绑定时，问题常常来自“什么时候发布、什么时候真正执行”。

## 主线时间线（建议顺读）

1. 先建立心智模型：事件到底是什么、与直接调用的差异是什么
   - 阅读：[01. 事件心智模型](../part-01-event-basics/01-event-mental-model.md)
2. 多个 Listener 的执行顺序与组合方式
   - 阅读：[02. 多监听器与顺序](../part-01-event-basics/02-multiple-listeners-and-order.md)
3. 条件与 payload：如何写出“只在特定条件触发”的事件监听
   - 阅读：[03. 条件与 payload](../part-01-event-basics/03-condition-and-payload.md)
4. 同步执行与异常：异常会不会中断后续 listener
   - 阅读：[04. 同步与异常](../part-01-event-basics/04-sync-and-exceptions.md)
5. 异步监听：从 @AsyncListener 到 multicaster 的线程模型
   - 阅读：[05. 异步监听](../part-02-async-and-transactional/05-async-listener.md)
   - 阅读：[06. 异步 multicaster](../part-02-async-and-transactional/06-async-multicaster.md)
6. 事务事件：什么时候触发、提交/回滚会怎么影响执行
   - 阅读：[07. 事务事件监听](../part-02-async-and-transactional/07-transactional-event-listener.md)

## 排坑与自检

- 常见坑：[90-common-pitfalls.md](../appendix/90-common-pitfalls.md)
- 自检：[99-self-check.md](../appendix/99-self-check.md)
