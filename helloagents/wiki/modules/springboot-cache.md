# springboot-cache

## Purpose

学习 Spring Cache：缓存注解、key 生成、缓存失效与常见坑。

## Module Overview

- **Responsibility:** 用最小示例与测试覆盖缓存命中/失效/条件缓存。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-04

## Specifications

### Requirement: 缓存学习闭环
**Module:** springboot-cache
通过可断言实验理解缓存行为。

#### Scenario: 缓存命中与失效可验证
- 通过测试断言方法调用次数/缓存内容

## Dependencies

- 与其他模块弱耦合

## Docs & 复现入口

- **Docs Index:** `springboot-cache/docs/README.md`
- **Docs Guide:** `springboot-cache/docs/part-00-guide/00-deep-dive-guide.md`
- **Lab:** `springboot-cache/src/test/java/com/learning/springboot/bootcache/part01_cache/BootCacheLabTest.java`
- **Exercise:** `springboot-cache/src/test/java/com/learning/springboot/bootcache/part00_guide/BootCacheExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：入口类包名不变；cache 示例集中在 `com.learning.springboot.bootcache.part01_cache`
- `src/test/java`：`part00_guide`（Exercises）/ `part01_cache`（Labs），并在 `part01_cache` 内提供 `ManualTicker`

## Change History

- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 src/main/src/test 分包，并修复 README/docs 引用
