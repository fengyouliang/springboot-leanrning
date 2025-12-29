# 15. 实例化前短路：postProcessBeforeInstantiation 能让构造器根本不执行

这一章讲一个“非常像魔法”的容器机制：

- `InstantiationAwareBeanPostProcessor#postProcessBeforeInstantiation`

它允许你在 bean 实例化之前返回一个对象，从而 **短路默认的创建路径**。

对应实验：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansPreInstantiationLabTest.java`

## 1. 现象：构造器抛异常会让 refresh 直接失败

对应测试：

- `SpringCoreBeansPreInstantiationLabTest.withoutBeforeInstantiationShortCircuit_refreshFailsAndConstructorWasCalled()`

你会看到：

- `FailingService` 构造器被调用
- 构造器抛异常导致容器 refresh 失败

这说明：**默认情况下，单例会在 refresh 阶段被创建**（非 lazy）。

## 2. 现象：短路后，构造器不再执行

对应测试：

- `SpringCoreBeansPreInstantiationLabTest.postProcessBeforeInstantiation_canShortCircuitDefaultInstantiationPath()`

我们注册了一个 `InstantiationAwareBeanPostProcessor`：

- 当容器准备创建 `FailingService` 时
- `postProcessBeforeInstantiation` 直接返回一个 JDK proxy（实现了 `GreetingService`）
- 容器就把这个 proxy 当作最终 bean

因此：

- 构造器不会执行
- refresh 不会失败

## 3. 这个机制有什么现实意义？

理解它的价值在于：

- 你能理解“容器为什么能把某个 bean 变成代理/替身对象”
- 你能理解“实例层增强”的入口不仅仅是 AOP（很多能力都是类似机制）

## 4. 常见坑

- **坑 1：返回的对象类型不兼容**
  - 容器后续按类型注入、按类型 getBean 可能会失败（`BeanNotOfRequiredTypeException`）。

- **坑 2：短路会绕过一些正常生命周期**
  - 短路意味着你不走默认实例化流程，很多生命周期回调/依赖注入的时机都会改变。

- **坑 3：学习可以用，工程里要非常谨慎**
  - 它属于极强的扩展点：一旦用错，系统会变得难以推理。

## 5. 一句话自检

- 你能解释清楚：为什么短路后构造器不执行，但 bean 仍然可以被容器拿到并调用吗？
