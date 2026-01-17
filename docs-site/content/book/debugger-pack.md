# Debugger Pack（Entrypoints / Watchpoints / Decisive Branch）
<!-- CHAPTER-CARD:START -->
!!! summary "章节学习卡片（五问闭环）"

    - 知识点：Debugger Pack（Entrypoints / Watchpoints / Decisive Branch）
    - 怎么使用：本页为索引/工具页：按页面提示找到入口（章节/Lab/断点地图），再回到主线章节顺读。
    - 原理：本页不讲机制原理，负责把“入口与路径”整理成可检索的导航。
    - 源码入口：N/A（本页为索引/工具页）
    - 推荐 Lab：N/A
<!-- CHAPTER-CARD:END -->


本页目标：让你在读书/跑 Lab 时，能快速把断点装在“最有信息密度”的位置上：入口方法、关键分支、以及能观察到核心数据结构变化的观察点（watchpoints）。

> 说明：不同版本的 Spring/Spring Boot 细节可能不同；当文档与代码冲突时，以代码为准。

---

## 小结与下一章

<!-- BOOKLIKE-V2:SUMMARY:START -->
- 一句话总结：Debugger Pack（Entrypoints / Watchpoints / Decisive Branch） —— 本页为索引/工具页：按页面提示找到入口（章节/Lab/断点地图），再回到主线章节顺读。
- 回到主线：本页不讲机制原理，负责把“入口与路径”整理成可检索的导航。
- 下一章：建议按模块目录/全书目录继续顺读。
<!-- BOOKLIKE-V2:SUMMARY:END -->

## 怎么用这页

<!-- BOOKLIKE-V2:INTRO:START -->
这一章围绕「Debugger Pack（Entrypoints / Watchpoints / Decisive Branch）」展开：先把边界说清楚，再沿主线推进到关键分支，最后用可运行入口把结论验证出来。

阅读建议：
- 先看章首的“章节学习卡片/本章要点”，建立预期；
- 建议先带着问题顺读一遍正文，再按证据链回到源码/断点验证。
<!-- BOOKLIKE-V2:INTRO:END -->

## 1) Boot / Environment（配置与最终值）

Entrypoints：

- `org.springframework.core.env.AbstractEnvironment#getActiveProfiles`
- `org.springframework.core.env.PropertySourcesPropertyResolver#getProperty`
- `org.springframework.boot.context.properties.bind.Binder#bind`（需要深挖绑定时）

---

## 2) IoC Container（定义层 → 实例层）

Entrypoints：

- `org.springframework.context.support.AbstractApplicationContext#refresh`
- `org.springframework.beans.factory.support.DefaultListableBeanFactory#registerBeanDefinition`
- `org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory#createBean`

Watchpoints：

- `DefaultListableBeanFactory#beanDefinitionMap`（定义是否真的注册进来）
- `DefaultSingletonBeanRegistry#singletonObjects`（实例是否真的创建出来）

Decisive Branch（常见分支）：

- 是否走 `BeanFactoryPostProcessor`/`BeanPostProcessor`
- 是否进入 early reference（循环依赖相关）

---

## 3) AOP / Proxy（代理与拦截链）

Entrypoints：

- `org.springframework.aop.framework.ProxyFactory#getProxy`
- `org.springframework.aop.framework.JdkDynamicAopProxy#invoke`
- `org.springframework.aop.framework.CglibAopProxy.DynamicAdvisedInterceptor#intercept`

Watchpoints：

- `org.springframework.aop.framework.AdvisedSupport#advisors`（拦截链到底有哪些）

Decisive Branch：

- JDK vs CGLIB（是否有接口、是否强制 CGLIB、final 限制）
- 自调用是否绕过代理（调用点是否在代理外部）

---

## 4) Tx（事务边界）

Entrypoints：

- `org.springframework.transaction.interceptor.TransactionInterceptor#invoke`
- `org.springframework.transaction.support.AbstractPlatformTransactionManager#getTransaction`

Decisive Branch：

- 传播行为：REQUIRED/REQUIRES_NEW/NESTED 等
- 回滚规则：Runtime vs Checked、rollbackFor/noRollbackFor

---

## 5) Web MVC（一次请求的关键节点）

Entrypoints：

- `org.springframework.web.servlet.DispatcherServlet#doDispatch`
- `org.springframework.web.method.support.InvocableHandlerMethod#invokeForRequest`

Decisive Branch：

- 参数绑定分支：`@RequestBody` vs `@ModelAttribute`
- 400 的根因分流：BindException vs MethodArgumentNotValidException vs HttpMessageNotReadableException

---

## 6) Data JPA（持久化上下文）

Watchpoints：

- `org.hibernate.engine.spi.PersistenceContext`（实体是否在一级缓存里）
- `org.hibernate.internal.SessionImpl`（flush/dirty checking 相关）

---

## 7) Security（过滤器链）

Entrypoints：

- `org.springframework.security.web.FilterChainProxy#doFilterInternal`

Decisive Branch：

- 认证是否成功、授权是否通过
- 401 vs 403 的分支根因
