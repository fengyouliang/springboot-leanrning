# 04. `final` 与代理限制：为什么 final method 拦截不到？

Spring AOP 的默认实现依赖“代理”，而代理的实现方式会带来一些**语言层面的硬限制**。

## CGLIB 为什么会受 `final` 限制？

CGLIB 代理的核心是：**生成目标类的子类**，然后覆盖（override）目标方法，把 advice 链插进去。

因此：

- `final class`：不能被继承 → 无法创建子类代理
- `final method`：不能被覆盖 → 该方法无法插入 advice
- `private method`：子类看不到/无法覆盖 → 通常也无法被拦截

## 在本模块如何验证

看测试：`SpringCoreAopProxyMechanicsLabTest#finalMethodsAreNotInterceptedByCglibProxies`

它的关键断言是：

- 调用 `nonFinal(...)` 会记录一次（被拦截）
- 再调用 `finalMethod(...)` 记录次数仍然不变（final method 没被拦截）

## 学习仓库里你应该怎么用这个结论？

1) 不要把“需要被 AOP/Tx/Validation 拦截的方法”写成 final  
2) 如果你更喜欢使用 `final`（例如偏函数式/不可变风格），那就更推荐：
   - 通过接口 + JDK 代理（拦截接口方法），或
   - 避免依赖基于代理的拦截（在学习仓库里先理解机制，再谈取舍）

## 常见误区

- “我给方法加了注解，但为什么完全没效果？”  
  很多时候不是注解没生效，而是 **这个方法从代理角度根本拦不住**（final/private/self-invocation）。

