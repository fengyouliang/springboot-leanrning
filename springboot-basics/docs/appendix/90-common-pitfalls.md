# 90：常见坑清单（建议反复对照）

## 配置没生效

- 先看 `Environment#getActiveProfiles()`：你以为的 profile 是否真的激活？
- 再看 `Environment#getProperty("app.xxx")`：最终值到底是什么？
- 如果是测试覆盖：检查 `@SpringBootTest(properties=...)` 或 `@TestPropertySource` 等来源是否在覆盖你。

## `@ConfigurationProperties` 没绑定

- prefix 写错（`app` vs `apps`）
- 字段名映射误判（`featureEnabled` ↔ `feature-enabled`）
- 忘了启用扫描/启用绑定（本模块靠 `@ConfigurationPropertiesScan`）

## Bean 没切换 / 条件不生效

- 配置覆盖与 Bean 注册是两条线：配置变了不代表 Bean 一定会变。
- profile 条件：确认类上 `@Profile` 是否匹配当前激活 profile。

## 建议的排查顺序

1. 用断言确认最终值（不要猜）
2. 缩小上下文（优先 tests）
3. 再用日志/断点解释“为什么”

