# 28. 自定义 Scope + scoped proxy：thread scope 的真实语义

Spring 的 scope 机制是可扩展的：你可以注册自定义 scope。

本章用 `SimpleThreadScope`（Spring 提供但默认不注册）演示：

- 自定义 scope 如何注册
- scope 的“每次从容器获取”语义
- 为什么把短生命周期 scope 注入到 singleton 里需要 `ObjectProvider` 或 scoped proxy

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansCustomScopeLabTest.java`

## 1. 注册自定义 scope（thread）

`SimpleThreadScope` 的关键点：

- 同一个 thread 内：同名 bean 返回同一个实例
- 不同 thread 之间：同名 bean 返回不同实例

对应测试：

- `SpringCoreBeansCustomScopeLabTest.threadScope_createsOneInstancePerThread_whenAccessedDirectly()`

## 2. 关键陷阱：把 scoped bean 直接注入 singleton，会被冻结在“注入那一刻”

对应测试：

- `SpringCoreBeansCustomScopeLabTest.injectingThreadScopedBeanIntoSingleton_withoutProxy_freezesTheTargetAtInjectionTime()`

原因与你在 prototype 注入 singleton 看到的现象一致：

- singleton 创建时解析依赖
- 只向容器要一次 scoped bean
- 之后一直用这个引用

## 3. 解法 1：ObjectProvider（推荐，机制最直观）

对应测试：

- `SpringCoreBeansCustomScopeLabTest.objectProvider_honorsThreadScope_whenUsedInsideSingleton()`

你注入的是 provider（容器句柄），每次调用时再去容器按当前 thread 解析目标对象。

## 4. 解法 2：scoped proxy（更“无感”，但引入代理语义）

对应测试：

- `SpringCoreBeansCustomScopeLabTest.scopedProxy_honorsThreadScope_whenInjectedIntoSingleton()`

本质：

- singleton 注入到的是一个 proxy
- proxy 在每次方法调用时从当前 scope 找到真实目标再转发

## 5. 常见坑

- **坑 1：以为 scope 会自动传播到注入点**
  - scope 的语义是“容器如何管理对象”；注入点如果不做延迟解析，仍然只取一次。

- **坑 2：scoped proxy 的调试成本**
  - 你看到的对象类型是 proxy，不是目标类；需要学会区分。

## 源码锚点（建议从这里下断点）

- `AbstractBeanFactory#registerScope`：注册自定义 scope 的入口（没有注册就不会走 scope 分发）
- `AbstractBeanFactory#doGetBean`：按 scope 分发的主入口（singleton/prototype/custom scope 都会在这里分流）
- `SimpleThreadScope#get`：thread scope 的核心（同线程缓存、跨线程隔离）
- `ObjectProvider#getObject`：provider 的延迟解析入口（每次调用都回到容器重新解析目标）
- `ScopedProxyFactoryBean#getObject`：scoped proxy 的生成入口（注入的是 proxy，调用时再定位目标）

## 断点闭环（用本仓库 Lab/Test 跑一遍）

入口：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansCustomScopeLabTest.java`
  - `threadScope_createsOneInstancePerThread_whenAccessedDirectly()`
  - `injectingThreadScopedBeanIntoSingleton_withoutProxy_freezesTheTargetAtInjectionTime()`
  - `objectProvider_honorsThreadScope_whenUsedInsideSingleton()`
  - `scopedProxy_honorsThreadScope_whenInjectedIntoSingleton()`

建议断点：

1) `AbstractBeanFactory#registerScope`：确认 thread scope 的注册发生在 refresh 之前
2) `SimpleThreadScope#get`：在同线程/不同线程获取时观察缓存命中与新建
3) direct injection 的 consumer 构造器/字段赋值点：观察“只取一次”导致冻结
4) `ObjectProvider#getObject`：观察 provider 每次调用都会触发一次新的解析（回到 `doGetBean`）
5) `ScopedProxyFactoryBean#getObject`（可选）：观察 proxy 生成与调用时的目标定位

## 排障分流：这是定义层问题还是实例层问题？

- “thread scope 没起作用/所有线程都拿到同一个实例” → **优先定义层（scope 注册）**：是否真的 `registerScope("thread", ...)`？（看 `registerScope`）
- “把 scoped bean 注入 singleton 后总是同一个实例” → **实例层（注入时机）**：这是 direct injection 的冻结效应；用 provider 或 scoped proxy（本章第 2/3/4 节）
- “调试时看到的类型是 proxy，不是目标类” → **实例层（代理语义）**：这是 scoped proxy 的预期形态（对照 [31](31-proxying-phase-bpp-wraps-bean.md)）
- “想当然认为 scope 会自动传播到注入点” → **概念澄清**：scope 管的是“容器如何取对象”，不自动改变注入点的解析次数（本章第 5 节）

## 6. 一句话自检

- 你能解释清楚：为什么 direct injection 会让 thread scope 失效？
- 你能解释清楚：ObjectProvider 与 scoped proxy 的差别吗？
