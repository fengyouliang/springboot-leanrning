# 29. FactoryBean 边界：getObjectType 返回 null 会让“按类型发现”失效

`FactoryBean` 的核心机制你已经在 [23 章](23-factorybean-deep-dive.md) 学过了。

这一章补一个非常实用的边界：

- 如果 `FactoryBean#getObjectType()` 返回 `null`
- 那么在“不允许 eager init”的按类型扫描里，它可能不会被当成候选

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansFactoryBeanEdgeCasesLabTest.java`

## 1. 现象：getBeanNamesForType(..., allowEagerInit=false) 找不到 unknownValue

这类现象非常“反直觉”，但它背后是一个很合理的设计取舍：

- `allowEagerInit=false` 的含义是：**为了性能与避免副作用，不要为了“类型判断”去创建 bean**。
- 对于 `FactoryBean` 来说，product 的类型往往只能在实例化 factory 后才能确定。
- 如果你的 `FactoryBean#getObjectType()` 又返回 `null`，容器在“不允许提前实例化”的前提下，就没有足够信息来做 type matching。

所以你看到的结果就会是：

- **按类型发现失败**：`getBeanNamesForType(SomeType, ..., allowEagerInit=false)` 找不到
- **按名字仍然可用**：`getBean("unknownValue")` 依然能创建并返回 product

这不是 bug，而是“元数据不足 + 不允许 eager init”共同导致的必然结果。

### 1.1 为什么真实项目里经常遇到？

很多框架/基础设施在启动时会做“按类型扫描”，但又必须避免触发大量 bean 初始化（否则启动时间不可控、还可能触发外部连接）：

- 因此它们经常走 `allowEagerInit=false` 的路径
- 你的 `FactoryBean` 如果不能提供稳定的 `getObjectType()`，就会出现“扫描不到”的情况

### 1.2 解决策略（按推荐优先级）

1. **优先：让 `getObjectType()` 返回稳定、明确的类型**
   - 这是最符合 Spring 预期的做法
2. **次选：减少按类型发现对它的依赖**
   - 能按名字注入/获取的场景，显式按名字处理（但要权衡可维护性）
3. **了解即可：通过更激进的 eager init 策略换取可发现性**
   - 在一些场景可以通过允许提前初始化来推断类型，但要非常谨慎：这会把“类型判断”变成“可能触发实例化”，引入副作用与性能风险

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

## 源码锚点（建议从这里下断点）

- `DefaultListableBeanFactory#getBeanNamesForType`：按类型发现入口（allowEagerInit 会影响 FactoryBean 的处理策略）
- `DefaultListableBeanFactory#doGetBeanNamesForType`：真正遍历候选并判断类型匹配的核心
- `FactoryBeanRegistrySupport#getTypeForFactoryBean`：尝试推断 FactoryBean 的 product type（`getObjectType()` 为 null 时会受限）
- `AbstractBeanFactory#getType`：按 name 获取类型的统一入口（FactoryBean 与普通 bean 都会走这里）
- `FactoryBean#getObjectType`：类型信息的源头（返回 null 会导致“按类型发现”能力退化）

## 断点闭环（用本仓库 Lab/Test 跑一遍）

入口：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansFactoryBeanEdgeCasesLabTest.java`
  - `factoryBeanWithNullObjectType_isNotDiscoverableByTypeWithoutEagerInit_butCanStillBeRetrievedByName()`

建议断点：

1) 测试里 `getBeanNamesForType(..., allowEagerInit=false)` 的调用行：对照返回数组为什么缺少 `unknownValue`
2) `DefaultListableBeanFactory#getBeanNamesForType`：观察 allowEagerInit 参数如何影响后续类型推断策略
3) `FactoryBeanRegistrySupport#getTypeForFactoryBean`：观察 `getObjectType()==null` 时容器为什么不能“猜类型”
4) 对照测试后半段 `getBean("unknownValue", Value.class)`：观察按名字取 bean 走的是另一条链路，仍然能拿到产品

## 排障分流：这是定义层问题还是实例层问题？

- “按类型发现不到某个 FactoryBean 的 product（尤其在 allowEagerInit=false）” → **定义层（类型元数据不足）**：检查 `getObjectType()` 是否返回 null（本章结论）
- “按名字能拿到，但按类型扫描/条件判断不稳定” → **定义层（类型匹配路径）**：type matching 与 name-based retrieval 是两条路径（本章第 2 节）
- “在 Boot 条件装配里出现诡异匹配结果” → **定义层 + 条件机制**：FactoryBean 的类型声明不可靠会影响条件判断，建议优先修正 `getObjectType()`（并回看 [10](10-spring-boot-auto-configuration.md)）
- “把它当成缓存/创建 bug 去排查” → **先确认类型信息**：这类问题往往不是实例缓存，而是类型推断与 allowEagerInit 的限制

## 4. 一句话自检

- 你能解释清楚：为什么 allowEagerInit=false 时容器不能“猜”出 unknownValue 的类型吗？
对应 Lab/Test：`spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansFactoryBeanEdgeCasesLabTest.java`
推荐断点：`AbstractBeanFactory#getType`、`DefaultListableBeanFactory#getBeanNamesForType`、`FactoryBeanRegistrySupport#getTypeForFactoryBean`
