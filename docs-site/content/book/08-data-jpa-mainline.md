# 第 8 章：Data JPA 主线

这一章解决的问题是：**为什么你只写了 Repository 接口就能 CRUD、为什么同一个实体查两次不一定打两次 SQL、为什么 N+1 会悄悄出现**。

---

## 主线（按时间线顺读）

1. Repository 代理生成：接口变成可运行对象（代理 + 实现）
2. EntityManager 与持久化上下文：一级缓存、脏检查、flush 时机
3. 事务边界与写入语义：什么时候提交、什么时候回滚
4. 懒加载与代理：`getReferenceById`/lazy association 的行为边界
5. 常见坑：N+1、fetch join/EntityGraph、事务外访问懒加载、测试中看见“假象”

---

## 深挖入口（模块 docs）

- 模块目录页：[`springboot-data-jpa/docs/README.md`](../springboot-data-jpa/docs/README.md)
- 模块主线时间线（含可跑入口）：[`springboot-data-jpa/docs/part-00-guide/03-mainline-timeline.md`](../springboot-data-jpa/docs/part-00-guide/03-mainline-timeline.md)

建议先跑的最小闭环：

- `BootDataJpaLabTest`

---

## 下一章怎么接

当你把数据访问跑通后，下一层经常要考虑性能与降本：缓存是最常见的横切能力之一。

- 下一章：[第 9 章：Cache 主线](09-cache-mainline.md)

