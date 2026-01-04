# 00 - Deep Dive Guide（springboot-data-jpa）

## 推荐学习目标
1. 用“实体状态机 + Persistence Context”解释大多数诡异行为
2. 能用最小测试复现 flush/脏检查/N+1，并能定位到 SQL 层的证据
3. 能把 `@DataJpaTest` 的 slice 边界与真实 Boot 启动边界区分开

## 推荐阅读顺序
1. `docs/part-01-data-jpa/01-entity-states.md`
2. `docs/part-01-data-jpa/02-persistence-context.md`
3. `docs/part-01-data-jpa/03-flush-and-visibility.md`
4. `docs/part-01-data-jpa/04-dirty-checking.md`
5. `docs/part-01-data-jpa/05-fetching-and-n-plus-one.md`
6. `docs/part-01-data-jpa/06-datajpatest-slice.md`
7. `docs/part-01-data-jpa/07-debug-sql.md`
8. `docs/appendix/90-common-pitfalls.md`
9. `docs/appendix/99-self-check.md`

## 如何跑实验
- 运行本模块测试：`mvn -pl springboot-data-jpa test`

