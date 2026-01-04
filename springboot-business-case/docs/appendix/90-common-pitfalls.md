# 90 - Common Pitfalls（springboot-business-case）

## 常见坑
1. 误把业务案例当成“只跑得起来的 demo”：缺乏断言与边界说明，容易失真
2. 异常传播路径不清晰：controller/service/listener/aspect 的责任边界混乱
3. 日志可观察性不足：看不到“谁触发了谁”，难以排障

