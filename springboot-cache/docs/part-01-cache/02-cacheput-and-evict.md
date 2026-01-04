# 02：`@CachePut/@CacheEvict`：更新与失效

## 实验入口

- `BootCacheLabTest#cachePutUpdatesCacheValue`
- `BootCacheLabTest#cacheEvictRemovesEntry`

## 你应该观察到什么

- `@CachePut` 会强制执行方法，并把返回值写入 cache
- `@CacheEvict` 会移除指定 key 的 entry（下一次访问会重新计算）

