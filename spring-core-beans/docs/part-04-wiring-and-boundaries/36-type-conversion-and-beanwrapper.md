# 36. 类型转换：BeanWrapper / ConversionService / PropertyEditor 的边界

这一章解决一个非常常见、但经常被“误归因”的问题：

> 我明明在配置里写的是字符串（例如 `"8080"`、`"PT30S"`、`"42"`），  
> 为什么注入到 Bean 的属性里时，类型能变成 `int` / `Duration` / 自定义值对象？

结论先行：

- Spring 在 bean 创建过程中会做**两类“字符串 → 目标类型”的转换**
  - **属性填充（populateBean）**：`BeanDefinition` 的 property value（常见是字符串）写入 Java 属性时的类型转换
  - **`@Value` 注入**：先做占位符解析（`${...}`/SpEL），再把结果转换为注入点类型
- 真正做“写入属性 + 类型转换”的核心组件通常是：`BeanWrapper`（实现类 `BeanWrapperImpl`）
- “转换规则从哪里来”主要取决于：
  - BeanFactory 是否安装了 `ConversionService`
  - 是否存在 legacy 的 `PropertyEditor`（历史兼容）

---

## 1. 两条你必须区分的链路：propertyValues vs `@Value`

### 1.1 propertyValues（定义层的值）如何变成实例属性

典型场景：

- 你在 BFPP/BDRPP 里修改了 `BeanDefinition#getPropertyValues()`，把 `port` 设成 `"8080"`
- 或者 XML / 其他配置源把属性值以字符串形式写入 definition

这些值在实例创建阶段会进入：

- `AbstractAutowireCapableBeanFactory#populateBean`
  - `BeanWrapper` 写入属性
  - `TypeConverter` / `ConversionService` 参与 `convertIfNecessary`

### 1.2 `@Value` 的链路：先解析字符串，再转换

典型场景：

- `@Value("${server.port}") int port`
- `@Value("${demo.id}") UserId userId`

这条链路通常是：

1) `AutowiredAnnotationBeanPostProcessor`（基础设施处理器）识别 `@Value`
2) `BeanFactory#resolveEmbeddedValue` 做 `${...}` / SpEL 的字符串解析
3) 将解析结果交给类型转换器，转换为注入点类型

对照阅读：

- 机制总览：[34. `@Value("${...}")` 占位符解析](34-value-placeholder-resolution-strict-vs-non-strict.md)
- 注入发生阶段：[30. 注入发生在什么时候：field vs constructor](30-injection-phase-field-vs-constructor.md)

---

## 2. 转换体系三件套：BeanWrapper / ConversionService / PropertyEditor

### 2.1 BeanWrapper：负责“把值写进对象属性”

你可以把 `BeanWrapper` 理解为：

- 对 JavaBean 属性的统一访问层（读/写）
- 写入属性时，它会按属性的目标类型触发类型转换

因此当你想“看见类型转换发生在哪一步”，最稳定的断点入口往往不是 `@Value` 或 `@Autowired`，而是：

- `BeanWrapperImpl#setPropertyValue`

### 2.2 ConversionService：现代转换体系（推荐理解）

如果 BeanFactory 安装了 `ConversionService`（常见是 `DefaultConversionService` 及其增强），Spring 会优先使用它完成：

- 字符串到数字/枚举/时间等常见类型
- 你注册的自定义 `Converter`

你在工程中“最可控”的方式，是提供名为 `conversionService` 的 bean，让 `ApplicationContext` 在 refresh 中把它安装到 `BeanFactory`。

### 2.3 PropertyEditor：历史兼容（建议知道存在即可）

在较早的 Spring 时代，类型转换主要靠 `PropertyEditor`。现代项目通常以 `ConversionService` 为主，但你在调试栈里仍可能看到它的影子（尤其是某些内置 editor）。

---

## 3. 最小实验：让“类型转换”可断言、可断点

### 3.1 复现入口（可运行）

- 入口测试（推荐先跑通再下断点）：
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansTypeConversionLabTest.java`
- 推荐运行命令：
  - 类级：`mvn -pl spring-core-beans -Dtest=SpringCoreBeansTypeConversionLabTest test`
  - 方法级（更快）：`mvn -pl spring-core-beans -Dtest=SpringCoreBeansTypeConversionLabTest#stringPropertyValue_canBeConvertedToIntDuringPopulateBean test`
- 你将断言/观察到：
  - **populateBean 阶段**会把定义层的字符串属性值（`"8080"`）转换成目标属性类型（`int`）
  - 自定义 `ConversionService` 能让“字符串 → 领域值对象”的转换在注入阶段发生（而不是你手写解析代码）

