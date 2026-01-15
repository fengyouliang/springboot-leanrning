# 第 13 章：Profiles 主线

这一章解决的问题是：**为什么同一个应用在 dev/prod 行为不一样、为什么某个 Bean 在某环境“消失了”、为什么条件装配没生效**。

---

## 主线（按时间线顺读）

Profile 影响两条线：

1. **配置文件参与与否**：哪些配置源进入 `Environment`
2. **Bean 注册与否**：哪些配置类/Bean 被注册到容器

因此排障时你要能先分流判断：

- 这是“最终属性值不对”的问题？
- 还是“Bean 根本没注册/注册错了实现”的问题？

---

## 深挖入口（模块 docs）

- 模块目录页：[`spring-core-profiles/docs/README.md`](../spring-core-profiles/docs/README.md)
- 模块主线时间线（含可跑入口）：[`spring-core-profiles/docs/part-00-guide/03-mainline-timeline.md`](../spring-core-profiles/docs/part-00-guide/03-mainline-timeline.md)

---

## 下一章怎么接

配置与 Bean 都到位后，下一类“必须把分支讲清楚”的机制是校验：Validation 的错误是怎么产生、怎么回传、为什么依赖代理。

- 下一章：[第 14 章：Validation 主线](14-validation-mainline.md)

