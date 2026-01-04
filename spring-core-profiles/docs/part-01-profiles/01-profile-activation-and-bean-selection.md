# Profile 激活与 Bean 选择

本章目标：你读完后应该能回答下面三件事：
1. Profile 可以从哪里激活？（配置文件、环境变量、启动参数、测试注解）
2. `@Profile` 的语义是什么？（“是否注册这个 bean 定义”）
3. 当同一接口有多实现时，在不同 profile 下如何稳定选择到预期的实现？

对应验证入口（最小可复现）：
- `src/test/java/com/learning/springboot/springcoreprofiles/**`

