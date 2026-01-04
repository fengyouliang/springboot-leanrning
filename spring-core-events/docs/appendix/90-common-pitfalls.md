# 90. 常见坑清单（建议反复对照）

## 坑 1：误以为事件默认异步

- 事实：事件默认同步（见 `SpringCoreEventsLabTest#eventsAreSynchronousByDefault`）
- 影响：监听器慢会直接拖慢发布方

## 坑 2：监听器抛异常会炸到发布方

- 事实：同步事件在同一调用栈里执行（见 `SpringCoreEventsMechanicsLabTest#listenerExceptionsPropagateToPublisher_byDefault`）
- 学习建议：先理解默认行为，再谈隔离/重试

## 坑 3：没有 `@Order` 却依赖执行顺序

- 事实：默认顺序不稳定
- 建议：需要确定性（尤其 tests）时显式 `@Order`

## 坑 4：以为写了 `@Async` 就一定异步

- 事实：没有 `@EnableAsync` 时 `@Async` 会被忽略（见 mechanics lab）

## 坑 5：事件对象可变导致监听器互相污染

- 建议：学习阶段优先用不可变事件（record），减少副作用

