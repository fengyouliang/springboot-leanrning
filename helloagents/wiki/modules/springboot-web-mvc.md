# springboot-web-mvc

## Purpose

学习 Spring MVC 的两条主线：

- REST API（JSON）：`@RestController`、校验、统一错误响应
- 传统 MVC（HTML）：`@Controller`、Thymeleaf 页面渲染、表单提交（绑定/校验/回显/PRG）、错误页与内容协商

## Module Overview

- **Responsibility:** 提供可运行 Web 示例与测试（MockMvc 等），帮助理解请求处理链路。
- **Status:** 🚧In Development
- **Last Updated:** 2026-01-07

## Specifications

### Requirement: Web MVC 学习闭环
**Module:** springboot-web-mvc
覆盖请求处理、参数绑定与异常处理策略，并补齐传统 MVC（HTML）渲染与错误页机制。

#### Scenario: 请求处理链路可被测试验证
- 通过 MockMvc 等方式断言响应与错误处理

### Requirement: 传统 MVC 页面渲染学习闭环
**Module:** springboot-web-mvc
覆盖 `@Controller`、Thymeleaf、表单提交（绑定/校验/回显/PRG）与错误页/Accept 内容协商，并提供可复现测试入口。

## Dependencies

- 与安全/测试模块有学习路径关联（可选）

## Docs & 复现入口

- **Docs Index:** `springboot-web-mvc/docs/README.md`
- **Docs Guide:** `springboot-web-mvc/docs/part-00-guide/00-deep-dive-guide.md`
- **Labs:**
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part01_web_mvc/BootWebMvcSpringBootLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part02_view_mvc/BootWebMvcViewLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part02_view_mvc/BootWebMvcErrorViewLabTest.java`
  - `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part02_view_mvc/BootWebMvcViewSpringBootLabTest.java`
- **Exercises:** `springboot-web-mvc/src/test/java/com/learning/springboot/bootwebmvc/part00_guide/BootWebMvcExerciseTest.java`

## Source Layout（与 docs Part 对齐）

- `src/main/java`：入口类包名不变；示例分两组：
  - REST 主线：`com.learning.springboot.bootwebmvc.part01_web_mvc`
  - 页面主线：`com.learning.springboot.bootwebmvc.part02_view_mvc`
- `src/test/java`：`part00_guide`（Exercises）/ `part01_web_mvc`（Labs）

## Change History

- [202601071034_all_modules_docs_ag_contract](../../history/2026-01/202601071034_all_modules_docs_ag_contract/) - ✅ 已执行：全模块 docs 章节结构整理（A–G 结构 + 对应 Lab/Test 入口块）；后续不再推荐 A–G 作为写作规范/闸门
- [202601062218_all_modules_docs_bookify](../../history/2026-01/202601062218_all_modules_docs_bookify/) - ✅ 已执行：以 docs/README.md 为 SSOT，对全部章节 upsert 统一尾部区块（### 对应 Lab/Test + 上一章｜目录｜下一章），并通过 `scripts/check-docs.sh`
- [202601041358_springboot-part-structure-sync](../../history/2026-01/202601041358_springboot-part-structure-sync/) - ✅ 已执行：对齐 docs Part 与 src/main/src/test 分包，并修复 README/docs 引用
- [202601061309_springboot-web-mvc-thymeleaf-view-rendering](../../history/2026-01/202601061309_springboot-web-mvc-thymeleaf-view-rendering/) - ✅ 已执行：补齐传统 MVC（Thymeleaf/表单/错误页/Accept）+ docs 与 tests 闭环
- [202601062024_springboot_modules_teaching_rollout](../../history/2026-01/202601062024_springboot_modules_teaching_rollout/) - ✅ 已执行：docs/README 章节链接 SSOT 化 + guide/appendix 可跑入口块补齐 + 自检闸门覆盖
