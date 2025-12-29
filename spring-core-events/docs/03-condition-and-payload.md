# 03. condition 与 payload：监听器为什么能“按条件触发”甚至接收普通对象？

Spring 事件有两个很实用的能力：

1) **按条件触发**：只在满足某些条件时才执行监听器  
2) **payload 事件**：发布普通对象，也可以被 `@EventListener` 接住

## 1) 条件触发：`@EventListener(condition = "...")`

验证入口：`SpringCoreEventsLabTest#conditionalEventListenerOnlyRunsWhenConditionMatches`

本模块里条件是：

- `#event.username().startsWith('A')`

因此：

- `Bob` 不触发
- `Alice` 触发

学习建议：

- 条件尽量保持简单可读（学习阶段尤其重要）
- 把“条件”当作一种轻量的过滤器，而不是把复杂业务规则塞进 SpEL

## 2) payload：发布 String 也能被监听器接到

验证入口：`SpringCoreEventsLabTest#publishingPlainObjectsAlsoWorks_asPayloadEvents`

核心规则很简单：

> 监听方法参数的类型，与 publish 的对象类型匹配即可。

本模块里：

- publish：`eventPublisher.publishEvent("hello")`
- listen：`public void on(String payload)`

## 一句话总结

- condition 让你更容易写“机制实验”（同一个发布动作，用不同输入触发不同监听器）
- payload 让事件机制更轻量：不一定每个动作都要建一个 event class

