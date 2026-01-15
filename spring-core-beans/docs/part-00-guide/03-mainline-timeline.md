# 主线时间线：Spring Core Beans（IoC 容器）

!!! summary
    - 这一模块关注：ApplicationContext/BeanFactory 如何把“定义”变成“对象”，并在过程中提供可插拔的扩展点。
    - 读完你应该能复述：**注册 BeanDefinition → 执行 Post-Processor → 实例化/注入 → 生命周期回调** 这一条主线。
    - 推荐顺序：先读《深挖导读》→ 本章（建立时间线）→ 顺读 Part 01 的主线章节 → 再进入 Part 03/04 深挖内部机制与边界。

!!! example "建议先跑的 Lab（把时间线变成证据）"

    - Lab：`SpringCoreBeansContainerLabTest`

## 在 Spring 主线中的位置

- 这是整个 Spring 生态的“发动机”：AOP、事务、WebMVC 等最终都要落在 **Bean 的创建、注入与增强** 上。
- 绝大多数“为什么我的 Bean 行为不对”的问题，本质都能映射到：**定义阶段**或**创建阶段**的某个关键分支。

## 主线时间线（推荐顺读：先把容器跑通）

1. 建立 Bean 的心智模型：容器到底在管理什么
   - 阅读：[深挖导读](00-deep-dive-guide.md)
   - 主线章节：[01. Bean 心智模型与注册入口](../part-01-ioc-container/01-bean-mental-model.md)
2. 把“依赖是怎么被解析与注入的”跑通（按类型/按名称/泛型/候选集）
   - 主线章节：[03. 依赖注入解析](../part-01-ioc-container/03-dependency-injection-resolution.md)
3. 把“作用域与生命周期”接起来（尤其是 prototype 的边界）
   - 主线章节：[04. 作用域与 prototype](../part-01-ioc-container/04-scope-and-prototype.md)
   - 主线章节：[05. 生命周期与回调](../part-01-ioc-container/05-lifecycle-and-callbacks.md)
4. 进入扩展点：Post-Processor 如何改变“定义”与“对象”
   - 主线章节：[06. Post-Processor](../part-01-ioc-container/06-post-processors.md)
   - 主线章节：[07. 配置类增强](../part-01-ioc-container/07-configuration-enhancement.md)
5. 把 Spring Boot 接上来：自动配置如何把条件装配落到容器里
   - 阅读：[10. 自动配置主线](../part-02-boot-autoconfig/10-spring-boot-auto-configuration.md)
   - 调试：[11. 调试与观测](../part-02-boot-autoconfig/11-debugging-and-observability.md)

## 深挖路线（按需）

- 想理解容器内部“按顺序发生了什么”：从 [12. 容器启动与基础设施处理器](../part-03-container-internals/12-container-bootstrap-and-infrastructure.md) 开始，再顺读 13–17。
- 想系统掌握“边界与坑点”（候选集/别名/覆盖/类型匹配/代理时机）：从 [18. Lazy 语义](../part-04-wiring-and-boundaries/18-lazy-semantics.md) 开始按目录推进。
- 想看 AOT 与真实世界输入形态：从 [40. AOT 与 Native 概览](../part-05-aot-and-real-world/40-aot-and-native-overview.md) 开始按目录推进。

## 排坑与自检

- 常见坑：[90-common-pitfalls.md](../appendix/90-common-pitfalls.md)
- 自检：[99-self-check.md](../appendix/99-self-check.md)
