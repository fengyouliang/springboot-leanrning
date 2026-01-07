# springboot-cache 文档

本模块聚焦 Spring Cache 抽象：`@Cacheable`/`@CachePut`/`@CacheEvict`、key/condition/unless、`sync` 防击穿，以及过期策略的可测试性。

## Start Here
- 导读：[part-00-guide/00-deep-dive-guide.md](part-00-guide/00-deep-dive-guide.md)

## Part 01 - Cache（主线机制）
- 01 `@Cacheable` 基础：[part-01-cache/01-cacheable-basics.md](part-01-cache/01-cacheable-basics.md)
- 02 `@CachePut` 与 `@CacheEvict`：[part-01-cache/02-cacheput-and-evict.md](part-01-cache/02-cacheput-and-evict.md)
- 03 key/condition/unless：[part-01-cache/03-key-condition-unless.md](part-01-cache/03-key-condition-unless.md)
- 04 `sync` 与击穿：[part-01-cache/04-sync-stampede.md](part-01-cache/04-sync-stampede.md)
- 05 过期与 Ticker：[part-01-cache/05-expiry-with-ticker.md](part-01-cache/05-expiry-with-ticker.md)

## Appendix
- 常见坑：[appendix/90-common-pitfalls.md](appendix/90-common-pitfalls.md)
- 自测题：[appendix/99-self-check.md](appendix/99-self-check.md)

## Labs & Exercises（最小可复现入口）
- Labs：`springboot-cache/src/test/java/com/learning/springboot/bootcache/part01_cache/BootCacheLabTest.java`
- Exercises：`springboot-cache/src/test/java/com/learning/springboot/bootcache/part00_guide/BootCacheExerciseTest.java`
