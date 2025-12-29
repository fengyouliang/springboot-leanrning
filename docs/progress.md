# 学习进度（Checklist）

> 这份清单用于“打卡式学习”：把学习从“看懂了”变成“能复现 + 能断言 + 能解释”。
>
> 建议每个模块都按同一套退出条件走：
> - **能解释**：用自己的话讲清 “机制 + 典型坑 + 为什么这样设计”
> - **能改写**：完成一个 Labs/Exercise 的改造题，并保持模块测试全绿
> - **能调试**：遇到红测/异常，能用断点/日志/断言定位根因并验证修复

## 0. 通用起步

- [ ] 环境就绪：`java -version` 为 17（或更高）
- [ ] 环境就绪：`mvn -v` 为 3.8+（建议）
- [ ] 全仓库默认全绿：`mvn -q test`

## 1. 主线（先跑通业务闭环）

- [ ] `springboot-basics`：配置绑定 + Profile（能解释配置优先级）
- [ ] `springboot-web-mvc`：Controller/校验/错误处理（能定位 400 的字段错误）
- [ ] `springboot-testing`：slice vs full context（能解释为什么 `@WebMvcTest` 更快）
- [ ] `springboot-data-jpa`：persistence context/flush/脏检查（能解释“一级缓存假象”）
- [ ] `springboot-actuator`：端点暴露 + 自定义 health（能解释 exposure 与安全边界）
- [ ] `springboot-business-case`：串联 MVC/JPA/Tx/AOP/Events（能定位代理/事务边界问题）

## 2. 机制线（把底层原理补齐）

- [ ] `spring-core-beans`：Bean 注册/注入/生命周期/扩展点（能解释 BFPP vs BPP）
- [ ] `spring-core-profiles`：`@Profile`/`@ConditionalOnProperty`（能定位条件为何不生效）
- [ ] `spring-core-validation`：校验集成 + method validation（能解释“为何依赖代理”）
- [ ] `spring-core-aop`：代理/切点/自调用陷阱（能判断 JDK vs CGLIB）
- [ ] `spring-core-tx`：事务边界/回滚/传播（能解释 checked exception 回滚规则）
- [ ] `spring-core-events`：同步/异步/after-commit（能稳定断言异步）
- [ ] `spring-core-resources`：Resource 抽象/pattern/jar 差异（能定位 classpath 路径问题）

## 3. 扩展模块（更贴近真实工程）

> 这些模块更偏“工程高频主题”，建议在完成主线后开始。

- [ ] `springboot-security`：认证/授权/CSRF/method security/JWT（能解释 401 vs 403，能复现 FilterChain 行为）
- [ ] `springboot-web-client`：RestClient vs WebClient（能写可测的错误处理/超时/重试）
- [ ] `springboot-async-scheduling`：`@Async` + `@Scheduled`（能解释代理与线程池，能写稳定测试）
- [ ] `springboot-cache`：Spring Cache + Caffeine（能解释 key/evict/sync/过期语义）

## 4. 每个模块的“最小打卡动作”（建议）

- [ ] 跑模块 tests：`mvn -q -pl <module> test`
- [ ] 完成至少 1 个 Exercise：移除 `@Disabled` → 根据提示实现 → 让测试变绿
- [ ] 给自己写一段总结（3–10 行）：这个模块最关键的“机制结论”是什么？最容易踩的坑是什么？

