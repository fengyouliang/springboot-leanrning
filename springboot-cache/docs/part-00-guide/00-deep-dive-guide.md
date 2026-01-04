# 00 - Deep Dive Guide（springboot-cache）

## 推荐学习目标
1. 能解释“缓存命中/未命中/更新/失效”的语义差异
2. 能把 key/condition/unless 的规则写成可断言的复现
3. 能解释 `sync` 解决的是什么问题，以及它的代价与边界

## 如何跑实验
- 运行本模块测试：`mvn -pl springboot-cache test`

