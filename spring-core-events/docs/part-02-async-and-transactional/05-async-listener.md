# 05. 异步监听器：`@Async` 生效需要什么？线程会怎么变？

异步监听器的目标是把“监听器逻辑”从发布方的线程里拆出去：

- 发布方更快返回
- 监听器在另一个线程执行（通常由线程池提供）

## 关键点：`@Async` 不是“写了就生效”

验证入口：`SpringCoreEventsMechanicsLabTest`

### 1) 开启 `@EnableAsync`：异步才会生效

看 `asyncListenerRunsOnDifferentThread_whenEnableAsyncIsOn`：

- 配置类加 `@EnableAsync`
- 提供 `ThreadPoolTaskExecutor`，并设置 `threadNamePrefix`
- 断言线程名以 `events-async-` 开头

### 2) 不开启 `@EnableAsync`：`@Async` 会被忽略

看 `asyncAnnotationIsIgnored_withoutEnableAsync`：

- 同样的 listener 方法加了 `@Async`
- 但由于没有 `@EnableAsync`，最终还是在当前线程执行

## 你应该得到的结论

- 异步不是事件的“默认能力”，而是另一个拦截器机制（`@Async`）叠加出来的
- 学习阶段最好用“线程名断言”来验证异步（比看日志稳定）

## 常见误区

- “我用了 `@Async`，为什么还是同步？”
  - 多半是没启用 async（或线程池没配置）

