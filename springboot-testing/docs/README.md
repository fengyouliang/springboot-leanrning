# springboot-testing 文档

本模块聚焦 Spring Boot 测试体系：`@SpringBootTest`、`@WebMvcTest` 等 slice、`@MockBean` 的替换语义，以及“如何用最小成本稳定复现问题”。

## Start Here
- 导读：[part-00-guide/00-deep-dive-guide.md](part-00-guide/00-deep-dive-guide.md)

## Part 01 - Testing（主线机制）
- 01 Slice 与 Mock：[part-01-testing/01-slice-and-mocking.md](part-01-testing/01-slice-and-mocking.md)

## Appendix
- 常见坑：[appendix/90-common-pitfalls.md](appendix/90-common-pitfalls.md)
- 自测题：[appendix/99-self-check.md](appendix/99-self-check.md)

## Labs & Exercises（最小可复现入口）
- WebMvc slice：`springboot-testing/src/test/java/com/learning/springboot/boottesting/part01_testing/GreetingControllerWebMvcLabTest.java`
- Full Boot：`springboot-testing/src/test/java/com/learning/springboot/boottesting/part01_testing/GreetingControllerSpringBootLabTest.java`
- `@MockBean` 语义：`springboot-testing/src/test/java/com/learning/springboot/boottesting/part01_testing/BootTestingMockBeanLabTest.java`
- Exercises：`springboot-testing/src/test/java/com/learning/springboot/boottesting/part00_guide/BootTestingExerciseTest.java`
