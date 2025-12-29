# 29. FactoryBean 边界：getObjectType 返回 null 会让“按类型发现”失效

`FactoryBean` 的核心机制你已经在 [23 章](23-factorybean-deep-dive.md) 学过了。

这一章补一个非常实用的边界：

- 如果 `FactoryBean#getObjectType()` 返回 `null`
- 那么在“不允许 eager init”的按类型扫描里，它可能不会被当成候选

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansFactoryBeanEdgeCasesLabTest.java`

## 1. 现象：getBeanNamesForType(..., allowEagerInit=false) 找不到 unknownValue

对应测试：

- `SpringCoreBeansFactoryBeanEdgeCasesLabTest.factoryBeanWithNullObjectType_isNotDiscoverableByTypeWithoutEagerInit_butCanStillBeRetrievedByName()`

实验里我们注册了两个 FactoryBean：

- `knownValue`：`getObjectType()` 返回 `Value.class`
- `unknownValue`：`getObjectType()` 返回 `null`

然后用：

- `getBeanNamesForType(Value.class, includeNonSingletons=true, allowEagerInit=false)`

观察点：

- 结果包含 `knownValue`
- 结果不包含 `unknownValue`

## 2. 但你仍然可以按名字拿到它

同一个测试里也验证了：

- `getBean("unknownValue", Value.class)` 仍然能拿到产品对象

这说明：

- “按类型发现”与“按名字取 bean”是两条不同的路径

## 3. 常见坑

- **坑 1：以为 FactoryBean 一定能被按类型发现**
  - 取决于 `getObjectType()` 是否可靠。

- **坑 2：类型判断导致条件注解误判**
  - Boot 的条件装配经常依赖 type matching；FactoryBean 的 object type 不准会产生非常诡异的条件匹配结果。

## 4. 一句话自检

- 你能解释清楚：为什么 allowEagerInit=false 时容器不能“猜”出 unknownValue 的类型吗？
