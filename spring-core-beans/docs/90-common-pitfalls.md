# 90. 常见坑清单（建议反复对照）

这份清单不是为了“背”，而是为了让你在遇到问题时能快速定位：到底是概念没建立，还是机制没搞清。

## 1) 以为“prototype 每次方法调用都是新对象”

典型症状：

- prototype 注入 singleton 后怎么一直不变？

正确理解：

- prototype 是“每次向容器获取都新建”
- 直接注入只获取了一次

解决方案：

- `ObjectProvider`
- `@Lookup`
- scoped proxy（谨慎）

见：[04. Scope 与 prototype 注入陷阱](04-scope-and-prototype.md)

## 2) 以为 `@Order` 能解决“单个依赖注入的歧义”

事实：

- `@Order` 更常用于集合注入的排序
- 单依赖选择优先看 `@Primary`、`@Qualifier` 等

见：[03. 依赖注入解析](03-dependency-injection-resolution.md)

## 3) 在 `@Configuration(proxyBeanMethods=false)` 里互相调用 `@Bean` 方法

典型症状：

- 明明是单例，却出现多个实例（或者行为像多例）

推荐写法：

- 用 `@Bean` 方法参数声明依赖

见：[07. @Configuration 增强](07-configuration-enhancement.md)

## 4) 把 `FactoryBean` 当作“普通 bean”

典型症状：

- `getBean("name")` 拿到的类型不对
- “怎么注入工厂本身？”

核心记忆：

- `"name"` → product
- `"&name"` → factory

见：[08. FactoryBean](08-factorybean.md)

## 5) 认为“循环依赖能跑起来就没问题”

事实：

- setter 循环能成功不代表设计合理
- 半初始化对象、代理、生命周期都会让问题变复杂
- Boot 环境里可能默认更严格，直接不让你启动

见：[09. 循环依赖](09-circular-dependencies.md)

## 6) 认为“自动装配就是自动注入”

事实：

- 自动装配主要是在启动时“导入配置并注册 BeanDefinition”
- 依赖注入解析仍遵循 Spring 容器规则

建议：

- 学会看条件报告（`--debug` / `debug=true`）

见：[10. Boot 自动装配](10-spring-boot-auto-configuration.md) 与 [11. 调试](11-debugging-and-observability.md)

## 7) 把 `applicationContext.getBean()` 当成日常依赖注入方式

事实：

- 这是 service locator 风格，会隐藏依赖关系，降低可测试性

建议：

- 默认用构造器注入
- 只有在确实需要“延迟/可选/按需获取”时才用 `ObjectProvider`

