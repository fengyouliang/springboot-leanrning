# 01：`@Async` 心智模型：代理与线程切换

本章只回答一个问题：**`@Async` 为什么能“切线程”？**

## 实验入口

- `springboot-async-scheduling/src/test/java/com/learning/springboot/bootasyncscheduling/BootAsyncSchedulingLabTest.java`
  - `asyncAnnotationDoesNothingWithoutEnableAsync`
  - `asyncRunsOnExecutorThreadWhenEnableAsyncPresent`

## 你应该观察到什么

- 没有 `@EnableAsync`：`@Async` 就像不存在，方法在当前线程执行
- 有 `@EnableAsync`：bean 会被代理，方法调用经代理转发到 executor 线程

## 机制解释（Why）

`@Async` 本质还是 **代理 + 拦截器**：

- 代理拦截方法调用
- 把“真正执行”提交给 `TaskExecutor`
- 对于返回 `Future/CompletableFuture` 的方法，把结果/异常封装起来返回

