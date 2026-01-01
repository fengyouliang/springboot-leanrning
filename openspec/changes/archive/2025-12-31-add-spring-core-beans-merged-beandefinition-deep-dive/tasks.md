## 1. Labs（默认启用，`mvn -q test` 全绿）

- [x] 1.1 新增 `SpringCoreBeansMergedBeanDefinitionLabTest`
  - [x] 使用小容器（优先 `GenericApplicationContext`/`AnnotationConfigApplicationContext`，避免 `@SpringBootTest`）
  - [x] 构造可控的 parent/child `BeanDefinition` 场景（程序化注册更直观）
  - [x] 覆盖并固化至少 3 个可断言现象：
    - [x] `getBeanDefinition(...)` 拿到的“原始定义”不等于最终参与创建的 merged `RootBeanDefinition`
    - [x] `getMergedLocalBeanDefinition(...)` 会把 parent/child 合并成最终 `RootBeanDefinition`（属性值/生命周期元数据可观察）
    - [x] `MergedBeanDefinitionPostProcessor#postProcessMergedBeanDefinition(...)` 在实例创建链路中被调用（可记录调用时机与 merged 结果）
  - [x] 输出少量 `OBSERVE:` 提示（不对日志做断言）

- [x] 1.2 新增 bean graph 调试实验：`SpringCoreBeansBeanGraphDebugLabTest`（命名可调整）
  - [x] 提供一个 test-only helper（例如 `BeanGraphDumper`）：
    - [x] 打印候选集合（by type / qualifier / primary 的结果对比）
    - [x] 打印最终注入的 bean（用断言固定）
    - [x] 打印一条简短依赖链（聚焦“为什么是它”，不追求全量图）
  - [x] Lab 用一个最小可控场景演示（优先复用 `docs/03` 的 DI 解析套路）
  - [x] 输出格式与 `docs/11` 自检流程对齐（“先看候选，再看收敛规则，再看注入结果”）

## 2. 文档与导航（中文）

- [x] 2.1 新增 merged BD 章节：`spring-core-beans/docs/35-merged-bean-definition.md`（编号如有调整，以最终约定为准）
  - [x] 1:1 链接到对应 `*LabTest` 路径
  - [x] 解释 merged 的语义：为什么需要 merged、merged 发生在时间线哪里
  - [x] 解释与注入/生命周期元数据的关系（对齐 `AutowiredAnnotationBeanPostProcessor` / `CommonAnnotationBeanPostProcessor` 的“基础设施”视角）
  - [x] 给出推荐断点与固定观察点清单（包含 `getMergedLocalBeanDefinition` 与 `postProcessMergedBeanDefinition`）

- [x] 2.2 更新 `spring-core-beans/docs/11-debugging-and-observability.md`：补充“异常 → 断点入口”对照表
  - [x] 至少覆盖：`UnsatisfiedDependencyException` / `NoSuchBeanDefinitionException` / `BeanCurrentlyInCreationException`
  - [x] 每条映射到 1–3 个断点入口，并关联到对应章节与 Lab（做到“从报错能秒跳到实验”）

- [x] 2.3 统一所有章节追加 footer（每章末尾 1–2 行）
  - [x] `对应 Lab/Test：...`
  - [x] `推荐断点：...`
  - [x] 先定义 footer 模板，再批量应用到 `spring-core-beans/docs/*.md`

- [x] 2.4 更新 `spring-core-beans/README.md`
  - [x] 推荐阅读顺序加入 merged BD 新章节
  - [x] Labs 索引表加入新增的 2 个 Labs
  - [x] 概念地图补充：merged BD / troubleshooting / bean graph debugging 的导航入口

## 3. Validation

- [x] 3.1 运行模块测试：`mvn -q -pl spring-core-beans test`
- [x] 3.2（可选）运行全仓库测试：`mvn -q test`
