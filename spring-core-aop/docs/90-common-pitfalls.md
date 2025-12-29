# 90. 常见坑清单（建议反复对照）

## 坑 1：自调用绕过代理

- 现象：同类内部调用的方法不被拦截
- 章节：见 [docs/03](03-self-invocation.md)
- 解决：抽到另一个 bean；或 exposeProxy（进阶，见 [docs/05](05-expose-proxy.md)）

## 坑 2：JDK 代理导致“按实现类拿不到 bean”

- 现象：按接口能注入/获取，按实现类类型获取失败
- 章节：见 [docs/02](02-jdk-vs-cglib.md)
- 解决：用接口注入；或强制 CGLIB（理解取舍后再决定）

## 坑 3：`final` 方法/类拦截不到

- 现象：明明加了注解，但方法完全不进入 advice
- 章节：见 [docs/04](04-final-and-proxy-limits.md)
- 解决：避免把需要拦截的方法写成 final；或走接口代理

## 坑 4：只有 Spring 管理的 bean 才能被拦截

- 现象：`new SomeService()` 出来的对象怎么都不进 advice
- 原因：代理只发生在容器创建 bean 的阶段

## 坑 5：切点写错导致“你以为学到了机制，其实是误命中”

- 建议：从最小切点起步（`@annotation`），再逐步扩大范围（`execution`）
- 章节：见 [docs/06](06-debugging.md)

