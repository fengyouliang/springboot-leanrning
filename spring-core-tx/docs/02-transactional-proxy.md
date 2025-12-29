# 02. `@Transactional` 如何生效：它也是 AOP（也是代理）

`@Transactional` 很多人把它当“事务开关”，但它的实现本质上是 **AOP 拦截器**。

> Spring 在调用目标方法前开启事务，在方法正常返回时提交，在异常传播时回滚。

## 在本模块如何验证“事务是靠代理实现的”

看测试：`SpringCoreTxLabTest#transactionalBeansAreProxied`

- `AopUtils.isAopProxy(accountService)` 为 true

这说明：你注入的 `accountService` 并不是纯粹的 `AccountService` 实例，而是一个代理对象。

## `@Transactional` 生效的 3 个前提（最常见）

1. 目标对象必须是 Spring 容器管理的 bean（`@Service` / `@Component` 等）
2. 调用入口必须“走代理”  
   - 同类内部自调用会绕过代理（AOP/Tx 的同一类坑）
3. 目标方法必须能被代理拦截  
   - `final` 方法、`private` 方法等可能导致拦截失效（见 AOP 模块的 [spring-core-aop/docs/04](../../spring-core-aop/docs/04-final-and-proxy-limits.md)）

## 一句话总结

当你觉得事务“不生效”时，先问自己：

> 这次调用有没有走到 `TransactionInterceptor` 这条 AOP 链？

