# 03：异常传播：Future vs void

本章回答：异步方法抛异常，调用方到底能不能看到？

## 实验入口

- Future/CompletableFuture：
  - `BootAsyncSchedulingLabTest#asyncExceptionsPropagateThroughFuture`
- void：
  - `BootAsyncSchedulingLabTest#asyncExceptionsFromVoidAreHandledByAsyncUncaughtExceptionHandler`

## 你应该观察到什么

- 返回 Future：异常会进入 Future（调用方 get/join 时才能拿到）
- void：异常不会传回调用方，而是交给 `AsyncUncaughtExceptionHandler`

