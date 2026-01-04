# springboot-basics 文档

本模块聚焦 Spring Boot 的“配置来源（PropertySources）+ Profiles + `@ConfigurationProperties` 绑定”主线。

## Start Here
- 导读：`docs/part-00-guide/00-deep-dive-guide.md`

## Part 01 - Boot Basics（配置与绑定）
- 01 配置来源与 Profiles：`docs/part-01-boot-basics/01-property-sources-and-profiles.md`
- 02 `@ConfigurationProperties` 绑定：`docs/part-01-boot-basics/02-configuration-properties-binding.md`

## Appendix
- 常见坑：`docs/appendix/90-common-pitfalls.md`
- 自测题：`docs/appendix/99-self-check.md`

## Labs & Exercises（最小可复现入口）
> 推荐从 tests 入手：先看断言，再反推机制。

- Default Profile / PropertySources：`springboot-basics/src/test/java/com/learning/springboot/bootbasics/part01_boot_basics/BootBasicsDefaultLabTest.java`
- Dev Profile：`springboot-basics/src/test/java/com/learning/springboot/bootbasics/part01_boot_basics/BootBasicsDevLabTest.java`
- Override（覆盖与优先级）：`springboot-basics/src/test/java/com/learning/springboot/bootbasics/part01_boot_basics/BootBasicsOverrideLabTest.java`
- Exercises：`springboot-basics/src/test/java/com/learning/springboot/bootbasics/part00_guide/BootBasicsExerciseTest.java`

