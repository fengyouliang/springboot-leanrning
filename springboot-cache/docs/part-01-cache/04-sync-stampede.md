# 04：`sync=true`：防缓存击穿（stampede）

## 实验入口

- `BootCacheLabTest#syncTrueAvoidsDuplicateComputationsForSameKey`

## 你应该观察到什么

- 并发请求同一个 key 时：
  - `sync=true` 能把“同 key 的并发计算”收敛成一次

## 机制解释（Why）

`sync=true` 的语义是：对同一个 key，只有一个线程负责计算并写入，其他线程等待结果。

