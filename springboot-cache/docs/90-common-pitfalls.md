# 90：常见坑清单（Cache）

## 把缓存当数据库

- cache 命中 ≠ 数据库存在/一致
- 缓存一致性要靠策略：put/evict、TTL、版本号等

## key 没想清楚

- 单参默认 key 通常是参数本身
- 多参默认 key 是 `SimpleKey`（Exercise 有引导）

## sync=true 的误解

- sync=true 不是“万能并发锁”
- 它只对同一个 key 的并发计算生效

