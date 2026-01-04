# 04. 同步与异常传播：为什么监听器抛异常会“炸到发布方”？

事件默认是同步的，所以异常传播也很直观：

> 监听器在发布方的调用栈里执行，因此监听器抛异常会直接传播回发布方。

## 在本模块如何验证

看 `SpringCoreEventsMechanicsLabTest#listenerExceptionsPropagateToPublisher_byDefault`

- 监听器直接 `throw new IllegalStateException("listener boom")`
- `context.publishEvent(...)` 会抛出同样的异常

## 你应该得到的结论

1) **同步事件不是“吞异常”的机制**

- 如果你希望“监听器失败不影响主流程”，你需要显式设计（比如异步、隔离、重试等）
- 学习仓库里建议先理解默认行为，再谈工程化处理

2) **事件不是“保证交付”的消息系统**

进程内同步事件更像“回调链”：

- 快
- 简单
- 但耦合在同一个线程与同一段调用链上

## 学习建议：如何避免“学歪”

当你想用事件做解耦时，先问自己：

- 这个动作如果失败，是否应该让主流程失败？
  - 应该：同步事件 + 异常传播是合理的
  - 不应该：考虑异步/隔离（见 [docs/05](05-async-listener.md) 与 [docs/06](06-async-multicaster.md)）

