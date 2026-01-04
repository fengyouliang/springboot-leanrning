# springboot-business-case 文档

本模块是“业务化案例”：在一个小型业务闭环里串起 Web MVC + Validation + Events + AOP(Tracing) +（可选）事务等基础设施。

> 约束：本模块的 `src/main/java` 采用领域分层（`api/app/domain/events/tracing`），**不强行改为 Part 分包**；本次仅对 docs 与 tests 做 Part 化，确保“书本结构 + 可复现实验入口”成立。

## Start Here
- 导读：`docs/part-00-guide/00-deep-dive-guide.md`

## Part 01 - Business Case（主线）
- 01 架构与主流程：`docs/part-01-business-case/01-architecture-and-flow.md`

## Appendix
- 常见坑：`docs/appendix/90-common-pitfalls.md`
- 自测题：`docs/appendix/99-self-check.md`

## Labs & Exercises（最小可复现入口）
- Labs：`springboot-business-case/src/test/java/com/learning/springboot/bootbusinesscase/part01_business_case/BootBusinessCaseLabTest.java`
- Exercises：`springboot-business-case/src/test/java/com/learning/springboot/bootbusinesscase/part00_guide/BootBusinessCaseExerciseTest.java`

