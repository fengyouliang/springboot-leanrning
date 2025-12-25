# boot-business-case（Capstone 综合案例）

这是一个“综合/真实”一点的练习模块，用来把常见的 Spring Boot 能力串起来，并刻意暴露一些**机制层面的关键点**：

- Web MVC：Controller + 请求绑定 + JSON
- Validation：`@Valid` 边界校验 + 错误响应
- JPA：Entity/Repository + H2（内存库）
- Tx：`@Transactional` 提交/回滚、事务边界
- Events：同步事件 vs `@TransactionalEventListener`（after-commit）
- AOP：代理生效、Advice 记录调用

本模块默认启动一个 HTTP API（端口 `8084`），更贴近真实业务的“入口/边界”学习方式。

## 运行

```bash
mvn -pl boot-business-case spring-boot:run
```

示例请求（创建订单）：

```bash
curl -s -X POST 'http://localhost:8084/api/orders' \
  -H 'Content-Type: application/json' \
  -d '{"customer":"Alice","sku":"SKU-1","quantity":2}'
```

## 测试

```bash
mvn -pl boot-business-case test
```

## Labs（已启用，默认全绿）

> 入口：`src/test/java/.../*LabTest.java`

- 创建订单：校验通过 → 事务提交 → 数据落库
- 参数不合法：返回 `400` + 字段错误
- AOP 代理生效：Service 方法被 Advice 记录
- 事务回滚：抛异常后数据不落库
- 事件机制对比：同步监听器在回滚场景仍会执行；after-commit 监听器只会在提交后执行

## Exercises（`@Disabled`，学习者手动开启）

> 入口：`src/test/java/.../*ExerciseTest.java`

- 新增一个查询接口（例如：按 id 查询订单）并写通过测试
- 增加一个“事务传播/回滚规则”的练习（例如 checked exception 是否回滚）
- 增加一个“自调用不触发代理”的练习（AOP/Tx 常见坑）

## Debug / 观察建议

- 观察 Service Bean 是否为 AOP 代理：`AopUtils.isAopProxy(bean)`
- 对比同步事件与 `@TransactionalEventListener` 的触发时机（commit/rollback）
- 在测试里用断点跟进：Controller → Service → Repository → Listener → Aspect

