# 92. 知识点地图（Concept → Chapter → Lab）

## 0. 复现入口（可运行）

- 本章为索引/术语类内容，不直接提供单一 Lab 入口。
- 建议做法：从本页跳转到对应章节后，按章节中的“复现入口（可运行）”运行对应 Test。

这份“知识点地图”用于两类阅读方式：

1) **顺读成体系**：按 Part 00 → 01 → 02 → 03 → 04 → Appendix
2) **按问题跳读**：按“症状/异常/现象”快速定位到章节与 Lab（可直接跑，立刻复现）

---

## 1) 顺读主线（最推荐）

如果你希望对 Spring Bean 有“全面透彻的理解”，建议按这个顺序读并跑对应 Labs：

1. `00`：深挖指南（把学习变成可重复实验）
2. `01–09`：IoC 主线（BeanDefinition → 注册 → 注入 → scope → 生命周期 → 扩展点 → 循环依赖）
3. `10–11`：Boot 自动装配与排障（为什么有/为什么没有）
4. `12–17`：容器内部机制（顺序/短路/early reference/回调顺序）
5. `18–37`：边界与高级语义（lazy/dependsOn/resolvable/alias/FactoryBean/代理/value/merged/转换/泛型）
6. `90/99`：坑点复盘与自测

---

## 2) 按问题跳读（症状 → 章节 → Lab）

### 2.1 注入失败（NoSuch / NoUnique / UnsatisfiedDependency）

- 章节：
  - `03` 依赖注入解析（候选收敛）
  - `33` `@Primary/@Priority/@Order` 的边界
  - `11` 调试与可观察性（从异常到断点）
- Labs：
  - `SpringCoreBeansInjectionAmbiguityLabTest`
  - `SpringCoreBeansAutowireCandidateSelectionLabTest`
  - `SpringCoreBeansExceptionNavigationLabTest`

### 2.2 prototype 注入 singleton 后“像单例”

- 章节：`04` Scope 与 prototype 注入陷阱
- Labs/Exercises：
  - `SpringCoreBeansLabTest`（prototype 相关用例）
  - `SpringCoreBeansExerciseTest`（改造题）

### 2.3 `@Value` 不严格/值变成 `"${...}"`

- 章节：`34` `@Value("${...}")` 占位符解析
- Lab：`SpringCoreBeansValuePlaceholderResolutionLabTest`

### 2.4 代理导致行为“不符合直觉”（self-invocation、最终对象不是原始实例）

- 章节：
  - `31` 代理产生阶段：BPP 如何把 Bean 换成 Proxy
  - `15/16`（pre/early）代理与短路/early reference
- Labs：
  - `SpringCoreBeansProxyingPhaseLabTest`
  - `SpringCoreBeansPreInstantiationLabTest`
  - `SpringCoreBeansEarlyReferenceLabTest`

### 2.5 循环依赖：为什么 setter 能救、constructor 无解？

- 章节：`09` 循环依赖概览 + `16` early reference 与循环依赖
- Labs：
  - `SpringCoreBeansContainerLabTest`（constructor vs setter）
  - `SpringCoreBeansEarlyReferenceLabTest`

### 2.6 “顺序”导致结果不同（post-processors、链路、排序误用）

- 章节：`14` 顺序（PriorityOrdered/Ordered/无序）
- Labs：`SpringCoreBeansPostProcessorOrderingLabTest`

### 2.7 泛型匹配“看起来有，但按泛型找不到”

- 章节：`37` 泛型匹配与注入坑
- Lab：`SpringCoreBeansGenericTypeMatchingPitfallsLabTest`

### 2.8 类型转换：字符串为何能注入到 int/自定义类型？

- 章节：`36` 类型转换（BeanWrapper/ConversionService）
- Lab：`SpringCoreBeansTypeConversionLabTest`

---

## 3) 一页纸：核心概念到章节的映射

> 这张映射用于“复述式学习”：你能把概念准确指向章节与断点入口，就意味着你真的掌握了它的边界。

- Bean 三层模型（定义/实例/代理）→ `01`、`15/16/31`
- 注册入口（scan/@Bean/@Import/registrar）→ `02`、`13`
- 候选选择（Qualifier/Primary/Priority/Order）→ `03`、`33`
- 处理器（BFPP/BDRPP/BPP）→ `06`、`12–14`
- 生命周期（回调顺序/销毁语义）→ `05`、`17`
- FactoryBean（product vs factory/边界）→ `08`、`23`、`29`
- 值解析与类型转换（@Value/ConversionService）→ `34`、`36`
- 泛型匹配（ResolvableType/代理丢失信息）→ `37`

---

上一章：[91. 术语表（Glossary）](91-glossary.md) ｜ 目录：[Docs TOC](../README.md) ｜ 下一章：[99. 自测题：你是否真的理解了？](99-self-check.md)