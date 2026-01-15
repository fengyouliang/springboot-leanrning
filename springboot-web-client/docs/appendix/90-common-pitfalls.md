# 90：常见坑清单（Web Client）

## 导读

- 本章主题：**90：常见坑清单（Web Client）**
- 阅读方式建议：先看“本章要点”，再沿主线阅读；需要时穿插源码/断点，最后跑通实验闭环。

!!! summary "本章要点"

    - 读完本章，你应该能用 2–3 句话复述“它解决什么问题 / 关键约束是什么 / 常见坑在哪里”。
    - 如果只看一眼：请先跑一次本章的最小实验，再回到主线对照阅读。


!!! example "本章配套实验（先跑再读）"

    - Lab：`BootWebClientRestClientLabTest` / `BootWebClientWebClientLabTest`

## 机制主线

- （本章主线内容暂以契约骨架兜底；建议结合源码与测试用例补齐主线解释。）

## 源码与断点

- 建议优先从“E 中的测试用例断言”反推调用链，再定位到关键类/方法设置断点。
- 若本章包含 Spring 内部机制，请以“入口方法 → 关键分支 → 数据结构变化”三段式观察。

## 最小可运行实验（Lab）

- 本章已在正文中引用以下 LabTest（建议优先跑它们）：
- Lab：`BootWebClientRestClientLabTest` / `BootWebClientWebClientLabTest`
- 建议命令：`mvn -pl springboot-web-client test`（或在 IDE 直接运行上面的测试类）

## 常见坑与边界

## 只测 happy path

- 只测 200 会让你在线上第一次遇到 400/500 才知道怎么处理。
- 建议至少固化：
  - 4xx → 业务异常（通常不重试）
  - 5xx/网络错误 → 可重试/告警（视场景）

## timeout/retry 不可测

- connect timeout 很容易 flaky（受网络/系统影响）
- 建议优先用“延迟响应”复现 read/response timeout

## 幂等性没想清楚

## Filter 顺序误判：request 顺序 ≠ response 顺序

- Symptom：你按注册顺序写了多个 `ExchangeFilterFunction`，以为 request/response 都按同样顺序执行；结果 debug 时发现 response 相关逻辑“倒着来”。
- Root Cause：`WebClient` 的 filter 本质上是对 `ExchangeFunction` 的一层层包裹：request 走外→内，response 信号回流时是内→外（表现为 response 侧顺序反转）。
- Verification：`BootWebClientWebClientFilterOrderLabTest#webClientFilters_requestOrderAndResponseOrder_areDifferent`
- Breakpoints：`DefaultWebClient$DefaultRequestBodyUriSpec#exchange`、`ExchangeFilterFunction` 链路的装配与调用
- Fix：写 filter 时区分 request/response 侧的执行顺序；把“期望顺序”直接写进 Lab/Test，避免靠脑补。

- GET 通常更安全重试
- POST/PUT/DELETE 可能有副作用：重试前要想清楚（Exercise 有引导）

## 对应 Lab（可运行）

- `BootWebClientRestClientLabTest`
- `BootWebClientWebClientLabTest`

## 小结与下一章

- 本章完成后：请对照上一章/下一章导航继续阅读，形成模块内连续主线。

<!-- BOOKIFY:START -->

### 对应 Lab/Test

- Lab：`BootWebClientRestClientLabTest` / `BootWebClientWebClientLabTest`

上一章：[part-01-web-client/05-testing-with-mockwebserver.md](../part-01-web-client/05-testing-with-mockwebserver.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[appendix/99-self-check.md](99-self-check.md)

<!-- BOOKIFY:END -->
