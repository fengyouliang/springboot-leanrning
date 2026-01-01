## 1. Docs（把 11/19 升级为源码级闭环手册）

- [x] 1.1 更新 `spring-core-beans/docs/11-debugging-and-observability.md`：增加“观测对象总览（5 类对象）”
  - [x] 为每类对象提供：1 个断点入口（`Class#method`）+ 固定 watch list（变量/容器结构）
  - [x] 明确每类对象回答的问题（“我到底在确认什么”）

- [x] 1.2 更新 `spring-core-beans/docs/11-debugging-and-observability.md`：补“代理定位闭环”
  - [x] 判定：如何识别 JDK proxy vs CGLIB（最小可执行步骤）
  - [x] 追踪：代理替换最常见落点（`initializeBean -> applyBeanPostProcessorsAfterInitialization`）
  - [x] 定位：如何锁定具体 `BeanPostProcessor`
  - [x] 关联 1 个最小可跑 Lab/Test 入口（见 2.2）

- [x] 1.3 更新 `spring-core-beans/docs/11-debugging-and-observability.md`：将“自检流程”升级为排障决策树
  - [x] 至少覆盖分流：Bean 不存在 / 注入选错 / 对象形态不对（proxy）/ 顺序问题（dependsOn、生命周期）
  - [x] 每条分流指向：推荐章节 + 推荐断点 + 可跑 Lab/Test

- [x] 1.4 更新 `spring-core-beans/docs/11-debugging-and-observability.md`：扩充异常导航表
  - [x] 新增一行：`Circular depends-on relationship`（定位为 definition 层拓扑环）
  - [x] 关联最小可跑入口：`SpringCoreBeansDependsOnLabTest.dependsOn_cycle_failsFast()`

- [x] 1.5 更新 `spring-core-beans/docs/11-debugging-and-observability.md`：把 Boot 条件报告“数据化”
  - [x] 提供在 `ApplicationContextRunner` 场景下读取 `ConditionEvaluationReport` 的建议路径
  - [x] 关联 1 个最小可跑 Lab/Test 入口（见 2.3，若采用）

- [x] 1.6 更新 `spring-core-beans/docs/11-debugging-and-observability.md`：增加“高收益条件断点模板”
  - [x] 创建链路：`beanName.equals("xxx")`
  - [x] DI 链路：`descriptor.getDependencyType() == Foo.class`
  - [x] 降噪：`beanName.startsWith("org.springframework.")`（反向过滤提示）

- [x] 1.7 更新 `spring-core-beans/docs/19-depends-on.md`：补 `dependsOn` vs `@Lazy` 交互小节
  - [x] 写死结论：`dependsOn` 通过 `getBean(dep)` 强行拉起 dependency
  - [x] 关联最小可跑入口（见 2.1）

- [x] 1.8 更新 `spring-core-beans/docs/19-depends-on.md`：补“为什么 dependsOn 不影响 DI 选择”的机制解释
  - [x] 用“发生阶段不同”对齐 `doGetBean`（创建前置） vs `doResolveDependency`（注入解析）

- [x] 1.9 更新 `spring-core-beans/docs/19-depends-on.md`：补“写入时机对照”
  - [x] `@Component`/扫描注册
  - [x] `@Bean`/配置解析
  - [x] 编程式 `BeanDefinition#setDependsOn`

- [x] 1.10 更新 `spring-core-beans/docs/19-depends-on.md`：把销毁顺序做成可断言闭环
  - [x] 引用新增用例（见 2.1）
  - [x] 强化与 `docs/11` 的互链（依赖图/销毁顺序观察点）

## 2. Labs（新增“闭环型”可断言实验）

- [x] 2.1 更新 `SpringCoreBeansDependsOnLabTest`
  - [x] 新增：`dependsOn_triggersLazyDependencyInstantiation()`
    - [x] 使用 `AnnotationConfigApplicationContext` + programmatic registration
    - [x] 断言：lazy bean 因 dependsOn 在 refresh 期间被实例化
  - [x] 新增：`dependsOn_affectsDestroyOrder_viaDependentBeanMap()`
    - [x] 用 `DisposableBean`/`AutoCloseable` 等方式记录销毁顺序
    - [x] 断言：关闭时先销毁 dependent 再销毁 dependency

- [x] 2.2 新增 `SpringCoreBeansBeanCreationTraceLabTest`
  - [x] 用最小 bean + test-only BPP/InstantiationAwareBPP 记录关键阶段：
    - [x] 实例化（constructor）
    - [x] 属性填充/注入阶段 hook（例如 `postProcessProperties`）
    - [x] 初始化（`@PostConstruct` 或 init 回调）
    - [x] after-init 代理/包装替换（可选但推荐）
  - [x] 断言至少 2 条稳定结论（避免对命中次数做脆弱断言）
  - [x] 输出少量 `OBSERVE:`（辅助断点观看，不对日志做断言）

- [x] 2.3（可选）新增或扩展一个 Boot 条件报告 Lab
  - [x] 用 `ApplicationContextRunner` 构造可控条件分支
  - [x] 在测试中读取 `ConditionEvaluationReport` 并输出最小 `OBSERVE:` 线索
  - [x] 在 `docs/11` 中引用该 Lab 作为“数据化条件报告”的入口

## 3. Validation

- [x] 3.1 运行模块测试：`mvn -q -pl spring-core-beans test`
- [x] 3.2 运行全仓库测试：`mvn -q test`
