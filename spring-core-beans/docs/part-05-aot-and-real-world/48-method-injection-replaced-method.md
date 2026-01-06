# 48. 方法注入（Method Injection）：replaced-method / MethodReplacer

这一章解决一个“你可能没在新项目里写过，但在读源码/排障时经常看到”的问题：

> **Spring beans 里的 replaced-method 是什么？它跟 AOP 有什么关系？它是怎么做到“改写方法实现”的？**

先给结论：

- `replaced-method` 属于 Spring beans 的 **method injection** 能力
- 它发生在 **实例化阶段**，通过 **CGLIB 子类化** 生成一个“可替换方法的子类”
- 它不是 AOP（不是 advisor/interceptor 那套调用链），但同样依赖代理/字节码增强思想

---

## 0. 复现入口（可运行）

入口测试：

- `spring-core-beans/src/test/java/com/learning/springboot/springcorebeans/part05_aot_and_real_world/SpringCoreBeansReplacedMethodLabTest.java`

推荐运行命令：

```bash
mvn -pl spring-core-beans -Dtest=SpringCoreBeansReplacedMethodLabTest test
```

对应 XML：

- `spring-core-beans/src/test/resources/part05_aot_and_real_world/xml/replaced-method.xml`

---

## 1. 是什么：它解决什么问题？不解决什么问题？

它解决的问题：

- 你想让某个 bean 的某个方法在运行时“由容器决定实现”，而不是固定写死在类里
- 或者你需要一种“配置驱动的可插拔方法实现”（历史上在 XML 配置时代更常见）

它不解决的问题：

- 它不是 AOP：不提供 pointcut/advice 的条件匹配与链式拦截
- 它不是依赖注入：不是“选哪个 bean 注入”
- 它更像是：**容器在创建对象时，生成一个“方法可被替换”的子类**

---

## 2. 怎么用：最小可用写法（XML）

最小结构（本仓库已提供可运行版本）：

- 一个目标 bean（包含要被替换的方法）
- 一个 `MethodReplacer`（实现 `reimplement(...)`）
- 在 `<bean>` 内声明 `<replaced-method name="..." replacer="..."/>`

你运行 Lab 后应该能断言：

- `service.greet("Alice")` 返回的是 replacer 的结果，而不是原始实现
- 目标对象的 class 变成了 CGLIB enhanced class（可用 `Enhancer.isEnhanced` 观察）

---

## 3. 原理：把现象放回容器主线（它发生在哪个阶段？）

把它放回 beans 主线，你会更容易理解：

1) XML 被解析为 BeanDefinition（定义层）
2) BeanDefinition 内部会携带一个 `MethodOverrides`（记录 lookup/replaced 的方法覆盖信息）
3) 当 BeanFactory 创建实例时：
   - 如果发现 definition 存在 method overrides
   - 就会走到 **InstantiationStrategy 的 method injection 分支**
4) Spring 使用 CGLIB 生成子类，并在目标方法处委托给 `MethodReplacer`

所以它的本质是：**定义层的“方法覆盖元数据”影响了实例化策略**。

---

## 4. 怎么实现的：关键类/关键方法/关键分支 + 断点入口

### 4.1 关键对象（你至少要认识名字）

- `AbstractBeanDefinition#getMethodOverrides`：定义层里存放 method override 元数据
- `MethodReplacer`：替换实现（你写的逻辑）
- `InstantiationStrategy`：
  - 当存在 method overrides 时，Spring 会切到 method injection 的 instantiate 分支

### 4.2 推荐断点（从“为什么会走到这里”到“替换发生点”）

- `AbstractAutowireCapableBeanFactory#createBeanInstance`（实例化入口）
- `AbstractAutowireCapableBeanFactory#instantiateWithMethodInjection`（method injection 分支）
- `SimpleInstantiationStrategy#instantiateWithMethodInjection`（策略抽象入口）
- `CglibSubclassingInstantiationStrategy#instantiateWithMethodInjection`（CGLIB 子类化实现）
- `MethodReplacer#reimplement`（你的替换逻辑被调用的点）

建议观察点：

- BeanDefinition 的 `methodOverrides` 是否为空（为什么会走到 method injection 分支）
- 生成后的 bean class 是否为 enhanced class（是否真的发生了子类化）
- replacer 是如何被注入/查找到的（它本身也是一个 bean）

---

## 5. 常见边界与误区

1) **误区：这是 AOP**
   - 不是。它是“实例化策略”层面的子类化替换。
2) **边界：final class / final method**
   - CGLIB 子类化的天然限制：final 类/方法无法被覆盖。
3) **误区：这在现代项目里没意义**
   - 你可能不写，但你要能在排障时识别：某个对象为什么是 enhanced class、为什么方法行为“不像源码那样”。

---

上一章：[47. BeanDefinitionReader：除了注解与 XML，还有 Properties / Groovy](47-beandefinitionreader-other-inputs-properties-groovy.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[49. 内置 FactoryBean 图鉴：MethodInvoking / ServiceLocator / & 前缀](49-built-in-factorybeans-gallery.md)
