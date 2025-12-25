# spring-core-aop

本模块用于学习 **Spring AOP 基础**：

- AOP 通过 **代理（proxy）** 生效（你的 Bean 可能会被包装）
- Advice 类型（本模块使用 `@Around`）
- Pointcut（本模块使用 `@annotation(...)` 作为切点）
- 一个常见坑：**自调用（self-invocation）**（在同一个类里用 `this` 调用方法会绕过代理）

## 学习目标

- 理解什么是 Spring AOP 代理（以及为什么需要它）
- 能写一个最小可用的 `@Aspect` 并应用到目标方法上
- 用测试验证 advice 确实生效
- 能识别“自调用导致 advice 不生效”的典型场景

## 运行

```bash
mvn -pl spring-core-aop spring-boot:run
```

运行后观察控制台输出：

- 被拦截方法的 AOP 计时日志
- 自调用示例：只会拦截到 `outer(...)`，而 `inner(...)` 不会被拦截（因为调用没有经过代理）

## 测试

```bash
mvn -pl spring-core-aop test
```

## Deep Dive（Labs / Exercises）

- Labs（默认启用）：
  - `SpringCoreAopLabTest`：验证 advice 生效 + 自调用陷阱
  - `SpringCoreAopProxyMechanicsLabTest`：代理类型（JDK/CGLIB）、final method 限制、Advice 顺序
- Exercises（默认禁用）：`SpringCoreAopExerciseTest`（带 `@Disabled`）

启用 Exercises：打开 `*ExerciseTest`，移除/注释 `@Disabled`，按提示完成后再运行 `mvn -pl spring-core-aop test`。

## 说明：自调用（self-invocation）陷阱

如果一个被代理的 bean 在自己内部调用自己的另一个方法（例如 `outer()` 通过 `this.inner()` 调用 `inner()`），
这次调用不会经过 Spring 代理，因此 advice 可能不会应用到 `inner()`。

常见解决思路（本模块不实现）：

- 把需要被拦截的方法抽到另一个 Spring Bean 中，通过注入那个 Bean 来调用
- 通过接口把“代理对象”再注入回自己（进阶用法）
- 使用 AspectJ 编译期/加载期织入（配置更重）

## 小练习

- 新增一个 advice（例如 `@Before`）打印方法名
- 再加一个 aspect，并用 `@Order` 控制顺序
- 把切点从 `@annotation` 改成 `execution(...)` 表达式

## 参考

- Spring Framework Reference：AOP
- Spring Boot Reference：AOP starter（`spring-boot-starter-aop`）