对应实验（可运行 + 可断言）：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part04_wiring_and_boundaries/SpringCoreBeansTypeConversionLabTest.java`

建议直接跑：

```bash
mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansTypeConversionLabTest test
```

你会看到两个核心现象：

1) `String → int` 的转换发生在属性填充阶段（populateBean），而不是在你定义 bean 的那一刻
2) 安装自定义 `ConversionService` 后，可以把字符串转换为你自己的值对象（例如 `UserId`）

---

## 4. Debug / 断点建议（把“转换”从黑盒变成白盒）

### 4.1 推荐断点（关键调用点）

> 目标：把“类型转换到底发生在哪里”定位到 1–2 个关键栈帧，而不是在巨大的创建流程里迷路。

- Bean 创建主线（你需要知道转换发生在什么时候）：
  - `AbstractAutowireCapableBeanFactory#populateBean`
  - `AbstractAutowireCapableBeanFactory#applyPropertyValues`
- BeanWrapper / TypeConverter（你需要知道谁在做 convert）：
  - `BeanWrapperImpl#setPropertyValue`
  - `AbstractNestablePropertyAccessor#processLocalProperty`
  - `TypeConverterDelegate#convertIfNecessary`

### 4.2 条件断点模板（降低噪声）

在 `AbstractAutowireCapableBeanFactory#applyPropertyValues` 上建议使用条件断点：

- 按 beanName 精确过滤：
  - `"serverPortHolder".equals(beanName)`
  - `"userIdConsumer".equals(beanName)`
- 按正在写入的属性名过滤（进入 BeanWrapper 后）：
  - `"port".equals(propertyName)`
  - `"userId".equals(propertyName)`

### 4.3 推荐观察点（watch list）

- `beanName`：当前正在装配的 bean
- `pvs` / `pvs.propertyValueList`：定义层写入的属性值（此时往往还是 String）
- `bw` / `bw.wrappedInstance`：正在被写入属性的真实实例
- `conversionService`：是否存在自定义转换体系（DefaultConversionService / 你的自定义实现）
- `propertyValue.value`：写入前的原始值（常见是 String）

如果你只想看清“发生了类型转换”这一件事，建议在这些点下断点：

1) `AbstractAutowireCapableBeanFactory#populateBean`
2) `BeanWrapperImpl#setPropertyValue`
3) `TypeConverterDelegate#convertIfNecessary`（或同名方法）
4) `GenericConversionService#convert`（观察是否走 ConversionService）

如果你看的场景是 `@Value`：

5) `AbstractBeanFactory#resolveEmbeddedValue`（先看解析出来的字符串是什么）
6) 再回到 `convertIfNecessary` 看字符串如何变成目标类型

推荐观察点（watch list）：

- 目标属性类型/注入点类型（`TypeDescriptor`/`requiredType`）
- 原始值（通常是 `String`）
- 当前 BeanFactory 的 `conversionService` 是否存在

---

## 5. 常见坑与边界

1) “我写了自定义 Converter，但就是不生效”
   - 优先排查：你的 `ConversionService` 是否真的被安装到 BeanFactory（命名是否为 `conversionService`；是否在 refresh 早期可用）
2) “`@ConfigurationProperties` 能转，`@Value` 转不了”
   - 这通常不是 Spring “不一致”，而是你把 **Binder（属性绑定）** 与 **Bean 注入/属性填充** 混为一谈：它们的转换链路与失败表现不同
3) “转换失败报错很难读”
   - 建议先把场景缩小到本模块这种 JUnit 最小容器，把异常栈压缩到 `populateBean/convertIfNecessary` 附近再分析

---

## 源码锚点（建议从这里下断点）

- `AbstractAutowireCapableBeanFactory#populateBean`：属性填充总入口
- `BeanWrapperImpl#setPropertyValue`：写入属性并触发转换
- `TypeConverterDelegate#convertIfNecessary`：转换决策点（是否能转、用什么转）
- `GenericConversionService#convert`：ConversionService 的实际转换入口
- `AbstractBeanFactory#resolveEmbeddedValue`：`@Value` 的字符串解析入口

---

上一章：[35. BeanDefinition 的合并（MergedBeanDefinition）：RootBeanDefinition 从哪里来？](35-merged-bean-definition.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[37. 泛型匹配与注入坑：ResolvableType 与代理导致的类型信息丢失](37-generic-type-matching-pitfalls.md)
