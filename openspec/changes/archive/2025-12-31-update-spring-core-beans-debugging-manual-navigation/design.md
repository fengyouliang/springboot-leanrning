# Design: “调试手册块（call chain + watch list + 反例）”与异常导航扩展

## Goals

1) 把关键章节写成“可直接照抄的调试手册”
   - 给出最短调用链（不要求读者把全链路单步到底）
   - 给出固定 watch list（不靠“看日志猜”）
   - 给出反例（把常见误判写死，并告诉你该在 debugger 里看什么来纠错）

2) 把 `docs/11` 的“异常 → 断点入口”表升级成真正的“报错即导航”
   - 覆盖更多高频异常
   - 每条异常都能跳到一个“最小可跑 Lab/Test”入口（最好精确到方法）

3) 不破坏现有章节的模板约束与检索体验
   - `docs/19` 属于 `12–34` 的机制章，必须保留现有的三段模板标题：
     - `## 源码锚点（建议从这里下断点）`
     - `## 断点闭环（用本仓库 Lab/Test 跑一遍）`
     - `## 排障分流：这是定义层问题还是实例层问题？`

## Non-goals

- 不做全量异常词典（异常表只覆盖高频 + 可映射到明确入口的）
- 不引入新外部依赖
- 不做生产级“依赖图导出/可视化工具”（学习定位保持 test-only + 最小能力）

## “调试手册块”模板定义

对目标章节（`docs/03`、`docs/19`、`docs/35`）追加 3 个固定小节（标题保持一致，方便全文检索与复用）：

1) `## 源码最短路径（call chain）`
   - 以“最短可跟栈”为目标：从入口到关键分支只列必要节点
   - 推荐表达：
     - 每个节点用 `Class#method`（或 `Class#method -> next`）列出
     - 每个节点补 1 行“此处看什么”（对应 watch list 的关键变量）

2) `## 固定观察点（watch list）`
   - 以“可在 debugger 里直接 watch/evaluate”为目标
   - 既包含局部变量（例如 `descriptor`/`mbdToUse`），也包含容器内部结构（例如 `dependentBeanMap`/`mergedBeanDefinitions`）
   - 对每个观察点补 1 行“它回答哪个问题”（避免堆变量名）

3) `## 反例（counterexample）`
   - 必须是“最小可复现”的误区
   - 必须指向一个本仓库的可跑入口（`*LabTest` 文件 + 测试方法名）
   - 明确写出：你会误判成什么、在 watch list 里应该看到什么来纠错

### 与既有模板的兼容方式

- `docs/03`（基础章）与 `docs/35`（新编号章）不受 `12–34` 模板标题约束，可直接追加上述 3 个 `##` 小节。
- `docs/19` 必须保留三段模板标题；本变更采用“增量追加”：
  - 保留现有三段模板区块不动
  - 在合适位置（建议在 `## 排障分流` 之后、footer 之前）追加“调试手册块”三小节
  - 这样既满足既有检索/模板要求，又新增更硬核的调试路径

## 章节级设计要点（每章要写到“源码级”的具体抓手）

### `docs/03`：把 `doResolveDependency` 的收敛规则写成“调试手册”

**核心输出**：当你在 `DefaultListableBeanFactory#doResolveDependency(...)` 停住时，如何用 1 次 watch list + 3 次 step-over 快速回答：

- 候选是怎么来的？（`findAutowireCandidates`）
- 是在哪条规则上“收敛到唯一候选”的？（`determineAutowireCandidate`）
- 为什么没有候选/候选太多？（异常分流）

**call chain（最短路径）建议覆盖：**

- `AutowiredAnnotationBeanPostProcessor#postProcessProperties`
  - `DefaultListableBeanFactory#resolveDependency`
    - `DefaultListableBeanFactory#doResolveDependency`
      - （命中 ResolvableDependency 分支）/ `findAutowireCandidates`
      - `determineAutowireCandidate`（以及 `determinePrimaryCandidate` / `determineHighestPriorityCandidate`）

**watch list 建议覆盖：**

- `descriptor.getDependencyType()` / `descriptor.getDependencyName()`
- `requiredType`
- `autowiredBeanNames`
- `candidateNames` / `matchingBeans`
- `autowireCandidateResolver`（尤其是 qualifier 相关 resolver）

**反例建议：**

- “给 bean 加 `@Order` 期待能解决单依赖歧义”（应跳转到 `docs/33` 并用其 Lab 复现）

