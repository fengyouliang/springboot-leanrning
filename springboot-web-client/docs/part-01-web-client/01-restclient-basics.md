# 01：RestClient（同步）最小闭环

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**01：RestClient（同步）最小闭环**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

本章用最小示例跑通 RestClient：发请求、解析 JSON、断言请求路径/headers。

## 你应该观察到什么

- RestClient 是阻塞式（blocking）调用：直接返回 `GreetingResponse`
- MockWebServer 能让你断言“请求到底发了什么”（path/header/body），比手工抓包更可控

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootWebClientRestClientLabTest`
- 建议命令：`mvn -pl springboot-web-client test`（或在 IDE 直接运行上面的测试类）

### 复现/验证补充说明（来自原文迁移）

## 实验入口

- `springboot-web-client/src/test/java/com/learning/springboot/bootwebclient/part01_web_client/BootWebClientRestClientLabTest.java`
  - `restClientGetsGreeting`
  - `restClientSendsExpectedPathAndHeaders`
  - `restClientCanPostJsonBody`

## F. 常见坑与边界

- （本章坑点待补齐：建议先跑一次 E，再回看断言失败场景与边界条件。）

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebClientRestClientLabTest`
- Test file：`springboot-web-client/src/test/java/com/learning/springboot/bootwebclient/part01_web_client/BootWebClientRestClientLabTest.java`

上一章：[part-00-guide/00-deep-dive-guide.md](../part-00-guide/00-deep-dive-guide.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[part-01-web-client/02-webclient-basics.md](02-webclient-basics.md)

<!-- BOOKIFY:END -->
