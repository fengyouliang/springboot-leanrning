# springboot-actuator 文档

本模块聚焦 Spring Boot Actuator 的暴露策略（exposure）、端点安全边界、以及“为什么我明明配置了但看不到端点”的排障路径。

## Start Here
- 导读：[part-00-guide/00-deep-dive-guide.md](part-00-guide/00-deep-dive-guide.md)

## Part 01 - Actuator（主线机制）
- 01 Actuator 基础与暴露：[part-01-actuator/01-actuator-basics.md](part-01-actuator/01-actuator-basics.md)

## Appendix
- 常见坑：[appendix/90-common-pitfalls.md](appendix/90-common-pitfalls.md)
- 自测题：[appendix/99-self-check.md](appendix/99-self-check.md)

## Labs & Exercises（最小可复现入口）
- Labs：`springboot-actuator/src/test/java/com/learning/springboot/bootactuator/part01_actuator/BootActuatorLabTest.java`
- Labs（暴露覆盖与优先级）：`springboot-actuator/src/test/java/com/learning/springboot/bootactuator/part01_actuator/BootActuatorExposureOverrideLabTest.java`
- Exercises：`springboot-actuator/src/test/java/com/learning/springboot/bootactuator/part00_guide/BootActuatorExerciseTest.java`