### `docs/19`：把 `dependentBeanMap` 的记录机制与销毁顺序写透

**核心输出**：学习者能解释清楚：

- “dependsOn” 是如何被转成 `dependentBeanMap`/`dependenciesForBeanMap` 的
- `dependentBeanMap` 既记录 dependsOn，也记录“真实注入依赖”（因此销毁顺序可能比你想象的更复杂）
- 销毁顺序为何与初始化顺序相反（先销毁 dependent，再销毁 dependency）

**call chain（最短路径）建议覆盖：**

- 初始化阶段：
  - `AbstractBeanFactory#doGetBean`
    - `getMergedLocalBeanDefinition`
    - `RootBeanDefinition#getDependsOn`
    - `DefaultSingletonBeanRegistry#registerDependentBean`
    - `getBean(dep)`（触发被依赖 bean 的创建）
- 销毁阶段：
  - `DefaultSingletonBeanRegistry#destroySingletons`
    - `destroyBean`
      - 基于 `dependentBeanMap` 先销毁 dependents

**watch list 建议覆盖：**

- `DefaultSingletonBeanRegistry#dependentBeanMap`
- `DefaultSingletonBeanRegistry#dependenciesForBeanMap`
- `dependentBeans` / `dependenciesForBean`（单次调用取出的集合）

**反例建议：**

- “我只写了 `dependsOn`，为什么关闭时销毁顺序/依赖图里出现更多依赖？”  
  解释：注入解析与 `BeanDefinitionValueResolver` 也会注册依赖关系。

### `docs/35`：补齐 merged 在 `createBean` 链路中的“精确位置”

**核心输出**：学习者能把 `merged` 放回时间线，并能在断点里准确知道：

- merged definition 是在哪里拿到的（以及缓存在哪里）
- `MergedBeanDefinitionPostProcessor` 是在 `doCreateBean` 的哪个阶段被调用的（before populateBean）

**call chain（最短路径）建议覆盖：**

- `AbstractBeanFactory#doGetBean`
  - `getMergedLocalBeanDefinition`
  - `AbstractAutowireCapableBeanFactory#createBean`
    - `doCreateBean`
      - `createBeanInstance`
      - `applyMergedBeanDefinitionPostProcessors`
      - `populateBean`
      - `initializeBean`

**watch list 建议覆盖：**

- `AbstractBeanFactory#mergedBeanDefinitions`（或等价缓存结构）
- `mbd` / `mbdToUse`（是否为 `RootBeanDefinition`、parentName、propertyValues、init/destroy 元数据）
- `mbd.isStale()`（或等价字段/标记）

**反例建议：**

- “我改了 `BeanDefinition`，但创建时没生效 / 还是旧的 merged”  
  解释：merged 有缓存与 stale 标记；需要用清缓存入口验证（学习者至少知道现象来自缓存，而不是‘Spring 随机’）。

## “异常 → 断点入口”表扩展设计（`docs/11`）

### 目标表格列

保持现有四列结构，并强化第 4 列要求：

| 你看到的异常 | 常见含义（先分流） | 最有效入口断点（优先打条件断点） | 关联章节 / 最小可跑 Lab/Test |

### 覆盖的异常（至少）

- `NoSuchBeanDefinitionException`
- `NoUniqueBeanDefinitionException`
- `UnsatisfiedDependencyException`
- `BeanCurrentlyInCreationException`
- `BeanCreationException`
- `BeanDefinitionStoreException`

### 最小可跑入口的落地策略

- 能复用既有 Lab/Test 就复用（避免重复用例）：
  - `NoUniqueBeanDefinitionException`：复用 `SpringCoreBeansAutowireCandidateSelectionLabTest`
  - `BeanCreationException`：复用 `SpringCoreBeansPreInstantiationLabTest` 或 `SpringCoreBeansContainerLabTest`（选择更小/更稳定的那一个）
  - `BeanCurrentlyInCreationException`：复用 `SpringCoreBeansEarlyReferenceLabTest`
- 缺少稳定复现入口的异常补齐最小 Lab/Test：
  - `BeanDefinitionStoreException`：新增一个只依赖 `spring-beans` 的 XML 读取用例（`XmlBeanDefinitionReader` + in-memory resource），确保异常类型稳定
  - `UnsatisfiedDependencyException`：新增一个“缺失依赖导致注入失败”的最小用例，确保异常类型稳定

