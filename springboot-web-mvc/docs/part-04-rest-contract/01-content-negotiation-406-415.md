# 01：Content Negotiation（406/415：Accept/Content-Type/produces/consumes）

## 导读

- 本章主题：**01：Content Negotiation（406/415：Accept/Content-Type/produces/consumes）**
- 目标：让 406/415 变成“可预期、可复现、可排障”的问题，而不是靠猜。

!!! summary "本章要点"

    - 415：客户端发来的 `Content-Type` 不被服务端接受（`consumes` 或 converter 不匹配）
    - 406：客户端的 `Accept` 要求服务端无法满足（`produces` 或 converter 不匹配）
    - 解决问题的第一步不是改业务代码，而是把 **请求头与方法映射约束** 对齐。


!!! example "本章配套实验（先跑再读）"

    - Lab：`BootWebMvcContractJacksonLabTest`

## 机制主线

- 本章用 `BootWebMvcContractJacksonLabTest` 固定两条证据链：
  - `/echo` 用错误 `Content-Type` → 415
  - `/ping` 用错误 `Accept` → 406
- 若你在排障时想“把猜测变成证据”，建议再配合 `BootWebMvcTestingDebuggingLabTest`：
  - 直接拿到 `resolvedException`，确认到底是 406 还是 415 的分支入口。

## 源码与断点

建议断点：
- `RequestMappingHandlerMapping#handleMatch`
- `org.springframework.web.servlet.mvc.method.RequestMappingInfoHandlerMapping#handleNoMatch`（映射阶段就不匹配时）
- `AbstractMessageConverterMethodArgumentResolver#readWithMessageConverters`
- `AbstractMessageConverterMethodProcessor#writeWithMessageConverters`

## 你应该怎么定位 406/415（按优先级）

> 目标：别在 controller 里盲改代码，而是沿着链路确认“到底在哪一段失败”。

1. **先确认映射约束**：controller 方法的 `produces/consumes` 是否与你的 `Accept/Content-Type` 对齐？
2. **再确认 converter**：
   - 415（read 失败）：能否找到“能读该 Content-Type”的 converter？
   - 406（write 失败）：能否找到“能写出 Accept 的格式”的 converter？
3. **用证据锁住分支**：MockMvc 的 `resolvedException`（见 `BootWebMvcTestingDebuggingLabTest`）是最快的“分支定位器”。

## 最小可运行实验（Lab）

- Lab：`BootWebMvcContractJacksonLabTest`
- Lab：`BootWebMvcTestingDebuggingLabTest`

## 常见坑与边界

- 你在 Postman/curl 里不小心带了 `Accept: */*` 或 `Content-Type` 缺失/错误，会让你误以为“后端逻辑坏了”，但实际上是契约不匹配。

## 小结与下一章

- 下一章进入 Jackson 可控：如何“只对某类请求严格”，避免全局影响。

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebMvcContractJacksonLabTest`
- Lab：`BootWebMvcTestingDebuggingLabTest`

上一章：[part-03-web-mvc-internals/05-controlleradvice-matching-and-ordering.md](../part-03-web-mvc-internals/05-controlleradvice-matching-and-ordering.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-04-rest-contract/02-jackson-objectmapper-controls.md](02-jackson-objectmapper-controls.md)

<!-- BOOKIFY:END -->
