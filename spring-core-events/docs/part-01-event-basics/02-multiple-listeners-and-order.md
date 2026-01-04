# 02. 多监听器与顺序：为什么 `@Order` 值得你认真对待？

一个事件通常不止一个监听器想要处理：

- 写审计日志
- 发欢迎通知
- 统计指标
- 触发后续异步任务

本章关注两个问题：

1) 多个监听器会不会都收到同一个事件？  
2) 多个监听器的执行顺序能不能依赖？

## 1) 多监听器：同一个事件会被“广播”

验证入口：`SpringCoreEventsLabTest#multipleListenersCanObserveTheSameEvent`

本模块用 `@Import` 注入了一个额外监听器：

- `ExtraUserRegisteredListener` 也会接收 `UserRegisteredEvent`
- 因此 audit log 里会出现两条记录

## 2) 顺序：默认不要依赖“自然顺序”

如果你没有显式指定顺序：

- 监听器的执行顺序可能与你的想象不一致
- 甚至在不同 JVM / 不同构建方式下表现不同

当你确实需要顺序（学习阶段很常见，因为你要做确定性断言），就用 `@Order`：

验证入口：`SpringCoreEventsLabTest#orderedListenersFollowOrderAnnotation`

## 你应该得到的结论

- 多监听器是事件机制的常态：它让你可以在不改发布方的情况下持续扩展能力
- 顺序默认不保证：需要确定性时就显式标注 `@Order`
