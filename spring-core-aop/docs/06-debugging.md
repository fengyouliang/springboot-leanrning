# 06. Debug / 观察：如何“看见”代理与切点

学习 AOP 时，最怕的不是概念难，而是“感觉它在工作，但我看不见”。这一章给出一套可复用的观察方法。

## 1) 先判断 bean 是否为代理

在测试/代码里直接断言：

- `AopUtils.isAopProxy(bean)`：是不是代理
- `AopUtils.isJdkDynamicProxy(bean)`：是不是 JDK 代理
- `AopUtils.isCglibProxy(bean)`：是不是 CGLIB 代理

本模块的 `SpringCoreAopLabTest` 已经给了现成例子。

## 2) 不要只靠日志：用“可断言的观察点”

`TracingAspect` 里除了 `System.out.println(...)`，更关键的是：

- 它把方法签名写入了 `InvocationLog`
- 测试通过断言 `InvocationLog` 来判断“是否拦截、拦截了谁”

这比“看控制台输出顺序”更稳定，也更适合学习。

## 3) 验证切点是否命中（从最小切点开始）

建议学习路径：

1. 先用最小切点（例如 `@annotation(Traced)`）确保你“能拦截”
2. 再尝试把切点换成更通用表达式（例如 `execution(...)`），对照命中范围变化

练习入口：`SpringCoreAopExerciseTest#exercise_changePointcutStyle`

## 4) 遇到“不拦截”的排查顺序（经验）

1. 调用入口是否走代理（是否自调用）
2. 目标方法是否能被拦截（`final/private` 等限制）
3. 切点表达式是否覆盖到目标方法
4. 代理类型是否与你的注入/获取方式匹配（JDK vs CGLIB）

