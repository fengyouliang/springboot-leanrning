# 21. 父子 ApplicationContext：可见性与覆盖边界

## 0. 复现入口（可运行）

- 入口测试（推荐先跑通再下断点）：
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansContextHierarchyLabTest.java`
- 推荐运行命令：
  - `mvn -pl spring-core-beans -Dtest=SpringCoreBeansContextHierarchyLabTest test`

当你进入真实工程或复杂测试环境，很容易遇到“多个 ApplicationContext”。

这一章用一个最小实验展示：

- parent/child context 的可见性规则
- child 的“覆盖”只发生在 child 内部

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansContextHierarchyLabTest.java`

## 1. 现象：child 能看到 parent，parent 看不到 child

对应测试：

- `SpringCoreBeansContextHierarchyLabTest.childContext_canSeeParentBeans_butParentCannotSeeChildBeans()`

你应该观察到：

- child 可以 `getBean(ParentOnlyBean.class)`（它其实来自 parent）
- parent 无法 `getBean(ChildOnlyBean.class)`

## 2. 覆盖（override）是“按名字”的，并且只在 child 生效

同一个 beanName（例如 `shared`）：

- parent 有一个 `shared`
- child 也注册一个 `shared`

结果是：

- `child.getBean("shared")` 返回 child 的 bean
- `parent.getBean("shared")` 仍然是 parent 的 bean

学习重点：

- 覆盖发生在查找链路上：child 先查自己，再查 parent
- 覆盖不等于“删除 parent 的 bean”

## 3. 常见坑

- **坑 1：按类型注入时可能出现歧义**
  - 如果 parent 与 child 都有同类型的 bean，按类型注入/查找可能变成多候选。

- **坑 2：以为 child 覆盖会影响 parent**
  - 不会。parent 完全不知道 child 的存在。

## 源码锚点（建议从这里下断点）

- `AbstractApplicationContext#setParent`：建立 parent/child 关系（没有 parent 就没有“向上可见”）
- `AbstractBeanFactory#doGetBean`：查找链路的关键（child 找不到会委托 parent beanFactory）
- `AbstractBeanFactory#containsLocalBean`：判断“本地是否存在某个名字”的入口（解释 override 是 name-based 且只在 child 生效）
- `DefaultListableBeanFactory#containsBeanDefinition`：本地定义层查找（“我到底注册没注册”）
- `BeanFactoryUtils#beanOfTypeIncludingAncestors`：按类型跨层查找的常见工具（也容易引发“多候选”）

## 断点闭环（用本仓库 Lab/Test 跑一遍）

入口：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansContextHierarchyLabTest.java`
  - `childContext_canSeeParentBeans_butParentCannotSeeChildBeans()`

建议断点：

1) 测试里 `child.getBean(...)` 与 `parent.getBean(...)` 的调用行：对照“谁能看到谁”
2) `AbstractBeanFactory#doGetBean`：观察 child 查找失败后如何沿 parent 链路继续找
3) `AbstractBeanFactory#containsLocalBean`：观察同名 beanName 时，child 是如何优先命中自己的

## 排障分流：这是定义层问题还是实例层问题？

- “child 拿不到 parent 的 bean” → **优先定义层/上下文关系问题**：child 是否真的设置了 parent？parent 是否 refresh 并注册了该定义？
- “我在 child 里覆盖了 bean，但 parent 的行为没变” → **这是预期（name-based、只在 child 生效）**：override 发生在查找链路上，不会反向影响 parent（本章第 2 节）
- “按类型注入出现歧义（parent/child 都有同类型）” → **实例层（候选解析）**：需要 `@Qualifier/@Primary` 等规则收敛（见 [03](../part-01-ioc-container/03-dependency-injection-resolution.md)/[33](33-autowire-candidate-selection-primary-priority-order.md)）
- “以为这是 Boot 专属现象” → **容器机制**：parent/child 是 `ApplicationContext` 层面的通用能力（本章 Lab 用小容器也能复现）

## 4. 一句话自检

- 你能解释清楚：为什么 child 可以拿到 parent 的 bean，但 parent 拿不到 child 的 bean 吗？
对应 Lab/Test：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansContextHierarchyLabTest.java`
推荐断点：`BeanFactoryUtils#beanNamesForTypeIncludingAncestors`、`AbstractBeanFactory#doGetBean`、`AbstractApplicationContext#setParent`

上一章：[20. registerResolvableDependency：能注入，但它不是 Bean](20-resolvable-dependency.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[22. Bean 名称与 alias：同一个实例，多一个名字](22-bean-names-and-aliases.md)