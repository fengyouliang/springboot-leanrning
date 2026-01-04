# springboot-data-jpa 文档

本模块聚焦 JPA/Hibernate 的实体状态、持久化上下文、flush/可见性、脏检查，以及 N+1 与排障路径。

## Start Here
- 导读：`docs/part-00-guide/00-deep-dive-guide.md`

## Part 01 - Data JPA（主线机制）
- 01 实体状态：`docs/part-01-data-jpa/01-entity-states.md`
- 02 持久化上下文：`docs/part-01-data-jpa/02-persistence-context.md`
- 03 flush 与可见性：`docs/part-01-data-jpa/03-flush-and-visibility.md`
- 04 脏检查：`docs/part-01-data-jpa/04-dirty-checking.md`
- 05 fetching 与 N+1：`docs/part-01-data-jpa/05-fetching-and-n-plus-one.md`
- 06 `@DataJpaTest` slice：`docs/part-01-data-jpa/06-datajpatest-slice.md`
- 07 Debug SQL：`docs/part-01-data-jpa/07-debug-sql.md`

## Appendix
- 常见坑：`docs/appendix/90-common-pitfalls.md`
- 自测题：`docs/appendix/99-self-check.md`

## Labs & Exercises（最小可复现入口）
- Labs：`springboot-data-jpa/src/test/java/com/learning/springboot/bootdatajpa/part01_data_jpa/BootDataJpaLabTest.java`
- Exercises：`springboot-data-jpa/src/test/java/com/learning/springboot/bootdatajpa/part00_guide/BootDataJpaExerciseTest.java`

