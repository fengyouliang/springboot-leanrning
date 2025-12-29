# 27. SmartLifecycle：start/stop 时机与 phase 顺序

`SmartLifecycle` 是容器提供的“启动/停止阶段”扩展点。

它非常适合表达：

- 我希望在容器 refresh 完成后自动 start
- 我希望在容器 close 时 stop
- 并且我希望多个组件之间按 phase 排序

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansSmartLifecycleLabTest.java`

## 1. 现象：start 按 phase 升序，stop 反向

对应测试：

- `SpringCoreBeansSmartLifecycleLabTest.smartLifecycleStartsInPhaseOrder_andStopsInReverseOrder()`

实验里我们注册了两个 lifecycle：

- A：phase=0
- B：phase=1

你会观察到：

- refresh 时：`start:A` → `start:B`
- close 时：`stop:B` → `stop:A`

## 2. 机制：LifecycleProcessor 统一管理

容器内部通过 `LifecycleProcessor`（默认 `DefaultLifecycleProcessor`）来：

- 在 refresh 阶段触发 `onRefresh()` → start
- 在 close 阶段触发 `onClose()` → stop

所以它不是“你手动调用 start/stop”，而是容器生命周期的一部分。

## 3. 常见坑

- **坑 1：把 SmartLifecycle 当成业务逻辑入口**
  - 它更像基础设施启动/停止钩子。

- **坑 2：stop(Runnable) 不调用 callback**
  - 容器会等待 callback，用于支持异步 stop；如果你不调用 callback，关闭可能卡住。

## 4. 一句话自检

- 你能解释清楚：为什么 stop 顺序是反向的吗？（提示：避免先停掉依赖者）
