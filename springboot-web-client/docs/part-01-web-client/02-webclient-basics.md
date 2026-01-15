# 02：WebClient（响应式）最小闭环

## 导读

- 本章主题：**02：WebClient（响应式）最小闭环**
- 阅读方式建议：先看“本章要点”，再沿主线阅读；需要时穿插源码/断点，最后跑通实验闭环。

!!! summary "本章要点"

    - 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
    - 如果只看一眼：请先跑一次本章的最小实验，再回到主线对照阅读。


!!! example "本章配套实验（先跑再读）"

    - Lab：`BootWebClientWebClientLabTest`
    - Test file：`springboot-web-client/src/test/java/com/learning/springboot/bootwebclient/part01_web_client/BootWebClientWebClientLabTest.java`

## 机制主线

本章用最小示例跑通 WebClient：发请求、解析 JSON、用 StepVerifier 断言响应。

## 你应该观察到什么

- WebClient 返回的是 `Mono<T>`：成功/失败都在 reactive 流里表达（不是“抛异常/返回值”二选一）
- `StepVerifier` 能把“next/error/complete”写成确定性断言，比随手 `.block()` 更稳定

## 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootWebClientWebClientLabTest`
- 建议命令：`mvn -pl springboot-web-client test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 实验入口

- `springboot-web-client/src/test/java/com/learning/springboot/bootwebclient/part01_web_client/BootWebClientWebClientLabTest.java`
  - `webClientGetsGreeting`
  - `webClientSendsExpectedPathAndHeaders`
  - `webClientCanPostJsonBody`

- WebClient 返回的是 `Mono<T>`：错误与结果都在 reactive 流里
- StepVerifier 能让你在测试里把“完成/错误”写成可断言的实验

## 常见坑与边界

### 坑点 1：用 `.block()` 代替 StepVerifier，导致“错误路径没测到/测试挂死”

- Symptom：测试看起来能跑通成功路径，但错误路径（4xx/5xx/timeout）没有任何断言；或者 `.block()` 没有超时导致卡住
- Root Cause：
  - reactive 流的错误是信号（error signal），需要你显式断言
  - `.block()` 更像“临时把响应式当同步用”，容易漏掉语义与边界
- Verification：
  - StepVerifier 固定成功路径：`BootWebClientWebClientLabTest#webClientGetsGreeting`
  - timeout 会失败（需要明确超时边界）：`BootWebClientWebClientLabTest#webClientResponseTimeoutFailsFast`
- Fix：成功/失败都优先用 StepVerifier 写断言；不得不 block 时也要明确 timeout（并把超时作为可回归证据）

## 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebClientWebClientLabTest`
- Test file：`springboot-web-client/src/test/java/com/learning/springboot/bootwebclient/part01_web_client/BootWebClientWebClientLabTest.java`

上一章：[part-01-web-client/01-restclient-basics.md](01-restclient-basics.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-01-web-client/03-error-handling.md](03-error-handling.md)

<!-- BOOKIFY:END -->
