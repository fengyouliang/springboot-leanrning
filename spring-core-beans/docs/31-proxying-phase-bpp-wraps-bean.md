# 31. 代理/替换阶段：`BeanPostProcessor` 如何把 Bean “换成 Proxy”

这一章把 AOP/事务里最常见、最折磨人的现象，拉回到容器机制本身：

> 你以为你注入的是目标对象，实际上容器可能把它替换成了另一个对象（proxy / wrapper）。  
> **只有“调用链走代理”，AOP/事务等能力才会生效。**

对应实验（可运行 + 可断言）：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansProxyingPhaseLabTest.java`

建议直接跑：

```bash
mvn -q -pl spring-core-beans -Dtest=SpringCoreBeansProxyingPhaseLabTest test
```

## 1. 现象：容器最终暴露的 Bean 可能不是“原始对象”

在实验里我们写了一个最小的 `BeanPostProcessor`：

- 在 `postProcessAfterInitialization(...)` 里判断：如果 bean 实现了 `WorkService` 接口
- 就返回一个 **JDK 动态代理**，而不是返回原始对象

因此你最终从容器拿到的 bean：

- `Proxy.isProxyClass(bean.getClass()) == true`
- 真实类名会类似 `$Proxy123`

这就是“代理/增强”的最小闭环。

## 2. 现象：self-invocation 仍然绕过代理

实验里的 `SelfInvocationService#outer(...)` 内部调用：

- `this.inner(...)`

当你调用 `proxy.outer(...)` 时：

- 代理拦截到了 `outer`
- 但 `outer` 内部的 `this.inner(...)` 是在目标对象内部直接调用  
  ⇒ **不会再走代理**  
  ⇒ `inner` 不会被拦截记录

这和 AOP/事务/方法参数校验里遇到的“自调用不生效”是同一个根因：**调用路径没走代理**。

## 3. 现象：JDK Proxy 会影响“按实现类注入/获取”

JDK 代理的本质是：

- 它只实现接口
- 并不会“变成”目标类的子类

因此：

- 你能按接口拿到 bean（例如 `WorkService`）
- 但你按实现类拿（例如 `SelfInvocationService`）会失败（实验里用断言验证）

这解释了很多真实项目里常见的困惑：

- “为什么我 `getBean(实现类.class)` 突然拿不到了？”
- “为什么我按实现类注入会报错，但按接口注入没问题？”

## 4. Debug / 观察建议

建议你按这个顺序调试（最快定位）：

1. 打印/观察 bean 的运行时类型：看是不是 `$Proxy...`
2. 如果是 JDK proxy：用 `Proxy.isProxyClass(bean.getClass())` 验证
3. 重点确认调用入口：到底有没有从代理进入？
   - 从容器 `getBean(...)` 拿到的对象调用 → 走代理
   - 同类内部 `this.xxx()` → 不走代理

## 5. 常见坑与实践建议

- **优先面向接口编程**：按接口注入比按实现类注入更稳
- 遇到 AOP/事务“不生效”，先问一句：
  - “这次调用有没有走到代理对象上？”
- self-invocation 的修复思路（原则层面）：
  - 拆分到另一个 bean（让调用变成跨 bean 调用）
  - 或者用更明确的调用路径让调用经过代理

## 6. 延伸阅读（AOP/Tx 的完整版本）

本章只是“容器视角的最小代理实验”。真正的 AOP/事务会在代理中织入拦截器链：

- AOP 心智模型（入口 + 代理）：`spring-core-aop/docs/01-aop-proxy-mental-model.md`
- JDK vs CGLIB（为什么有时能按实现类注入）：`spring-core-aop/docs/02-jdk-vs-cglib.md`
- 自调用陷阱（AOP 版本）：`spring-core-aop/docs/03-self-invocation.md`
- 事务也是代理（Tx 版本）：`spring-core-tx/docs/02-transactional-proxy.md`

