# 97. Explore/Debug 用例（可选启用，不影响默认回归）

## 0. 你为什么需要它？

`spring-core-beans` 的 Labs 有两类：

1. **Core Labs（默认参与回归）**：用于保证“主线机制可复现/可断言”，CI 默认会跑。  
2. **Explore/Debug 用例（可选启用）**：用于“更深一层的断点观察/内部状态验证”，默认不影响 CI 稳定性与耗时。

这一章只做一件事：把 Explore 用例的**开启方式**与**观察点**写成显式规则。

---

## 1. 运行方式（显式开关）

Explore 用例默认不运行。你需要显式打开系统属性：

- 开启 Explore：`-Dspringcorebeans.explore=true`

示例：只跑 Explore 用例里的某个测试类：

```bash
mvn -pl spring-core-beans -Dspringcorebeans.explore=true -Dtest=SpringCoreBeansSingletonCacheExploreTest test
```

如果你想“在不改任何代码的前提下”跑一轮完整深挖（会包含核心回归测试）：

```bash
mvn -pl spring-core-beans -Dspringcorebeans.explore=true test
```

---

## 2. Explore 用例清单（入口与观察点）

### 2.1 单例缓存：`DefaultSingletonBeanRegistry` 的核心缓存表

- 入口测试：
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/appendix/SpringCoreBeansSingletonCacheExploreTest.java`
- 你要观察的点：
  - singleton 与 prototype 在缓存层面的差异（prototype 不会进 `singletonObjects`）
- 断点建议：
  - `DefaultSingletonBeanRegistry#getSingleton`
  - `DefaultSingletonBeanRegistry#addSingleton`

### 2.2 JavaBeans 内省缓存：`CachedIntrospectionResults` 的缓存行为

- 入口测试：
  - `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/appendix/SpringCoreBeansCachedIntrospectionExploreTest.java`
- 你要观察的点：
  - 为什么 BeanWrapper/属性注入不会每次都重新 `Introspector.getBeanInfo`
  - 缓存如何与 ClassLoader 绑定（`acceptClassLoader` / `clearClassLoader`）
- 断点建议：
  - `CachedIntrospectionResults`（查看缓存命中）
  - `BeanWrapperImpl` / `AbstractNestablePropertyAccessor`（调用链入口）

---

上一章：[96. spring-beans Public API Gap 清单（按包/机制域分批深化）](96-spring-beans-public-api-gap.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[99. 自测题（Self Check）](99-self-check.md)

