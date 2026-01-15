# 01：Servlet Async（Callable）与测试（asyncDispatch）

## 导读

- 本章主题：**01：Servlet Async（Callable）与测试（asyncDispatch）**
- 目标：用一个最小异步端点 + MockMvc 的 async 断言，把“线程模型/生命周期”讲清楚。

!!! summary "本章要点"

    - controller 返回 `Callable` 时，请求通常会进入 async 模式：这意味着“发起请求”和“得到最终响应”不在同一个同步链路里完成。
    - 测试异步请求不要靠 sleep：用 `asyncStarted` + `asyncDispatch` 固定行为。


!!! example "本章配套实验（先跑再读）"

    - Lab：`BootWebMvcAsyncSseLabTest`

## 机制主线

- 本章用 `BootWebMvcAsyncSseLabTest` 固定 async 生命周期：先断言 asyncStarted，再 dispatch 拿最终响应。

## 源码与断点

建议断点：
- `org.springframework.web.context.request.async.WebAsyncManager#startCallableProcessing`
- `org.springframework.web.servlet.mvc.method.annotation.CallableMethodReturnValueHandler#handleReturnValue`

## 最小可运行实验（Lab）

- Lab：`BootWebMvcAsyncSseLabTest`

## 常见坑与边界

- 异步逻辑一旦引入线程切换，最容易出现“偶现红测”；所以示例必须是“可控、有限、可快速完成”的。

## 小结与下一章

- 下一章进入 SSE：如何用 `SseEmitter` 返回 `text/event-stream`，以及测试如何避免挂死。

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebMvcAsyncSseLabTest`

上一章：[part-05-real-world-http/05-conditional-requests-last-modified-etag-filter.md](../part-05-real-world-http/05-conditional-requests-last-modified-etag-filter.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-06-async-sse/02-sse-emitter.md](02-sse-emitter.md)

<!-- BOOKIFY:END -->
