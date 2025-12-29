## 0. Workspace Wiring
- [ ] 0.1 将新模块加入根 `pom.xml`（按学习顺序排列）
- [ ] 0.2 更新根 `README.md` Catalog：新增 4 个模块条目，并标注 Web/端口或 test-driven

## 1. Module: `springboot-security`（优先）
- [ ] 1.1 新增模块骨架（pom/main/resources/test/README/docs）
- [ ] 1.2 增加 Deep Dive Track：至少 20 个实验（≥12 Labs + ≥8 Exercises）
- [ ] 1.3 覆盖主题：认证/授权、CSRF、method security、FilterChain、异常处理、JWT/Stateless
- [ ] 1.4 README（中文）完成索引：运行/测试、Labs/Exercises、Debug 路径
- [ ] 1.5 docs（中文）章节化：每章链接到对应实验测试

## 2. Module: `springboot-web-client`
- [ ] 2.1 新增模块骨架（pom/main/resources/test/README/docs）
- [ ] 2.2 增加 Deep Dive Track：至少 20 个实验（≥12 Labs + ≥8 Exercises）
- [ ] 2.3 覆盖主题：RestClient vs WebClient、错误处理、超时、重试、拦截/Filter、测试策略
- [ ] 2.4 README（中文）完成索引
- [ ] 2.5 docs（中文）章节化：每章链接到对应实验测试

## 3. Module: `springboot-async-scheduling`
- [ ] 3.1 新增模块骨架（pom/main/resources/test/README/docs）
- [ ] 3.2 增加 Deep Dive Track：至少 18 个实验（≥10 Labs + ≥8 Exercises）
- [ ] 3.3 覆盖主题：`@Async` 代理、executor、异常处理、自调用陷阱、`@Scheduled` 语义与测试
- [ ] 3.4 README（中文）完成索引
- [ ] 3.5 docs（中文）章节化：每章链接到对应实验测试

## 4. Module: `springboot-cache`
- [ ] 4.1 新增模块骨架（pom/main/resources/test/README/docs）
- [ ] 4.2 增加 Deep Dive Track：至少 18 个实验（≥10 Labs + ≥8 Exercises）
- [ ] 4.3 覆盖主题：`@Cacheable/@CachePut/@CacheEvict`、key/condition/unless、sync、过期（Caffeine 可控）
- [ ] 4.4 README（中文）完成索引
- [ ] 4.5 docs（中文）章节化：每章链接到对应实验测试

## 5. Validation
- [ ] 5.1 模块级：`mvn -q -pl springboot-security test`
- [ ] 5.2 模块级：`mvn -q -pl springboot-web-client test`
- [ ] 5.3 模块级：`mvn -q -pl springboot-async-scheduling test`
- [ ] 5.4 模块级：`mvn -q -pl springboot-cache test`
- [ ] 5.5 全仓库：`mvn -q test`

