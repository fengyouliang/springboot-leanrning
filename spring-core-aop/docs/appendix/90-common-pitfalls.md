# 90. 常见坑清单（建议反复对照）

## 坑 1：自调用绕过代理

- 现象：同类内部调用的方法不被拦截
- 章节：见 [docs/03](03-self-invocation.md)
- 解决：抽到另一个 bean；或 self 注入/`ObjectProvider`；或 exposeProxy（进阶，见 [docs/05](05-expose-proxy.md)）
- 对应 Lab：`SpringCoreAopLabTest#selfInvocationDoesNotTriggerAdviceForInnerMethod`
- 推荐断点：`JdkDynamicAopProxy#invoke` / `CglibAopProxy.DynamicAdvisedInterceptor#intercept`

## 坑 2：JDK 代理导致“按实现类拿不到 bean”

- 现象：按接口能注入/获取，按实现类类型获取失败
- 章节：见 [docs/02](02-jdk-vs-cglib.md)
- 解决：用接口注入；或强制 CGLIB（理解取舍后再决定）
- 对应 Lab：`SpringCoreAopProxyMechanicsLabTest#jdkDynamicProxyIsUsedForInterfaceBasedBeans_whenProxyTargetClassIsFalse`
- 推荐断点：`DefaultAopProxyFactory#createAopProxy`

## 坑 3：`final` 方法/类拦截不到

- 现象：明明加了注解，但方法完全不进入 advice
- 章节：见 [docs/04](04-final-and-proxy-limits.md)
- 解决：避免把需要拦截的方法写成 final；或走接口代理
- 对应 Lab：`SpringCoreAopProxyMechanicsLabTest#finalMethodsAreNotInterceptedByCglibProxies`

## 坑 4：只有 Spring 管理的 bean 才能被拦截

- 现象：`new SomeService()` 出来的对象怎么都不进 advice
- 原因：代理只发生在容器创建 bean 的阶段
- 排查要点：确认调用入口拿到的是“容器里的 bean”，而不是你手动 new 的对象

## 坑 5：切点写错导致“你以为学到了机制，其实是误命中”

- 建议：从最小切点起步（`@annotation`），再逐步扩大范围（`execution`）
- 章节：见 [docs/06](06-debugging.md)
- 对应 Exercise：`SpringCoreAopExerciseTest#exercise_changePointcutStyle`

## 坑 6：在 `@PostConstruct` / 构造器里调用被拦截方法，结果“怎么不生效？”

典型误判：

- “我都加了注解/切面了，为什么初始化阶段就是不进 advice？”

事实：

- proxy 通常在 **初始化后阶段** 产生（BPP after-init）
- 构造器与 `@PostConstruct` 发生时，bean 还没有被替换成最终 proxy
- 并且这类调用经常还是 `this.xxx()`（自调用），会再次绕过 proxy

建议：

- 不要依赖 AOP 去拦截构造期/初始化期内部调用
- 把需要被拦截的逻辑放到真正的业务入口（例如 service public 方法），并确保调用链走 bean proxy

深挖入口：见 [00 深挖指南](00-deep-dive-guide.md)

## 坑 7：开启 exposeProxy 以后，“换线程/异步”突然拿不到 currentProxy

事实：

- `AopContext.currentProxy()` 基于 thread-local，上下文不自动跨线程传播

建议：

- exposeProxy 主要用于“理解机制/偶发修复”，不要作为常规架构方案
- 工程上更推荐：重构拆分 bean 或自注入/`ObjectProvider`（见 docs/03、docs/05）

## 坑 8：多个切面顺序搞反，以为 `@Order` “越大越先执行”

事实（建议用测试验证结论，不要靠记忆）：

- `@Order` 值越小，优先级通常越高（更靠外层/更早进入）

对应 Lab：

- `SpringCoreAopProxyMechanicsLabTest#adviceOrderingCanBeControlledWithOrderAnnotation`

推荐观察点：

- 断点进 `DefaultAdvisorChainFactory#getInterceptorsAndDynamicInterceptionAdvice` 看拦截器链顺序

## 坑 9：this/target 写反，在 JDK proxy 下永远不命中

典型误判：

- 你知道实现类是 `Impl`，于是写了 `this(Impl)`，以为“会命中 Impl”
- 但项目实际是 JDK proxy（接口代理），proxy 不是 Impl 的子类
- 结果：`this(Impl)` 永远不命中，导致你误判 AOP 失效

解决：

- 优先用更稳的切点（`execution`/`@annotation`），再逐步引入 this/target 收敛范围
- 或明确理解代理类型与 this/target 的差异（用 Lab 固化结论）

章节与 Lab：

- 章节：见 [docs/08](08-pointcut-expression-system.md)
- Lab：`SpringCoreAopPointcutExpressionsLabTest`

## 坑 10：把“叠加”误认为“很多层 proxy”，排障方向跑偏

事实：

- 真实项目主流形态是：**一个 proxy 上挂多个 advisors**（事务/缓存/安全/切面都在 advisors 列表里）
- 多层 proxy（套娃）并非默认，但在某些场景会出现（手工 ProxyFactory、多个包装型 BPP、scoped proxy 等）

解决：

- 用 `Advised#getAdvisors()` 直接把“叠加实体”看见
- 再判断 target 是否还是 proxy，确认是否存在套娃

章节与 Lab：

- 章节：见 [docs/09](09-multi-proxy-stacking.md)
- Lab：`SpringCoreAopMultiProxyStackingLabTest`
