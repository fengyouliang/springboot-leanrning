# 01 - Slice 与 Mock（Testing）

## 本章定位
本章把“测试类型选择”讲清楚：什么时候用 `@WebMvcTest`，什么时候必须用 `@SpringBootTest`，以及 `@MockBean` 的替换边界。

## 最小可复现入口
- WebMvc slice：`springboot-testing/src/test/java/com/learning/springboot/boottesting/part01_testing/GreetingControllerWebMvcLabTest.java`
- Full Boot：`springboot-testing/src/test/java/com/learning/springboot/boottesting/part01_testing/GreetingControllerSpringBootLabTest.java`
- MockBean：`springboot-testing/src/test/java/com/learning/springboot/boottesting/part01_testing/BootTestingMockBeanLabTest.java`

