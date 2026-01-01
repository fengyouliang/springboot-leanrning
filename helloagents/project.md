# 项目技术约定（Project Technical Conventions）

## 技术栈

- **Java:** 17
- **构建工具:** Maven（多模块）
- **Spring Boot:** 由父 `pom.xml` 统一管理

## 代码与命名约定

- **模块组织:** 每个学习主题一个独立 Maven module（例如 `spring-core-beans`、`spring-core-events`）。
- **包名约定:** `com.learning.springboot.<module>`（例如 `com.learning.springboot.springcorebeans`）。
- **风格优先级:** 以当前仓库代码风格为准（避免为了“更优雅”而过度重构）。

## 测试与验证约定

- **测试框架:** JUnit 5 + AssertJ（由 `spring-boot-starter-test` 提供）
- **测试目标:** “可断言的观察点”优先于日志（能稳定复现实验结论）
- **命令约定:** 优先 `mvn -pl <module> test` 只跑单模块

