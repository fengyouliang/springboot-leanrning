# 90：常见坑清单（Web Client）

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

