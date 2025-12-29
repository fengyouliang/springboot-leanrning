# 22. Bean 名称与 alias：同一个实例，多一个名字

很多人第一次见 alias 都会把它当成“复制一个 bean”。

这一章用一个最小实验固定一个结论：

- alias 只是名字映射，不会创建第二个实例

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansBeanNameAliasLabTest.java`

## 1. 现象：两个名字拿到的是同一个对象

对应测试：

- `SpringCoreBeansBeanNameAliasLabTest.aliasResolvesToSameSingletonInstanceAsCanonicalName()`

实验里我们：

1) 注册 `primaryName`
2) `registerAlias("primaryName", "aliasName")`

结果：

- `getBean("primaryName")` 与 `getBean("aliasName")` 拿到的是同一个实例（same reference）

## 2. alias 在容器里的定位

你可以把 alias 理解为：

- 从 `aliasName` 映射到 `primaryName`
- 最终仍然是“同一个 beanDefinition/同一个 singleton instance”

## 3. 常见坑

- **坑 1：alias 冲突**
  - alias 不能随意复用，否则会导致覆盖/异常（取决于容器设置）。

- **坑 2：alias 不会改变类型**
  - alias 只是名字；它不改变注入规则、不改变 `@Primary`/`@Qualifier` 的语义。

## 4. 一句话自检

- 你能解释清楚：alias 解决的是什么问题？（更灵活的名称入口，而不是复制对象）
