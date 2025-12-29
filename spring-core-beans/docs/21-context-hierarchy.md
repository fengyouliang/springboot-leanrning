# 21. 父子 ApplicationContext：可见性与覆盖边界

当你进入真实工程或复杂测试环境，很容易遇到“多个 ApplicationContext”。

这一章用一个最小实验展示：

- parent/child context 的可见性规则
- child 的“覆盖”只发生在 child 内部

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansContextHierarchyLabTest.java`

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

## 4. 一句话自检

- 你能解释清楚：为什么 child 可以拿到 parent 的 bean，但 parent 拿不到 child 的 bean 吗？
