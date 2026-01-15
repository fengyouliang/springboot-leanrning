# 01：CORS 与预检（OPTIONS：浏览器为什么要先问一句）

## 导读

- 本章主题：**01：CORS 与预检（OPTIONS：浏览器为什么要先问一句）**
- 目标：用测试稳定复现“预检请求”和响应头，让你能解释：为什么前端明明没发 GET，却先发了 OPTIONS。

!!! summary "本章要点"

    - CORS 是浏览器约束：服务端必须用 `Access-Control-*` 响应头“授权”跨域访问。
    - 预检（preflight）是浏览器在某些请求条件下先发的 OPTIONS，用来确认方法/headers 是否被允许。


!!! example "本章配套实验（先跑再读）"

    - Lab：`BootWebMvcRealWorldHttpLabTest`

## 机制主线

- 本章用 `BootWebMvcRealWorldHttpLabTest` 固定预检请求与响应头断言。

## 源码与断点

建议断点：
- `org.springframework.web.cors.DefaultCorsProcessor#processRequest`
- `org.springframework.web.servlet.handler.AbstractHandlerMapping#getHandler`

## 最小可运行实验（Lab）

- Lab：`BootWebMvcRealWorldHttpLabTest`

## 常见坑与边界

- 你只在后端放开 GET，但忘了允许前端带的自定义 header（例如 `X-Request-Id`），预检会失败。

## 小结与下一章

- 下一章进入 multipart 上传：为什么 `@RequestBody` 解析不了 `multipart/form-data`。

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebMvcRealWorldHttpLabTest`

上一章：[part-04-rest-contract/04-problemdetail-vs-custom-error.md](../part-04-rest-contract/04-problemdetail-vs-custom-error.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-05-real-world-http/02-multipart-upload.md](02-multipart-upload.md)

<!-- BOOKIFY:END -->
