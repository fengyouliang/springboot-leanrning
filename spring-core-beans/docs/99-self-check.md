# 99. 自测题：你是否真的理解了？

建议学习方式：

- 先不看代码，尝试回答问题
- 再去对应章节/实验里验证
- 最后再启用 Exercises 把理解落实成可运行的结论

## A. 心智模型（对应 01/06）

1) 用一句话解释：什么是 `BeanDefinition`？它与 Bean 实例的关系是什么？
2) BFPP 与 BPP 的差别是什么？它们分别作用在“定义层”还是“实例层”？
3) 为什么说“自动装配本质上也是在注册 BeanDefinition”？

## B. 注册入口（对应 02/10）

4) `@ComponentScan`、`@Bean`、`@Import` 这三种入口分别解决什么问题？
5) `ImportSelector` 与 `ImportBeanDefinitionRegistrar` 的角色差异是什么？
6) 你如何解释 Spring Boot 自动装配“从哪里拿到要导入的配置类列表”？

## C. 依赖注入（对应 03）

7) 同类型多个候选时，`@Qualifier` 与 `@Primary` 各自适合什么场景？
8) `ObjectProvider` 解决的是什么问题？它为什么有助于 prototype 注入？
9) 遇到 `NoUniqueBeanDefinitionException` 时，你的排查顺序是什么？

## D. Scope 与生命周期（对应 04/05）

10) prototype 的语义是什么？为什么“prototype 注入 singleton”会像单例？
11) `@PostConstruct` 在 bean 创建流程的哪个阶段触发？
12) 为什么 prototype 的 `@PreDestroy` 常常不会触发？

## E. 机制题（对应 07/08/09）

13) `proxyBeanMethods=false` 下，为什么在 `@Bean` 方法体里互相调用可能会 new 出额外实例？
14) 为什么 `getBean("sequence")` 拿到的是 Long 而不是 `SequenceFactoryBean`？
15) 构造器循环依赖为什么必然失败？setter 循环为什么有时能成功？

## F. 动手题（建议直接做 Exercises）

这些题都已经在本模块的 Exercises 里给出（默认 `@Disabled`）：

- 让 `FormattingService` 切换为 lower formatter（体会 `@Qualifier`）
- 去掉 `@Qualifier`，改用 `@Primary` 解决歧义
- 让 `DirectPrototypeConsumer` 每次都拿到新 id（体会 prototype 注入陷阱与解决方式）

对应文件：

- `src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansExerciseTest.java`

