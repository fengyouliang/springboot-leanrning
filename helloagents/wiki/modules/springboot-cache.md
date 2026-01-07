# springboot-cache

## Purpose

学习 Spring Cache：缓存注解、key 生成、缓存失效与常见坑。

## Module Overview

- **Responsibility:** 用最小示例与测试覆盖缓存命中/失效/条件缓存。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-07

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
- **Lab (SpEL Key):** `springboot-cache/src/test/java/com/learning/springboot/bootcache/part01_cache/BootCacheSpelKeyLabTest.java`
- **Exercise:** `springboot-cache/src/test/java/com/learning/springboot/bootcache/part00_guide/BootCacheExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：入口类包名不变；cache 示例集中在 `com.learning.springboot.bootcache.part01_cache`
- `src/test/java`：`part00_guide`（Exercises）/ `part01_cache`（Labs），并在 `part01_cache` 内提供 `ManualTicker`

## Change History

- [202601071034_all_modules_docs_ag_contract](../../history/2026-01/202601071034_all_modules_docs_ag_contract/) - ✅ 已执行：全模块 docs 升级 A–G 章节契约（每章 A–G + 对应 Lab/Test + 至少 1 个 LabTest），并更新根 README 跨模块入口
- [202601062218_all_modules_docs_bookify](../../history/2026-01/202601062218_all_modules_docs_bookify/) - ✅ 已执行：以 docs/README.md 为 SSOT，对全部章节 upsert 统一尾部区块（### 对应 Lab/Test + 上一章｜目录｜下一章），并通过 `scripts/check-docs.sh`
- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 src/main/src/test 分包，并修复 README/docs 引用
- [202601062024_springboot_modules_teaching_rollout](../../history/2026-01/202601062024_springboot_modules_teaching_rollout/) - ✅ 已执行：docs/README 章节链接 SSOT 化 + guide/appendix 可跑入口块补齐 + 补齐 min-labs=2 + 自检闸门覆盖
