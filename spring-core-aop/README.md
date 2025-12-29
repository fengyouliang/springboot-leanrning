# spring-core-aop

本模块用“可运行的最小示例 + 可验证的测试实验（Labs / Exercises）”讲透 Spring AOP 的核心机制。

这份 `README.md` 只做索引与导航；更深入的解释请按章节阅读：见 [docs/](docs/)。

## 你将学到什么

- AOP 默认通过 **代理（proxy）** 生效（你的 Bean 可能会被包装成另一个对象）
- Advice / Pointcut 的最小闭环（本模块以 `@Around` + `@annotation(...)` 为主）
- 代理的典型限制：JDK vs CGLIB、`final` 方法、以及自调用陷阱

## 前置知识

- 建议先完成 `spring-core-beans`（知道什么是 Bean/容器就够）
- （可选）了解“方法调用链”与“入口是否走 Spring Bean”的区别

## 关键命令

### 运行

```bash
mvn -pl spring-core-aop spring-boot:run
```

运行后观察控制台输出：

- 被拦截方法的 AOP 计时日志
- 自调用示例：只会拦截到 `outer(...)`，而 `inner(...)` 不会被拦截（因为内部调用没有经过代理）

### 测试

```bash
mvn -pl spring-core-aop test
```

## 推荐 docs 阅读顺序（从现象到机制）

1. [AOP 心智模型：代理 + 入口（call path）](docs/01-aop-proxy-mental-model.md)
2. [JDK vs CGLIB：代理类型与可注入类型差异](docs/02-jdk-vs-cglib.md)
3. [自调用陷阱：为什么 `this.inner()` 不会被拦截](docs/03-self-invocation.md)
4. [`final` 限制：为什么 final method 拦截不到](docs/04-final-and-proxy-limits.md)
5. [exposeProxy：用 `AopContext.currentProxy()` 绕过自调用（进阶）](docs/05-expose-proxy.md)
6. [Debug / 观察：如何“看见”代理与切点](docs/06-debugging.md)
7. [常见坑清单（建议反复对照）](docs/90-common-pitfalls.md)

## Labs / Exercises 索引（按知识点 / 难度）

> 说明：⭐=入门，⭐⭐=进阶，⭐⭐⭐=挑战。Exercises 默认 `@Disabled`。

| 类型 | 入口 | 知识点 | 难度 | 推荐阅读 |
| --- | --- | --- | --- | --- |
| Lab | `src/test/java/com/learning/springboot/springcoreaop/SpringCoreAopLabTest.java` | 最小 advice 闭环 + 自调用陷阱 | ⭐⭐ | `docs/01`、`docs/03` |
| Lab | `src/test/java/com/learning/springboot/springcoreaop/SpringCoreAopProxyMechanicsLabTest.java` | JDK vs CGLIB、final 限制、advice 顺序 | ⭐⭐⭐ | `docs/02`、`docs/04`、`docs/06` |
| Exercise | `src/test/java/com/learning/springboot/springcoreaop/SpringCoreAopExerciseTest.java` | exposeProxy/多切面顺序/pointcut 风格等练习 | ⭐⭐–⭐⭐⭐ | 先把 Labs 理解透再做 |

## 概念 → 在本模块哪里能“看见”

| 你要理解的概念 | 去读哪一章 | 去看哪个测试/代码 | 你应该能解释清楚 |
| --- | --- | --- | --- |
| advice 为什么能“拦截”方法 | [docs/01](docs/01-aop-proxy-mental-model.md) | `SpringCoreAopLabTest#adviceIsAppliedToTracedMethod` + `TracingAspect` | 代理如何把横切逻辑织入调用链 |
| 自调用为什么绕过代理 | [docs/03](docs/03-self-invocation.md) | `SpringCoreAopLabTest#selfInvocationDoesNotTriggerAdviceForInnerMethod` + `SelfInvocationExampleService` | “走没走代理”决定 advice 生效与否 |
| JDK vs CGLIB 代理差异 | [docs/02](docs/02-jdk-vs-cglib.md) | `SpringCoreAopProxyMechanicsLabTest#jdkDynamicProxyIsUsed...` | 为什么有时 `getBean(实现类.class)` 会失败 |
| `final` method 拦截不到 | [docs/04](docs/04-final-and-proxy-limits.md) | `SpringCoreAopProxyMechanicsLabTest#finalMethodsAreNotInterceptedByCglibProxies` | CGLIB 基于继承，无法覆盖 final |
| 多个切面顺序怎么控制 | [docs/06](docs/06-debugging.md) | `SpringCoreAopProxyMechanicsLabTest#adviceOrderingCanBeControlledWithOrderAnnotation` | `@Order` 对 advice 链的影响 |

## 常见 Debug 路径

- 先确认“是不是代理”：`AopUtils.isAopProxy(bean)`
- 再确认“是什么代理”：`AopUtils.isJdkDynamicProxy(bean)` / `AopUtils.isCglibProxy(bean)`
- 观察切点是否命中：先让 advice 里写入 `InvocationLog`（比依赖日志输出更稳定）
- 遇到“不拦截”的问题，优先排查：是否自调用、是否 `final`、是否调用入口走的是 Spring 管理的 bean

## 常见坑

- 你以为你在调用目标对象，其实你在调用代理对象（类型/调试现象会不一样）
- 自调用绕过代理：同类内部 `this.xxx()` 不会触发 advice
- `final` 方法/类的限制：CGLIB 不能覆盖 final method，JDK 代理也只能代理接口方法
- 只有 Spring 容器管理的 bean 才能被代理；`new` 出来的对象不会被拦截
- pointcut 写得“太宽/太窄”都会让你误判机制（建议先用最小切点验证）

## 参考

- Spring Framework Reference：AOP
- Spring Boot Reference：AOP starter（`spring-boot-starter-aop`）
