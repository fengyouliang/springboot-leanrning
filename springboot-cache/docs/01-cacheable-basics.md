# 01：`@Cacheable` 最小闭环

## 实验入口

- `springboot-cache/src/test/java/com/learning/springboot/bootcache/BootCacheLabTest.java`
  - `cacheableCachesResultForSameKey`
  - `cacheableUsesDifferentEntriesForDifferentKeys`

## 你应该观察到什么

- 同一个 key（例如 name=alice）只计算一次，后续从 cache 直接返回
- 不同 key 会命中不同 entry

