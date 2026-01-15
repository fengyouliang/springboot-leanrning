# 第 4 章：织入主线（LTW/CTW）

这一章解决的问题是：**代理做不到的增强怎么办**？当你需要在类加载期/编译期把增强“织进字节码”，AspectJ weaving（LTW/CTW）就会成为另一条主线。

---

## 主线（按时间线顺读）

1. 明确目标：你要拦截的是 `execution` 还是 `call`？constructor/field get/set 还是方法？
2. 选择织入方式：
   - LTW：类加载时织入（类加载器/agent/织入器协作）
   - CTW：编译期织入（构建产物已被织入）
3. 验证织入是否生效：不是“看配置”，而是用可断言证据（测试/断点/可观测输出）
4. 排障主线：classloader、weaver 配置、切点表达式是否匹配、织入时机与目标类是否一致

---

## 深挖入口（模块 docs）

- 模块目录页：[`spring-core-aop-weaving/docs/README.md`](../spring-core-aop-weaving/docs/README.md)
- 模块主线时间线（含可跑入口）：[`spring-core-aop-weaving/docs/part-00-guide/03-mainline-timeline.md`](../spring-core-aop-weaving/docs/part-00-guide/03-mainline-timeline.md)

---

## 下一章怎么接

“方法边界增强”最常见的落点是事务：把业务写在一堆方法里，你需要一个可验证的事务边界。

- 下一章：[第 5 章：事务主线（Tx）](05-tx-mainline.md)

