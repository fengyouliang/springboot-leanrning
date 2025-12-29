# 02. JDK vs CGLIB：代理类型与“可注入类型”差异

Spring AOP 最容易让人困惑的一点是：**代理类型不同，会直接改变“你能不能按某个类型拿到 bean”**。

## 两种代理的核心差异

### 1) JDK 动态代理（interface-based）

- 代理对象 **实现接口**，但不会继承你的实现类
- 优点：不需要 CGLIB；对 final 限制更少（因为不靠继承）
- 典型现象：你能按接口类型注入/获取，但 **按实现类类型可能拿不到**

### 2) CGLIB 代理（class-based）

- 代理对象是你的类的 **子类**（通过继承生成）
- 优点：即使没有接口也能代理
- 代价：受到继承规则限制（`final` 类/方法相关，见 [docs/04](04-final-and-proxy-limits.md)）

## 在本模块如何验证

重点看 `SpringCoreAopProxyMechanicsLabTest` 里的两段配置：

- `@EnableAspectJAutoProxy(proxyTargetClass = false)`：倾向使用 JDK 代理
- `@EnableAspectJAutoProxy(proxyTargetClass = true)`：强制使用 CGLIB 代理

对应断言（强烈建议逐个断点跟进）：

- `jdkDynamicProxyIsUsedForInterfaceBasedBeans_whenProxyTargetClassIsFalse`
  - `AopUtils.isJdkDynamicProxy(greeter)` 为 true
  - `context.getBean(PlainGreeter.class)` 会失败（按实现类拿不到）
- `cglibProxyIsUsedForClassBasedBeans_whenProxyTargetClassIsTrue`
  - `AopUtils.isCglibProxy(greeter)` 为 true

## 为什么“按实现类拿不到”？

当 Spring 使用 JDK 代理时，最终注册到容器里的对象类型是一个 `com.sun.proxy.$ProxyXX`。
它只“长得像”接口，不是你的实现类子类，因此按实现类类型查找会找不到。

## 实战建议（学习仓库里也适用）

- **想要最稳定的注入方式**：定义接口，用接口注入（能直观看到“JDK 代理”的语义）
- **想要最少样板代码**：没有接口也可以，但要理解你更可能得到 CGLIB 代理（以及它的限制）

