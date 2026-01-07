# 90：常见坑清单（Web Client）

<!-- AG-CONTRACT:START -->

## A. 本章定位

- 本章主题：**90：常见坑清单（Web Client）**
- 阅读方式建议：先看 B 的结论，再按 C→D 跟主线，最后用 E 跑通闭环。

## B. 核心结论

- 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
- 如果只看一眼：请先跑一次 E 的最小实验，再回到 C 对照主线。

## C. 机制主线

- （本章主线内容暂以契约骨架兜底；建议结合源码与测试用例补齐主线解释。）

## D. 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## E. 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootWebClientRestClientLabTest` / `BootWebClientWebClientLabTest`
- 建议命令：`mvn -pl springboot-web-client test`（或在 IDE 直接运行上面的测试类）

## F. 常见坑与边界

## 只测 happy path

- 只测 200 会让你在线上第一次遇到 400/500 才知道怎么处理。
- 建议至少固化：
  - 4xx → 业务异常（通常不重试）
  - 5xx/网络错误 → 可重试/告警（视场景）

## timeout/retry 不可测

- connect timeout 很容易 flaky（受网络/系统影响）
- 建议优先用“延迟响应”复现 read/response timeout

## 幂等性没想清楚

- GET 通常更安全重试
- POST/PUT/DELETE 可能有副作用：重试前要想清楚（Exercise 有引导）

## 对应 Lab（可运行）

- `BootWebClientRestClientLabTest`
- `BootWebClientWebClientLabTest`

## G. 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- AG-CONTRACT:END -->

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebClientRestClientLabTest` / `BootWebClientWebClientLabTest`

上一章：[part-01-web-client/05-testing-with-mockwebserver.md](../part-01-web-client/05-testing-with-mockwebserver.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[appendix/99-self-check.md](99-self-check.md)

<!-- BOOKIFY:END -->
