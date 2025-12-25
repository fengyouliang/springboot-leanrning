# 01. Bean 心智模型：BeanDefinition vs Bean 实例

这一章的目标是先把“Bean 到底是什么”这件事说清楚：**Bean 不是对象本身，而是“容器管理对象的一整套机制”**。如果你脑子里只有“Bean = 被 `@Component` 标注的类”，后面一定会在 Scope、生命周期、代理、自动装配上不断踩坑。

## 1. 你要建立的 3 层心智模型

把 Spring 容器（IoC Container）理解成三层：

1) **配置来源（inputs）**：注解、`@Bean` 方法、`@Import`、XML、程序化注册……
2) **定义层（definitions）**：容器把输入解析成 `BeanDefinition`（以及一堆相关元数据）
3) **实例层（instances）**：容器根据定义创建对象、注入依赖、执行回调，并在合适的时机销毁

一句话概括：

- `BeanDefinition` 描述“如何创建一个 Bean”
- Bean instance 是“创建出来的那个对象”

## 2. BeanDefinition 是什么（以及它通常包含什么）

`BeanDefinition` 可以理解为“对象工厂的配方 + 生命周期/依赖元数据”。常见信息包括（不要求记 API，先记概念）：

- beanName：这个 bean 在容器里的名字
- beanClass / factoryMethod / factoryBeanName：用哪种方式创建实例
- scope：`singleton` / `prototype` / 其他 scope
- lazyInit：是否延迟创建（常见于 `@Lazy`）
- dependsOn：依赖顺序（`@DependsOn`）
- propertyValues / constructorArgs：要注入什么
- autowireCandidate、primary 等候选资格信息

这也是为什么“扩展点”通常分两类：

- **在定义层动手**：例如 BFPP（`BeanFactoryPostProcessor`）可以改 `BeanDefinition`
- **在实例层动手**：例如 BPP（`BeanPostProcessor`）可以包一层代理/修改对象

## 3. BeanFactory vs ApplicationContext：责任边界

很多学习资料把它们混在一起讲，导致初学者误以为它们是“同一个东西的不同名字”。

- `BeanFactory`：最核心的容器能力（Bean 的创建、依赖注入、Scope、生命周期的骨架）
- `ApplicationContext`：在 `BeanFactory` 之上提供更多“应用层能力”
  - 资源加载（Resource）
  - 国际化（MessageSource）
  - 事件发布（ApplicationEventPublisher）
  - 环境（Environment）
  - 更丰富的自动检测与装配逻辑（配合各种后处理器）

在 Spring Boot 应用中，你基本总是在使用 `ApplicationContext`（因为 Boot 启动时创建的就是它的某个实现）。

## 4. 容器启动的高层流程（你至少要能复述）

你不需要背源码，但要能说清楚“发生了什么顺序”。一个典型的容器启动可以粗略理解为：

1) **收集配置**（扫描、解析 `@Configuration`、处理 `@Import` 等）
2) **注册 BeanDefinition** 到 `BeanDefinitionRegistry`
3) **执行 BFPP**：允许在实例化之前调整定义（或再注册一些定义）
4) **注册 BPP**：这些会影响后续 Bean 的创建/初始化
5) **创建单例 Bean**（非 lazy 的单例通常会在 refresh 过程中预实例化）
6) **发布容器就绪相关事件**（这是 `ApplicationContext` 的能力）

注意：**“注册定义”与“创建实例”是两个阶段**。这句话会贯穿你对 Spring 的全部理解。

## 5. 在本模块里如何“看见”这件事

你可以用容器内部实验直接确认“定义不等于实例”：

- 对应实验：`src/test/java/com/learning/springboot/springcorebeans/SpringCoreBeansContainerLabTest.java`
  - `beanDefinitionIsNotTheBeanInstance()`

这个实验想传达的是：

- 你可以从 `BeanFactory` 拿到 `BeanDefinition`
- 也可以从容器拿到 `ExampleBean` 实例
- 它们是两种不同概念对象

## 6. 一句话自检

读完这一章，你至少要能回答：

1) “BeanDefinition 和 Bean instance 的区别是什么？”
2) “为什么说 BFPP 更像是在改‘配方’，BPP 更像是在改‘做出来的菜’？”
3) “为什么 Spring Boot 的自动装配本质上就是在某个阶段批量注册 BeanDefinition？”

下一章开始我们会从“BeanDefinition 从哪里来”讲起：扫描、`@Bean`、`@Import`、registrar，以及它们和 Spring Boot 自动装配的关系。

