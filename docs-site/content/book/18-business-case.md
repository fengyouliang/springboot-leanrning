# 第 18 章：Business Case 收束

如果前面的章节让你“分别理解了机制”，这一章要解决的是：**把机制组合起来，形成一个真实的业务闭环，并且你能在红测/异常出现时定位到是哪一层机制出了问题**。

---

## 主线（按时间线顺读）

你可以把 business case 看成“从入口一路走到数据层再回来”的压测场景：

1. Web 入口（Controller/绑定/校验/错误处理）
2. Security（认证/授权/CSRF 等边界）
3. Service 层的 AOP/事务（边界与传播）
4. Data JPA（持久化上下文/flush/懒加载）
5. Events（事务后事件/异步）
6. Observability（日志/指标/health/trace 的可观测信号）

---

## 深挖入口（模块 docs）

- 模块目录页：[`springboot-business-case/docs/README.md`](../springboot-business-case/docs/README.md)
- 模块主线时间线（含可跑入口）：[`springboot-business-case/docs/part-00-guide/03-mainline-timeline.md`](../springboot-business-case/docs/part-00-guide/03-mainline-timeline.md)

推荐先跑的最小闭环：

- `BootBusinessCaseLabTest`

---

## 回到书的“工具页”

- 想快速找可跑入口：[Labs 索引](labs-index.md)
- 想先把断点装好：[Debugger Pack](debugger-pack.md)
- 想开始动手练习：[Exercises & Solutions](exercises-and-solutions.md)

