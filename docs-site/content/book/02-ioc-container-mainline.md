# 第 2 章：IoC 容器主线（Beans）

如果你把 Spring Boot 当成“启动一个应用”，那 **IoC 容器**就是“把应用装配成一个可运行系统”的核心：它决定了 Bean 从哪里来、什么时候创建、怎么注入、有哪些扩展点、为什么会出现各种“看起来很诡异”的边界行为。

---

## 主线（按时间线顺读）

你可以把容器的主线拆成两个层次：**定义层**与**实例层**。

1. 定义进入容器：扫描/注册/导入，把 `BeanDefinition` 收集起来
2. 定义被“加工”：`BeanFactoryPostProcessor`（BFPP）阶段改定义/改注册表
3. 实例被创建：实例化 → 填充属性（依赖注入）→ 初始化回调
4. 实例被“增强”：`BeanPostProcessor`（BPP）阶段包一层代理/注入额外能力
5. 生命周期与销毁：singleton/prototype 差异、destroy 语义、循环依赖与 early reference

---

## 深挖入口（模块 docs）

- 模块目录页（超大模块，建议按入口顺读）：[`spring-core-beans/docs/README.md`](../spring-core-beans/docs/README.md)
- 模块主线时间线（含可跑入口）：[`spring-core-beans/docs/part-00-guide/03-mainline-timeline.md`](../spring-core-beans/docs/part-00-guide/03-mainline-timeline.md)

建议先跑的最小闭环（从“看见容器”开始）：

- `SpringCoreBeansLabTest` / `SpringCoreBeansContainerLabTest`

---

## 下一章怎么接

容器能把对象装配起来，但很多“横切能力”（事务/缓存/安全/日志）需要在方法调用边界做增强：这就是 AOP/代理登场的地方。

- 下一章：[第 3 章：AOP/代理主线](03-aop-proxy-mainline.md)

