# spring-core-events

本模块用于学习 **Spring Application Events（应用事件）**：

- 使用 `ApplicationEventPublisher` 发布事件
- 使用 `@EventListener` 处理事件
- 理解默认行为：事件默认是 **同步** 的

## 学习目标

- 理解应用事件的使用场景（解耦）
- 能在 Service 中发布一个简单的领域事件
- 能在 Listener 中处理事件，并产生一个可观察结果
- 用测试验证事件监听器被正确触发

## 运行

```bash
mvn -pl spring-core-events spring-boot:run
```

运行后观察控制台输出：

- 发布方发出 `UserRegisteredEvent`
- 监听方收到事件并写入内存审计日志
- runner 在发布后打印审计日志条目

## 测试

```bash
mvn -pl spring-core-events test
```

## Deep Dive（Labs / Exercises）

- Labs（默认启用）：
  - `SpringCoreEventsLabTest`：多监听器、`@Order`、condition、payload 事件、默认同步
  - `SpringCoreEventsMechanicsLabTest`：异常传播、`@Async`（启用/不启用）的线程差异
- Exercises（默认禁用）：`SpringCoreEventsExerciseTest`（带 `@Disabled`）

启用 Exercises：打开 `*ExerciseTest`，移除/注释 `@Disabled`，按提示完成后再运行 `mvn -pl spring-core-events test`。

## 说明

- 事件默认是同步的：发布方法会在监听器执行完成后才返回
- 也可以做异步事件（例如 `@Async` + `@EnableAsync`），但为了保持最小闭环，本模块暂不实现

## 小练习

- 新增另一个监听器，用不同格式写审计信息
- 新增第二种事件类型（例如 `UserDeletedEvent`）并处理
- 让监听器具备幂等性，并说明为什么需要幂等

## 参考

- Spring Framework Reference：Application Events and Listeners
